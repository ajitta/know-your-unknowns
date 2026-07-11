"""Guard against README <-> frontmatter trigger-phrase drift.

Every trigger phrase advertised in a README "Auto-triggers:" (en) or
"자동 트리거:" (ko) line must be honored by some SKILL.md description —
the description is what auto-triggering actually reads.

A README phrase counts as covered when:
  (a) it appears verbatim (case-insensitive) inside any description, or
  (b) some quoted phrase from a description is a substring of it
      (e.g. README "운영 루프로 진행해줘" ⊇ description "운영 루프로 진행").

Run with: python3 -m unittest tests.test_trigger_containment -v
"""
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRIGGER_LABELS = ("Auto-triggers:", "Auto-trigger phrases:", "자동 트리거:", "자동 트리거 문구:")
QUOTED = re.compile(r'[“"]([^”"]+)[”"]')


def readme_phrases(path):
    """Yield (lineno, phrase) for every quoted phrase in a trigger block."""
    lines = open(path, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if any(stripped.startswith(lbl) for lbl in TRIGGER_LABELS):
            block, start = [stripped], i
            while i + 1 < len(lines) and lines[i + 1].strip():
                i += 1
                block.append(lines[i].strip())
            for phrase in QUOTED.findall(" ".join(block)):
                yield start + 1, phrase
        i += 1


def descriptions():
    """Return (all_desc_text, desc_quoted_phrases) across every SKILL.md."""
    texts, quoted = [], []
    skills_dir = os.path.join(ROOT, "skills")
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.exists(path):
            continue
        content = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if not m:
            continue
        # collapse folded-scalar line breaks so phrases split across lines match
        desc = re.sub(r"\s+", " ", m.group(1))
        texts.append(desc)
        quoted.extend(QUOTED.findall(desc))
    return " ".join(texts).lower(), [q.lower() for q in quoted]


class TriggerContainmentTest(unittest.TestCase):
    def check_readme(self, filename):
        all_desc, desc_quoted = descriptions()
        misses = []
        for lineno, phrase in readme_phrases(os.path.join(ROOT, filename)):
            p = phrase.lower()
            if p in all_desc:
                continue
            if any(dq in p for dq in desc_quoted):
                continue
            misses.append("%s:%d %r" % (filename, lineno, phrase))
        self.assertEqual(
            misses, [],
            "README-advertised trigger phrases missing from every SKILL.md "
            "description:\n" + "\n".join(misses),
        )

    def test_english_readme(self):
        self.check_readme("README.md")

    def test_korean_readme(self):
        self.check_readme("README.ko.md")


if __name__ == "__main__":
    unittest.main()
