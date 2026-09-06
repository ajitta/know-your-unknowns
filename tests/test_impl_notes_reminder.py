"""Tests for hooks/scripts/impl_notes_reminder.py and hooks/hooks.json.

Standard library only (unittest) — run with:
    python3 -m unittest discover -s tests -v

Each test pipes a hook-style JSON payload into the script as a subprocess,
exactly as Claude Code's hook pipeline does, and isolates state by pointing
TMPDIR at a per-test directory (the script stores state under
tempfile.gettempdir() when CLAUDE_PLUGIN_DATA is unset).
"""
import glob
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "hooks", "scripts", "impl_notes_reminder.py")
HOOKS_JSON = os.path.join(ROOT, "hooks", "hooks.json")
POSIX_ONLY = unittest.skipUnless(hasattr(os, "getuid"), "POSIX permissions only")


class HookTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = self._tmp.name
        self.addCleanup(self._tmp.cleanup)
        # a project that opted in: IMPLEMENTATION_NOTES.md already exists
        self.project = os.path.join(self.tmp, "project")
        os.makedirs(self.project)
        with open(
            os.path.join(self.project, "IMPLEMENTATION_NOTES.md"), "w",
            encoding="utf-8",
        ) as fh:
            fh.write("# notes\n")
        # a project that never opted in; .git stops the upward walk
        self.bare = os.path.join(self.tmp, "bare")
        os.makedirs(os.path.join(self.bare, ".git"))

    # --- harness ---------------------------------------------------------

    def env(self, env_extra=None):
        env = dict(os.environ)
        # Isolate state files: tempfile.gettempdir() honors TMPDIR/TEMP/TMP.
        env["TMPDIR"] = self.tmp
        env["TEMP"] = self.tmp
        env["TMP"] = self.tmp
        for name in (
            "UNKNOWNS_NOTES_THRESHOLD", "FIELD_GUIDE_NOTES_THRESHOLD",
            "UNKNOWNS_NOTES_REPEAT", "UNKNOWNS_NOTES_ALWAYS",
            "CLAUDE_PLUGIN_DATA", "CLAUDE_PROJECT_DIR",
        ):
            env.pop(name, None)
        if env_extra:
            env.update(env_extra)
        return env

    def run_hook(self, stdin_bytes, env_extra=None, args=()):
        """Invoke the hook script once; returns CompletedProcess."""
        return subprocess.run(
            [sys.executable, SCRIPT] + list(args),
            input=stdin_bytes,
            capture_output=True,
            env=self.env(env_extra),
            cwd=self.tmp,  # hermetic: never resolve paths against the runner's cwd
            timeout=30,
        )

    def payload(self, session_id="test-session", cwd=False, **extra):
        data = {"session_id": session_id, "tool_name": "Edit"}
        data["cwd"] = self.project if cwd is False else cwd
        if data["cwd"] is None:
            del data["cwd"]
        data.update(extra)
        return json.dumps(data).encode("utf-8")

    def state_dir(self):
        """Locate the script's own state directory (created on first run)."""
        pattern = os.path.join(self.tmp, "unknowns-notes-*")
        if not glob.glob(pattern):
            self.run_hook(
                self.payload(session_id="warmup"),
                env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1000"},
            )
        matches = glob.glob(pattern)
        self.assertEqual(len(matches), 1, matches)
        return matches[0]

    def state_path(self, session_id="test-session"):
        return os.path.join(self.state_dir(), "%s.json" % session_id)

    def read_state(self, session_id="test-session"):
        with open(self.state_path(session_id), encoding="utf-8") as fh:
            return json.load(fh)

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

    def test_unknown_mode_flag_is_ignored(self):
        result = self.run_hook(self.payload(), args=["--nope"])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")

    def test_missing_session_id_uses_default_state_file(self):
        data = json.dumps({"tool_name": "Edit", "cwd": self.project}).encode()
        result = self.run_hook(data, env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1"})
        self.assertEqual(result.returncode, 0)
        self.assertIn(b"reached 1", result.stdout)
        self.assertEqual(self.read_state("default")["count"], 1)

    # --- threshold environment handling ----------------------------------

    def test_threshold_zero_disables_hook(self):
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "0"}
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")
        self.assertEqual(glob.glob(os.path.join(self.tmp, "unknowns-notes-*")), [])

    def test_negative_threshold_disables_hook(self):
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "-5"}
        )
        self.assertEqual(result.stdout, b"")
        self.assertEqual(glob.glob(os.path.join(self.tmp, "unknowns-notes-*")), [])

    def test_garbage_threshold_warns_and_falls_through_to_legacy_var(self):
        env = {
            "UNKNOWNS_NOTES_THRESHOLD": "not-a-number",
            "FIELD_GUIDE_NOTES_THRESHOLD": "2",
        }
        first = self.run_hook(self.payload(), env_extra=env)
        self.assertEqual(first.stdout, b"")
        self.assertIn(b"not an integer", first.stderr)
        second = self.run_hook(self.payload(), env_extra=env)
        self.assertIn(b"reached 2", second.stdout)

    def test_new_threshold_var_wins_over_legacy(self):
        env = {
            "UNKNOWNS_NOTES_THRESHOLD": "1",
            "FIELD_GUIDE_NOTES_THRESHOLD": "99",
        }
        self.assertIn(b"reached 1", self.run_hook(self.payload(), env_extra=env).stdout)

    # --- firing behavior --------------------------------------------------

    def test_fires_exactly_once_at_threshold(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "3"}
        self.assertEqual(self.run_hook(self.payload(), env_extra=env).stdout, b"")
        self.assertEqual(self.run_hook(self.payload(), env_extra=env).stdout, b"")

        third = self.run_hook(self.payload(), env_extra=env)
        out = json.loads(third.stdout)
        self.assertIn("reached 3", out["systemMessage"])
        # suppressOutput has no effect; a successful hook's stdout is never shown
        self.assertEqual(set(out), {"systemMessage", "hookSpecificOutput"})
        self.assertEqual(
            out["hookSpecificOutput"]["hookEventName"], "PostToolUse"
        )
        self.assertEqual(
            out["hookSpecificOutput"]["additionalContext"], out["systemMessage"]
        )

        state = self.read_state()
        self.assertEqual(state["count"], 3)
        self.assertTrue(state["reminded"])

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

    def test_repeat_mode_accepts_word_values(self):
        for value in ("true", "YES", "on"):
            with self.subTest(value=value):
                sid = "repeat-%s" % value
                env = {"UNKNOWNS_NOTES_THRESHOLD": "1",
                       "UNKNOWNS_NOTES_REPEAT": value}
                first = self.run_hook(self.payload(session_id=sid), env_extra=env)
                second = self.run_hook(self.payload(session_id=sid), env_extra=env)
                self.assertIn(b"reached 1", first.stdout)
                self.assertIn(b"reached 2", second.stdout)

    def test_subagent_edit_counts_but_does_not_consume_the_reminder(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        sub = self.run_hook(
            self.payload(agent_id="sub-1", agent_type="unknowns:unknowns-scout"),
            env_extra=env,
        )
        self.assertEqual(sub.stdout, b"")
        state = self.read_state()
        self.assertEqual(state["count"], 1)
        self.assertFalse(state["reminded"])

        main = self.run_hook(self.payload(), env_extra=env)
        self.assertIn(b"reached 2", main.stdout)

    def test_editing_the_notes_file_is_not_counted(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "2"}
        notes = os.path.join(self.project, "IMPLEMENTATION_NOTES.md")
        for _ in range(3):
            result = self.run_hook(
                self.payload(tool_input={"file_path": notes}), env_extra=env
            )
            self.assertEqual(result.stdout, b"")
        state = self.read_state()
        self.assertEqual(state["count"], 0)
        self.assertTrue(state["notes_touched"])

    def test_notebook_edits_of_the_notes_file_are_not_counted(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        result = self.run_hook(
            self.payload(
                tool_name="NotebookEdit",
                tool_input={"notebook_path": "/elsewhere/IMPLEMENTATION_NOTES.md"},
            ),
            env_extra=env,
        )
        self.assertEqual(result.stdout, b"")
        self.assertEqual(self.read_state()["count"], 0)

    def test_ordinary_edits_are_counted(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        result = self.run_hook(
            self.payload(tool_input={"file_path": os.path.join(self.project, "a.py")}),
            env_extra=env,
        )
        self.assertIn(b"reached 1", result.stdout)

    # --- project opt-in gate ----------------------------------------------

    def test_project_without_notes_file_is_never_reminded(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        result = self.run_hook(self.payload(cwd=self.bare), env_extra=env)
        self.assertEqual(result.stdout, b"")
        self.assertEqual(glob.glob(os.path.join(self.tmp, "unknowns-notes-*")), [])

    def test_unknowns_output_dir_opts_a_project_in_before_notes_exist(self):
        # the loop/plan skills write .unknowns/ long before anyone runs
        # `notes init`; those projects are the hook's intended audience
        os.makedirs(os.path.join(self.bare, ".unknowns"))
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        result = self.run_hook(self.payload(cwd=self.bare), env_extra=env)
        self.assertIn(b"reached 1", result.stdout)
        self.assertIn(b"/unknowns:notes init", result.stdout)

    def test_unknowns_output_dir_is_found_from_a_subdirectory(self):
        os.makedirs(os.path.join(self.bare, ".unknowns"))
        result = self.run_hook(
            self.payload(cwd=os.path.join(self.bare, "src")),
            env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1"},
        )
        self.assertIn(b"reached 1", result.stdout)

    def test_a_file_named_unknowns_does_not_opt_the_project_in(self):
        with open(os.path.join(self.bare, ".unknowns"), "w") as fh:
            fh.write("not a directory\n")
        result = self.run_hook(
            self.payload(cwd=self.bare),
            env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1"},
        )
        self.assertEqual(result.stdout, b"")

    def test_always_flag_overrides_the_gate_and_hints_init(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1", "UNKNOWNS_NOTES_ALWAYS": "1"}
        result = self.run_hook(self.payload(cwd=self.bare), env_extra=env)
        self.assertIn(b"/unknowns:notes init", result.stdout)

    def test_notes_file_found_by_walking_up_from_a_subdirectory(self):
        deep = os.path.join(self.project, "src", "inner")
        os.makedirs(deep)
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        result = self.run_hook(self.payload(cwd=deep), env_extra=env)
        self.assertIn(b"IMPLEMENTATION_NOTES.md.", result.stdout)
        self.assertNotIn(b"/unknowns:notes init", result.stdout)

    def test_project_dir_env_is_used_when_cwd_moved_away(self):
        env = {
            "UNKNOWNS_NOTES_THRESHOLD": "1",
            "CLAUDE_PROJECT_DIR": self.project,
        }
        result = self.run_hook(self.payload(cwd=self.bare), env_extra=env)
        self.assertIn(b"IMPLEMENTATION_NOTES.md.", result.stdout)

    def test_missing_cwd_uses_a_neutral_tail_instead_of_a_relative_lookup(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1", "UNKNOWNS_NOTES_ALWAYS": "1"}
        result = self.run_hook(self.payload(cwd=None), env_extra=env)
        self.assertIn(b"IMPLEMENTATION_NOTES.md.", result.stdout)
        self.assertNotIn(b"/unknowns:notes init", result.stdout)

    # --- state file handling ----------------------------------------------

    def test_session_id_is_sanitized_no_path_traversal(self):
        sid = "../../etc/passwd session!"
        self.run_hook(self.payload(session_id=sid))
        entries = os.listdir(self.state_dir())
        states = [name for name in entries if name.endswith(".json")]
        self.assertEqual(len(states), 1, entries)
        for name in entries:
            self.assertNotIn("/", name)
            self.assertNotIn("!", name)

    def test_corrupted_state_file_resets_instead_of_crashing(self):
        with open(self.state_path(), "w", encoding="utf-8") as fh:
            fh.write("{corrupted")
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "10"}
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.read_state()["count"], 1)

    def test_wrong_typed_state_resets_instead_of_crashing(self):
        for bad in ({"count": "abc"}, {"count": None}, {"count": -3},
                    {"count": True}, {"count": 1, "reminded": "no"}):
            with self.subTest(bad=bad):
                with open(self.state_path(), "w", encoding="utf-8") as fh:
                    json.dump(bad, fh)
                result = self.run_hook(
                    self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "10"}
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, b"")
                self.assertIsInstance(self.read_state()["count"], int)

    def test_persist_failure_warns_and_does_not_fire(self):
        # a directory at the state path makes the atomic replace fail while the
        # state directory itself stays writable
        os.mkdir(os.path.join(self.state_dir(), "blocked.json"))
        result = self.run_hook(
            self.payload(session_id="blocked"),
            env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1"},
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")
        self.assertIn(b"state persist failed", result.stderr)

    @POSIX_ONLY
    def test_state_directory_and_file_are_private(self):
        self.run_hook(self.payload())
        state_dir = self.state_dir()
        self.assertEqual(os.stat(state_dir).st_mode & 0o777, 0o700)
        self.assertEqual(os.stat(self.state_path()).st_mode & 0o777, 0o600)

    @POSIX_ONLY
    def test_planted_state_dir_disables_the_hook(self):
        # a symlink stands in for the real threat: a state directory this user
        # did not create, sitting at a predictable path in a shared temp dir
        state_dir = self.state_dir()
        for name in os.listdir(state_dir):
            os.unlink(os.path.join(state_dir, name))
        os.rmdir(state_dir)
        real = os.path.join(self.tmp, "elsewhere")
        os.makedirs(real)
        os.symlink(real, state_dir)
        result = self.run_hook(
            self.payload(), env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1"}
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")
        self.assertIn(b"not owned by this user", result.stderr)

    def test_plugin_data_dir_is_preferred_when_set(self):
        data_dir = os.path.join(self.tmp, "plugin-data")
        result = self.run_hook(
            self.payload(),
            env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1",
                       "CLAUDE_PLUGIN_DATA": data_dir},
        )
        self.assertIn(b"reached 1", result.stdout)
        self.assertTrue(
            os.path.exists(os.path.join(data_dir, "state", "test-session.json"))
        )
        self.assertEqual(glob.glob(os.path.join(self.tmp, "unknowns-notes-*")), [])

    def test_concurrent_invocations_are_all_counted(self):
        env = self.env({"UNKNOWNS_NOTES_THRESHOLD": "1000"})
        data = self.payload(session_id="race")
        count = 20
        procs = [
            subprocess.Popen(
                [sys.executable, SCRIPT],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, env=env, cwd=self.tmp,
            )
            for _ in range(count)
        ]
        try:
            for proc in procs:
                proc.stdin.write(data)  # buffered: nothing runs until close
            for proc in procs:
                proc.stdin.close()      # release them together
            for proc in procs:
                self.assertEqual(proc.wait(timeout=60), 0)
        finally:
            for proc in procs:
                for stream in (proc.stdin, proc.stdout, proc.stderr):
                    if stream and not stream.closed:
                        stream.close()
                if proc.poll() is None:
                    proc.kill()
        self.assertEqual(self.read_state("race")["count"], count)

    # --- encoding ----------------------------------------------------------

    def test_non_ascii_payload_is_counted_on_a_legacy_codepage(self):
        data = self.payload(
            tool_input={"file_path": "/x/파일.md", "new_string": "한글 🎉"}
        )
        result = self.run_hook(
            data,
            env_extra={"UNKNOWNS_NOTES_THRESHOLD": "10",
                       "PYTHONIOENCODING": "ascii"},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.read_state()["count"], 1)

    def test_emitted_json_is_ascii_on_a_legacy_codepage(self):
        for encoding in ("ascii", "cp949", "cp932"):
            with self.subTest(encoding=encoding):
                result = self.run_hook(
                    self.payload(session_id="enc-%s" % encoding, cwd=self.bare),
                    env_extra={"UNKNOWNS_NOTES_THRESHOLD": "1",
                               "UNKNOWNS_NOTES_ALWAYS": "1",
                               "PYTHONIOENCODING": encoding},
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                result.stdout.decode("ascii")  # raises if any byte is non-ASCII
                json.loads(result.stdout)

    # --- SessionStart / Stop / SessionEnd modes ----------------------------

    def test_session_start_reinjects_the_rule_and_rearms(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        self.assertIn(b"reached 1", self.run_hook(self.payload(), env_extra=env).stdout)
        self.assertTrue(self.read_state()["reminded"])

        restart = self.run_hook(
            self.payload(), env_extra=env, args=["--session-start"]
        )
        self.assertEqual(restart.returncode, 0)
        self.assertIn(b"IMPLEMENTATION_NOTES.md", restart.stdout)
        self.assertFalse(self.read_state()["reminded"])
        # the PostToolUse reminder can fire again after compaction
        self.assertIn(b"reached 2", self.run_hook(self.payload(), env_extra=env).stdout)

    def test_session_start_is_silent_in_a_project_without_notes(self):
        result = self.run_hook(
            self.payload(cwd=self.bare), args=["--session-start"]
        )
        self.assertEqual(result.stdout, b"")

    def test_stop_fires_once_when_notes_were_never_written(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "2"}
        self.run_hook(self.payload(), env_extra=env)
        self.run_hook(self.payload(), env_extra=env)

        first = self.run_hook(self.payload(), env_extra=env, args=["--stop"])
        out = json.loads(first.stdout)
        self.assertEqual(out["hookSpecificOutput"]["hookEventName"], "Stop")
        self.assertIn("was not updated", out["systemMessage"])
        self.assertTrue(self.read_state()["stop_reminded"])

        second = self.run_hook(self.payload(), env_extra=env, args=["--stop"])
        self.assertEqual(second.stdout, b"")

    def test_stop_is_silent_when_the_notes_file_was_touched(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        self.run_hook(self.payload(), env_extra=env)
        self.run_hook(
            self.payload(tool_input={"file_path": "/x/IMPLEMENTATION_NOTES.md"}),
            env_extra=env,
        )
        result = self.run_hook(self.payload(), env_extra=env, args=["--stop"])
        self.assertEqual(result.stdout, b"")

    def test_stop_is_silent_below_the_threshold_and_while_looping(self):
        env = {"UNKNOWNS_NOTES_THRESHOLD": "5"}
        self.run_hook(self.payload(), env_extra=env)
        below = self.run_hook(self.payload(), env_extra=env, args=["--stop"])
        self.assertEqual(below.stdout, b"")

        env = {"UNKNOWNS_NOTES_THRESHOLD": "1"}
        self.run_hook(self.payload(), env_extra=env)
        looping = self.run_hook(
            self.payload(stop_hook_active=True), env_extra=env, args=["--stop"]
        )
        self.assertEqual(looping.stdout, b"")

    def test_cleanup_removes_the_session_state(self):
        self.run_hook(self.payload())
        path = self.state_path()
        self.assertTrue(os.path.exists(path))
        result = self.run_hook(self.payload(), args=["--cleanup"])
        self.assertEqual(result.returncode, 0)
        self.assertFalse(os.path.exists(path))

    def test_cleanup_is_harmless_without_state(self):
        result = self.run_hook(self.payload(session_id="never-ran"),
                               args=["--cleanup"])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, b"")


class HooksJsonTest(unittest.TestCase):
    """hooks.json is what Claude Code actually runs; the tests above bypass it."""

    def setUp(self):
        with open(HOOKS_JSON, encoding="utf-8") as fh:
            self.config = json.load(fh)
        self.events = self.config["hooks"]

    def handlers(self):
        for event, entries in self.events.items():
            for entry in entries:
                for handler in entry["hooks"]:
                    yield event, entry, handler

    def test_declares_every_event_the_plugin_relies_on(self):
        self.assertEqual(
            set(self.events),
            {"PreToolUse", "PostToolUse", "SessionStart", "Stop", "SessionEnd"},
        )

    def test_exec_form_with_args_so_paths_with_spaces_survive(self):
        for event, _entry, handler in self.handlers():
            with self.subTest(event=event):
                self.assertEqual(handler["type"], "command")
                self.assertEqual(handler["command"], "python3")
                script = handler["args"][0]
                self.assertTrue(script.startswith("${CLAUDE_PLUGIN_ROOT}/"), script)
                relative = script[len("${CLAUDE_PLUGIN_ROOT}/"):]
                self.assertTrue(os.path.exists(os.path.join(ROOT, relative)), script)

    def test_post_tool_use_matcher_lists_exactly_the_edit_tools(self):
        entries = self.events["PostToolUse"]
        self.assertEqual(len(entries), 1)
        matcher = entries[0]["matcher"]
        # The matcher is a literal tool-name list, not a regex. MultiEdit is not
        # a tool in current releases; NotebookEdit is and must be counted.
        self.assertEqual(set(matcher.split("|")), {"Edit", "Write", "NotebookEdit"})

    def test_pre_tool_use_guards_bash_for_the_read_only_agents(self):
        entries = self.events["PreToolUse"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["matcher"], "Bash")
        self.assertIn(
            "agent_readonly_guard.py", entries[0]["hooks"][0]["args"][0]
        )

    def test_session_start_only_reruns_after_compaction(self):
        entries = self.events["SessionStart"]
        self.assertEqual([e["matcher"] for e in entries], ["compact"])
        self.assertIn("--session-start", entries[0]["hooks"][0]["args"])


if __name__ == "__main__":
    unittest.main()
