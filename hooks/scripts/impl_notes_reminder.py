#!/usr/bin/env python3
"""[unknowns] PostToolUse(Edit|Write) hook.

When file edits reach a threshold (default 10), deliver a reminder to record
plan deviations in IMPLEMENTATION_NOTES.md, to both the user (systemMessage)
and Claude's context (hookSpecificOutput.additionalContext).

- Standard library only (no external deps such as jq)
- State stored in the temp dir as a per-user, per-session file
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


def _env_int(names, default):
    for name in names:
        raw = os.environ.get(name)
        if raw is None:
            continue
        try:
            return int(raw)
        except ValueError:
            continue
    return default


def main() -> int:
    threshold = _env_int(
        ["UNKNOWNS_NOTES_THRESHOLD", "FIELD_GUIDE_NOTES_THRESHOLD"], 10
    )
    if threshold <= 0:
        return 0
    repeat = os.environ.get("UNKNOWNS_NOTES_REPEAT", "0").strip().lower() in (
        "1", "true", "yes",
    )

    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    if not isinstance(data, dict):
        return 0

    raw_sid = str(data.get("session_id", "default"))
    session_id = re.sub(r"[^A-Za-z0-9._-]", "_", raw_sid)[:64] or "default"
    try:
        user = getpass.getuser()
    except Exception:
        user = "user"
    user = re.sub(r"[^A-Za-z0-9._-]", "_", user)[:32] or "user"
    state_path = os.path.join(
        tempfile.gettempdir(), "unknowns-notes-%s-%s.json" % (user, session_id)
    )

    state = {"count": 0, "reminded": False}
    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            loaded = json.load(fh)
        if isinstance(loaded, dict):
            state.update(loaded)
    except Exception:
        pass

    state["count"] = int(state.get("count", 0)) + 1
    if repeat:
        fire = state["count"] % threshold == 0
    else:
        fire = state["count"] >= threshold and not state.get("reminded", False)
    if fire:
        state["reminded"] = True

    try:
        with open(state_path, "w", encoding="utf-8") as fh:
            json.dump(state, fh)
    except Exception as exc:
        # without persistence the counter restarts at 1 every call and the
        # reminder can never fire; stderr shows up in hook debug output
        sys.stderr.write("[unknowns] state persist failed: %s\n" % exc)

    if fire:
        cwd = data.get("cwd") or ""
        notes_path = os.path.join(cwd, "IMPLEMENTATION_NOTES.md")
        exists = os.path.exists(notes_path)
        tail = (
            "." if exists
            else (
                " (file does not exist yet — run the notes skill with init:"
                " /unknowns:notes init, or /notes init for copied installs)."
            )
        )
        msg = (
            "[unknowns] File edits reached %d this session. "
            "If any decision was not in the plan/spec (an unknown), record it "
            "in IMPLEMENTATION_NOTES.md%s" % (state["count"], tail)
        )
        # systemMessage is shown only to the user; additionalContext is
        # injected into Claude's context (both can coexist). suppressOutput
        # only hides the raw stdout JSON from the transcript, so keep it.
        print(json.dumps({
            "systemMessage": msg,
            "suppressOutput": True,
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": msg,
            },
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
