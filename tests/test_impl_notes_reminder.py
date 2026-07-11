"""Tests for hooks/scripts/impl_notes_reminder.py.

Standard library only (unittest) — run with:
    python3 -m unittest discover -s tests -v

Each test pipes a PostToolUse-style JSON payload into the script as a
subprocess, exactly as Claude Code's hook pipeline does, and isolates state
by pointing TMPDIR at a per-test directory (the script stores state via
tempfile.gettempdir()).
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "hooks", "scripts", "impl_notes_reminder.py",
)


class HookTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = self._tmp.name
        self.addCleanup(self._tmp.cleanup)

    def run_hook(self, stdin_bytes, env_extra=None):
        """Invoke the hook script once; returns CompletedProcess."""
        env = dict(os.environ)
        # Isolate state files: tempfile.gettempdir() honors TMPDIR/TEMP/TMP.
        env["TMPDIR"] = self.tmp
        env["TEMP"] = self.tmp
        env["TMP"] = self.tmp
        env.pop("UNKNOWNS_NOTES_THRESHOLD", None)
        env.pop("FIELD_GUIDE_NOTES_THRESHOLD", None)
        env.pop("UNKNOWNS_NOTES_REPEAT", None)
        if env_extra:
            env.update(env_extra)
        return subprocess.run(
            [sys.executable, SCRIPT],
            input=stdin_bytes,
            capture_output=True,
            env=env,
            timeout=10,
        )

    def payload(self, session_id="test-session", cwd=None):
        data = {"session_id": session_id, "tool_name": "Edit"}
        if cwd is not None:
            data["cwd"] = cwd
        return json.dumps(data).encode("utf-8")

    def state_path(self, session_id="test-session"):
        return os.path.join(self.tmp, "unknowns-notes-%s.json" % session_id)

    # --- malformed input -------------------------------------------------

    def test_empty_stdin_is_silent_success(self):
        result = self.run_hook(b"")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")

    def test_malformed_json_is_silent_success(self):
        result = self.run_hook(b"{not json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")

    def test_non_dict_json_is_silent_success(self):
        result = self.run_hook(b"[1, 2, 3]")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")

    # --- threshold environment handling ----------------------------------

    def test_threshold_zero_disables_hook(self):
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "0"}
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")
        self.assertFalse(os.path.exists(self.state_path()))

    def test_garbage_threshold_falls_through_to_legacy_var(self):
        env = {
            "UNKNOWNS_NOTES_THRESHOLD": "not-a-number",
            "FIELD_GUIDE_NOTES_THRESHOLD": "2",
        }
        first = self.run_hook(self.payload(), env_extra=env)
        self.assertEqual(first.stdout, b"")
        second = self.run_hook(self.payload(), env_extra=env)
        self.assertIn(b"reached 2", second.stdout)

    # --- firing behavior --------------------------------------------------

    def test_fires_exactly_once_at_threshold(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "3"}
        self.assertEqual(self.run_hook(self.payload(), env_extra=env).stdout, b"")
        self.assertEqual(self.run_hook(self.payload(), env_extra=env).stdout, b"")

        third = self.run_hook(self.payload(), env_extra=env)
        out = json.loads(third.stdout)
        self.assertIn("reached 3", out["systemMessage"])
        self.assertTrue(out["suppressOutput"])
        self.assertEqual(
            out["hookSpecificOutput"]["hookEventName"], "PostToolUse"
        )
        self.assertEqual(
            out["hookSpecificOutput"]["additionalContext"], out["systemMessage"]
        )

        with open(self.state_path(), encoding="utf-8") as fh:
            state = json.load(fh)
        self.assertEqual(state, {"count": 3, "reminded": True})

        fourth = self.run_hook(self.payload(), env_extra=env)
        self.assertEqual(fourth.stdout, b"")

    def test_repeat_mode_fires_at_every_multiple(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "2", "UNKNOWNS_NOTES_REPEAT": "1"}
        outputs = [
            self.run_hook(self.payload(), env_extra=env).stdout for _ in range(4)
        ]
        self.assertEqual(outputs[0], b"")
        self.assertIn(b"reached 2", outputs[1])
        self.assertEqual(outputs[2], b"")
        self.assertIn(b"reached 4", outputs[3])

    # --- state file handling ----------------------------------------------

    def test_session_id_is_sanitized_no_path_traversal(self):
        sid = "../../etc/passwd session!"
        self.run_hook(self.payload(session_id=sid))
        entries = os.listdir(self.tmp)
        self.assertEqual(len(entries), 1)
        name = entries[0]
        self.assertTrue(name.startswith("unknowns-notes-"))
        self.assertNotIn("/", name.replace("unknowns-notes-", ""))
        self.assertNotIn("!", name)

    def test_corrupted_state_file_resets_instead_of_crashing(self):
        with open(self.state_path(), "w", encoding="utf-8") as fh:
            fh.write("{corrupted")
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "10"}
        )
        self.assertEqual(result.returncode, 0)
        with open(self.state_path(), encoding="utf-8") as fh:
            state = json.load(fh)
        self.assertEqual(state["count"], 1)

    # --- message content ----------------------------------------------------

    def test_message_tail_depends_on_notes_file_existence(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}

        bare = self.run_hook(
            self.payload(session_id="no-notes", cwd=self.tmp), env_extra=env
        )
        self.assertIn(b"/unknowns:notes init", bare.stdout)

        notes_dir = os.path.join(self.tmp, "with-notes")
        os.makedirs(notes_dir)
        with open(
            os.path.join(notes_dir, "IMPLEMENTATION_NOTES.md"), "w"
        ) as fh:
            fh.write("# notes\n")
        present = self.run_hook(
            self.payload(session_id="has-notes", cwd=notes_dir), env_extra=env
        )
        self.assertNotIn(b"/unknowns:notes init", present.stdout)
        self.assertIn(b"IMPLEMENTATION_NOTES.md.", present.stdout)


if __name__ == "__main__":
    unittest.main()
