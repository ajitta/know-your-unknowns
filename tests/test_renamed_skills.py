"""Guard the 0.12.0 skill renames: `loop` -> `unknowns-loop`, `notes` -> `deviation-log`,
`plan` -> `tweakable-plan`.

A bare `loop` belongs to Claude Code's built-in interval runner, `notes` did not say
what it logs, and a bare `plan` collides with native plan mode and other plugins' plan skills. Once renamed, an old name that creeps back into a skill body, an eval, a
README or the packaging sends users and the model to a skill that no longer exists.

Asserted:
  * the skill folders carry the new names and the old folders are gone
  * no current file refers to an old name in a form that addresses the skill
    (`unknowns:loop`, `/unknowns:notes`, `**loop** skill`, `skills/notes/`,
    `trigger-en-loop`, a `"loop":` key ...)
  * the trigger words users actually say survive in the descriptions:
    "loop" in unknowns-loop, "implementation notes" in deviation-log, "plan this" in
    tweakable-plan

Exempt: CHANGELOG.md and IMPLEMENTATION_NOTES.md (dated records), and docs/ except
the files that describe the current plugin (trigger-matrix.md, index.html), because the
dated reports there describe the versions they measured. This file is exempt too.

Run with: python3 -m unittest tests.test_renamed_skills -v
"""
import os
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RENAMES = {"loop": "unknowns-loop", "notes": "deviation-log", "plan": "tweakable-plan"}
CURRENT_DOCS = {"docs/trigger-matrix.md", "docs/index.html"}
EXEMPT = {"CHANGELOG.md", "IMPLEMENTATION_NOTES.md", "tests/test_renamed_skills.py"}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".html", ".txt", ""}


def old_name_patterns(old):
    return [
        re.compile(r"\$?unknowns:%s\b(?!-)" % old),          # unknowns:loop, $unknowns:loop, /unknowns:loop
        re.compile(r"\*\*%s\*\* skill" % old),               # the **loop** skill
        re.compile(r"skills/%s/" % old),                     # skills/loop/
        re.compile(r"trigger-(?:en|ko)-%s\b(?!-)" % old),    # trigger-en-loop
        re.compile(r"behavior-%s-" % old),                   # behavior-notes-...
        re.compile(r"^name: %s$" % old, re.MULTILINE),       # frontmatter
        re.compile(r'"%s"\s*:' % old),                       # a JSON key
        re.compile(r"fires-unknowns-%s\b(?!-)" % old),       # grader file names
    ]


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    if out.returncode != 0:
        return [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                if p.is_file() and ".git" not in p.parts]
    return out.stdout.splitlines()


def checked(rel):
    if rel in EXEMPT or rel.startswith(("releases/", ".git/")):
        return False
    if rel.startswith("docs/") and rel not in CURRENT_DOCS:
        return False
    return Path(rel).suffix in TEXT_SUFFIXES


class RenamedSkillsTest(unittest.TestCase):
    def test_folders_carry_the_new_names(self):
        for base in (ROOT / "skills", ROOT / "plugins" / "unknowns" / "skills"):
            names = {p.name for p in base.iterdir() if p.is_dir()}
            for old, new in RENAMES.items():
                self.assertIn(new, names, base)
                self.assertNotIn(old, names, base)

    def test_no_current_file_addresses_an_old_name(self):
        hits = []
        for rel in tracked_files():
            path = ROOT / rel
            if not checked(rel) or not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for old in RENAMES:
                for pattern in old_name_patterns(old):
                    for match in pattern.finditer(text):
                        line = text.count("\n", 0, match.start()) + 1
                        hits.append("%s:%d %r" % (rel, line, match.group(0)))
        self.assertEqual(hits, [], "old skill names are back:\n" + "\n".join(hits))

    def test_trigger_words_survive_the_rename(self):
        def description(name):
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            return " ".join(re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1).lower().split())
        self.assertIn('"unknowns loop"', description("unknowns-loop"))
        self.assertIn('"implementation notes"', description("deviation-log"))
        self.assertIn('"plan this"', description("tweakable-plan"))


if __name__ == "__main__":
    unittest.main()
