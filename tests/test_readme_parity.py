"""Guard against README.md <-> README.ko.md structural drift.

The two READMEs are twins: same document, two languages. Prose differs, but the
scaffolding must not, because the scaffolding is what a fix wave silently breaks
— a section added to one file only, a code block that lost its closing fence, a
table row dropped in translation, an install URL or an env var updated on one
side.

Asserted:
  * equal counts of headings, fenced-code-block delimiters and table rows
  * identical sets of URLs, `/unknowns:<skill>` commands and `UNKNOWNS_*` names

Deliberately not asserted: heading text, ordering, or word counts — those are
translation, not structure.

Run with: python3 -m unittest tests.test_readme_parity -v
"""
import os
import re
import unittest
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = "README.md"
KO = "README.ko.md"

HEADING = re.compile(r"^#{1,6}\s")
FENCE = re.compile(r"^\s*```")
TABLE_ROW = re.compile(r"^\s*\|")
URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
COMMAND = re.compile(r"/unknowns:[a-z][a-z-]*")
ENV_NAME = re.compile(r"\bUNKNOWNS_[A-Z0-9_]+")


def read(filename):
    return Path(os.path.join(ROOT, filename)).read_text(encoding="utf-8")


def counts(text):
    """Structural line counts, ignoring anything inside fenced code blocks
    except the fences themselves (a table drawn inside a sample does not count).
    """
    headings = fences = rows = 0
    in_fence = False
    for line in text.split("\n"):
        if FENCE.match(line):
            fences += 1
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if HEADING.match(line):
            headings += 1
        elif TABLE_ROW.match(line):
            rows += 1
    return {"headings": headings, "fence delimiters": fences, "table rows": rows}


def urls(text):
    # trailing sentence punctuation is prose, not part of the URL
    return {match.rstrip(".,;:") for match in URL.findall(text)}


class ReadmeParityTest(unittest.TestCase):
    def setUp(self):
        self.en = read(EN)
        self.ko = read(KO)

    def test_structural_counts_match(self):
        en, ko = counts(self.en), counts(self.ko)
        for key in en:
            self.assertEqual(
                en[key], ko[key],
                "%s: %s has %d, %s has %d" % (key, EN, en[key], KO, ko[key]),
            )

    def test_fences_are_balanced(self):
        for filename, text in ((EN, self.en), (KO, self.ko)):
            fences = counts(text)["fence delimiters"]
            self.assertEqual(
                fences % 2, 0,
                "%s has an unclosed fenced code block (%d delimiters)"
                % (filename, fences),
            )

    def test_urls_match(self):
        self.assertEqual(
            urls(self.en), urls(self.ko),
            "URLs present in only one README: %s"
            % sorted(urls(self.en) ^ urls(self.ko)),
        )

    def test_skill_commands_match(self):
        en = set(COMMAND.findall(self.en))
        ko = set(COMMAND.findall(self.ko))
        self.assertTrue(en, "no /unknowns: commands found in %s" % EN)
        self.assertEqual(
            en, ko,
            "/unknowns: commands present in only one README: %s"
            % sorted(en ^ ko),
        )

    def test_env_var_names_match(self):
        en = set(ENV_NAME.findall(self.en))
        ko = set(ENV_NAME.findall(self.ko))
        self.assertTrue(en, "no UNKNOWNS_* env names found in %s" % EN)
        self.assertEqual(
            en, ko,
            "UNKNOWNS_* names present in only one README: %s" % sorted(en ^ ko),
        )

    def test_twins_link_to_each_other(self):
        self.assertIn(KO, self.en)
        self.assertIn(EN, self.ko)


if __name__ == "__main__":
    unittest.main()
