#!/usr/bin/env python3
"""Validate sources and build the committed unknowns plugin and release zips.

Stdlib only, Python 3.7+. Edit skills/, claude-code/, plugin-manifest.json and
packaging/, then regenerate. --check writes nothing and detects stale output.
The frontmatter reader accepts the repository's YAML subset: scalar fields,
folded/literal blocks and a metadata mapping. Unsupported syntax fails closed.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import posixpath
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
PLUGINS = ROOT / "plugins"
DIST = ROOT / "releases"
PACKAGING = ROOT / "packaging"
PLUGIN_README = PACKAGING / "plugin-README.md"
OPENAI_DIR = PACKAGING / "openai"
CLAUDE_ICON = PACKAGING / "icon.png"
CLAUDE_ICON_PATH = ".claude-plugin/icon.png"
MANIFEST = ROOT / "plugin-manifest.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
RELEASE = ROOT / "plugin-release.json"
CHANGELOG = ROOT / "CHANGELOG.md"
ZIP_NAME = "know-your-unknowns.zip"
OPENAI_ZIP_NAME = "know-your-unknowns-openai.zip"
README_MIN_WORDS = 40
OPENAI_CATEGORIES = {
    "Productivity", "Creativity", "Developer Tools", "Business & Operations",
    "Data & Analytics", "Communication", "Education & Research", "Security",
    "Finance", "Healthcare", "Travel", "Entertainment", "Other",
}
ALLOWED_KEYS = {"name", "description", "license", "metadata", "compatibility", "allowed-tools"}
SHIPPED_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".svg"}
RESOURCE_RE = re.compile(r"(?<![\w/.-])((?:references|assets|scripts)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+)\b")
PROJECT_FILES = {"IMPLEMENTATION_NOTES.md", "CHANGELOG.md", "CLAUDE.md",
                 "AGENTS.md", ".gitignore", ".claude/rules/unknowns.md"}
PROJECT_PREFIXES = (".unknowns/",)
FILE_PATH_RE = re.compile(r"(?!/)[\w .<>/$+-]+\.[A-Za-z0-9]+(?:#[\w-]+)?")


def scalar(value):
    if value.startswith('"'):
        result = json.loads(value)
        if not isinstance(result, str):
            raise ValueError("expected a YAML string")
        return result
    if value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            raise ValueError("unterminated YAML string")
        return value[1:-1].replace("''", "'")
    if ": " in value or " #" in value or value.startswith(("&", "*", "!", "{", "[")):
        raise ValueError("unsupported YAML scalar; quote it")
    return value


def frontmatter(text):
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("SKILL.md needs opening and closing frontmatter delimiters")
    raw, body = text[4:].split("\n---\n", 1)
    fields, metadata = {}, {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z-]*):(?:[ \t]+(.*))?", line)
        if not match:
            raise ValueError("invalid frontmatter line: " + repr(line))
        key, value = match.group(1), match.group(2) or ""
        if key in fields:
            raise ValueError("duplicate frontmatter key: " + key)
        block = []
        while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" ")):
            block.append(lines[i])
            i += 1
        if key == "metadata" and not value:
            for item in block:
                if not item.strip():
                    continue
                m = re.fullmatch(r"  ([a-z][a-z_-]*):[ \t]+(.+)", item)
                if not m or m.group(1) in metadata:
                    raise ValueError("invalid or duplicate metadata line: " + repr(item))
                metadata[m.group(1)] = scalar(m.group(2))
            fields[key] = metadata
        elif value in (">", ">-", "|", "|-"):
            if any(item.strip() and not item.startswith("  ") for item in block):
                raise ValueError("block scalar needs two-space indentation")
            chunks = [item[2:] if item.startswith("  ") else "" for item in block]
            # The repository's folded descriptions contain single paragraphs.
            if value.startswith(">"):
                paragraphs = "\n".join(chunks).split("\n\n")
                result = "\n".join(" ".join(p.splitlines()) for p in paragraphs)
            else:
                result = "\n".join(chunks)
            fields[key] = result.rstrip("\n") + ("" if value.endswith("-") else "\n")
        else:
            if any(item.strip() for item in block):
                raise ValueError("unexpected indented scalar content")
            fields[key] = scalar(value)
    return fields, metadata, body


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def _normalized(path):
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def source_files(folder):
    return {
        p.relative_to(folder).as_posix(): _normalized(p)
        for p in sorted(folder.rglob("*"))
        if p.is_file() and "__pycache__" not in p.parts
        and p.name != ".DS_Store" and p.suffix != ".pyc"
    }


def sibling_refs(text):
    known = {p.stem for p in (SKILLS / "loop" / "references").glob("*.md")}
    return set(re.findall(r"(?<![\w/.-])([a-z][a-z-]*)\.md\b", text)) & known


def ref_closure(start):
    seen, queue = set(), sorted(start)
    while queue:
        name = queue.pop()
        if name in seen:
            continue
        seen.add(name)
        source = SKILLS / "loop" / "references" / (name + ".md")
        if not source.is_file():
            raise ValueError("missing shared reference: " + name)
        queue.extend(sorted(sibling_refs(source.read_text(encoding="utf-8")) - seen))
    return seen


def vendored_paths(body):
    refs = set(re.findall(r"(?<![\w/.-])references/([a-z-]+)\.md\b", body))
    shared = {p.stem for p in (SKILLS / "loop" / "references").glob("*.md")}
    refs = ref_closure(refs & shared)
    return {"references/" + name + ".md" for name in refs}


def plugin_files(skills):
    files = {
        ".claude-plugin/plugin.json": _normalized(MANIFEST),
        "README.md": _normalized(PLUGIN_README),
        "LICENSE": _normalized(ROOT / "LICENSE"),
        "NOTICE": _normalized(ROOT / "NOTICE"),
        CLAUDE_ICON_PATH: CLAUDE_ICON.read_bytes(),  # binary: no line-ending normalization
    }
    for skill in skills:
        prefix = "skills/" + skill.name + "/"
        own = source_files(skill)
        body = frontmatter(own["SKILL.md"].decode("utf-8"))[2]
        for rel in sorted(vendored_paths(body)):
            data = _normalized(SKILLS / "loop" / rel)
            if rel in own and own[rel] != data:
                raise ValueError(skill.name + ": source conflicts with shared " + rel)
            own[rel] = data
        files.update({prefix + rel: data for rel, data in own.items()})
    files.update({"agents/" + rel: data
                  for rel, data in source_files(ROOT / "claude-code" / "agents").items()})
    return files


def validate_markdown_paths(skill_name, files, skill_body):
    """Resolve packaged references in every Markdown resource of a standalone skill."""
    errors = []
    prefix = "skills/" + skill_name + "/"
    for path, data in sorted(files.items()):
        if not path.startswith(prefix) or not path.endswith(".md"):
            continue
        text = data.decode("utf-8")
        if path == prefix + "SKILL.md":
            # Direct source validation also works before that source is regenerated.
            text += "\n" + skill_body
        paths = set(RESOURCE_RE.findall(text))
        paths.update(token for token in re.findall(r"(?<!`)`([^`\n]+)`(?!`)", text)
                     if FILE_PATH_RE.fullmatch(token))
        paths.update(link.split("#", 1)[0] for link in re.findall(r"\]\(([^)]+)\)", text)
                     if not re.match(r"[a-z]+:|#|/", link))
        for rel in sorted(paths):
            rel = rel.split("#", 1)[0]
            if posixpath.normpath(rel) in PROJECT_FILES or posixpath.normpath(rel).startswith(PROJECT_PREFIXES):
                continue
            candidates = {posixpath.normpath(prefix + rel),
                          posixpath.normpath(posixpath.dirname(path) + "/" + rel)}
            if not any(candidate.startswith(prefix) and candidate in files for candidate in candidates):
                errors.append(path[len(prefix):] + ": missing generated relative path: " + rel)
    return errors


def validate_skill(skill, files):
    errors = []
    fields, metadata, body = frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))
    name = fields.get("name", "")
    if name != skill.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("name must match the skill folder and use lowercase letters, digits and hyphens")
    if set(fields) - ALLOWED_KEYS:
        errors.append("unsupported frontmatter keys: " + repr(sorted(set(fields) - ALLOWED_KEYS)))
    if not 1 <= len(fields.get("description", "")) <= 1024:
        errors.append("description must have 1..1024 characters")
    if "version" in metadata and metadata["version"] != json.loads(_normalized(MANIFEST))["version"]:
        errors.append("metadata.version differs from plugin-manifest.json")
    if "$" + "{CLAUDE_PLUGIN_ROOT}" in body:
        errors.append("body contains a plugin-root substitution")
    errors.extend(validate_markdown_paths(skill.name, files, body))
    yaml_path = skill / "agents" / "openai.yaml"
    if not yaml_path.is_file():
        errors.append("agents/openai.yaml missing")
    else:
        text = yaml_path.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            m = re.search(r"^  " + field + r": (.+)$", text, re.M)
            value = scalar(m.group(1)) if m else ""
            if not value:
                errors.append("agents/openai.yaml missing interface." + field)
            if field == "short_description" and len(value) > 64:
                errors.append("agents/openai.yaml short_description exceeds 64 characters")
            if field == "display_name" and not value.startswith("Unknowns: "):
                errors.append("agents/openai.yaml display_name must start with Unknowns: ")
            if field == "default_prompt" and not value.startswith("Use $unknowns:" + skill.name + " to "):
                errors.append("agents/openai.yaml default_prompt must name the skill")
        if not re.search(r"^policy:\n  allow_implicit_invocation: true\s*$", text, re.M):
            errors.append("agents/openai.yaml policy.allow_implicit_invocation must be true")
    return [skill.name + ": " + error for error in errors]


def collect_errors(skills, files):
    errors = []
    manifest = json.loads(_normalized(MANIFEST))
    if manifest.get("name") != "unknowns":
        errors.append("plugin-manifest.json name must be unknowns")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", manifest.get("version", "")):
        errors.append("plugin-manifest.json needs a semantic version")
    for key in ("description", "author", "license", "homepage", "repository"):
        if not manifest.get(key):
            errors.append("plugin-manifest.json missing " + key)
    market = json.loads(_normalized(MARKETPLACE))
    if market.get("name") != "know-your-unknowns" or [
        (p.get("name"), p.get("source")) for p in market.get("plugins", [])
    ] != [("unknowns", "./plugins/unknowns")]:
        errors.append("marketplace must list unknowns -> ./plugins/unknowns")
    for entry in market.get("plugins", []):
        if "version" in entry and entry["version"] != manifest["version"]:
            errors.append("marketplace version differs from plugin-manifest.json")
    if not skills:
        errors.append("no source skills found")
    for skill in skills:
        errors.extend(validate_skill(skill, files))
    if len(re.sub(r"```.*?```", "", files["README.md"].decode("utf-8"), flags=re.S).split()) < README_MIN_WORDS:
        errors.append("packaging/plugin-README.md needs at least 40 words")
    errors.extend(validate_openai_interface(*openai_parts()))
    errors.extend("packaging/icon.png: " + x for x in validate_png_icon(files[CLAUDE_ICON_PATH]))
    errors.extend(shipped_violations(files))
    errors.extend(shipped_violations(openai_files(files)))
    return errors


def validate_png_icon(data: bytes) -> list[str]:
    """The Claude plugin directory's listing icon: a square PNG, 512 to 2,048 px, under 2 MB."""
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        return ["must be a PNG file"]
    width, height = int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")
    e = []
    if width != height or not 512 <= width <= 2048:
        e.append(f"must be square, 512 to 2,048 px on each side (found {width}x{height})")
    if len(data) >= 2 * 1024 * 1024:
        e.append("must be under 2 MB")
    return e


def shipped_violations(files):
    """Only instructions, manifests, listing images and license notices are shipped."""
    errors = []
    for rel in files:
        parts = Path(rel).parts
        if rel in ("LICENSE", "NOTICE", CLAUDE_ICON_PATH):
            pass
        elif Path(rel).suffix not in SHIPPED_SUFFIXES:
            errors.append(rel + ": only Markdown, YAML, JSON and listing image assets may ship")
        if "hooks" in parts or "scripts" in parts or (parts[0] == "skills" and "assets" in parts):
            errors.append(rel + ": hooks, scripts and skill assets must not ship")
        if Path(rel).suffix == ".svg" and not rel.startswith("assets/"):
            errors.append(rel + ": SVG assets belong only to the plugin listing")
    return errors

def _one_line(s: object) -> bool:
    return isinstance(s, str) and s.strip() != "" and "\n" not in s and "\r" not in s


def validate_openai_interface(interface: dict, assets: dict[str, bytes]) -> list[str]:
    """The OpenAI directory's final-submission rules for interface fields and images."""
    e = []
    if not (_one_line(interface.get("displayName")) and len(interface["displayName"]) <= 30):
        e.append("displayName: one line, at most 30 characters")
    if not (_one_line(interface.get("shortDescription")) and len(interface["shortDescription"]) <= 30):
        e.append("shortDescription: one line, at most 30 characters")
    long = interface.get("longDescription")
    if not (isinstance(long, str) and long.strip() and len(long) <= 4000):
        e.append("longDescription: required, at most 4,000 characters")
    if not (_one_line(interface.get("developerName")) and len(interface["developerName"]) <= 80):
        e.append("developerName: one line, at most 80 characters")
    if interface.get("category") not in OPENAI_CATEGORIES:
        e.append(f"category must be one of {sorted(OPENAI_CATEGORIES)}")
    caps = interface.get("capabilities", [])
    if len(caps) > 20 or not all(_one_line(c) and len(c) <= 120 for c in caps):
        e.append("capabilities: at most 20, each one line and at most 120 characters")
    prompts = interface.get("defaultPrompt", [])
    if isinstance(prompts, str):
        prompts = [prompts]
    if len(prompts) > 3 or len(set(prompts)) != len(prompts) or not all(
        _one_line(p) and len(p) <= 128 and "@" not in p for p in prompts
    ):
        e.append("defaultPrompt: at most 3 unique one-line prompts of at most 128 characters, no @mention")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if key in interface and not (isinstance(interface[key], str) and interface[key].startswith("https://") and len(interface[key]) <= 1024):
            e.append(f"{key}: an https:// URL of at most 1,024 characters")
    for key in ("logo", "composerIcon"):
        path = interface.get(key, "")
        if not (isinstance(path, str) and path.startswith("./assets/") and path.endswith(".svg")):
            e.append(f"{key}: must be ./assets/<name>.svg")
            continue
        data = assets.get(path[2:])
        if data is None:
            e.append(f"{key}: {path} not found in packaging/openai/")
            continue
        m = re.search(r'<svg\b[^>]*\bviewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', data.decode("utf-8"))
        if not m or m.group(1) != m.group(2) or float(m.group(1)) < 48 or float(m.group(1)) > 4096:
            e.append(f"{key}: SVG needs a square numeric viewBox between 48 and 4,096")
    return [f"packaging/openai/interface.json: {x}" for x in e]


def openai_parts() -> tuple[dict, dict[str, bytes]]:
    interface = json.loads(OPENAI_DIR.joinpath("interface.json").read_text(encoding="utf-8"))
    assets = {
        f"assets/{f.name}": _normalized(f) for f in sorted((OPENAI_DIR / "assets").glob("*")) if f.is_file()
    }
    return interface, assets


def openai_files(files: dict[str, bytes]) -> dict[str, bytes]:
    """The OpenAI directory upload: Codex manifest with interface, plus image assets."""
    interface, assets = openai_parts()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest.pop("displayName", None)  # interface.displayName carries it in the Codex manifest
    manifest["skills"] = "./skills/"
    manifest["interface"] = interface
    out = {k: v for k, v in files.items() if not k.startswith((".claude-plugin/", "hooks/", "agents/"))}
    out[".codex-plugin/plugin.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    out.update(assets)
    return out


def plugin_name() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["name"]


def zip_bytes(files: dict[str, bytes]) -> bytes:
    top = plugin_name()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as zf:
        for rel in sorted(files):
            info = zipfile.ZipInfo(f"{top}/{rel}", (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3  # unix; ZipInfo defaults to 0 on Windows
            info.external_attr = 0o644 << 16
            zf.writestr(info, files[rel])
    return buf.getvalue()


def content_digest(files: dict[str, bytes]) -> str:
    """sha256 over plugin files (excluding only manifest.version), listing and assets,
    so a version bump alone leaves it unchanged; unreleased notes permit a new baseline."""
    h = hashlib.sha256()
    extra = {}
    if OPENAI_DIR.is_dir():
        interface, assets = openai_parts()
        extra = {"openai:interface.json": json.dumps(interface, sort_keys=True).encode()}
        extra.update({f"openai:{k}": v for k, v in assets.items()})
    for rel, data in sorted({**files, **extra}.items()):
        if rel == ".claude-plugin/plugin.json":
            manifest = json.loads(data)
            manifest.pop("version", None)
            data = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
        h.update(rel.encode() + b"\0" + data + b"\0")
    return h.hexdigest()


def _release_state(files: dict[str, bytes]) -> tuple[str, str, dict]:
    version = json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]
    try:
        recorded = json.loads(RELEASE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        recorded = {}
    return version, content_digest(files), recorded


def _bump_error(version: str) -> str:
    return (f"shipped files changed since plugin {version}: bump version in plugin-manifest.json "
            "or add non-empty ## [Unreleased] notes to CHANGELOG.md, then run tools/package.py")


def has_unreleased_notes() -> bool:
    """A real entry, not an empty heading or comments, permits unreleased rebuilds."""
    try:
        text = CHANGELOG.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False
    match = re.search(r"^## \[Unreleased\][ \t]*\n(.*?)(?=^##[ \t]|\Z)", text, re.M | re.S)
    if not match:
        return False
    entry = re.sub(r"<!--.*?-->", "", match.group(1), flags=re.S)
    entry = re.sub(r"^#{3,6}[ \t].*$", "", entry, flags=re.M)
    return bool(entry.strip(" \t\r\n-*"))


def check_release(files: dict[str, bytes]) -> list[str]:
    version, digest, recorded = _release_state(files)
    if recorded.get("version") != version:
        return [f"plugin-release.json records {recorded.get('version')!r}, plugin-manifest.json says {version!r}: run tools/package.py"]
    if recorded.get("digest") != digest:
        if has_unreleased_notes():
            return ["plugin-release.json lags the unreleased source: run tools/package.py"]
        return [_bump_error(version)]
    expected = (json.dumps({"version": version, "digest": digest}, indent=2) + "\n").encode()
    if RELEASE.read_bytes() != expected:
        return ["plugin-release.json differs from a fresh build: run tools/package.py"]
    return []


def record_release(files: dict[str, bytes]) -> list[str]:
    version, digest, recorded = _release_state(files)
    if recorded.get("version") == version and recorded.get("digest") != digest and not has_unreleased_notes():
        return [_bump_error(version)]
    RELEASE.write_bytes((json.dumps({"version": version, "digest": digest}, indent=2) + "\n").encode())
    return []


def check_generated(files: dict[str, bytes]) -> list[str]:
    """plugins/unknowns/ and the zip match the source byte for byte."""
    errors = []
    out = PLUGINS / plugin_name()
    on_disk = {f.relative_to(out).as_posix(): f.read_bytes() for f in out.rglob("*") if f.is_file()} if out.is_dir() else {}
    if on_disk != files:
        stale = sorted(set(on_disk) ^ set(files)) + sorted(k for k in files if k in on_disk and on_disk[k] != files[k])
        errors.append(f"plugins/{plugin_name()}/ lags the source ({', '.join(stale[:5]) or 'missing'}): run tools/package.py")
    zpath = DIST / ZIP_NAME
    if not zpath.is_file() or zpath.read_bytes() != zip_bytes(files):
        errors.append(f"releases/{ZIP_NAME} lags the source: run tools/package.py")
    opath = DIST / OPENAI_ZIP_NAME
    if not opath.is_file() or opath.read_bytes() != zip_bytes(openai_files(files)):
        errors.append(f"releases/{OPENAI_ZIP_NAME} lags the source: run tools/package.py")
    return errors


def write_outputs(files: dict[str, bytes]) -> None:
    out = PLUGINS / plugin_name()
    if out.exists():
        for f in sorted(out.rglob("*"), reverse=True):
            f.unlink() if f.is_file() else f.rmdir()
    for rel, data in files.items():
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / ZIP_NAME).write_bytes(zip_bytes(files))
    (DIST / OPENAI_ZIP_NAME).write_bytes(zip_bytes(openai_files(files)))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check committed output without writing")
    args = parser.parse_args(argv)
    try:
        skills = skill_dirs()
        files = plugin_files(skills)
        errors = collect_errors(skills, files)
        if not errors:
            errors = check_release(files) + check_generated(files) if args.check else record_release(files)
        for error in errors:
            print("ERROR", error.encode("ascii", "backslashreplace").decode("ascii"))
        if errors:
            return 1
        if not args.check:
            write_outputs(files)
            print("Built plugins/unknowns/ and both release zips")
        print("OK: {} skills; version {}; {}".format(
            len(skills), json.loads(_normalized(MANIFEST))["version"],
            "committed output is current" if args.check else "outputs regenerated"))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("ERROR", str(error).encode("ascii", "backslashreplace").decode("ascii"))
        return 1


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")
    sys.exit(main())
