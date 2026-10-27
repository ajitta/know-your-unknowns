"""The single-turn runner's scaffold: `case.yaml` names a script that lays input files into the run."""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_manual", ROOT / "evals" / "run-manual.py")
rm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rm)

CAN_RUN_BASH = os.name != "nt" and shutil.which("bash") is not None


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


class ScaffoldTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="scaffold-test-")
        self.case_dir = os.path.join(self.tmp, "sample-case")
        self.sandbox = os.path.join(self.tmp, "sandbox")
        os.makedirs(self.sandbox)
        write(os.path.join(self.case_dir, "prompt.md"), "---\nruns: 3\n---\n\nReview this.\n")
        write(os.path.join(self.case_dir, "graders", "says-hi.md"), "---\ntype: regex\n---\n\nhi\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def case_yaml(self, text):
        write(os.path.join(self.case_dir, "case.yaml"), text)
        return rm.load_case(self.case_dir)

    def test_case_yaml_names_the_scaffold_script(self):
        case = self.case_yaml('schema_version: "1.1"\nname: sample-case\n'
                              'context:\n  scaffold_script: place-files.sh\n')
        self.assertEqual(case["scaffold_script"], "place-files.sh")

    def test_no_case_yaml_means_no_scaffold(self):
        case = rm.load_case(self.case_dir)
        self.assertIsNone(case["scaffold_script"])
        rm.run_scaffold(case, self.sandbox)
        self.assertEqual(rm.snapshot(self.sandbox), set())

    @unittest.skipUnless(CAN_RUN_BASH, "needs bash outside Windows")
    def test_scaffold_lays_files_and_git_history_into_the_sandbox(self):
        write(os.path.join(self.case_dir, "files", "a.txt"), "one\n")
        write(os.path.join(self.case_dir, "place-files.sh"),
              '#!/usr/bin/env bash\nset -eu\ncp -R "$(dirname "$0")/files/." .\n'
              'git init -q && git add -A\n'
              'git -c user.name=t -c user.email=t@example.invalid commit -qm base\n')
        case = self.case_yaml("context:\n  scaffold_script: place-files.sh\n")
        rm.run_scaffold(case, self.sandbox)
        self.assertTrue(os.path.isdir(os.path.join(self.sandbox, ".git")))
        # git internals are never reported as files the run created
        self.assertEqual(rm.snapshot(self.sandbox), {"a.txt"})

    @unittest.skipUnless(CAN_RUN_BASH, "needs bash outside Windows")
    def test_a_failing_scaffold_stops_the_run(self):
        write(os.path.join(self.case_dir, "place-files.sh"), "#!/usr/bin/env bash\nexit 3\n")
        case = self.case_yaml("context:\n  scaffold_script: place-files.sh\n")
        with self.assertRaises(SystemExit) as raised:
            rm.run_scaffold(case, self.sandbox)
        self.assertIn("scaffold script failed (exit 3)", str(raised.exception))

    def verify_problems(self):
        old = rm.HERE
        rm.HERE = self.tmp
        try:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rm.verify(str(ROOT / "plugins" / "unknowns"))
        finally:
            rm.HERE = old
        return [line for line in out.getvalue().splitlines() if line.startswith("FAIL")]

    def test_verify_flags_a_missing_script(self):
        self.case_yaml("context:\n  scaffold_script: nowhere.sh\n")
        problems = self.verify_problems()
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("scaffold script 'nowhere.sh' is missing", problems[0])

    def test_verify_flags_a_script_outside_the_case(self):
        write(os.path.join(self.tmp, "elsewhere.sh"), "true\n")
        self.case_yaml("context:\n  scaffold_script: ../elsewhere.sh\n")
        problems = self.verify_problems()
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("is outside the case", problems[0])

    def test_verify_flags_unknown_keys_and_a_wrong_name(self):
        self.case_yaml("name: other-case\nfixture: files\n")
        problems = "\n".join(self.verify_problems())
        self.assertIn("case.yaml has unknown key(s) ['fixture']", problems)
        self.assertIn("is not the folder name", problems)

    def test_verify_accepts_a_present_script(self):
        write(os.path.join(self.case_dir, "place-files.sh"), "true\n")
        self.case_yaml('schema_version: "1.1"\nname: sample-case\n'
                       'context:\n  scaffold_script: place-files.sh\n')
        self.assertEqual(self.verify_problems(), [])

    def test_prompt_md_rejects_a_fixture_key(self):
        # the CLI fails to load a case whose prompt.md carries a key it does not know
        write(os.path.join(self.case_dir, "prompt.md"), "---\nruns: 3\nfixture: files\n---\n\nx\n")
        with self.assertRaises(ValueError):
            rm.load_case(self.case_dir)

    @unittest.skipUnless(CAN_RUN_BASH, "needs an executable script outside Windows")
    def test_agent_reports_are_kept(self):
        # a stand-in for `claude -p`: the caller spawns an agent, whose own tool call and
        # result carry a parent id, and the agent's report comes back to the caller
        events = [
            {"type": "assistant", "message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "t1", "name": "Agent", "input": {"subagent_type": "r"}}]}},
            {"type": "user", "parent_tool_use_id": "t1", "message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "t9", "content": "inner tool output"}]}},
            {"type": "user", "message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "t1",
                 "content": [{"type": "text", "text": "criterion 3: missing"}]}]}},
            {"type": "result", "result": "summary for the user"},
        ]
        fake = os.path.join(self.tmp, "fake-claude")
        write(fake, "#!/bin/sh\ncat <<'EOF'\n%s\nEOF\n" % "\n".join(json.dumps(e) for e in events))
        os.chmod(fake, 0o755)
        run = rm.run_once(rm.load_case(self.case_dir), True, self.tmp, fake)
        self.assertEqual(run["agent_reports"], ["criterion 3: missing"])
        self.assertEqual(run["last_message"], "summary for the user")


if __name__ == "__main__":
    unittest.main()
