#!/usr/bin/env python3
"""Build one uploadable .zip per skill for Claude Desktop / web (Customize → Skills).

The plugin form (`scripts/build-plugin.sh`) is the better install where it is
available: one upload, plus the agents and hooks. This script exists for the
surfaces that take a *skill* but not a plugin — a free plan, or an org that has
plugin installs turned off — where each skill is uploaded on its own.

A skill uploaded on its own is not the same file as a skill inside the plugin,
so this script ports it. Every difference is listed here and nowhere else:

  1. The description. The upload form documents a 200-character maximum and the
     SKILL.md descriptions run 248-383, so the short ones in
     `scripts/skill-descriptions.json` are substituted. Those are shortened rather
     than replaced: every trigger phrase the README advertises survives, and
     `tests/test_skill_descriptions.py` fails if one does not.
  2. Cross-skill reference paths. Inside the plugin, SKILL.md bodies write
     `${CLAUDE_PLUGIN_ROOT}/skills/loop/references/x.md`, which Claude Code
     substitutes with the installed plugin root (the model's working directory is
     the user's project, so a bare relative path would not resolve). A lone skill
     folder has no plugin root, so the operational references are copied into the
     skill and the paths are rewritten to `references/x.md`.
  3. `$ARGUMENTS` is a Claude Code substitution. Nothing substitutes it elsewhere,
     so it becomes plain words.
  4. `argument-hint` is dropped: it describes a slash invocation these surfaces
     do not have.

Nothing else changes — same body, same triggers, same procedure.

References are bundled transitively: a reference file that names a sibling
("`surfaces.md` in this folder") brings that sibling along.

`--target local` builds for a Claude Code `.claude/skills/` copy instead of an
upload: plain folders, not zips, and only difference 2 applies — the
full description, `argument-hint` and `$ARGUMENTS` stay, since Claude Code
reads all three natively and the 200-character limit belongs to the upload form.
One local-only rewrite: agent names lose the plugin namespace
(`unknowns:unknowns-scout` -> `unknowns-scout`), matching agents copied into
`.claude/agents/`.

Usage:  python3 scripts/build-skill-zips.py [--out dist] [--target upload|local]
Output: upload -> dist/<skill>.zip  (each holding <skill>/SKILL.md [+ references/])
        local  -> dist/local/<skill>/SKILL.md [+ references/]
"""
import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REFS = SKILLS / "loop" / "references"

# Limits: `name` 64 and `description` 1024 are the Agent Skills spec
# (platform.claude.com, agent-skills/overview). The Claude help centre states 200
# for a description uploaded through Customize → Skills, which is the tighter of
# the two and the one that applies here, so it is what this script enforces.
NAME_MAX = 64
DESC_MAX = 200
SHORT = json.loads((ROOT / "scripts" / "skill-descriptions.json").read_text(encoding="utf-8"))

ARGUMENTS_PROSE = "the request that invoked this skill"
AGENTS = sorted(path.stem for path in (ROOT / "agents").glob("*.md"))


def port(body: str, keep_arguments: bool = False) -> tuple[str, set[str]]:
    """Rewrite a SKILL.md body for a standalone skill. Returns (text, refs used)."""
    used = set()
    def ref(match):
        used.add(match.group(1))
        return f"references/{match.group(1)}.md"

    root = r"(?:\$\{CLAUDE_PLUGIN_ROOT\}/)?"
    body = re.sub(root + r"skills/loop/references/([a-z-]+)\.md", ref, body)
    if not keep_arguments:
        body = body.replace("`$ARGUMENTS`", ARGUMENTS_PROSE).replace("$ARGUMENTS", ARGUMENTS_PROSE)
    else:
        # local copies go next to agents copied into .claude/agents/, where the
        # plugin namespace is gone: `unknowns:unknowns-scout` -> `unknowns-scout`
        body = re.sub(r"\bunknowns:(%s)\b" % "|".join(map(re.escape, AGENTS)), r"\1", body)
    return body, used


def sibling_refs(text: str) -> set[str]:
    """Reference files a reference names by bare file name (e.g. `surfaces.md`).

    A name that is part of a path (`.unknowns/scorecard.md`) is a data file the
    skill writes, not a sibling to bundle, so anything after `/` or `.` is skipped.
    """
    known = {path.stem for path in REFS.glob("*.md")}
    return {name for name in re.findall(r"(?<![\w/.-])([a-z][a-z-]*)\.md\b", text) if name in known}


def ref_closure(start: set[str]) -> set[str]:
    """`start` plus every reference those files name, transitively."""
    seen, queue = set(), sorted(start)
    while queue:
        name = queue.pop()
        if name in seen:
            continue
        seen.add(name)
        source = REFS / f"{name}.md"
        if source.exists():
            text = source.read_text(encoding="utf-8")
            # siblings named bare ("`surfaces.md`") and by full plugin path alike
            queue.extend(sorted((sibling_refs(text) | port(text)[1]) - seen))
    return seen


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

        ported, used = port(body, keep_arguments=local)
        used = ref_closure(used)
        skill_dir = staging / folder
        (skill_dir).mkdir(parents=True)
        header = f"---\n{raw}\n---\n" if local else emit_frontmatter(fields)
        (skill_dir / "SKILL.md").write_text(header + ported, encoding="utf-8")
        for ref_name in sorted(used):
            source = REFS / f"{ref_name}.md"
            if not source.exists():
                problems.append(f"{folder}: references missing {source.name}")
                continue
            target = skill_dir / "references"
            target.mkdir(exist_ok=True)
            ported_ref, _ = port(source.read_text(encoding="utf-8"),
                                 keep_arguments=local)
            (target / source.name).write_text(ported_ref, encoding="utf-8")

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
        built.append((archive, len(used)))

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
