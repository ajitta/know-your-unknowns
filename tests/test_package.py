"""Packaging checks for source validation, standalone skills and committed zips."""
import ast
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("package", ROOT / "tools" / "package.py")
pkg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pkg)


class PackageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skills = pkg.skill_dirs()
        cls.files = pkg.plugin_files(cls.skills)

    def test_check_command(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "package.py"), "--check"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("committed output is current", result.stdout)

    def test_validation(self):
        self.assertEqual(pkg.collect_errors(self.skills, self.files), [])

    def test_generated_frontmatter_uses_only_agent_skill_spec_keys(self):
        extra = {}
        for skill in self.skills:
            text = (ROOT / "plugins" / "unknowns" / "skills" / skill.name / "SKILL.md").read_text(encoding="utf-8")
            fields = pkg.frontmatter(text)[0]
            if set(fields) - pkg.ALLOWED_KEYS:
                extra[skill.name] = sorted(set(fields) - pkg.ALLOWED_KEYS)
        self.assertEqual(extra, {})

    def test_vendored_shared_files_are_identical(self):
        # Check every copy independently of the build's vendored_paths selection.
        shared = list((ROOT / "skills" / "loop" / "references").glob("*.md"))
        copies = 0
        for skill in self.skills:
            body = (skill / "SKILL.md").read_text(encoding="utf-8")
            target = ROOT / "plugins" / "unknowns" / "skills" / skill.name
            for source in shared:
                rel = source.relative_to(ROOT / "skills" / "loop")
                dest = target / rel
                if rel.as_posix() in body:
                    self.assertTrue(dest.is_file(), dest)
                if dest.is_file():
                    copies += 1
                    self.assertEqual(dest.read_bytes(), source.read_bytes(), dest)
            if (target / "references" / "output-routing.md").exists():
                self.assertTrue((target / "references/surfaces.md").is_file(), skill.name)
            if (target / "references" / "scorecard.md").exists():
                self.assertTrue((target / "references" / "surfaces.md").is_file())
        self.assertGreater(copies, len(shared))
        # A skill with no shared references remains small.
        self.assertFalse((ROOT / "plugins/unknowns/skills/interview/assets").exists())

    def test_source_and_generated_skill_bodies_are_identical(self):
        for skill in self.skills:
            self.assertEqual((skill / "SKILL.md").read_bytes(),
                             self.files["skills/" + skill.name + "/SKILL.md"])

    def test_no_repository_files_shipped(self):
        allowed = {".claude-plugin", "README.md", "LICENSE", "NOTICE", "skills", "agents"}
        self.assertEqual({name.split("/")[0] for name in self.files}, allowed)
        for folder in ("agents",):
            self.assertEqual(pkg.source_files(ROOT / "claude-code" / folder),
                             {key[len(folder) + 1:]: data for key, data in self.files.items()
                              if key.startswith(folder + "/")})

    def test_no_code_or_hooks_shipped(self):
        for path in (ROOT / "plugins" / "unknowns").rglob("*"):
            if path.is_file():
                rel = path.relative_to(ROOT / "plugins" / "unknowns").as_posix()
                self.assertEqual(pkg.shipped_violations({rel: path.read_bytes()}), [])
        for filename in (pkg.ZIP_NAME, pkg.OPENAI_ZIP_NAME):
            with zipfile.ZipFile(ROOT / "releases" / filename) as archive:
                files = {name.split("/", 1)[1]: archive.read(name) for name in archive.namelist()}
                self.assertEqual(pkg.shipped_violations(files), [], filename)
        for rel in ("hooks/hooks.json", "skills/plan/scripts/run.md", "skills/plan/assets/icon.svg",
                    "skills/plan/run.py", "run.sh", "page.js", "main.ts", "image.png"):
            self.assertTrue(pkg.shipped_violations({rel: b"example"}), rel)

    def test_openai_interfaces(self):
        for skill in self.skills:
            text = (skill / "agents/openai.yaml").read_text(encoding="utf-8")
            self.assertIn("allow_implicit_invocation: true", text)
            prompt = re.search(r"  default_prompt: (.+)", text).group(1)
            self.assertTrue(json.loads(prompt).startswith("Use $unknowns:" + skill.name + " to "))
        interface, assets = pkg.openai_parts()
        self.assertEqual(interface["displayName"], "Know Your Unknowns")
        self.assertEqual(len(interface["defaultPrompt"]), 3)
        self.assertEqual(pkg.validate_openai_interface(interface, assets), [])

    def test_generated_files_use_lf(self):
        for name, data in self.files.items():
            self.assertNotIn(b"\r", data, name)

    def test_zips_reproducible_and_versioned(self):
        version = json.loads(pkg.MANIFEST.read_text(encoding="utf-8"))["version"]
        for filename, files, manifest in (
            (pkg.ZIP_NAME, self.files, ".claude-plugin/plugin.json"),
            (pkg.OPENAI_ZIP_NAME, pkg.openai_files(self.files), ".codex-plugin/plugin.json"),
        ):
            fresh = pkg.zip_bytes(files)
            self.assertEqual(fresh, pkg.zip_bytes(files))
            self.assertEqual(fresh, (ROOT / "releases" / filename).read_bytes())
            with zipfile.ZipFile(io.BytesIO(fresh)) as archive:
                self.assertEqual({p.split("/")[0] for p in archive.namelist()}, {"unknowns"})
                self.assertEqual(json.loads(archive.read("unknowns/" + manifest))["version"], version)
                for info in archive.infolist():
                    self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
                    self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                    self.assertEqual(info.create_system, 3)
                    self.assertEqual(info.external_attr >> 16, 0o644)

    def test_openai_zip_has_skills_and_assets_but_no_claude_agents_or_hooks(self):
        with zipfile.ZipFile(ROOT / "releases" / pkg.OPENAI_ZIP_NAME) as archive:
            names = set(archive.namelist())
            self.assertFalse(any(p.startswith(("unknowns/hooks/", "unknowns/agents/",
                                               "unknowns/.claude-plugin/")) for p in names))
            self.assertIn("unknowns/.codex-plugin/plugin.json", names)
            self.assertTrue({"unknowns/assets/icon.svg", "unknowns/assets/logo.svg"} <= names)
            # agents/openai.yaml is per-skill interface metadata, not a Claude agent.
            self.assertEqual({p for p in names if p.startswith("unknowns/skills/")},
                             {"unknowns/" + p for p in self.files if p.startswith("skills/")})

    def test_digest_requires_version_bump_without_unreleased_notes(self):
        with tempfile.TemporaryDirectory() as temp:
            release = Path(temp) / "plugin-release.json"
            changelog = Path(temp) / "CHANGELOG.md"
            changelog.write_bytes(b"# Changelog\n\n## [0.9.2]\n\nReleased notes.\n")
            with mock.patch.object(pkg, "RELEASE", release), mock.patch.object(pkg, "CHANGELOG", changelog):
                self.assertEqual(pkg.record_release(self.files), [])
                recorded = release.read_bytes()
                changed = dict(self.files)
                changed["skills/plan/SKILL.md"] += b"\nChanged content\n"
                self.assertTrue(pkg.record_release(changed))
                self.assertEqual(release.read_bytes(), recorded)
                self.assertTrue(pkg.check_release(changed))
                self.assertEqual(pkg.check_release(self.files), [])

    def test_digest_can_be_regenerated_at_same_version_with_unreleased_notes(self):
        with tempfile.TemporaryDirectory() as temp:
            release = Path(temp) / "plugin-release.json"
            changelog = Path(temp) / "CHANGELOG.md"
            changelog.write_bytes(b"# Changelog\n\n## [Unreleased]\n\n- Portable package in progress.\n")
            with mock.patch.object(pkg, "RELEASE", release), mock.patch.object(pkg, "CHANGELOG", changelog):
                self.assertEqual(pkg.record_release(self.files), [])
                recorded = json.loads(release.read_bytes())
                changed = dict(self.files)
                changed["skills/plan/SKILL.md"] += b"\nUnreleased change\n"
                self.assertTrue(pkg.check_release(changed), "--check must reject a stale record even during development")
                self.assertEqual(pkg.record_release(changed), [])
                updated = json.loads(release.read_bytes())
                self.assertEqual(updated["version"], recorded["version"])
                self.assertNotEqual(updated["digest"], recorded["digest"])
                self.assertEqual(pkg.check_release(changed), [])

    def test_unreleased_entry_must_contain_notes(self):
        with tempfile.TemporaryDirectory() as temp:
            changelog = Path(temp) / "CHANGELOG.md"
            with mock.patch.object(pkg, "CHANGELOG", changelog):
                self.assertFalse(pkg.has_unreleased_notes())
                for text in ("# Changelog\n", "## [Unreleased]\n\n", "## [Unreleased]\n\n### Added\n<!-- pending -->\n",
                             "## [Unreleased]\n\n## [0.9.2]\n\nReleased notes.\n"):
                    with self.subTest(text=text):
                        changelog.write_bytes(text.encode())
                        self.assertFalse(pkg.has_unreleased_notes())
                        release = Path(temp) / "plugin-release.json"
                        with mock.patch.object(pkg, "RELEASE", release):
                            self.assertEqual(pkg.record_release(self.files), [])
                            changed = dict(self.files, **{"README.md": b"changed"})
                            self.assertTrue(pkg.record_release(changed))
                changelog.write_bytes(b"## [Unreleased]\r\n\r\n- Pending release.\r\n")
                self.assertTrue(pkg.has_unreleased_notes())

    def test_missing_relative_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            skill = Path(temp) / "plan"
            import shutil
            shutil.copytree(ROOT / "skills" / "plan", skill)
            body = skill / "SKILL.md"
            body.write_bytes(body.read_bytes() + b"\nRead references/missing.md and [guide](guide.md).\n")
            errors = pkg.validate_skill(skill, self.files)
            self.assertTrue(any("references/missing.md" in e for e in errors), errors)
            self.assertTrue(any("guide.md" in e for e in errors), errors)

    def test_bad_frontmatter_is_rejected(self):
        for text in (
            "name: plan\n",
            "---\nname plan\n---\nbody",
            "---\nname: plan\nname: quiz\n---\nbody",
            "---\ndescription: plain: broken\n---\nbody",
            "---\ndescription: >\n x\n---\nbody",
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                pkg.frontmatter(text)

    def test_folded_frontmatter(self):
        fields, _, body = pkg.frontmatter("---\nname: plan\ndescription: >\n  First line\n  second line\n---\nbody")
        self.assertEqual(fields["description"], "First line second line\n")
        self.assertEqual(body, "body")

    def test_python37_syntax(self):
        # Available on the supported current CI interpreter; the packager uses no
        # runtime evaluated generic annotations and no dependencies.
        ast.parse((ROOT / "tools/package.py").read_text(encoding="utf-8"), feature_version=(3, 7))

    def test_legacy_console_encoding(self):
        env = dict(os.environ, PYTHONIOENCODING="ascii")
        result = subprocess.run([sys.executable, str(ROOT / "tools/package.py"), "--check"],
                                capture_output=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        result.stdout.decode("ascii")


if __name__ == "__main__":
    unittest.main()
