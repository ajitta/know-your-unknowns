#!/usr/bin/env python3
"""Build standalone skill uploads from the generated plugins/unknowns/skills/.

Run tools/package.py first. Shared reference instructions are already vendored
by that build, so this script copies them without path rewriting. Upload zips
use the trigger-preserving short descriptions and name/description frontmatter
only. --target local keeps full frontmatter and removes agent plugin namespaces.
Neither target contains hooks, presentation assets, or executable files.

Usage: python3 scripts/build-skill-zips.py [--out dist] [--target upload|local]
"""
import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "unknowns" / "skills"
# Limits: `name` 64 and `description` 1024 are the Agent Skills spec
# (platform.claude.com, agent-skills/overview). The Claude help centre states 200
# for a description uploaded through Customize → Skills, which is the tighter of
# the two and the one that applies here, so it is what this script enforces.
NAME_MAX = 64
DESC_MAX = 200
SHORT = json.loads((ROOT / "scripts" / "skill-descriptions.json").read_text(encoding="utf-8"))

AGENTS = sorted(path.stem for path in (ROOT / "plugins" / "unknowns" / "agents").glob("*.md"))


def local_body(body: str) -> str:
    """Copied Claude Code agents have no plugin namespace."""
    return re.sub(r"\bunknowns:(%s)\b" % "|".join(map(re.escape, AGENTS)), r"\1", body)


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise SystemExit("SKILL.md has no YAML frontmatter")
    return match.group(1), match.group(2)


def parse_frontmatter(raw: str) -> dict:
    """Enough YAML for this project's frontmatter: scalars and `>` folded blocks."""
    fields, key = {}, None
    for line in raw.split("\n"):
        if line.startswith(" ") and key:
            fields[key] = (fields[key] + " " + line.strip()).strip()
        elif ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            fields[key] = "" if value.strip() == ">" else value.strip()
    return fields


def emit_frontmatter(fields: dict) -> str:
    out = ["---"]
    for key in ("name", "description"):
        value = fields[key].replace("\n", " ").strip()
        out.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    out.append("---")
    return "\n".join(out) + "\n"


def build(out_dir: Path, target: str = "upload") -> int:
    if not any(SKILLS.glob("*/SKILL.md")):
        print("Run python tools/package.py before building skill uploads.", file=sys.stderr)
        return 1
    local = target == "local"
    if local:
        out_dir = out_dir / "local"
        out_dir.mkdir(parents=True, exist_ok=True)
    problems, built = [], []
    staging = out_dir / ".staging"
    if staging.exists():
        shutil.rmtree(staging)

    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        folder = skill_md.parent.name
        raw, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        fields = parse_frontmatter(raw)
        name = fields.get("name", "")
        description = SHORT.get(folder) if not local else fields.get("description", "")
        if description is None:
            problems.append(f"{folder}: no short description in "
                            f"scripts/skill-descriptions.json")
            description = fields.get("description", "")
        fields["description"] = description

        if name != folder:
            problems.append(f"{folder}: frontmatter name {name!r} != folder name")
        if len(name) > NAME_MAX:
            problems.append(f"{folder}: name is {len(name)} chars (max {NAME_MAX})")
        if not local and len(description) > DESC_MAX:
            problems.append(f"{folder}: description is {len(description)} chars — the "
                            f"upload form documents a {DESC_MAX}-char maximum")

        ported = local_body(body) if local else body
        skill_dir = staging / folder
        shutil.copytree(skill_md.parent, skill_dir)
        header = f"---\n{raw}\n---\n" if local else emit_frontmatter(fields)
        (skill_dir / "SKILL.md").write_bytes((header + ported).encode("utf-8"))
        if local:
            archive = out_dir / folder
            if archive.exists():
                shutil.rmtree(archive)
            shutil.copytree(skill_dir, archive)
        else:
            archive = out_dir / f"{folder}.zip"
            with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
                for path in sorted(skill_dir.rglob("*")):
                    if path.is_file():
                        zf.write(path, path.relative_to(staging).as_posix())
        built.append((archive, len(list((skill_dir / "references").glob("*.md")))))

    shutil.rmtree(staging)
    for archive, refs in built:
        size = (sum(f.stat().st_size for f in archive.rglob("*") if f.is_file())
                if archive.is_dir() else archive.stat().st_size)
        print(f"  {archive.name:<18} {size:>6} bytes  "
              f"{refs} reference file{'s' if refs != 1 else ''}")
    kind = "skill folders" if local else "skill zips"
    print(f"built {len(built)} {kind} in {out_dir}/")
    if problems:
        print("\nproblems:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="dist", help="output directory (default: dist)")
    parser.add_argument("--target", choices=("upload", "local"), default="upload",
                        help="upload: zips for Customize → Skills (default); "
                             "local: folders for a Claude Code .claude/skills/ copy")
    args = parser.parse_args()
    destination = (ROOT / args.out).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    raise SystemExit(build(destination, args.target))
