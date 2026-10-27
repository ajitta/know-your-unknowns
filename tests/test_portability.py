"""Guard the portable package: self-contained skills, agents that inherit tools, measured steps."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "unknowns"
MISSING_TOOL = "Without a tool, do the step in the conversation and say what could not be checked."
MISSING_PICK = "a missing pick is undecided."


def skill(name):
    return (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


class PortabilityTest(unittest.TestCase):
    def test_no_host_substitutions_or_page_runtime(self):
        forbidden = re.compile(r"CLAUDE_PLUGIN_ROOT|\$ARGUMENTS|argument-hint|AskUserQuestion|render-page|\.html|UNKNOWNS_|hooks active")
        for path in PLUGIN.rglob("*"):
            if path.is_file() and path.suffix != ".png":
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), path)

    def test_skills_are_self_contained(self):
        # Each skill loads alone on every surface, so it ships only its body and interface.
        for folder in (PLUGIN / "skills").iterdir():
            files = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
            self.assertEqual(files, {"SKILL.md", "agents/openai.yaml"}, folder.name)

    def test_missing_tool_line_is_one_shared_sentence(self):
        # Rule 11: one wording, at most once per skill, so one grep finds every copy.
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            self.assertLessEqual(text.count(MISSING_TOOL), 1, path)
            self.assertNotIn("No file system", text, path)
            self.assertNotIn("No question tool", text, path)

    def test_reacting_skills_say_a_missing_pick_is_undecided(self):
        for name in ("blindspot", "brainstorm", "buy-in", "prototypes", "reference", "teach-me", "tweakable-plan"):
            self.assertIn(MISSING_PICK, skill(name), name)

    def test_agents_inherit_every_tool(self):
        for path in (PLUGIN / "agents").glob("*.md"):
            fm = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S).group(1)
            for key in ("tools:", "disallowedTools:", "permissionMode:", "hooks:", "isolation:"):
                self.assertNotIn(key, fm, path)

    def test_reviewer_packet_matches_its_caller(self):
        # Rule 11: buy-in hands the reviewer the fields the reviewer expects.
        fields = ("the done criteria, the outcome, the approved plan, the deviation log, the deliverable "
                  "(for code, the diff range or touched files and how to run the tests), and the claims the work rests on")
        self.assertIn(fields, skill("buy-in"))
        self.assertIn(fields, (PLUGIN / "agents/independent-reviewer.md").read_text(encoding="utf-8"))

    def test_quiz_keeps_six_question_gate_and_hidden_key(self):
        text = skill("quiz")
        self.assertIn("Prepare **6 questions**; pass = **all 6 correct**.", text)
        self.assertIn("Five are multiple choice.", text)
        self.assertIn("sixth is a **teach-back**", text)
        self.assertIn("Keep the key out of the questions and reply until the user has answered.", text)
        self.assertIn("exact change site", text)

    def test_skills_name_their_cell_and_do_open_requests_directly(self):
        # Rule 0: each skill names the cell it serves; a self-evident request skips the method.
        open_line = ("A self-evident request, where both of you already know what to do "
                     "(the **Open** cell), is done directly, without this method.")
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn(open_line, text, path)
            self.assertRegex(text, r"This skill serves the \*\*(Blind|Hidden|Unknown)\*\* cell", path)
            fm = re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)
            self.assertIn("Self-evident requests are done directly.", fm, path)

    def test_loop_ends_with_the_outcome_check(self):
        text = skill("unknowns-loop")
        self.assertIn("**Outcome check**", text)
        self.assertGreater(text.index("**Outcome check**"), text.index("**Verify**"))

    def test_deviations_are_logged_in_one_named_file(self):
        for name in ("deviation-log", "interview"):
            self.assertIn("IMPLEMENTATION_NOTES.md", skill(name), name)


if __name__ == "__main__":
    unittest.main()
