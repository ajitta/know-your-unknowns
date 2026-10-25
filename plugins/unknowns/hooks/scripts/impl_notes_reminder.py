#!/usr/bin/env python3
"""[unknowns] IMPLEMENTATION_NOTES.md reminder hook.

Four modes, one script (see hooks/hooks.json):

- no argument       PostToolUse(Edit|Write|NotebookEdit): count file edits and,
                    at the threshold, remind the user and Claude to record plan
                    deviations in IMPLEMENTATION_NOTES.md
- --session-start   SessionStart: on startup/resume/clear/fork, announce the
                    "[unknowns] hooks active" marker the skills key on, only
                    while a reminder is still to come; after compaction,
                    restate the rule (compaction summarized the reminder away),
                    re-arm it, and carry the marker when re-arming persisted;
                    also point back at an unfinished loop (.unknowns/loop.json
                    with status "active")
- --stop            Stop: if the threshold was crossed and the notes file was
                    never touched, say so once (touched = edited through
                    Edit/Write, or the file appeared or its mtime changed since
                    the session's first counted edit, which catches Bash appends)
- --cleanup         SessionEnd: delete this session's state file

Opt-in by project: the reminder fires where the project already uses the
methodology - an IMPLEMENTATION_NOTES.md, or the `.unknowns/` directory the
skills write their output to (searched from CLAUDE_PROJECT_DIR, then the hook's
cwd, walking up to the repo root). UNKNOWNS_NOTES_ALWAYS=1 fires everywhere.
Where the project opted in but the notes file does not exist yet, the reminder
carries the "create the file" hint.

- Standard library only (no external deps such as jq)
- State lives under ${CLAUDE_PLUGIN_DATA}/state, else a 0700 per-user directory
  in the temp dir; writes are locked and atomic
- UNKNOWNS_NOTES_THRESHOLD adjusts the threshold; 0 disables
  (legacy FIELD_GUIDE_NOTES_THRESHOLD also recognized)
- Default: once per session. UNKNOWNS_NOTES_REPEAT=1 repeats at every
  threshold multiple (10, 20, 30...)
"""
import getpass
import json
import os
import re
import sys
import tempfile

NOTES_NAME = "IMPLEMENTATION_NOTES.md"
# where every skill's output ladder falls back to and where the loop keeps
# loop.json, so its presence means this project has run the methodology
WORK_DIR = ".unknowns"
DEFAULT_THRESHOLD = 10
# what the skills look for in context to know the reminder runs here
ACTIVE_MARKER = "[unknowns] hooks active"
MAX_WALK = 40


def _warn(text):
    # hook stderr on exit 0 is visible in Claude Code's debug output only
    try:
        sys.stderr.write("[unknowns] %s\n" % text)
    except Exception:
        pass


def _env_int(names, default):
    for name in names:
        raw = os.environ.get(name)
        if raw is None:
            continue
        try:
            return int(raw)
        except ValueError:
            _warn("ignoring %s=%r (not an integer)" % (name, raw))
    return default


def _env_flag(name):
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def _safe(text, limit):
    return re.sub(r"[^A-Za-z0-9._-]", "_", text)[:limit]


# --- state -----------------------------------------------------------------

def _state_dir(create=True):
    """Private directory for state files, or None if no safe one exists."""
    data = os.environ.get("CLAUDE_PLUGIN_DATA")
    if data:
        path = os.path.join(data, "state")
    else:
        try:
            user = getpass.getuser()
        except Exception:
            user = "user"
        path = os.path.join(
            tempfile.gettempdir(), "unknowns-notes-%s" % (_safe(user, 32) or "user")
        )
    if not os.path.isdir(path):
        if not create:
            return None
        try:
            os.makedirs(path, mode=0o700, exist_ok=True)
        except Exception as exc:
            _warn("state dir unavailable: %s" % exc)
            return None
    # a shared temp dir means another user could have planted this directory
    try:
        stat = os.lstat(path)
    except Exception as exc:
        _warn("state dir unavailable: %s" % exc)
        return None
    getuid = getattr(os, "getuid", None)
    if os.path.islink(path) or (getuid is not None and stat.st_uid != getuid()):
        _warn("state dir %s is not owned by this user - reminder disabled" % path)
        return None
    return path


def _state_path(state_dir, session_id):
    return os.path.join(state_dir, "%s.json" % (_safe(session_id, 64) or "default"))


def _lock(state_path):
    """Best-effort exclusive lock across the read-modify-write."""
    try:
        fd = os.open(state_path + ".lock", os.O_CREAT | os.O_RDWR, 0o600)
    except Exception:
        return None
    try:
        import fcntl

        fcntl.flock(fd, fcntl.LOCK_EX)
    except Exception:
        try:
            import msvcrt

            msvcrt.locking(fd, msvcrt.LK_LOCK, 1)
        except Exception:
            pass
    return fd


def _unlock(fd):
    if fd is None:
        return
    try:
        import fcntl

        fcntl.flock(fd, fcntl.LOCK_UN)
    except Exception:
        pass
    try:
        os.close(fd)
    except Exception:
        pass


def _read_state(state_path):
    state = {
        "count": 0,
        "reminded": False,
        "notes_touched": False,
        "stop_reminded": False,
        # the notes file as it stood at the first counted edit:
        # None = not recorded (older state file), else
        # {"path", "exists", "mtime"} plus, when absent, "candidates": the
        # paths that were looked at and found empty
        "notes_at_start": None,
    }
    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            loaded = json.load(fh)
    except Exception:
        return state
    if not isinstance(loaded, dict):
        return state
    count = loaded.get("count")
    if isinstance(count, int) and not isinstance(count, bool) and count >= 0:
        state["count"] = count
    for flag in ("reminded", "notes_touched", "stop_reminded"):
        state[flag] = bool(loaded.get(flag))
    snap = loaded.get("notes_at_start")
    if isinstance(snap, dict) and isinstance(snap.get("exists"), bool):
        mtime = snap.get("mtime")
        path = snap.get("path") if isinstance(snap.get("path"), str) else None
        candidates = snap.get("candidates")
        if not snap["exists"] and isinstance(candidates, list):
            state["notes_at_start"] = {
                "path": None, "exists": False, "mtime": None,
                "candidates": [c for c in candidates if isinstance(c, str)],
            }
        elif path and isinstance(mtime, (int, float)) and not isinstance(mtime, bool):
            state["notes_at_start"] = {"path": path, "exists": True, "mtime": float(mtime)}
    return state


def _notes_candidates(bases):
    """Every path _find_markers checks for the notes file, in the same walk."""
    found = []
    for base in bases:
        try:
            current = os.path.abspath(base)
        except Exception:
            continue
        for _ in range(MAX_WALK):
            found.append(os.path.realpath(os.path.join(current, NOTES_NAME)))
            if os.path.exists(os.path.join(current, ".git")):
                break
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent
    return found


def _notes_snapshot(notes_path, bases=()):
    """The notes file the gate found right now; when none, where it looked."""
    if notes_path is not None:
        try:
            return {"path": os.path.realpath(notes_path), "exists": True,
                    "mtime": os.path.getmtime(notes_path)}
        except OSError:
            pass
    return {"path": None, "exists": False, "mtime": None,
            "candidates": _notes_candidates(bases)}


def _write_state(state_path, state):
    """Atomic replace; returns False (with a warning) when it could not persist."""
    tmp_path = "%s.%d.tmp" % (state_path, os.getpid())
    try:
        fd = os.open(tmp_path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(state, fh)
        os.replace(tmp_path, state_path)
        return True
    except Exception as exc:
        # without persistence the counter cannot advance, and a pre-seeded state
        # file would otherwise re-fire on every edit
        _warn("state persist failed: %s" % exc)
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        return False


# --- payload and project ----------------------------------------------------

def _read_payload():
    """Parse stdin as UTF-8 bytes; None when there is nothing usable."""
    try:
        raw = sys.stdin.buffer.read()
    except Exception:
        return None
    if not raw:
        return None
    try:
        data = json.loads(raw.decode("utf-8", "replace"))
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def _emit(payload):
    # ASCII-only JSON, written as bytes: a legacy stdout codepage can neither
    # mangle nor crash on it
    sys.stdout.buffer.write(json.dumps(payload).encode("utf-8") + b"\n")


def _bases(data):
    """Where to look for the notes file: project root first, then Claude's cwd."""
    found = []
    for candidate in (os.environ.get("CLAUDE_PROJECT_DIR"), data.get("cwd")):
        if isinstance(candidate, str) and candidate.strip():
            found.append(candidate)
    return found


def _find_markers(bases):
    """Walk up from each base to the repo root.

    Returns (notes path or None, opted in). A project opts in by keeping an
    IMPLEMENTATION_NOTES.md, or a .unknowns/ directory — which means a skill
    has already written output here even though notes were never initialized.
    """
    opted_in = False
    for base in bases:
        try:
            current = os.path.abspath(base)
        except Exception:
            continue
        for _ in range(MAX_WALK):
            candidate = os.path.join(current, NOTES_NAME)
            if os.path.exists(candidate):
                return candidate, True
            if os.path.isdir(os.path.join(current, WORK_DIR)):
                opted_in = True
            if os.path.exists(os.path.join(current, ".git")):
                break
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent
    return None, opted_in


LOOP_FILE = "loop.json"
LOOP_MAX_BYTES = 65536


def _find_loop(bases):
    """Path of the nearest .unknowns/loop.json below the repo root, or None."""
    for base in bases:
        try:
            current = os.path.abspath(base)
        except Exception:
            continue
        for _ in range(MAX_WALK):
            candidate = os.path.join(current, WORK_DIR, LOOP_FILE)
            if os.path.isfile(candidate):
                return candidate
            if os.path.exists(os.path.join(current, ".git")):
                break
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent
    return None


def _one_line(value, limit):
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def _loop_hint(bases):
    """Resume hint for an unfinished loop, or None.

    Compaction re-attaches invoked skills most-recent-first within a fixed
    budget, so the loop skill - invoked first - is the one most likely to be
    dropped, together with its own "re-invoke me after compaction" line. The
    tracker survives on disk; this points back at it. Only status "active"
    counts: a file without a status may be a finished loop from before the
    field existed, and a false "resume" is worse than none.
    """
    path = _find_loop(bases)
    if path is None:
        return None
    try:
        if os.path.getsize(path) > LOOP_MAX_BYTES:
            return None
        with open(path, "r", encoding="utf-8") as fh:
            loop = json.load(fh)
    except Exception:
        return None
    if not isinstance(loop, dict) or loop.get("status") != "active":
        return None
    return (
        "[unknowns] A loop is in progress (task: %s; tier: %s; stage: %s). "
        "Compaction may have dropped the loop skill's text: re-invoke the "
        "unknowns loop skill with `resume` before continuing.\n"
        % (
            _one_line(loop.get("task", "?"), 120),
            _one_line(loop.get("tier", "?"), 20),
            _one_line(loop.get("stage", "?"), 40),
        )
    )


def _gate(data):
    """(fire allowed, notes path, bases) — see _find_markers for the opt-in."""
    bases = _bases(data)
    notes, opted_in = _find_markers(bases)
    if opted_in or _env_flag("UNKNOWNS_NOTES_ALWAYS"):
        return True, notes, bases
    return False, None, bases


def _is_notes_edit(data):
    """True when the tool call edited IMPLEMENTATION_NOTES.md itself."""
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return False
    for key in ("file_path", "notebook_path"):
        value = tool_input.get(key)
        if isinstance(value, str) and os.path.basename(value) == NOTES_NAME:
            return True
    return False


def _reminder(count, notes_path, bases):
    if notes_path is not None or not bases:
        tail = "."
    else:
        tail = (
            " (file does not exist yet - run the notes skill with init:"
            " /unknowns:notes init, or /notes init for copied installs)."
        )
    return (
        "[unknowns] File edits reached %d this session. "
        "If any decision was not in the plan/spec (an unknown), record it "
        "in %s%s" % (count, NOTES_NAME, tail)
    )


# --- modes ------------------------------------------------------------------

def post_tool_use(data, threshold, repeat):
    allowed, notes_path, bases = _gate(data)
    if not allowed:
        return 0
    state_dir = _state_dir()
    if state_dir is None:
        return 0
    state_path = _state_path(state_dir, str(data.get("session_id", "default")))

    fire = False
    persisted = False
    lock = _lock(state_path)
    try:
        state = _read_state(state_path)
        if _is_notes_edit(data):
            # recording a deviation is the act being asked for, not an edit to count
            state["notes_touched"] = True
            _write_state(state_path, state)
            return 0
        state["count"] += 1
        if state["notes_at_start"] is None:
            state["notes_at_start"] = _notes_snapshot(notes_path, bases)
        if repeat:
            fire = state["count"] % threshold == 0
        else:
            fire = state["count"] >= threshold and not state["reminded"]
        if fire and data.get("agent_id"):
            # a subagent's context is discarded when it returns, so the reminder
            # would be spent where nobody curates the notes file
            fire = False
        if fire:
            state["reminded"] = True
        persisted = _write_state(state_path, state)
        count = state["count"]
    finally:
        _unlock(lock)

    if not (fire and persisted):
        return 0
    msg = _reminder(count, notes_path, bases)
    # systemMessage is shown only to the user; additionalContext is injected
    # into Claude's context (both can coexist). A successful hook's raw stdout
    # never reaches the transcript, so there is nothing else to suppress.
    _emit({
        "systemMessage": msg,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        },
    })
    return 0


def session_start(data, threshold, repeat):
    """SessionStart: announce the reminder, and restate the rule after compaction.

    The skills cannot observe whether hooks run on their surface, so the
    ACTIVE_MARKER line is their signal: present means a reminder is still to
    come in this session (plugin hooks run, the project opted in, threshold > 0,
    state persists, the once-per-session reminder not yet spent); absent means
    the notes skill applies its own self-check. It is emitted only under those
    conditions, so it never promises a reminder that will not arrive. Once the
    reminder has fired, the skill goes back to self-checking.
    """
    allowed, _notes_path, bases = _gate(data)
    if not allowed:
        return 0
    if data.get("source") == "compact":
        # independent of the notes reminder: a loop tracker exists only where
        # the loop ran, and threshold 0 turns off the reminder, not the loop
        hint = _loop_hint(bases)
        if hint:
            sys.stdout.buffer.write(hint.encode("utf-8"))
    if threshold <= 0:
        return 0
    state_dir = _state_dir()
    if data.get("source") != "compact":
        # startup, resume, clear (and fork): announce only while a reminder is
        # still to come. Without a state dir the counter cannot run; after the
        # once-per-session reminder has fired (a resumed session), none follows.
        if state_dir is None:
            return 0
        state_path = _state_path(state_dir, str(data.get("session_id", "default")))
        if _read_state(state_path)["reminded"] and not repeat:
            return 0
        sys.stdout.buffer.write(
            (
                "%s: file edits are counted and a reminder to record plan "
                "deviations in %s arrives at %d edits.\n"
                % (ACTIVE_MARKER, NOTES_NAME, threshold)
            ).encode("utf-8")
        )
        return 0
    rearmed = False
    if state_dir is not None:
        state_path = _state_path(state_dir, str(data.get("session_id", "default")))
        lock = _lock(state_path)
        try:
            state = _read_state(state_path)
            if state["reminded"]:
                state["reminded"] = False
                rearmed = _write_state(state_path, state)
            else:
                rearmed = True
        finally:
            _unlock(lock)
    # plain stdout on SessionStart is added to Claude's context; the marker
    # rides along only when the counter can actually remind again
    prefix = "%s. " % ACTIVE_MARKER if rearmed else "[unknowns] "
    sys.stdout.buffer.write(
        (
            "%sNotes rule (restated after compaction): record any "
            "decision that was not in the plan/spec (an unknown) in %s.\n"
            % (prefix, NOTES_NAME)
        ).encode("utf-8")
    )
    return 0


def _notes_changed(notes_path, at_start):
    """True when the notes file appeared or its mtime changed since the first edit.

    "The file" means the same path: one that existed at the first counted edit,
    or one created at a location that was checked then and found empty.

    The file is compared with itself - the mtime recorded at the first counted
    edit - never with this hook's clock, so a file stamped in the future (a fast
    clock on another machine, a network share, `cp -p`) is not mistaken for one
    written now. A write within one mtime tick on a coarse filesystem is missed,
    which only restores the old behaviour (one Stop reminder); the other
    direction, calling an untouched file written, would silence the reminder and
    is the failure this check must not add. No snapshot (a state file from before
    this field existed) means no inference at all.
    """
    if at_start is None:
        return False
    now = _notes_snapshot(notes_path)
    if not now["exists"]:
        return False
    if at_start["exists"]:
        # a different file (the agent cd'd into another package or repo) says
        # nothing about the one that was there at the start
        return now["path"] == at_start["path"] and now["mtime"] != at_start["mtime"]
    # absent at the start: it counts only if it now sits at a path that was
    # checked then and found empty, i.e. it was created during the session; an
    # old file found somewhere else (another package, a sibling repo) does not
    return now["path"] in at_start.get("candidates", [])


def stop(data, threshold):
    """Stop: threshold crossed and the notes file never touched."""
    if data.get("stop_hook_active"):
        return 0
    allowed, notes_path, _bases = _gate(data)
    if not allowed:
        return 0
    state_dir = _state_dir(create=False)
    if state_dir is None:
        return 0
    state_path = _state_path(state_dir, str(data.get("session_id", "default")))

    fire = False
    persisted = False
    count = 0
    lock = _lock(state_path)
    try:
        state = _read_state(state_path)
        count = state["count"]
        if not state["notes_touched"] and _notes_changed(notes_path, state["notes_at_start"]):
            # appended through Bash (`cat >>`), a script or another editor: no
            # Edit/Write event saw it, but the file on disk says it was written
            state["notes_touched"] = True
            _write_state(state_path, state)
        fire = (
            count >= threshold
            and not state["notes_touched"]
            and not state["stop_reminded"]
        )
        if fire:
            state["stop_reminded"] = True
            persisted = _write_state(state_path, state)
    finally:
        _unlock(lock)

    if not (fire and persisted):
        return 0
    msg = (
        "[unknowns] %d file edits this session and %s was not updated. "
        "Record the decisions that were not in the plan/spec (unknowns), or "
        "say there were none." % (count, NOTES_NAME)
    )
    _emit({
        "systemMessage": msg,
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": msg,
        },
    })
    return 0


def cleanup(data):
    """SessionEnd: state files outlive the session otherwise."""
    state_dir = _state_dir(create=False)
    if state_dir is None:
        return 0
    state_path = _state_path(state_dir, str(data.get("session_id", "default")))
    for path in (state_path, state_path + ".lock"):
        try:
            os.unlink(path)
        except OSError:
            pass
    return 0


def main(argv) -> int:
    mode = argv[1] if len(argv) > 1 else ""
    if mode not in ("", "--session-start", "--stop", "--cleanup"):
        return 0

    data = _read_payload()
    if data is None:
        return 0
    if mode == "--cleanup":
        return cleanup(data)

    threshold = _env_int(
        ["UNKNOWNS_NOTES_THRESHOLD", "FIELD_GUIDE_NOTES_THRESHOLD"],
        DEFAULT_THRESHOLD,
    )
    if mode == "--session-start":
        # handles threshold <= 0 itself: the loop resume hint does not depend on it
        return session_start(data, threshold, _env_flag("UNKNOWNS_NOTES_REPEAT"))
    if threshold <= 0:
        return 0
    if mode == "--stop":
        return stop(data, threshold)
    return post_tool_use(data, threshold, _env_flag("UNKNOWNS_NOTES_REPEAT"))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
