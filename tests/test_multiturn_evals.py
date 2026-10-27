"""Structural checks for the multi-turn eval runner; no model is called."""
import contextlib
import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_multiturn", ROOT / "evals" / "run-multiturn.py")
mt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mt)

CASE = """---
description: "A test case"
tags: [multiturn]
runs: 1
user_turns: 2
allowed_tools: [Read, Skill]
---

## Opening message

Interview me about the export feature.

## Persona

You know the export runs nightly. Stop once you get a decision table.
"""

LLM_GRADER = """---
type: llm
focus: transcript
---

Every reply asks at most four questions.
"""


def transcript(*replies):
    turns = []
    for text in replies:
        turns.append({"role": "user", "text": "hi"})
        turns.append({"role": "assistant", "text": text, "tool_calls": [], "skills": []})
    return {"arm": "with", "stop_reason": "user-stop", "error": None,
            "user_turns_used": len(replies) - 1, "cost_usd": 0, "duration_seconds": 0,
            "turns": turns}


class MultiturnCaseTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="mt-test-")
        self.case_dir = os.path.join(self.tmp, "sample-case")
        os.makedirs(os.path.join(self.case_dir, "graders"))
        self.write("case.md", CASE)
        self.write("graders/asks-four.md", LLM_GRADER)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, rel, text):
        with open(os.path.join(self.case_dir, rel), "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)

    def test_parses_frontmatter_sections_and_graders(self):
        case = mt.load_case(self.case_dir)
        self.assertEqual(case["user_turns"], 2)
        self.assertEqual(case["allowed_tools"], ["Read", "Skill"])
        self.assertEqual(case["opening"], "Interview me about the export feature.")
        self.assertIn("runs nightly", case["persona"])
        self.assertEqual(case["graders"][0]["name"], "asks-four")
        self.assertIn("at most four", case["graders"][0]["criteria"])
        self.assertEqual(mt.verify_case(case), [])

    def test_verify_flags_broken_cases(self):
        self.write("case.md", CASE.replace("## Persona", "## Notes").replace(
            "runs: 1", "runs: 1\nturns: 3"))
        self.write("graders/bad-regex.md", "---\ntype: regex\nturn: middle\n---\n(unclosed\n")
        self.write("graders/no-max.md", "---\ntype: question_count\n---\n")
        problems = "\n".join(mt.verify_case(mt.load_case(self.case_dir)))
        self.assertIn("unknown key(s) ['turns']", problems)
        self.assertIn("'## Persona' is missing", problems)
        self.assertIn("bad pattern", problems)
        self.assertIn("turn must be one of", problems)
        self.assertIn("integer max", problems)

    def test_verify_requires_a_grader_past_the_first_reply(self):
        os.remove(os.path.join(self.case_dir, "graders", "asks-four.md"))
        self.write("graders/first.md", "---\ntype: regex\nturn: first\n---\nlists\n")
        problems = mt.verify_case(mt.load_case(self.case_dir))
        self.assertTrue(any("only the first reply" in p for p in problems), problems)

    def test_repository_cases_verify(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(mt.verify(), 0)
        names = [case["name"] for case in mt.discover()]
        self.assertEqual(len(names), 4)

    def test_run_manual_discovery_skips_multiturn(self):
        result = subprocess.run([sys.executable, str(ROOT / "evals" / "run-manual.py"), "--list"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("multiturn", result.stdout)


class MultiturnGradingTest(unittest.TestCase):
    def test_question_count(self):
        reply = ("Round 1.\n\n**1. Which channel?**\n- a) email\n- b) Slack\n\n"
                 "**2. Who can receive it**\n*Why it matters:* data leaks.\n- a) members\n\n"
                 "### Q3 \u2014 Retention?\n\n4) Formats?\n\n"
                 "| 5 | in a table? |\n```\n6. in code?\n```\n> 7. quoted?\n   8. nested?\n"
                 "9. Plain numbered statement.\n")
        self.assertEqual(mt.count_questions(reply), 4)

    def test_question_count_skips_numbered_options(self):
        reply = ("**1. How is the report delivered?**\n*Why it matters:* integrations.\n"
                 "1. **Email only.** Simplest.\n2. **Email plus Slack.** More work.\n\n"
                 "**2. Who can receive it**\n1. Members only\n2. Anyone\n\n"
                 "**3. Retention?**\n*Why it matters:* storage.\n1. **Delete at 7 days.**\n"
                 "2. **Keep 30 days.**\n\n1. **Proceed with this prompt now.**\n2. **Stop here.**\n")
        self.assertEqual(mt.count_questions(reply), 3)

    def test_question_count_grader_reads_every_reply(self):
        grader = {"type": "question_count", "max": 2, "turn": "all", "name": "q"}
        ok, why = mt.grade_mechanical(grader, transcript("1. A?\n2. B?", "1. A?\n2. B?\n3. C?"))
        self.assertFalse(ok)
        self.assertIn("2:3", why)
        grader["turn"] = "first"
        self.assertTrue(mt.grade_mechanical(grader, transcript("1. A?", "1. A?\n2. B?\n3. C?"))[0])

    def test_turn_selectors(self):
        replies = [{"text": "short"}, {"text": "x" * 900}, {"text": "closing offer?"}]
        self.assertEqual([n for n, _ in mt.select_turns(replies, "final_substantive")], [2])
        self.assertEqual([n for n, _ in mt.select_turns(replies, "last")], [3])
        self.assertEqual([n for n, _ in mt.select_turns(replies, 1)], [1])
        self.assertEqual(len(mt.select_turns(replies, "all")), 3)

    def test_regex_any_and_all(self):
        grader = {"type": "regex", "pattern": "export", "turn": "any", "name": "r"}
        data = transcript("nothing here", "the export job")
        self.assertTrue(mt.grade_mechanical(grader, data)[0])
        grader["turn"] = "all"
        self.assertFalse(mt.grade_mechanical(grader, data)[0])

    def test_tool_used_counts_selected_replies(self):
        data = transcript("a", "b")
        data["turns"][3]["tool_calls"] = [
            {"name": "Write", "input": {"file_path": ".unknowns/2026-01-01-quiz-x-key.md"}}]
        grader = {"type": "tool_used", "tool": "Write", "input_match": "quiz-[^\"]*-key\\.md",
                  "turn": "all", "name": "k"}
        self.assertTrue(mt.grade_mechanical(grader, data)[0])
        grader["turn"] = "first"
        self.assertFalse(mt.grade_mechanical(grader, data)[0])

    def test_llm_graders_wait_for_a_judge_and_failed_runs_are_not_graded(self):
        case = {"name": "c", "graders": [{"type": "llm", "name": "j", "criteria": "x"}]}
        result = mt.grade_run(case, transcript("hello?"))
        self.assertIsNone(result["graders"][0]["passed"])
        broken = transcript("hello?")
        broken.update(stop_reason="error", error="assistant reply 1 timed out")
        result = mt.grade_run(case, broken)
        self.assertFalse(result["graded"])
        self.assertIn("not graded", result["graders"][0]["explanation"])

    def test_stop_and_verdict_parsing(self):
        self.assertTrue(mt.parse_stop("STOP"))
        self.assertTrue(mt.parse_stop("  STOP\n"))
        self.assertFalse(mt.parse_stop("Please stop asking about retention."))
        self.assertEqual(mt.parse_overall("1. ok\nOVERALL: FAIL\nOVERALL: PASS"), "PASS")
        self.assertIsNone(mt.parse_overall("no verdict"))
        self.assertTrue(mt.asks_something("Reply with steal or skip by number."))
        self.assertFalse(mt.asks_something("Here is the prompt.\n```\nWhat next?\n```"))

    def test_judge_and_user_prompts_hide_tools(self):
        data = transcript("Done.")
        data["turns"][1]["tool_calls"] = [{"name": "Skill", "input": {"skill": "unknowns:quiz"}}]
        text = mt.conversation_text(data["turns"])
        self.assertIn("=== ASSISTANT reply 1 ===", text)
        self.assertNotIn("unknowns:quiz", text)

    def test_console_messages_are_ascii(self):
        source = (ROOT / "evals" / "run-multiturn.py").read_text(encoding="utf-8")
        self.assertTrue(source.isascii())


if __name__ == "__main__":
    unittest.main()
