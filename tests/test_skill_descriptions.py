"""Guard the short descriptions the Claude Desktop / web skill zips ship with.

`scripts/skill-descriptions.json` exists because the Customize → Skills upload
form documents a 200-character maximum and the SKILL.md descriptions run 248-283.
Two descriptions per skill is two things that can drift, so this file pins the
part that matters: a short description is allowed to lose words, never a trigger
phrase the README advertises.

Asserted:
  * one entry per skill folder, and no entry without a skill
  * every short description is within the documented 200-character limit
  * every English trigger phrase the README advertises for a skill survives in
    that skill's short description (the Korean ones are covered by evals, exactly
    as in test_trigger_containment)
  * `scripts/build-skill-zips.py` builds every skill cleanly and the result is a
    single-folder zip holding SKILL.md, with no plugin-root paths left in it

Run with: python3 -m unittest tests.test_skill_descriptions -v
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_trigger_containment import HANGUL, ROOT, readme_phrases  # noqa: E402

DESC_MAX = 200
SHORT_PATH = Path(ROOT) / "scripts" / "skill-descriptions.json"
SKILLS_DIR = Path(ROOT) / "skills"


def short_descriptions():
    data = json.loads(SHORT_PATH.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def skill_names():
    return {p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists()}


class ShortDescriptionTest(unittest.TestCase):
    def test_every_skill_has_one_and_only_skills_do(self):
        self.assertEqual(set(short_descriptions()), skill_names())

    def test_within_the_documented_limit(self):
        too_long = {
            name: len(text)
            for name, text in short_descriptions().items()
            if len(text) > DESC_MAX
        }
        self.assertEqual(
            too_long, {},
            "short descriptions over the %d-character upload limit: %s"
            % (DESC_MAX, too_long),
        )

    def test_keeps_every_english_trigger_phrase(self):
        wanted = defaultdict(set)
        for _, skill, phrase in readme_phrases(os.path.join(ROOT, "README.md")):
            if skill and not HANGUL.search(phrase):
                wanted[skill].add(phrase)
        short = short_descriptions()
        misses = [
            "%s: %r" % (skill, phrase)
            for skill, phrases in sorted(wanted.items())
            for phrase in sorted(phrases)
            if phrase.lower() not in short.get(skill, "").lower()
        ]
        self.assertEqual(
            misses, [],
            "README-advertised trigger phrases dropped from the short "
            "description used by the skill zips:\n" + "\n".join(misses),
        )


class SkillZipBuildTest(unittest.TestCase):
    def test_builds_clean_single_folder_zips(self):
        with tempfile.TemporaryDirectory() as out:
            result = subprocess.run(
                [sys.executable, os.path.join(ROOT, "scripts", "build-skill-zips.py"),
                 "--out", out],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            built = sorted(Path(out).glob("*.zip"))
            self.assertEqual({p.stem for p in built}, skill_names())
            for archive in built:
                with zipfile.ZipFile(archive) as zf:
                    names = zf.namelist()
                    roots = {n.split("/")[0] for n in names}
                    self.assertEqual(
                        roots, {archive.stem},
                        "%s must hold exactly one top-level folder" % archive.name,
                    )
                    self.assertIn("%s/SKILL.md" % archive.stem, names)
                    body = zf.read("%s/SKILL.md" % archive.stem).decode("utf-8")
                self.assertNotIn(
                    "skills/loop/references/", body.replace(
                        "github.com/ajitta/know-your-unknowns/blob/main/"
                        "skills/loop/references/talk-source.md", ""),
                    "%s still points at a path that only exists inside the plugin"
                    % archive.name,
                )
                self.assertNotIn("$ARGUMENTS", body)
                self.assertNotIn(
                    "${CLAUDE_PLUGIN_ROOT}", body,
                    "%s keeps a plugin-only substitution" % archive.name,
                )

    def test_skill_bodies_anchor_cross_skill_paths_at_the_plugin_root(self):
        # The model reads these paths from the user's project directory, so a
        # bare `skills/loop/...` does not resolve; Claude Code substitutes
        # ${CLAUDE_PLUGIN_ROOT} in plugin SKILL.md content.
        bare = re.compile(r"(?<!\$\{CLAUDE_PLUGIN_ROOT\}/)skills/loop/references/")
        for skill_md in sorted(Path(ROOT, "skills").glob("*/SKILL.md")):
            with self.subTest(skill=skill_md.parent.name):
                text = skill_md.read_text(encoding="utf-8")
                self.assertIsNone(bare.search(text), skill_md)


    def build(self, *extra):
        out = tempfile.mkdtemp()
        self.addCleanup(__import__("shutil").rmtree, out, True)
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "scripts", "build-skill-zips.py"),
             "--out", out, *extra],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return Path(out)

    def test_bundled_references_bring_the_siblings_they_name(self):
        refs = {p.stem for p in (SKILLS_DIR / "loop" / "references").glob("*.md")}
        sibling = re.compile(r"(?<![\w/.-])([a-z][a-z-]*)\.md\b")
        for archive in sorted(self.build().glob("*.zip")):
            with zipfile.ZipFile(archive) as zf:
                names = set(zf.namelist())
                for name in names:
                    if "/references/" not in name:
                        continue
                    text = zf.read(name).decode("utf-8")
                    for ref in set(sibling.findall(text)) & (refs - {"talk-source"}):
                        with self.subTest(archive=archive.name, ref=ref):
                            self.assertIn("%s/references/%s.md" % (archive.stem, ref),
                                          names)

    def test_local_target_keeps_what_claude_code_reads_natively(self):
        out = self.build("--target", "local") / "local"
        self.assertEqual({p.name for p in out.iterdir()}, skill_names())
        body = (out / "blindspot" / "SKILL.md").read_text(encoding="utf-8")
        original = (SKILLS_DIR / "blindspot" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("$ARGUMENTS", body)
        self.assertIn("argument-hint:", body)
        # full description, frontmatter byte-for-byte
        self.assertEqual(body.split("\n---\n", 1)[0], original.split("\n---\n", 1)[0])
        self.assertNotIn("${CLAUDE_PLUGIN_ROOT}", body)
        self.assertTrue((out / "blindspot" / "references" / "surfaces.md").exists())
        loop = (out / "loop" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("independent-reviewer", loop)
        self.assertNotIn("unknowns:independent-reviewer", loop)
        self.assertNotIn("unknowns:unknowns-scout",
                         (out / "blindspot" / "SKILL.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
