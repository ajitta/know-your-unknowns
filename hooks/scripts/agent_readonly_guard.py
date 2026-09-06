#!/usr/bin/env python3
"""[unknowns] PreToolUse(Bash) guard for this plugin's read-only sub-agents.

Plugin-shipped agents cannot declare `permissionMode` or their own hooks, so
"read-only" is otherwise prose only. This hook fires on every Bash call, exits
immediately unless `agent_type` names one of our agents, and denies the calls
that would change the user's tree:

- unknowns-scout        investigation only: an allowlist of read commands
- independent-reviewer  tests/lint/build stay allowed; mutating commands do not

Deliberately conservative: unparsable commands, unknown agents and anything not
matched are allowed. Set UNKNOWNS_AGENT_GUARD=0 to disable the guard entirely.
"""
import json
import os
import re
import shlex
import sys

# segment separators; redirections are inspected, not used as separators
OPERATORS = frozenset((";", ";;", "&&", "||", "|", "|&", "&", "(", ")"))

# `cmd <<EOF` / `cmd <<-'EOF'`, but never the `<<<` here-string
HEREDOC = re.compile(
    r"(?<!<)<<(?!<)-?\s*(?:\"([^\"]*)\"|'([^']*)'|\\?([A-Za-z_][A-Za-z0-9_]*))"
)

# commands the scout may run (first word of a segment, path stripped)
SCOUT_ALLOW = frozenset("""
awk basename cat cd column comm cut date df diff dirname du echo egrep false
fd fgrep file find git grep head jq ls nl printf pwd readlink realpath rg sed
sort stat tail test tr tree true type uname uniq wc which whoami yq
""".split())

# commands neither agent may run
DESTRUCTIVE = frozenset(("rm", "rmdir", "shred", "truncate", "dd", "mv", "tee",
                         "sudo", "doas"))

# git subcommands that always change the repository
GIT_WRITE = frozenset("""
add am apply checkout cherry-pick clean commit filter-branch gc init merge mv
prune pull push rebase reset restore revert rm switch update-ref
""".split())

# git subcommands that only write with certain arguments (listing them is fine)
GIT_SUB_WRITE = {
    "remote": frozenset(("add", "remove", "rm", "rename", "set-url", "set-head",
                         "prune")),
    "worktree": frozenset(("add", "remove", "move", "prune", "lock", "unlock")),
    "submodule": frozenset(("add", "update", "init", "deinit", "sync", "set-url")),
    "stash": frozenset(("", "push", "save", "pop", "apply", "drop", "clear",
                        "store", "create")),
}
GIT_FLAG_WRITE = {
    "tag": frozenset(("-d", "--delete", "-a", "-s", "-f", "--force", "-m")),
    "branch": frozenset(("-d", "-D", "--delete", "-m", "-M", "--move", "-c",
                         "-C", "--copy", "-f", "--force")),
    "config": frozenset(("--add", "--unset", "--unset-all", "--replace-all",
                         "--edit", "-e")),
}
# flags that turn the same subcommands into a query: `git tag -l 'v*'` has the
# argument count of a tag creation but only lists
GIT_FLAG_READ = {
    "tag": frozenset(("-l", "--list", "-n", "--contains", "--no-contains",
                      "--points-at", "--merged", "--no-merged", "--sort",
                      "--format", "-i", "--ignore-case")),
    "branch": frozenset(("-l", "--list", "-a", "--all", "-r", "--remotes",
                         "-v", "-vv", "--verbose", "--contains",
                         "--no-contains", "--points-at", "--merged",
                         "--no-merged", "--show-current", "--sort",
                         "--format", "-i", "--ignore-case")),
    "config": frozenset(("--get", "--get-all", "--get-regexp",
                         "--get-urlmatch", "-l", "--list")),
}

# command -> subcommands that install or publish
PACKAGE_WRITE = {
    "npm": frozenset(("i", "install", "ci", "add", "un", "uninstall", "remove",
                      "rm", "update", "up", "upgrade", "link", "publish")),
    "pnpm": frozenset(("i", "install", "add", "remove", "rm", "un", "uninstall",
                       "update", "up", "link", "publish")),
    "yarn": frozenset(("install", "add", "remove", "up", "upgrade", "link",
                       "publish")),
    "bun": frozenset(("install", "i", "add", "remove", "rm", "update", "link",
                      "publish")),
    "pip": frozenset(("install", "uninstall")),
    "pip3": frozenset(("install", "uninstall")),
    "poetry": frozenset(("add", "remove", "install", "update", "publish")),
    "cargo": frozenset(("install", "add", "remove", "publish")),
    "go": frozenset(("get", "install")),
    "gem": frozenset(("install", "uninstall", "update", "push")),
    "composer": frozenset(("install", "require", "remove", "update")),
    "brew": frozenset(("install", "uninstall", "upgrade", "update", "remove")),
    "apt": frozenset(("install", "remove", "purge", "upgrade", "update")),
    "apt-get": frozenset(("install", "remove", "purge", "upgrade", "update")),
    "yum": frozenset(("install", "remove", "upgrade", "update")),
    "dnf": frozenset(("install", "remove", "upgrade", "update")),
    "apk": frozenset(("add", "del", "upgrade")),
}

GH_WRITE = frozenset(("create", "merge", "close", "edit", "delete", "comment",
                      "review", "ready", "reopen"))

REDIRECT_SINKS = frozenset(("/dev/null", "/dev/stdout", "/dev/stderr", "-"))
TEMP_PREFIXES = ("/tmp/", "/var/tmp/", "/private/tmp/", "/var/folders/",
                 "/private/var/folders/")
# independent-reviewer.md tells the agent to put scratch files under $TMPDIR;
# nothing expands the variable before the guard sees the command
TEMP_VARS = ("$TMPDIR", "${TMPDIR}", "$TMP", "${TMP}", "$TEMP", "${TEMP}")


def _emit(payload):
    sys.stdout.buffer.write(json.dumps(payload).encode("utf-8") + b"\n")


def _read_payload():
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


def _role(data):
    raw = data.get("agent_type")
    if not isinstance(raw, str):
        return None
    name = raw.split(":")[-1].strip().lower()
    if name == "unknowns-scout":
        return "scout"
    if name == "independent-reviewer":
        return "reviewer"
    return None


def _strip_heredocs(command):
    """Drop heredoc bodies before tokenizing: they are data, not shell words.

    `python3 <<'PY' ... PY` is an execution style independent-reviewer.md
    prescribes; without this, a `>` or a bare word inside the body reads as a
    redirection or a command name.
    """
    lines = command.split("\n")
    kept, index = [], 0
    while index < len(lines):
        line = lines[index]
        kept.append(line)
        index += 1
        for match in HEREDOC.finditer(line):
            delimiter = next(g for g in match.groups() if g is not None)
            while index < len(lines):
                body = lines[index]
                index += 1
                if body.strip() == delimiter:
                    break
    return "\n".join(kept)


def _tokenize(command):
    text = _strip_heredocs(command)
    text = re.sub(r"\\\n", " ", text)   # a continued line is one command
    text = text.replace("\n", " ; ")    # every other newline separates two
    lexer = shlex.shlex(text, posix=True, punctuation_chars=True)
    lexer.whitespace_split = True
    return list(lexer)


def _segments(tokens):
    """Split a token list on shell operators; yields one command each."""
    segment = []
    for token in tokens:
        if token in OPERATORS:
            if segment:
                yield segment
            segment = []
        else:
            segment.append(token)
    if segment:
        yield segment


def _is_redirect(token):
    return ">" in token and set(token) <= set("<>&|12")


def _is_temp(target):
    for var in TEMP_VARS:
        if target == var or target.startswith(var + "/"):
            return True
    prefixes = list(TEMP_PREFIXES)
    tmpdir = os.environ.get("TMPDIR")
    if tmpdir:
        prefixes.append(tmpdir.rstrip("/") + "/")
    return any(target.startswith(prefix) for prefix in prefixes)


def _first_word(segment):
    """The command name, skipping VAR=value prefixes and redirections."""
    skip_next = False
    for token in segment:
        if skip_next:
            skip_next = False
            continue
        if _is_redirect(token):
            skip_next = True
            continue
        if "=" in token and not token.startswith("="):
            head = token.split("=", 1)[0]
            if head.replace("_", "").isalnum():
                continue
        return os.path.basename(token)
    return ""


def _args_after(segment, command):
    """Arguments following the command name, redirection targets removed."""
    args, seen, skip_next = [], False, False
    for token in segment:
        if skip_next:
            skip_next = False
            continue
        if _is_redirect(token):
            skip_next = True
            continue
        if not seen:
            seen = os.path.basename(token) == command
            continue
        args.append(token)
    return args


def _redirect_violation(segment):
    for index, token in enumerate(segment):
        if not _is_redirect(token):
            continue
        target = segment[index + 1] if index + 1 < len(segment) else ""
        if target.isdigit() or target in REDIRECT_SINKS or _is_temp(target):
            continue
        return "writes a file by redirection (%s %s)" % (token, target or "?")
    return None


def _git_positional(args):
    """Positional args of a git command, skipping the values of global options.

    `git -C <path>` and `git -c <key>=<value>` take a value that does not start
    with "-", so a naive positional list makes that value look like the
    subcommand and every write check below silently passes.
    """
    out = []
    skip_next = False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg in ("-C", "-c", "--git-dir", "--work-tree", "--namespace",
                   "--exec-path", "--config-env"):
            skip_next = True
            continue
        if arg.startswith("-"):
            continue
        out.append(arg)
    return out


def _git_violation(args, positional):
    sub = positional[0] if positional else ""
    second = positional[1] if len(positional) > 1 else ""
    if sub in GIT_WRITE:
        return "`git %s` changes the repository" % sub
    if sub in GIT_FLAG_WRITE:
        if any(a in GIT_FLAG_WRITE[sub] for a in args):
            return "`git %s` writes when given those arguments" % sub
        creates = len(positional) >= (3 if sub == "config" else 2)
        if creates and not any(a in GIT_FLAG_READ[sub] for a in args):
            return "`git %s` writes when given those arguments" % sub
    if sub in GIT_SUB_WRITE and second in GIT_SUB_WRITE[sub]:
        return "`git %s %s` changes the repository" % (sub, second)
    return None


def _segment_violation(segment, role):
    command = _first_word(segment)
    if not command:
        return None
    if command in DESTRUCTIVE:
        return "`%s` changes files" % command
    args = _args_after(segment, command)
    positional = [a for a in args if not a.startswith("-")]
    sub = positional[0] if positional else ""

    if command in ("sed", "perl"):
        for arg in args:
            if arg == "--in-place" or (
                arg.startswith("-") and not arg.startswith("--") and "i" in arg
            ):
                return "`%s -i` edits files in place" % command
    if command == "git":
        found = _git_violation(args, _git_positional(args))
        if found:
            return found
    if command in PACKAGE_WRITE and sub in PACKAGE_WRITE[command]:
        return "`%s %s` installs or publishes packages" % (command, sub)
    if command == "uv":
        if sub in ("add", "remove", "sync"):
            return "`uv %s` changes the environment" % sub
        if sub == "pip" and len(positional) > 1 and positional[1] in (
            "install", "uninstall", "sync"
        ):
            return "`uv pip %s` changes the environment" % positional[1]
    if command == "gh" and len(positional) > 1 and positional[1] in GH_WRITE:
        return "`gh %s %s` writes to the remote" % (sub, positional[1])

    if command == "find" and "-delete" in args:
        return "`find -delete` removes files"

    found = _redirect_violation(segment)
    if found:
        return found

    if role != "scout":
        return None
    # the scout only reads: everything else needs to be on the allowlist
    if command == "find" and any(
        a in ("-exec", "-execdir", "-ok", "-okdir") for a in args
    ):
        return "`find -exec` can run any command"
    if command not in SCOUT_ALLOW:
        return "`%s` is outside the scout's read-only command set" % command
    return None


def _violation(command, role):
    try:
        tokens = _tokenize(command)
    except ValueError:
        return None  # unparsable (an unbalanced quote): do not block
    for segment in _segments(tokens):
        found = _segment_violation(segment, role)
        if found:
            return found
    return None


def main() -> int:
    if os.environ.get("UNKNOWNS_AGENT_GUARD", "").strip().lower() in (
        "0", "off", "false", "no"
    ):
        return 0
    data = _read_payload()
    if data is None:
        return 0
    role = _role(data)
    if role is None:
        return 0
    tool_input = data.get("tool_input")
    if not isinstance(tool_input, dict):
        return 0
    command = tool_input.get("command")
    if not isinstance(command, str) or not command.strip():
        return 0

    found = _violation(command, role)
    if not found:
        return 0
    if role == "scout":
        reason = (
            "[unknowns] unknowns-scout is a read-only investigation agent, so "
            "this Bash call was denied: %s. Investigate with git read commands, "
            "ls/cat/head/grep/rg/find/jq and the Read/Grep/Glob tools, and "
            "report what should change instead of changing it." % found
        )
    else:
        reason = (
            "[unknowns] independent-reviewer must not modify the tree, so this "
            "Bash call was denied: %s. Running tests, lint and build is fine; "
            "report the needed change instead of applying it." % found
        )
    _emit({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
