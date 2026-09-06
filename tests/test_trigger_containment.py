"""Guard against README <-> frontmatter trigger-phrase drift.

Every trigger phrase advertised in a README "Auto-triggers:" (en) or
"자동 트리거:" (ko) line must be honored by the description of the skill that
section is about — the description is what auto-triggering actually reads.

A README phrase counts as covered when, in *that skill's* description:
  (a) it appears verbatim (case-insensitive), or
  (b) some multi-word quoted phrase is a substring of it
      (e.g. README "운영 루프로 진행해줘" ⊇ description "운영 루프로 진행").

Only the `description:` value is read (never argument-hint or name), only the
part before an anti-trigger clause ("Do NOT", "NOT for", "아닙니다") counts as
advertising, and single-word quotes are excluded from rule (b) so that "loop"
cannot vouch for "please loop over these files". Phrases outside a skill
section fall back to the pooled descriptions.

Run with: python3 -m unittest tests.test_trigger_containment -v
"""
import os
import re
import unittest
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRIGGER_LABELS = ("Auto-triggers:", "Auto-trigger phrases:", "자동 트리거:", "자동 트리거 문구:")
QUOTED = re.compile(r'[“"]([^”"]+)[”"]')
SECTION = re.compile(r"^#{2,4}\s.*/unknowns:([a-z-]+)")
# everything from here on describes when NOT to trigger
NEGATIVE_MARKERS = ("Do NOT", "NOT for", "NOT auto-trigger", "NOT ", "Skip for",
                    "not this skill", "아닙니다", "아님")


def readme_phrases(path):
    """Yield (lineno, skill, phrase) for every quoted phrase in a trigger block."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    skill = None
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("#"):
            match = SECTION.match(stripped)
            skill = match.group(1) if match else None
        elif any(stripped.startswith(label) for label in TRIGGER_LABELS):
            block, start = [stripped], i
            while i + 1 < len(lines) and lines[i + 1].strip():
                i += 1
                block.append(lines[i].strip())
            for phrase in QUOTED.findall(" ".join(block)):
                yield start + 1, skill, phrase
        i += 1


def description_value(frontmatter):
    """The `description:` value only — YAML block scalars are indented."""
    captured, capturing = [], False
    for line in frontmatter.split("\n"):
        if re.match(r"^description\s*:", line):
            capturing = True
            captured.append(re.sub(r"^description\s*:\s*[|>]?[-+]?\s*", "", line))
            continue
        if capturing:
            if line.strip() and not line[:1].isspace():
                break
            captured.append(line.strip())
    return re.sub(r"\s+", " ", " ".join(captured)).strip()


def advertised_part(description):
    """Drop the anti-trigger tail: it tells the model when to stay away."""
    cut = len(description)
    for marker in NEGATIVE_MARKERS:
        index = description.find(marker)
        if index != -1:
            cut = min(cut, index)
    return description[:cut]


def descriptions():
    """skill name -> (full description, multi-word phrases it advertises)."""
    result = {}
    skills_dir = os.path.join(ROOT, "skills")
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.exists(path):
            continue
        content = Path(path).read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if not match:
            continue
        description = description_value(match.group(1))
        pool = [
            quoted.lower()
            for quoted in QUOTED.findall(advertised_part(description))
            if len(quoted.split()) > 1
        ]
        result[name] = (description.lower(), pool)
    return result


class TriggerContainmentTest(unittest.TestCase):
    def check_readme(self, filename):
        skills = descriptions()
        pooled = (
            " ".join(desc for desc, _ in skills.values()),
            [phrase for _, pool in skills.values() for phrase in pool],
        )
        misses = []
        for lineno, skill, phrase in readme_phrases(os.path.join(ROOT, filename)):
            description, pool = skills.get(skill, pooled)
            candidate = phrase.lower()
            if candidate in description:
                continue
            if any(quoted in candidate for quoted in pool):
                continue
            misses.append(
                "%s:%d %r (section: %s)" % (filename, lineno, phrase, skill or "-")
            )
        self.assertEqual(
            misses, [],
            "README-advertised trigger phrases that the section's SKILL.md "
            "description does not honor:\n" + "\n".join(misses),
        )

    def test_english_readme(self):
        self.check_readme("README.md")

    def test_korean_readme(self):
        self.check_readme("README.ko.md")

    def test_every_skill_description_is_parsed(self):
        skills = descriptions()
        self.assertEqual(len(skills), 11, sorted(skills))
        for name, (description, _pool) in skills.items():
            self.assertTrue(description, "empty description for %s" % name)
            self.assertNotIn("argument-hint", description)

    def test_readme_sections_map_to_real_skills(self):
        known = set(descriptions())
        for filename in ("README.md", "README.ko.md"):
            sections = {
                skill for _lineno, skill, _phrase
                in readme_phrases(os.path.join(ROOT, filename)) if skill
            }
            self.assertTrue(sections, filename)
            self.assertEqual(sections - known, set(), filename)


if __name__ == "__main__":
    unittest.main()
