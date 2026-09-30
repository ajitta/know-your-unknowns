#!/usr/bin/env python3
"""Run this eval suite by the manual headless method.

`claude plugin eval` is the first-class runner for the cases in this directory, but
it is gated behind early access on some accounts. This script runs the *same* case
files through plain `claude -p`, the method docs/trigger-eval-v0.3.0.md used by hand,
so the suite is reproducible today and produces a comparable record.

What it does and does not do:

  * It reads `<case>/prompt.md` and `<case>/graders/*.md` exactly as the CLI does.
  * It grades the mechanical grader types itself: `tool_used`, `regex`, `file_exists`.
  * It CANNOT grade `llm` or `baseline` graders -- those need a judge model. It records
    each one as `manual` and writes its rubric to `summary.md` in the results
    directory, for a human to score by hand.
  * Each run happens in a fresh temporary working directory, so `file_exists` and
    `target: files` mean the same thing they mean under the real runner.
  * With `--arm both` it runs each case twice, with and without `--plugin-dir`, which
    is the manual equivalent of `--ablation with-without`.
  * With `--crowd N` it also loads a generated filler plugin of N ordinary-looking
    skills. Claude Code gives the skill listing a budget (1% of the context window by
    default) and drops descriptions, least-used first (usage counts, decayed by
    recency), when it overflows; a clean eval environment rarely overflows, so a
    trigger that passes there can still lose its description on a machine with many
    skills. The crowd arm measures that. Usage counts live in the Claude config and
    headless runs update them too, so every crowd run gets a fresh, empty
    CLAUDE_CONFIG_DIR (no usage history; synced or managed plugins may still load)
    and the filler plugin is loaded first, so ties in the ranking do not favour this
    plugin. Each crowd run writes a --debug-file and the report records what the CLI
    logged: whether the listing went over budget, and which plugins loaded.
    A fresh config dir holds no sign-in on most machines, so crowd runs need
    ANTHROPIC_API_KEY (or credentials the CLI finds outside the config dir); a run
    that fails to start is reported as FAILED, never scored as "did not fire".
    `--budget-fraction F` sets skillListingBudgetFraction for the run, to force an
    overflow regardless of the model's context window.

Usage:

    python3 evals/run-manual.py --case 'trigger-*' --runs 1
    python3 evals/run-manual.py --case 'behavior-notes-*' --arm both
    python3 evals/run-manual.py --case 'trigger-*' --crowd 60 --budget-fraction 0.002
    python3 evals/run-manual.py --list

Stdlib only, Python 3.8+. No PyYAML: the frontmatter in this suite is deliberately
restricted to plain scalars, flow lists, and the one nested `focus:` mapping.
"""

import argparse
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# Grader types this script can decide without a judge model.
MECHANICAL = {"tool_used", "regex", "file_exists"}

# Everything `claude -p` might reach for that these cases do not grant. Passed to
# --disallowedTools so a case's allowed_tools list means the same thing it means
# under `claude plugin eval`.
DENYABLE = [
    "Bash", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch",
    "Agent", "Task", "Workflow", "AskUserQuestion", "Artifact",
]


# --------------------------------------------------------------------------- io

def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def split_frontmatter(text, where):
    """Return (frontmatter dict, body). Mirrors the CLI's prose-.md reader."""
    text = text.lstrip("﻿")
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*\n?", text, re.DOTALL)
    if not match:
        raise ValueError("%s: unterminated frontmatter" % where)
    return parse_frontmatter(match.group(1), where), text[match.end():]


def parse_frontmatter(block, where):
    """Minimal YAML subset: `key: scalar`, `key: [a, b]`, and one nested mapping."""
    out = {}
    pending = None
    for raw in block.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1] in " \t":
            if pending is None:
                raise ValueError("%s: unexpected indented line %r" % (where, raw))
            key, _, value = raw.strip().partition(":")
            out[pending][key.strip()] = scalar(value.strip())
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            raise ValueError("%s: not a key/value line: %r" % (where, raw))
        key, value = key.strip(), value.strip()
        if value == "":
            out[key] = {}
            pending = key
        else:
            out[key] = scalar(value)
            pending = None
    return out


def scalar(value):
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [scalar(part.strip()) for part in inner.split(",")]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    low = value.lower()
    if low in ("true", "false"):
        return low == "true"
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


# ------------------------------------------------------------------ case model

BODY_KEY = {"llm": "criteria", "baseline": "criteria", "regex": "pattern"}

# The legal `prompt.md` frontmatter keys, shared by the loader and `--verify` so a key
# the one accepts cannot be a traceback in the other.
TOP_KEYS = {"schema_version", "name", "description", "tags", "plugins", "runs",
            "expected_outcome"}
EXEC_KEYS = {"model", "max_turns", "timeout_seconds", "allowed_tools",
             "artifact_publish", "growthbook_overrides", "append_system_prompt", "env"}


def load_case(case_dir):
    prompt_path = os.path.join(case_dir, "prompt.md")
    front, body = split_frontmatter(read(prompt_path), prompt_path)
    unknown = set(front) - TOP_KEYS - EXEC_KEYS
    if unknown:
        raise ValueError("%s: unknown frontmatter key(s) %s" % (prompt_path, sorted(unknown)))

    graders = []
    graders_dir = os.path.join(case_dir, "graders")
    for name in sorted(os.listdir(graders_dir)) if os.path.isdir(graders_dir) else []:
        if not name.endswith(".md"):
            continue
        path = os.path.join(graders_dir, name)
        gfront, gbody = split_frontmatter(read(path), path)
        if "type" not in gfront:
            raise ValueError('%s: frontmatter must include "type:"' % path)
        grader = dict(gfront)
        grader["name"] = name[:-3]
        key = BODY_KEY.get(grader["type"])
        if key and key not in grader and gbody.strip():
            grader[key] = gbody.strip()
        graders.append(grader)
    if not graders:
        raise ValueError("%s: no graders" % case_dir)

    return {
        "name": os.path.basename(case_dir),
        "dir": case_dir,
        "description": front.get("description", ""),
        "tags": front.get("tags", []),
        "prompt": body.strip(),
        "runs": int(front.get("runs", 3)),
        "max_turns": int(front.get("max_turns", 10)),
        "timeout_seconds": int(front.get("timeout_seconds", 300)),
        "allowed_tools": front.get("allowed_tools", []),
        "model": front.get("model"),
        "graders": graders,
    }


def discover(case_glob, tag):
    cases = []
    for entry in sorted(os.listdir(HERE)):
        case_dir = os.path.join(HERE, entry)
        if not os.path.isdir(case_dir) or entry in ("results", "mocks", "__pycache__"):
            continue
        if not os.path.exists(os.path.join(case_dir, "prompt.md")):
            continue
        if case_glob and not fnmatch.fnmatch(entry, case_glob):
            continue
        case = load_case(case_dir)
        if tag and tag not in case["tags"]:
            continue
        cases.append(case)
    return cases


def plugin_root():
    """Walk up from evals/ to the directory holding .claude-plugin/plugin.json.

    Written as a search rather than a constant so it keeps working after the
    plugin payload moves under plugins/unknowns/.
    """
    current = HERE
    for _ in range(6):
        current = os.path.dirname(current)
        if os.path.exists(os.path.join(current, ".claude-plugin", "plugin.json")):
            return current
    raise SystemExit("could not find .claude-plugin/plugin.json above %s" % HERE)


# ------------------------------------------------------------------- execution

def snapshot(root):
    seen = set()
    for base, _dirs, files in os.walk(root):
        for name in files:
            seen.add(os.path.relpath(os.path.join(base, name), root).replace(os.sep, "/"))
    return seen


# Filler skills for --crowd: plausible, unrelated work, some sharing trigger words
# ("plan", "review", "test", "explain") with this plugin so the listing competes
# the way a real one does. Names are prefixed so they never collide.
CROWD_TOPICS = [
    ("sprint-plan", "Plan a sprint from a backlog: size tickets, pick a goal, and draft the sprint board. Use when the user says plan the sprint or sprint planning."),
    ("pr-review", "Review a pull request for style, naming and obvious bugs, and draft review comments. Use on review this PR or code review."),
    ("test-writer", "Write unit tests for a function or module using the project's test framework. Use when asked to add tests or improve coverage."),
    ("explain-code", "Explain what a piece of code does, line by line, for a newcomer. Use on explain this code or what does this do."),
    ("release-notes", "Draft release notes from merged pull requests and commit messages. Use on write release notes or changelog draft."),
    ("sql-helper", "Write or optimize SQL queries and explain query plans. Use when the user asks for a query, index advice or a slow query fix."),
    ("api-docs", "Generate API reference docs from route handlers and types. Use on document this API or generate API docs."),
    ("refactor", "Refactor code for readability without changing behavior: extract functions, rename, simplify. Use on refactor this or clean up."),
    ("bug-triage", "Triage a bug report: reproduce, find the likely module, and propose a fix plan. Use on triage this bug or investigate this issue."),
    ("dockerize", "Write a Dockerfile and compose file for the project. Use on containerize this app or add Docker."),
    ("ci-setup", "Set up a CI pipeline for lint, test and build. Use on add CI or set up GitHub Actions."),
    ("perf-profile", "Profile slow code paths and suggest optimizations. Use on this is slow, profile this, or performance review."),
    ("migration", "Plan and write a database migration with a rollback. Use on add a migration or change the schema."),
    ("security-scan", "Scan code for common security issues and explain each. Use on security review or check for vulnerabilities."),
    ("commit-msg", "Write a conventional commit message from the staged diff. Use on write a commit message."),
    ("onboarding", "Write an onboarding guide for a codebase: setup, architecture tour, first tasks. Use on onboarding doc or explain the codebase to a new hire."),
    ("design-doc", "Draft a design doc with context, goals, options and a recommendation. Use on write a design doc or RFC."),
    ("meeting-notes", "Turn a meeting transcript into notes with decisions and action items. Use on summarize this meeting."),
    ("regex-helper", "Write and explain a regular expression with test cases. Use on write a regex."),
    ("i18n", "Extract user-facing strings and set up translations. Use on internationalize or add translations."),
]


def crowd_plugin(count, into):
    """Write a throwaway plugin with `count` filler skills; returns its root."""
    root = os.path.join(into, "crowd-plugin")
    if os.path.isdir(root):
        # a reused --out must not keep fillers from an earlier, larger crowd
        shutil.rmtree(root)
    os.makedirs(os.path.join(root, ".claude-plugin"), exist_ok=True)
    with open(os.path.join(root, ".claude-plugin", "plugin.json"), "w",
              encoding="utf-8") as handle:
        json.dump({"name": "evalcrowd", "version": "0.0.0",
                   "description": "Filler skills for the crowded-listing eval arm."},
                  handle)
    for index in range(count):
        slug, text = CROWD_TOPICS[index % len(CROWD_TOPICS)]
        name = "crowd-%02d-%s" % (index, slug)
        folder = os.path.join(root, "skills", name)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "SKILL.md"), "w", encoding="utf-8") as handle:
            handle.write("---\nname: %s\ndescription: %s\n---\n\n%s\n"
                         % (name, json.dumps(text), text))
    return root


LISTING_OVER = re.compile(
    r"Skill listing over budget: (\d+) skills, (\d+) chars > (\d+) budget")
INLINE_PLUGIN = re.compile(r"Loaded inline plugin from path: (\S+)")


def listing_report(debug_file):
    """What the CLI logged about the skill listing and the plugins it loaded."""
    try:
        text = read(debug_file)
    except OSError:
        return {"debug_log": False}
    over = LISTING_OVER.search(text)
    return {
        "debug_log": True,
        "over_budget": bool(over),
        "skills": int(over.group(1)) if over else None,
        "chars": int(over.group(2)) if over else None,
        "budget_chars": int(over.group(3)) if over else None,
        # every plugin the CLI loaded, including synced or managed ones that still
        # load with an empty config dir (and this plugin and the filler plugin)
        "plugins_loaded": sorted(set(INLINE_PLUGIN.findall(text))),
    }


def run_once(case, with_plugin, root, claude_bin, crowd_root=None, budget_fraction=None):
    sandbox = tempfile.mkdtemp(prefix="unknowns-eval-")
    config_dir = tempfile.mkdtemp(prefix="unknowns-eval-config-") if crowd_root else None
    try:
        before = snapshot(sandbox)
        cmd = [claude_bin, "-p", case["prompt"],
               "--output-format", "stream-json", "--verbose",
               "--max-turns", str(case["max_turns"])]
        if case["model"]:
            cmd += ["--model", case["model"]]
        if crowd_root:
            # first, so listing-order ties go to the fillers, not to this plugin
            cmd += ["--plugin-dir", crowd_root]
        if with_plugin:
            cmd += ["--plugin-dir", root]
        if budget_fraction is not None:
            cmd += ["--settings", json.dumps({"skillListingBudgetFraction": budget_fraction})]
        env = dict(os.environ)
        debug_file = None
        if config_dir:
            env["CLAUDE_CONFIG_DIR"] = config_dir
            # the CLI's own word on the listing, instead of the model's report
            debug_file = os.path.join(config_dir, "eval-debug.log")
            cmd += ["--debug-file", debug_file]
        if case["allowed_tools"]:
            cmd += ["--allowedTools"] + list(case["allowed_tools"])
        denied = [tool for tool in DENYABLE if tool not in case["allowed_tools"]]
        if denied:
            cmd += ["--disallowedTools"] + denied

        started = time.time()
        timed_out = False
        try:
            proc = subprocess.run(cmd, cwd=sandbox, capture_output=True, text=True,
                                  timeout=case["timeout_seconds"], env=env)
            stdout, stderr, code = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired:
            stdout, stderr, code = "", "timed out after %ds" % case["timeout_seconds"], -1
            timed_out = True

        events, tool_calls, last_message = [], [], ""
        model_used = None
        result_error = False
        for line in stdout.splitlines():
            line = line.strip()
            if not line.startswith("{"):
                continue
            try:
                event = json.loads(line)
            except ValueError:
                continue
            events.append(event)
            if event.get("type") == "system" and isinstance(event.get("model"), str):
                model_used = event["model"]
            if event.get("type") == "result" and event.get("is_error") is True:
                result_error = True
            if event.get("type") == "result" and isinstance(event.get("result"), str):
                last_message = event["result"]
            message = event.get("message")
            # Not every stream-json event carries a message object: some newer
            # CLI events put a plain string under "message". Skip those.
            if not isinstance(message, dict):
                continue
            for block in message.get("content", []) or []:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use":
                    tool_calls.append({
                        "name": block.get("name", ""),
                        "input": block.get("input", {}),
                    })
                elif block.get("type") == "text" and message.get("role") == "assistant":
                    last_message = block.get("text", "") or last_message

        listing = listing_report(debug_file) if debug_file else None
        # a run that could not start (no sign-in in a fresh config dir, a bad flag)
        # makes no tool calls either; it must not be scored as "did not fire". Its
        # message may still be text ("Not logged in"), so the message is not the test.
        failed = not timed_out and not tool_calls and (code != 0 or result_error)

        created = sorted(snapshot(sandbox) - before)
        file_text = {}
        for rel in created:
            try:
                with open(os.path.join(sandbox, rel), encoding="utf-8") as handle:
                    file_text[rel] = handle.read()
            except (OSError, UnicodeDecodeError):
                file_text[rel] = ""

        return {
            "arm": ("with" if with_plugin else "without") + ("+crowd" if crowd_root else ""),
            "exit_code": code,
            "timed_out": timed_out,
            "failed": failed,
            "listing": listing,
            "model": model_used,
            "stderr": stderr[-2000:],
            "duration_seconds": round(time.time() - started, 1),
            "last_message": last_message,
            "tool_calls": tool_calls,
            "files_created": created,
            "file_text": file_text,
            "trace": json.dumps(events, ensure_ascii=False),
        }
    finally:
        shutil.rmtree(sandbox, ignore_errors=True)
        if config_dir:
            shutil.rmtree(config_dir, ignore_errors=True)


# --------------------------------------------------------------------- grading

def flags_to_re(flags):
    out = 0
    for char in str(flags or ""):
        out |= {"i": re.I, "m": re.M, "s": re.S}.get(char, 0)
    return out


def target_text(target, run):
    if isinstance(target, dict):
        return run["file_text"].get(target.get("path", ""), "")
    if target == "trace":
        return run["trace"]
    if target == "files":
        return "\n".join(run["files_created"])
    return run["last_message"]


def glob_to_re(pattern):
    out, index = "^", 0
    while index < len(pattern):
        char = pattern[index]
        if char == "*":
            if pattern[index + 1:index + 2] == "*":
                if pattern[index + 2:index + 3] == "/":
                    out += "(?:.*/)?"
                    index += 3
                    continue
                out += ".*"
                index += 2
                continue
            out += "[^/]*"
        elif char == "?":
            out += "."
        elif char in ".+^${}()|[]\\":
            out += "\\" + char
        else:
            out += char
        index += 1
    return re.compile(out + "$")


def grade(grader, run):
    kind = grader["type"]
    if kind == "tool_used":
        wanted = grader["tool"]
        pattern = grader.get("input_match")
        count = 0
        for call in run["tool_calls"]:
            if call["name"] != wanted:
                continue
            if pattern and not re.search(str(pattern),
                                         json.dumps(call["input"], ensure_ascii=False)):
                continue
            count += 1
        low = int(grader.get("min", 1))
        high = grader.get("max")
        high = float("inf") if high is None else int(high)
        ok = low <= count <= high
        return ok, "%s called %dx (expected %s..%s)" % (
            wanted, count, low, "inf" if high == float("inf") else high)

    if kind == "regex":
        text = target_text(grader.get("target", "last_message"), run)
        found = re.findall(str(grader["pattern"]), text, flags_to_re(grader.get("flags")))
        mode = str(grader.get("match", "contains"))
        if mode == "contains":
            return bool(found), "found %d matches (expected >=1)" % len(found)
        if mode == "not_contains":
            return not found, "found %d matches (expected 0)" % len(found)
        if mode.startswith("count:"):
            want = int(mode.split(":", 1)[1])
            return len(found) == want, "found %d matches (expected %d)" % (len(found), want)
        return False, 'unknown match mode "%s"' % mode

    if kind == "file_exists":
        rx = glob_to_re(str(grader["path"]))
        present = any(rx.match(rel) for rel in run["files_created"])
        want = grader.get("exists", True)
        return present == want, "%s %s (expected %s)" % (
            grader["path"], "exists" if present else "missing",
            "present" if want else "absent")

    return None, "needs a judge model"


def is_display_only(grader):
    """`tool: Skill` with no `arm:` is reported but excluded from the score."""
    return grader["type"] == "tool_used" and grader.get("tool") == "Skill" \
        and "arm" not in grader


def score_run(case, run):
    if run.get("timed_out") or run.get("failed"):
        why = "run timed out" if run.get("timed_out") else (
            "run failed (exit %s): %s" % (run.get("exit_code"),
                                          (run.get("stderr") or "").strip()[-200:]))
        # A run that never finished produced no tool calls and no files. Grading it
        # would score every "did not fire" assertion as a pass and every "fired"
        # assertion as a fail — a measurement artifact indistinguishable from the
        # real result. Report it as an error instead.
        return {"graders": [{"name": g["name"], "type": g["type"],
                             "weight": float(g.get("weight", 1)),
                             "display_only": is_display_only(g), "passed": None,
                             "criteria": g.get("criteria", ""),
                             "explanation": why + " — not graded"}
                            for g in case["graders"]],
                "mechanical_score": None, "manual_graders": 0,
                "timed_out": bool(run.get("timed_out")), "failed": bool(run.get("failed"))}
    results, earned, total, manual = [], 0.0, 0.0, 0
    for grader in case["graders"]:
        passed, why = grade(grader, run)
        display_only = is_display_only(grader)
        weight = float(grader.get("weight", 1))
        entry = {"name": grader["name"], "type": grader["type"], "weight": weight,
                 "display_only": display_only, "explanation": why}
        if passed is None:
            entry["passed"] = None
            entry["criteria"] = grader.get("criteria", "")
            manual += 1
        else:
            entry["passed"] = bool(passed)
            if not display_only:
                total += weight
                if passed:
                    earned += weight
        results.append(entry)
    return {"graders": results,
            "mechanical_score": (earned / total) if total else None,
            "manual_graders": manual}


# -------------------------------------------------------------------- verify

GRADER_KEYS = {
    "regex": {"type", "name", "target", "pattern", "flags", "match", "weight", "arm"},
    "tool_order": {"type", "name", "before", "after", "weight", "arm"},
    "tool_used": {"type", "name", "tool", "input_match", "min", "max", "weight", "arm"},
    "file_exists": {"type", "name", "path", "exists", "weight", "arm"},
    "llm": {"type", "name", "criteria", "focus", "weight", "arm"},
    "baseline": {"type", "name", "baseline_file", "criteria", "weight", "arm"},
}
DIR_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._@+-]*$")


def skill_descriptions(root):
    """The folded `description:` of every skill, straight off disk."""
    out = {}
    skills_dir = os.path.join(root, "skills")
    for name in sorted(os.listdir(skills_dir)) if os.path.isdir(skills_dir) else []:
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.exists(path):
            continue
        match = re.match(r"^---\n(.*?)\n---\n", read(path), re.DOTALL)
        if not match:
            continue
        keep, inside = [], False
        for line in match.group(1).split("\n"):
            if line.startswith("description:"):
                inside = True
                continue
            if inside:
                if line[:1].strip():
                    break
                keep.append(line.strip())
        out[name] = " ".join(keep)
    return out


def verify(root):
    """Structural self-check. Costs nothing: no model is called."""
    problems = []
    descriptions = skill_descriptions(root)
    cases = discover(None, None)
    if not cases:
        problems.append("no cases found")

    for case in cases:
        name = case["name"]
        if not DIR_NAME.match(name):
            problems.append("%s: directory name is not a legal case slug" % name)
        front, _ = split_frontmatter(read(os.path.join(case["dir"], "prompt.md")), name)
        stray = set(front) - TOP_KEYS - EXEC_KEYS
        if stray:
            problems.append("%s: prompt.md has unknown key(s) %s" % (name, sorted(stray)))
        if not case["prompt"]:
            problems.append("%s: empty prompt" % name)
        if "TODO: describe what the agent should do" in case["prompt"]:
            problems.append("%s: prompt is still the blank init template" % name)
        if case["runs"] < 3:
            problems.append("%s: runs < 3 (the suite floor)" % name)
        if not [g for g in case["graders"] if not is_display_only(g)]:
            problems.append("%s: every grader is display-only; needs an outcome grader" % name)

        for grader in case["graders"]:
            label = "%s/%s" % (name, grader["name"])
            kind = grader["type"]
            if kind not in GRADER_KEYS:
                problems.append("%s: unknown grader type %r" % (label, kind))
                continue
            stray = set(grader) - GRADER_KEYS[kind]
            if stray:
                problems.append("%s: unknown key(s) %s" % (label, sorted(stray)))
            if kind == "regex":
                if not str(grader.get("pattern", "")).strip():
                    problems.append("%s: regex grader has no pattern" % label)
                else:
                    try:
                        re.compile(str(grader["pattern"]))
                    except re.error as err:
                        problems.append("%s: bad pattern (%s)" % (label, err))
                if not re.match(r"^[dgimsuvy]*$", str(grader.get("flags", ""))):
                    problems.append("%s: flags must be JS RegExp flags" % label)
            if kind in ("llm", "baseline") and not str(grader.get("criteria", "")).strip():
                problems.append("%s: rubric is empty" % label)
            if kind == "tool_used":
                if "tool" not in grader:
                    problems.append("%s: tool_used needs `tool:`" % label)
                if grader.get("input_match"):
                    try:
                        re.compile(str(grader["input_match"]))
                    except re.error as err:
                        problems.append("%s: bad input_match (%s)" % (label, err))

        match = re.match(r"^trigger-(en|ko)-(.+)$", name)
        if match:
            skill = match.group(2)
            if skill not in descriptions:
                problems.append("%s: no skills/%s/SKILL.md" % (name, skill))
                continue
            # The case names the one phrase it exercises, as `description: "... : '<phrase>'"`.
            # Reading it from there rather than scanning every quoted string in the skill
            # description keeps the check off the phrases a description quotes as ANTI-triggers.
            declared = re.search(r":\s*'([^']+)'\s*$", str(case["description"]).strip())
            if not declared:
                problems.append(
                    "%s: description must end with the trigger phrase the case "
                    "exercises, in the form: '<phrase>'" % name)
            else:
                phrase = declared.group(1)
                # English phrases must be quoted in the description: containment is
                # how they match. Korean phrases must NOT be — descriptions are
                # English-only as of 0.5.1, and these cases exist precisely to prove
                # the phrase still fires without being written there.
                if match.group(1) == "en":
                    quoted = re.findall(r'"([^"]+)"', descriptions[skill])
                    if phrase.lower() not in [q.lower() for q in quoted]:
                        problems.append(
                            "%s: phrase %r is no longer quoted in skills/%s/SKILL.md (%s)"
                            % (name, phrase, skill, " | ".join(quoted)))
                elif re.search(r"[가-힣]", descriptions[skill]):
                    problems.append(
                        "%s: skills/%s/SKILL.md carries Korean again — descriptions "
                        "are English-only, and this case's whole point is that the "
                        "phrase fires without it" % (name, skill))
                if phrase.lower() not in re.sub(r"\s+", " ", case["prompt"]).lower():
                    problems.append(
                        "%s: prompt no longer contains its declared phrase %r"
                        % (name, phrase))
            if not any(g["type"] == "tool_used"
                       and g.get("input_match") == "unknowns:" + skill
                       for g in case["graders"]):
                problems.append("%s: no trigger indicator for unknowns:%s" % (name, skill))

        if name.startswith("neg-"):
            guards = [g for g in case["graders"] if g["type"] == "tool_used"
                      and g.get("tool") == "Skill" and "arm" in g]
            for guard in guards:
                if guard.get("min") != 0 or guard.get("max") != 0 or guard.get("arm") != "both":
                    problems.append("%s/%s: a must-NOT-fire guard needs min: 0, max: 0, "
                                    "arm: both" % (name, guard["name"]))

    for problem in problems:
        print("FAIL  " + problem)
    print("\n%d case(s), %d grader(s), %d problem(s)"
          % (len(cases), sum(len(c["graders"]) for c in cases), len(problems)))
    return 1 if problems else 0


# ------------------------------------------------------------------------ main

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--case", help="glob over case directory names")
    parser.add_argument("--tag", help="only cases carrying this tag")
    parser.add_argument("--runs", type=int, help="override each case's runs")
    parser.add_argument("--timeout", type=int,
                        help="override each case's timeout_seconds; raise it when "
                             "running batches in parallel, since contention pushes "
                             "wall time up and a timeout is not a result")
    parser.add_argument("--arm", choices=["with", "without", "both"], default="with",
                        help="'both' is the manual equivalent of --ablation with-without")
    parser.add_argument("--plugin-dir", help="plugin root (default: found above evals/)")
    parser.add_argument("--crowd", type=int, default=0, metavar="N",
                        help="also load a generated plugin of N filler skills, to test "
                             "triggering when the skill listing overflows its budget; "
                             "each such run uses a fresh, empty CLAUDE_CONFIG_DIR")
    parser.add_argument("--budget-fraction", type=float, metavar="F",
                        help="skillListingBudgetFraction for the run (default budget is "
                             "0.01 of the context window); small values force overflow")
    parser.add_argument("--claude", default="claude", help="claude binary")
    parser.add_argument("--out", help="results directory (default: evals/results/manual-<ts>)")
    parser.add_argument("--list", action="store_true", help="list matching cases and exit")
    parser.add_argument("--verify", action="store_true",
                        help="structural self-check only; calls no model, costs nothing")
    args = parser.parse_args()

    if args.verify:
        return verify(args.plugin_dir or plugin_root())

    cases = discover(args.case, args.tag)
    if not cases:
        raise SystemExit("no cases matched")

    if args.list:
        for case in cases:
            print("%-46s runs=%d  %s" % (case["name"], case["runs"],
                                         ",".join(str(t) for t in case["tags"])))
        print("\n%d case(s)" % len(cases))
        return 0

    root = args.plugin_dir or plugin_root()
    if shutil.which(args.claude) is None and not os.path.exists(args.claude):
        raise SystemExit("claude binary not found: %s" % args.claude)

    out_dir = args.out or os.path.join(
        HERE, "results", "manual-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))
    os.makedirs(out_dir, exist_ok=True)

    arms = ["with", "without"] if args.arm == "both" else [args.arm]
    crowd_root = None
    if args.crowd > 0:
        # kept beside the results, so a run can be re-created with the same crowd
        crowd_root = crowd_plugin(args.crowd, out_dir)
    report = {"method": "manual (claude -p, stream-json)",
              "plugin_dir": root, "arms": arms, "crowd_skills": args.crowd,
              "budget_fraction": args.budget_fraction,
              "isolated_config": bool(crowd_root),
              "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "cases": []}

    for case in cases:
        if args.timeout:
            case["timeout_seconds"] = args.timeout
        runs = args.runs or case["runs"]
        print("\n=== %s (%d run(s) x %d arm(s))" % (case["name"], runs, len(arms)))
        entry = {"name": case["name"], "description": case["description"],
                 "tags": case["tags"], "runs": []}
        for arm in arms:
            for index in range(runs):
                run = run_once(case, arm == "with", root, args.claude, crowd_root,
                               args.budget_fraction)
                scored = score_run(case, run)
                run.pop("trace", None)
                run.update(scored)
                entry["runs"].append(run)
                shown = "TIMEOUT" if scored.get("timed_out") else "FAILED" if scored.get("failed") else (
                    "n/a" if scored["mechanical_score"] is None
                    else "%.2f" % scored["mechanical_score"])
                print("  [%-7s run %d] mechanical=%s  manual=%d  %ds"
                      % (arm, index + 1, shown, scored["manual_graders"],
                         run["duration_seconds"]))
                listing = run.get("listing")
                if listing:
                    print("      listing: %s%s" % (
                        ("over budget, %s skills, %s > %s chars"
                         % (listing["skills"], listing["chars"], listing["budget_chars"]))
                        if listing.get("over_budget") else
                        ("within budget" if listing.get("debug_log") else "no debug log"),
                        ("; plugins loaded: %s" % ", ".join(listing["plugins_loaded"]))
                        if listing.get("plugins_loaded") else ""))
                for grader in scored["graders"]:
                    mark = {True: "PASS", False: "FAIL", None: "JUDGE"}[grader["passed"]]
                    note = " (display-only)" if grader["display_only"] else ""
                    print("      %-5s %-34s %s%s"
                          % (mark, grader["name"], grader["explanation"], note))
        report["cases"].append(entry)

    with open(os.path.join(out_dir, "manual-result.json"), "w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)

    lines = ["# Manual eval run", "",
             "- method: `claude -p` + stream-json (see evals/README.md)",
             "- plugin dir: `%s`" % os.path.relpath(root, os.path.dirname(HERE) or "."),
             "- arms: %s" % ", ".join(arms),
             "- crowd: %d filler skills%s%s" % (
                 args.crowd,
                 ", fresh CLAUDE_CONFIG_DIR per run" if crowd_root else "",
                 (", skillListingBudgetFraction %s" % args.budget_fraction)
                 if args.budget_fraction is not None else ""), "",
             "| case | arm | mechanical | graders needing a judge |",
             "|---|---|---|---|"]
    for case in report["cases"]:
        for run in case["runs"]:
            shown = ("TIMEOUT" if run.get("timed_out") else "FAILED" if run.get("failed")
                     else "n/a" if run["mechanical_score"] is None
                     else "%.2f" % run["mechanical_score"])
            listing = run.get("listing") or {}
            if listing.get("over_budget"):
                shown += " (listing over budget: %s skills)" % listing["skills"]
            lines.append("| %s | %s | %s | %d |"
                         % (case["name"], run["arm"], shown, run["manual_graders"]))
    lines += ["", "## Rubrics still to score by hand", ""]
    for case in report["cases"]:
        pending = [g for run in case["runs"] for g in run["graders"] if g["passed"] is None]
        for grader in {g["name"]: g for g in pending}.values():
            lines += ["### %s / %s" % (case["name"], grader["name"]), "",
                      grader.get("criteria", ""), ""]
    with open(os.path.join(out_dir, "summary.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")

    print("\nwrote %s" % out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
