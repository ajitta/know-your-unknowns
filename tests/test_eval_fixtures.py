"""The single-turn runner's `fixture:` key: copied into the sandbox, layered into git, verified."""
import contextlib
import importlib.util
import io
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_manual", ROOT / "evals" / "run-manual.py")
rm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rm)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


class FixtureTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="fixture-test-")
        self.case_dir = os.path.join(self.tmp, "sample-case")
        self.sandbox = os.path.join(self.tmp, "sandbox")
        os.makedirs(self.sandbox)
        write(os.path.join(self.case_dir, "graders", "says-hi.md"),
              "---\ntype: regex\n---\n\nhi\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def case(self, fixture_line):
        write(os.path.join(self.case_dir, "prompt.md"),
              "---\ndescription: \"x\"\nruns: 3\n%s\n---\n\nReview this.\n" % fixture_line)
        return rm.load_case(self.case_dir)

    def test_one_folder_is_copied_as_is(self):
        write(os.path.join(self.case_dir, "fixture", "report.md"), "162 members\n")
        write(os.path.join(self.case_dir, "fixture", "data", "members.csv"), "month,n\n1,50\n")
        rm.copy_fixture(self.case("fixture: fixture"), self.sandbox)
        self.assertEqual(rm.snapshot(self.sandbox), {"report.md", "data/members.csv"})
        self.assertFalse(os.path.exists(os.path.join(self.sandbox, ".git")))

    @unittest.skipIf(shutil.which("git") is None, "git not installed")
    def test_a_list_of_folders_becomes_one_commit_each(self):
        write(os.path.join(self.case_dir, "fx", "base", "a.txt"), "one\n")
        write(os.path.join(self.case_dir, "fx", "change", "a.txt"), "two\n")
        write(os.path.join(self.case_dir, "fx", "change", "b.txt"), "new\n")
        rm.copy_fixture(self.case("fixture: [fx/base, fx/change]"), self.sandbox)
        log = subprocess.run(["git", "log", "--format=%s"], cwd=self.sandbox,
                             capture_output=True, text=True, check=True).stdout.split()
        self.assertEqual(log, ["change", "base"])
        diff = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"], cwd=self.sandbox,
                              capture_output=True, text=True, check=True).stdout.split()
        self.assertEqual(diff, ["a.txt", "b.txt"])
        # git internals are never reported as files the run created
        self.assertEqual(rm.snapshot(self.sandbox), {"a.txt", "b.txt"})

    def test_no_fixture_leaves_the_sandbox_empty(self):
        rm.copy_fixture(self.case(""), self.sandbox)
        self.assertEqual(rm.snapshot(self.sandbox), set())

    def verify_problems(self, fixture_line):
        self.case(fixture_line)
        old = rm.HERE
        rm.HERE = self.tmp
        try:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rm.verify(str(ROOT / "plugins" / "unknowns"))
        finally:
            rm.HERE = old
        return [line for line in out.getvalue().splitlines() if line.startswith("FAIL")]

    def test_verify_flags_a_missing_fixture_folder(self):
        problems = self.verify_problems("fixture: nowhere")
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("fixture folder 'nowhere' is missing", problems[0])

    def test_verify_flags_a_fixture_outside_the_case(self):
        os.makedirs(os.path.join(self.tmp, "elsewhere"))
        problems = self.verify_problems("fixture: ../elsewhere")
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("is not a folder inside the case", problems[0])

    def test_verify_accepts_a_present_fixture(self):
        write(os.path.join(self.case_dir, "fixture", "plan.md"), "plan\n")
        self.assertEqual(self.verify_problems("fixture: fixture"), [])


if __name__ == "__main__":
    unittest.main()
