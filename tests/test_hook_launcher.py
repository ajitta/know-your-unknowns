"""Tests for the interpreter launcher in hooks/hooks.json.

Standard library only (unittest) — run with:
    python3 -m unittest discover -s tests -v

Every handler in hooks.json is one shell string, because exec form
(`command` + `args`) has to name one interpreter, and no single name works on
every platform: Windows usually has no `python3`, or has the Microsoft Store
stub that exits 9009. Claude Code runs a shell string with `sh -c` on Linux and
macOS, with Git Bash on Windows, and with PowerShell on Windows when Git Bash is
missing (hooks reference, "Exec form and shell form"). The string is therefore
a sh/PowerShell polyglot:

    echo `# <#` >/dev/null; <sh part> #> > $null; <PowerShell part>

sh sees an empty command substitution, runs the sh part and treats the rest of
the line as a comment. PowerShell sees `echo '#'`, a block comment `<# ... #>`
over the sh part, and `> $null` that silences the echo.

- sh part: off Windows it is `exec python3 "<script>" <args>`, the same process,
  argv, stdout/stderr and script exit codes as the old exec-form hook. On Windows (`OS=Windows_NT`, Git
  Bash) it probes python3, python and `py -3` with a one-line check that the
  interpreter is Python 3, and execs the first that passes.
- PowerShell part: the same probe and order.

Exit codes are what the PreToolUse guard's fail-safe depends on, so they are
pinned here for every shell: a deny is JSON on exit 0; a missing script is
Python's exit 2, which blocks the call (as the exec-form hook did); no
interpreter at all is a non-zero exit other than 2: on Linux and macOS the
shell's own `exec: python3: not found` (127), on Windows the launcher's
message and exit 1. Claude Code treats either as a non-blocking error, as it
did the exec-form hook's "cannot start". One exception is documented: on
Windows without Git Bash a failing shell-form PreToolUse hook can block the
call unless `onFailure` is set, so the guard sets `"onFailure": "continue"`
(exit 2 is a verdict, not a failure, and still blocks).

These tests run each handler's string through every shell this machine has:
sh, bash and dash on POSIX, Git Bash and Windows PowerShell on Windows, and
pwsh wherever it is installed. `ClaudeCodeTest` then runs the real
`claude --init-only` (when `claude` is on PATH), which fires SessionStart from
the real hooks.json without logging in.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS_JSON = os.path.join(ROOT, "hooks", "hooks.json")
WINDOWS = os.name == "nt"
ACTIVE_MARKER = "[unknowns] hooks active"
NO_PYTHON = "[unknowns] no working Python 3 found"

# The one launcher every handler uses; {script} and {args} vary per handler.
SH_PART = (
    'echo `# <#` >/dev/null; '
    's="${{CLAUDE_PLUGIN_ROOT}}/hooks/scripts/{script}"; '
    'for p in python3 python "py -3"; do '
    "[ \"${{OS-}}\" != Windows_NT ] || "
    "$p -c 'import sys;sys.exit(sys.version_info<(3,))' </dev/null >/dev/null 2>&1 || continue; "
    'exec $p "$s"{args}; done; '
    'echo "[unknowns] no working Python 3 found (tried python3, python, py -3)" >&2; exit 1 '
)
PS_PART = (
    '#> > $null; '
    '$s = "${{CLAUDE_PLUGIN_ROOT}}/hooks/scripts/{script}"; '
    "foreach ($p in 'python3', 'python', 'py') {{ "
    "$a = @(); if ($p -eq 'py') {{ $a = @('-3') }}; "
    "if (Get-Command $p -CommandType Application -ErrorAction SilentlyContinue) {{ "
    "& $p @a -c 'import sys;sys.exit(sys.version_info<(3,))' 2>$null; "
    "if ($LASTEXITCODE -eq 0) {{ & $p @a $s{args}; exit $LASTEXITCODE }} }} }}; "
    "[Console]::Error.WriteLine('[unknowns] no working Python 3 found "
    "(tried python3, python, py -3)'); exit 1"
)

# event -> (script, arguments) the launcher must run
EXPECTED = {
    "PreToolUse": ("agent_readonly_guard.py", ()),
    "PostToolUse": ("impl_notes_reminder.py", ()),
    "SessionStart": ("impl_notes_reminder.py", ("--session-start",)),
    "Stop": ("impl_notes_reminder.py", ("--stop",)),
    "SessionEnd": ("impl_notes_reminder.py", ("--cleanup",)),
}


def render(script, args):
    joined = "".join(" " + a for a in args)
    return (SH_PART + PS_PART).format(script=script, args=joined)


def load_handlers():
    with open(HOOKS_JSON, encoding="utf-8") as fh:
        config = json.load(fh)
    out = {}
    for event, entries in config["hooks"].items():
        for entry in entries:
            for handler in entry["hooks"]:
                out.setdefault(event, []).append(handler)
    return out


def command_for(event):
    return load_handlers()[event][0]["command"]


def _git_bash():
    configured = os.environ.get("CLAUDE_CODE_GIT_BASH_PATH")
    if configured and os.path.isfile(configured):
        return configured
    for base in (os.environ.get("ProgramFiles"), os.environ.get("ProgramW6432"),
                 os.environ.get("LOCALAPPDATA") and
                 os.path.join(os.environ["LOCALAPPDATA"], "Programs")):
        if base:
            candidate = os.path.join(base, "Git", "bin", "bash.exe")
            if os.path.isfile(candidate):
                return candidate
    return None


def shells():
    """(name, kind, executable) for every shell Claude Code may use here."""
    found = []
    if WINDOWS:
        bash = _git_bash()
        if bash:
            found.append(("git-bash", "sh", bash))
        for name in ("powershell", "pwsh"):
            exe = shutil.which(name)
            if exe:
                found.append((name, "ps", exe))
    else:
        seen = set()
        for name in ("sh", "bash", "dash"):
            exe = shutil.which(name)
            if exe and os.path.realpath(exe) not in seen:
                seen.add(os.path.realpath(exe))
                found.append((name, "sh", exe))
        exe = shutil.which("pwsh")
        if exe:
            found.append(("pwsh", "ps", exe))
    return found


def shell_argv(kind, exe, command):
    """The command line Claude Code builds, as far as the docs describe it.

    sh gets the placeholder unchanged and expands it from the exported
    CLAUDE_PLUGIN_ROOT; PowerShell gets the documented `${env:NAME}` rewrite.
    """
    if kind == "sh":
        return [exe, "-c", command]
    command = command.replace("${CLAUDE_PLUGIN_ROOT}", "${env:CLAUDE_PLUGIN_ROOT}")
    return [exe, "-NoProfile", "-NonInteractive", "-Command", command]


class LauncherTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = self._tmp.name
        self.addCleanup(self._tmp.cleanup)
        self.shells = shells()
        if not self.shells:
            self.skipTest("no shell found")

    def env(self, path=None, plugin_root=ROOT, **extra):
        env = dict(os.environ)
        for name in ("UNKNOWNS_NOTES_THRESHOLD", "UNKNOWNS_NOTES_ALWAYS",
                     "UNKNOWNS_AGENT_GUARD", "CLAUDE_PLUGIN_DATA",
                     "CLAUDE_PROJECT_DIR"):
            env.pop(name, None)
        env["TMPDIR"] = env["TEMP"] = env["TMP"] = self.tmp
        env["CLAUDE_PLUGIN_ROOT"] = plugin_root
        if path is not None:
            env["PATH"] = path
        env.update(extra)
        return env

    def run_shell(self, kind, exe, event, payload, env):
        return subprocess.run(
            shell_argv(kind, exe, command_for(event)),
            input=json.dumps(payload).encode("utf-8"),
            capture_output=True, env=env, cwd=self.tmp, timeout=60,
        )

    def session_start(self, kind, exe, env):
        payload = {"session_id": "launcher-test", "source": "startup",
                   "cwd": self.tmp, "hook_event_name": "SessionStart"}
        env.setdefault("UNKNOWNS_NOTES_ALWAYS", "1")
        return self.run_shell(kind, exe, "SessionStart", payload, env)

    def scout_rm(self, kind, exe, env):
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash",
                   "tool_input": {"command": "rm -rf build"},
                   "agent_type": "unknowns:unknowns-scout", "agent_id": "a1"}
        return self.run_shell(kind, exe, "PreToolUse", payload, env)

    def assertMarker(self, result, label):
        self.assertEqual(result.returncode, 0, (label, result.stderr))
        self.assertIn(ACTIVE_MARKER, result.stdout.decode("utf-8", "replace"),
                      (label, result.stderr))

    def assertDeny(self, result, label):
        self.assertEqual(result.returncode, 0, (label, result.stderr))
        out = json.loads(result.stdout.decode("utf-8"))["hookSpecificOutput"]
        self.assertEqual(out["permissionDecision"], "deny", label)


class HooksJsonLauncherTest(unittest.TestCase):
    def test_every_handler_is_the_shared_launcher_in_shell_form(self):
        handlers = load_handlers()
        self.assertEqual(set(handlers), set(EXPECTED))
        for event, (script, args) in EXPECTED.items():
            with self.subTest(event=event):
                self.assertEqual(len(handlers[event]), 1)
                handler = handlers[event][0]
                self.assertEqual(handler["type"], "command")
                # `args` would switch the handler to exec form, `shell` would
                # pin one shell; both defeat the per-platform choice.
                self.assertNotIn("args", handler)
                self.assertNotIn("shell", handler)
                # Only the guard sets onFailure, and only to keep a failure
                # non-blocking on Windows without Git Bash (exit 2 still blocks).
                if event == "PreToolUse":
                    self.assertEqual(handler.get("onFailure"), "continue")
                else:
                    self.assertNotIn("onFailure", handler)
                self.assertEqual(handler["command"], render(script, args))
                self.assertTrue(os.path.isfile(
                    os.path.join(ROOT, "hooks", "scripts", script)))

    def test_the_guard_matches_bash_only(self):
        # onFailure keeps a widened matcher safe too, but a change here should
        # be deliberate: the guarded agents have no PowerShell tool.
        with open(HOOKS_JSON, encoding="utf-8") as fh:
            entries = json.load(fh)["hooks"]["PreToolUse"]
        self.assertEqual([e["matcher"] for e in entries], ["Bash"])

    def test_timeouts_are_unchanged(self):
        handlers = load_handlers()
        for event in ("PreToolUse", "PostToolUse", "SessionStart", "Stop"):
            self.assertEqual(handlers[event][0].get("timeout"), 5, event)
        self.assertNotIn("timeout", handlers["SessionEnd"][0])

    def test_the_sh_part_hides_nothing_from_the_powershell_comment(self):
        # A `#>` inside the sh part would end PowerShell's block comment early.
        self.assertNotIn("#>", SH_PART)
        self.assertNotIn("<#", SH_PART.replace("`# <#`", ""))


class ShellsTest(LauncherTestCase):
    def test_lists_the_shells_it_found(self):
        # Shows in `-v` output which shells the run below actually covered.
        names = [name for name, _kind, _exe in self.shells]
        print("\n    shells: %s; python3=%s python=%s py=%s" % (
            ", ".join(names), shutil.which("python3"), shutil.which("python"),
            shutil.which("py")), file=sys.stderr)
        if WINDOWS and os.environ.get("CI"):
            self.assertIn("git-bash", names)
            self.assertIn("powershell", names)

    def test_session_start_marker_through_every_shell(self):
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                self.assertMarker(self.session_start(kind, exe, self.env()), name)

    def test_guard_denies_through_every_shell(self):
        # stdin must reach the script: the deny depends on the payload
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                self.assertDeny(self.scout_rm(kind, exe, self.env()), name)

    def test_main_thread_bash_stays_silent_through_every_shell(self):
        payload = {"hook_event_name": "PreToolUse", "tool_name": "Bash",
                   "tool_input": {"command": "rm -rf build"}}
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                result = self.run_shell(kind, exe, "PreToolUse", payload, self.env())
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), b"", name)

    def test_plugin_root_with_spaces_and_dollar(self):
        root = os.path.join(self.tmp, "plug in $HOME")
        shutil.copytree(os.path.join(ROOT, "hooks"), os.path.join(root, "hooks"))
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                env = self.env(plugin_root=root)
                self.assertMarker(self.session_start(kind, exe, env), name)

    def test_missing_script_still_blocks_with_exit_2(self):
        # The exec-form hook ran `python3 <missing>`, which exits 2: on
        # PreToolUse that blocks the call (open-questions A7). Keep it.
        empty = os.path.join(self.tmp, "no-plugin")
        os.makedirs(empty)
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                result = self.scout_rm(kind, exe, self.env(plugin_root=empty))
                self.assertEqual(result.returncode, 2, (name, result.stderr))

    def test_no_python_is_a_non_blocking_failure(self):
        # No interpreter: exit non-zero but never 2, with a message, so
        # Claude Code reports a non-blocking error instead of denying every
        # Bash call or failing silently.
        bare = os.path.join(self.tmp, "bare-bin")
        os.makedirs(bare)
        path = bare
        if WINDOWS:
            path = os.pathsep.join(
                (bare, os.path.join(os.environ.get("SystemRoot", r"C:\Windows"),
                                    "System32")))
        for candidate in ("python3", "python", "py"):
            if shutil.which(candidate, path=path):
                self.skipTest("%s is still reachable on %s" % (candidate, path))
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                result = self.scout_rm(kind, exe, self.env(path=path))
                self.assertNotIn(result.returncode, (0, 2), (name, result.stderr))
                self.assertNotEqual(result.stderr.strip(), b"", name)
                if WINDOWS or kind == "ps":
                    self.assertIn(NO_PYTHON, result.stderr.decode("utf-8", "replace"))

    def test_a_broken_python3_falls_back_on_windows(self):
        # The Microsoft Store stub is a python3 that exists and exits 9009.
        # Put a python3 that fails first on PATH; the launcher must move on.
        # POSIX shells take the Windows branch when OS=Windows_NT is set.
        fake = os.path.join(self.tmp, "fake-bin")
        os.makedirs(fake)
        if WINDOWS:
            where = os.path.join(os.environ.get("SystemRoot", r"C:\Windows"),
                                 "System32", "where.exe")
            shutil.copy(where, os.path.join(fake, "python3.exe"))  # rejects -c
            real = os.path.dirname(sys.executable)
            extra = {}
        else:
            stub = os.path.join(fake, "python3")
            with open(stub, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("#!/bin/sh\nexit 49\n")  # 9009 & 0xFF
            os.chmod(stub, 0o755)
            os.symlink(sys.executable, os.path.join(fake, "python"))
            real = None
            extra = {"OS": "Windows_NT"}
        path = fake if real is None else os.pathsep.join((fake, real))
        if WINDOWS:
            path = os.pathsep.join((path, os.path.join(
                os.environ.get("SystemRoot", r"C:\Windows"), "System32")))
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                env = self.env(path=path, **extra)
                self.assertDeny(self.scout_rm(kind, exe, env), name)
                self.assertMarker(self.session_start(kind, exe, dict(env)), name)

    @unittest.skipIf(WINDOWS, "POSIX stubs; the probe string is the same on Windows")
    def test_a_python_2_is_skipped_for_py_3(self):
        # A `python` that runs `-c` but is Python 2 must not win over `py -3`.
        # The stub reports version 2.7 to any -c code and fails on a script.
        fake = os.path.join(self.tmp, "py2-bin")
        os.makedirs(fake)
        stubs = {
            "python3": "#!/bin/sh\nexit 49\n",
            "python": ('#!/bin/sh\nif [ "$1" = -c ]; then exec "%s" -c '
                       '"import sys; sys.version_info = (2, 7, 18); '
                       'exec(compile(sys.argv[1], \'<c>\', \'exec\'))" "$2"; fi\n'
                       'echo "SyntaxError: invalid syntax" >&2; exit 1\n'
                       ) % sys.executable,
            "py": '#!/bin/sh\n[ "$1" = -3 ] && shift\nexec "%s" "$@"\n' % sys.executable,
        }
        for name, body in stubs.items():
            path = os.path.join(fake, name)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(body)
            os.chmod(path, 0o755)
        path = os.pathsep.join((fake, "/usr/bin", "/bin"))
        for name, kind, exe in self.shells:
            with self.subTest(shell=name):
                env = self.env(path=path, OS="Windows_NT")
                self.assertDeny(self.scout_rm(kind, exe, env), name)

    @unittest.skipIf(WINDOWS, "the POSIX branch never runs on Windows")
    def test_posix_branch_is_a_plain_exec_of_python3(self):
        # Off Windows the sh part must not probe or fall back: python3 or
        # nothing, like the exec-form hook. A failing python3 is not skipped.
        fake = os.path.join(self.tmp, "fake-bin")
        os.makedirs(fake)
        stub = os.path.join(fake, "python3")
        with open(stub, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("#!/bin/sh\necho stub-ran >&2\nexit 49\n")
        os.chmod(stub, 0o755)
        os.symlink(sys.executable, os.path.join(fake, "python"))
        env = self.env(path=fake)
        env.pop("OS", None)
        for name, kind, exe in self.shells:
            if kind != "sh":
                continue
            with self.subTest(shell=name):
                result = self.scout_rm(kind, exe, env)
                self.assertEqual(result.returncode, 49, (name, result.stderr))
                self.assertIn(b"stub-ran", result.stderr)


def _claude():
    if os.environ.get("UNKNOWNS_SKIP_CLAUDE") == "1":
        return None
    return shutil.which("claude")


# CI sets this so a missing CLI or shell fails the run instead of skipping.
REQUIRED = os.environ.get("UNKNOWNS_REQUIRE_CLAUDE") == "1"


@unittest.skipUnless(_claude() or REQUIRED, "claude CLI not on PATH")
class ClaudeCodeTest(unittest.TestCase):
    """The real Claude Code resolves and runs the hooks.json command.

    `claude --init-only` fires SessionStart without logging in, so it needs no
    credentials; an empty CLAUDE_CONFIG_DIR keeps the user's own config out.
    The marker in the debug log is the hook's stdout as Claude Code read it.
    """

    def setUp(self):
        if not _claude():
            self.fail("UNKNOWNS_REQUIRE_CLAUDE=1 but claude is not on PATH")
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = self._tmp.name
        self.addCleanup(self._tmp.cleanup)

    def run_claude(self, plugin_dir, env_extra=None):
        project = os.path.join(self.tmp, "project")
        config = os.path.join(self.tmp, "config")
        os.makedirs(project, exist_ok=True)
        os.makedirs(config, exist_ok=True)
        log = os.path.join(self.tmp, "debug.log")
        env = dict(os.environ)
        env.pop("UNKNOWNS_NOTES_THRESHOLD", None)
        env.update({"CLAUDE_CONFIG_DIR": config, "UNKNOWNS_NOTES_ALWAYS": "1",
                    "TMPDIR": self.tmp, "TEMP": self.tmp, "TMP": self.tmp})
        env.update(env_extra or {})
        result = subprocess.run(
            [_claude(), "--init-only", "--plugin-dir", plugin_dir,
             "--debug-file", log],
            capture_output=True, env=env, cwd=project, timeout=180,
        )
        text = ""
        if os.path.exists(log):
            with open(log, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        return result, text

    def hook_lines(self, log):
        return "\n".join(l for l in log.splitlines() if "SessionStart" in l)

    def plugin_copy(self, shell, probe):
        """The plugin's hooks in a temp copy, plus one SessionStart probe hook
        that prints which shell ran it; `shell` pins every handler to it."""
        # A space and a literal `$HOME` in the path: if Claude Code ever
        # substituted the placeholder as text in sh form, this would break.
        plugin = os.path.join(self.tmp, "plug in $HOME")
        shutil.copytree(os.path.join(ROOT, "hooks"), os.path.join(plugin, "hooks"))
        shutil.copytree(os.path.join(ROOT, ".claude-plugin"),
                        os.path.join(plugin, ".claude-plugin"))
        hooks_json = os.path.join(plugin, "hooks", "hooks.json")
        with open(hooks_json, encoding="utf-8") as fh:
            config = json.load(fh)
        probe_handler = {"type": "command", "command": probe}
        if shell:
            probe_handler["shell"] = shell
            for entries in config["hooks"].values():
                for entry in entries:
                    for handler in entry["hooks"]:
                        handler["shell"] = shell
        config["hooks"]["SessionStart"][0]["hooks"].append(probe_handler)
        with open(hooks_json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(config, fh, indent=2)
        return plugin

    def assertHookPrinted(self, log, text):
        # The launcher's own command text never contains the marker, so the
        # marker in the log can only be the hook's output.
        self.assertNotIn(text, render("x", ()))
        self.assertIn(text, log, self.hook_lines(log)[-2000:])

    def test_session_start_fires_from_the_real_hooks_json(self):
        # The default shell, from the `plug in $HOME` copy: proves sh form
        # gets the path from the environment, not by text substitution.
        plugin = self.plugin_copy(None, 'echo "[probe] root=$CLAUDE_PLUGIN_ROOT"')
        result, log = self.run_claude(plugin)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertRegex(log, r"\[probe\] root=.*plug in \$HOME", self.hook_lines(log)[-2000:])
        print("\n    " + self.hook_lines(log)[-600:], file=sys.stderr)
        self.assertHookPrinted(log, ACTIVE_MARKER)

    def test_session_start_fires_through_powershell(self):
        # Windows without Git Bash runs the same string in PowerShell. Pin
        # PowerShell with `shell` in a copy and prove it ran there.
        if not (shutil.which("pwsh") or (WINDOWS and shutil.which("powershell"))):
            if REQUIRED:
                self.fail("UNKNOWNS_REQUIRE_CLAUDE=1 but no PowerShell on PATH")
            self.skipTest("no PowerShell")
        plugin = self.plugin_copy(
            "powershell", 'echo "[probe] edition=$($PSVersionTable.PSEdition)"')
        result, log = self.run_claude(plugin)
        self.assertEqual(result.returncode, 0, result.stderr)
        print("\n    " + self.hook_lines(log)[-600:], file=sys.stderr)
        self.assertRegex(log, r"\[probe\] edition=(Core|Desktop)",
                         self.hook_lines(log)[-2000:])
        self.assertHookPrinted(log, ACTIVE_MARKER)

    @unittest.skipUnless(WINDOWS, "Git Bash is the Windows default shell")
    def test_windows_runs_the_default_form_in_git_bash(self):
        # With Git for Windows installed the same string runs in Git Bash, so
        # the test above covered PowerShell and this one covers the sh part.
        plugin = self.plugin_copy(None, 'echo "[probe] bash=${BASH_VERSION:-none}"')
        result, log = self.run_claude(plugin)
        self.assertEqual(result.returncode, 0, result.stderr)
        print("\n    " + self.hook_lines(log)[-600:], file=sys.stderr)
        self.assertRegex(log, r"\[probe\] bash=\d", self.hook_lines(log)[-2000:])
        self.assertHookPrinted(log, ACTIVE_MARKER)


if __name__ == "__main__":
    unittest.main()
