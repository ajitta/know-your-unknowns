"""Guard the portable instruction contracts after removing presentation code."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "unknowns"
QUESTION = "Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit."
OUTPUT = "Deliver Markdown in the conversation with the same structure. End the turn with the assembled reply as plain text in chat."
SCOUT_CONTRACT = "Keep the scout pass read-only: never create or modify files, run implementation commands, or invent findings."
REVIEW_CONTRACT = "Keep the review read-only: never edit or commit repository files or write outside a temporary directory."


def skill(name):
    return (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


class PortabilityTest(unittest.TestCase):
    def test_no_host_substitutions_or_page_runtime(self):
        forbidden = re.compile(r"CLAUDE_PLUGIN_ROOT|\$ARGUMENTS|argument-hint|AskUserQuestion|render-page|\.html|UNKNOWNS_|hooks active")
        for path in PLUGIN.rglob("*"):
            if path.is_file():
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), path)

    def test_markdown_deliverables_keep_assembled_replies(self):
        for name in ("blindspot", "brainstorm", "buy-in", "loop", "plan",
                     "prototypes", "quiz", "reference", "teach-me"):
            self.assertIn(OUTPUT, skill(name), name)
            self.assertIn("references/output-routing.md", skill(name), name)

    def test_shared_question_fallback(self):
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn(QUESTION, text, path)
        for name in ("surfaces", "output-routing", "scorecard"):
            self.assertIn(QUESTION, (PLUGIN / "skills/loop/references" / (name + ".md")).read_text(encoding="utf-8"))

    def test_subagent_fallbacks_keep_readonly_contracts(self):
        for name in ("blindspot", "brainstorm"):
            text = skill(name)
            self.assertIn(SCOUT_CONTRACT, text)
            self.assertIn("No sub-agent → do the pass yourself as a separate step", text)
            self.assertIn("Scout pass performed by the assistant", text)
        for name in ("loop", "buy-in"):
            text = skill(name)
            self.assertIn(REVIEW_CONTRACT, text)
            self.assertIn("No sub-agent → do the pass yourself as a separate step", text)
            self.assertIn("Assistant review; not independent", text)

    def test_agent_tool_boundaries(self):
        scout = (PLUGIN / "agents/unknowns-scout.md").read_text(encoding="utf-8")
        reviewer = (PLUGIN / "agents/independent-reviewer.md").read_text(encoding="utf-8")
        self.assertEqual(re.search(r"^tools: (.+)$", scout, re.M).group(1).split(", "),
                         ["Read", "Grep", "Glob", "WebFetch", "WebSearch"])
        self.assertIn("Hand questions requiring command execution back to the caller", scout)
        self.assertIn("Bash", re.search(r"^tools: (.+)$", reviewer, re.M).group(1))
        self.assertIn("Never commit, push, install dependencies, or write outside a temporary directory.", reviewer)
        for text in (scout, reviewer):
            self.assertNotIn("permissionMode:", text)
            self.assertNotIn("hooks:", text)

    def test_deviation_records_without_files(self):
        for name in ("loop", "plan", "notes", "prototypes", "reference", "interview", "brainstorm"):
            text = skill(name)
            self.assertIn("IMPLEMENTATION_NOTES.md", text, name)
            self.assertIn("before ending the turn", text, name)
            self.assertIn("No file system →", text, name)
            if name in ("plan", "prototypes", "reference", "interview", "brainstorm"):
                self.assertIn("Stop and ask before changes to architecture, user-visible behavior, data loss, or security.", text, name)
                self.assertNotIn("Stop and ask before changes to architecture, user-visible behavior, data, or security.", text, name)

    def test_quiz_keeps_six_question_gate_and_private_teachback_key(self):
        text = skill("quiz")
        self.assertIn("Ask **6 questions**; pass = **all 6 correct**.", text)
        self.assertIn("Five are multiple choice.", text)
        self.assertIn("sixth is a **teach-back**", text)
        self.assertIn("Keep the key out of the questions and reply until the user has answered.", text)
        self.assertIn("Print the key as Markdown only after the answer", text)
        self.assertIn("not committed to a file in advance", text)
        self.assertIn("exact change site (file:line)", text)

    def test_shared_reviewer_packet(self):
        text = skill("loop")
        packet = text.split("b. Hand the agent this packet:\n\n", 1)[1].split("\n\nc.", 1)[0]
        surfaces = (PLUGIN / "skills/loop/references/surfaces.md").read_text(encoding="utf-8")
        self.assertIn(packet, surfaces)


if __name__ == "__main__":
    unittest.main()
