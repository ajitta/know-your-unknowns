#!/usr/bin/env python3
"""[unknowns] PreToolUse(Bash) guard for this plugin's read-only sub-agents.

Plugin-shipped agents cannot declare `permissionMode` or their own hooks, so
"read-only" is otherwise prose only. This hook fires on every Bash call, exits
immediately unless `agent_type` names one of our agents, and denies the calls
that would change the user's tree:

- unknowns-scout        investigation only: an allowlist of read commands
- independent-reviewer  tests/lint/build stay allowed; mutating commands do not

Both roles: wrappers (xargs, env, timeout, sh -c, eval, find -exec) are
unwrapped and the inner command is checked; commands that write the files
named in their arguments (cp, touch, mkdir, ln, chmod, ...) and the write
options of reading commands (sort -o, sed w, awk print >, yq -i, find -fprint,
git --output) are denied unless every target is under a temp directory
(/tmp, $TMPDIR, or a variable assigned from $(mktemp) in the same command; a
`..` segment never counts). Nesting deeper than MAX_DEPTH is denied. Scripts
the agent runs (python3 -c, a test file) are not inspected.

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
                         "sudo", "doas", "unlink"))

# commands that create or change files named in their arguments; allowed only
# when every file they would write is under a temp directory
#   kind: which positional arguments are write targets
#     "all"  - every positional (touch, mkdir)
#     "last" - the destination (cp, ln, install, rsync)
#     "rest" - all but the first, which is a mode or owner (chmod, chown, chgrp)
#   takes_value: options whose separate next word is a value, not a file
FILE_WRITERS = {
    "touch": ("all", frozenset(("-d", "-r", "-t", "--date", "--reference"))),
    "mkdir": ("all", frozenset(("-m", "--mode", "--context"))),
    "mkfifo": ("all", frozenset(("-m", "--mode", "--context"))),
    "cp": ("last", frozenset(("-S", "--suffix"))),
    "ln": ("last", frozenset(("-S", "--suffix"))),
    "install": ("last", frozenset(("-m", "--mode", "-o", "--owner", "-g",
                                   "--group", "-S", "--suffix"))),
    "rsync": ("last", frozenset(("-e", "--rsh", "-f", "--filter", "--exclude",
                                 "--include", "--exclude-from",
                                 "--include-from", "--files-from", "-T",
                                 "--temp-dir", "--log-file", "--partial-dir",
                                 "--backup-dir", "--suffix", "--chmod",
                                 "--rsync-path", "--password-file", "--port",
                                 "--timeout", "--bwlimit", "--max-size",
                                 "--min-size", "--compare-dest", "--copy-dest",
                                 "--link-dest"))),
    "chmod": ("rest", frozenset()),
    "chown": ("rest", frozenset()),
    "chgrp": ("rest", frozenset()),
}
# commands whose -t / --target-directory names the destination directory
TARGET_DIR_WRITERS = frozenset(("cp", "ln", "install"))

# commands that only run another command: the wrapped command is checked too
#   value: options that take a separate value, so the command starts after it.
#   GNU xargs -i/-l/-e take an optional *attached* value, so they are flags here.
WRAPPERS = {
    "xargs": frozenset(("-I", "-J", "-n", "-P", "-L", "-R", "-S", "-d", "-s",
                        "-E", "-a", "--arg-file", "--delimiter",
                        "--max-args", "--max-procs", "--max-lines",
                        "--max-chars", "--replace", "--eof",
                        "--process-slot-var")),
    "env": frozenset(("-u", "--unset", "-C", "--chdir", "-S",
                      "--split-string")),
    "command": frozenset(),
    "builtin": frozenset(),
    "exec": frozenset(("-a",)),
    "nice": frozenset(("-n", "--adjustment")),
    "nohup": frozenset(),
    "time": frozenset(("-f", "--format", "-o", "--output")),
    "timeout": frozenset(("-s", "--signal", "-k", "--kill-after")),
    "stdbuf": frozenset(("-i", "-o", "-e")),
    "ionice": frozenset(("-c", "-n", "-p")),
}
# `timeout` takes a duration before the command
WRAPPER_LEADING_ARGS = {"timeout": 1}

# shells that run a script string given with -c
SHELLS = frozenset(("sh", "bash", "zsh", "dash", "ksh", "fish"))

# wrappers, shells and find -exec nest; deeper than this is denied, not trusted
MAX_DEPTH = 6

# git subcommands that always change the repository
GIT_WRITE = frozenset("""
add am apply checkout checkout-index cherry-pick clean clone commit fetch
filter-branch gc init merge merge-file mv prune pull push read-tree rebase
replace reset restore revert rm switch update-index update-ref
""".split())

# git subcommands that only write with certain arguments (listing them is fine)
GIT_SUB_WRITE = {
    "remote": frozenset(("add", "remove", "rm", "rename", "set-url", "set-head",
                         "prune", "update")),
    "worktree": frozenset(("add", "remove", "move", "prune", "lock", "unlock")),
    "submodule": frozenset(("add", "update", "init", "deinit", "sync", "set-url")),
    "stash": frozenset(("", "push", "save", "pop", "apply", "drop", "clear",
                        "store", "create")),
    "notes": frozenset(("add", "append", "copy", "edit", "merge", "prune",
                        "remove")),
    "bisect": frozenset(("start", "good", "bad", "new", "old", "skip", "reset",
                         "run", "replay")),
    "sparse-checkout": frozenset(("set", "add", "init", "disable", "reapply")),
    "reflog": frozenset(("expire", "delete")),
    "bundle": frozenset(("create",)),
}
# `git -c <key>=<value>` keys that make git run a program of the caller's choice
GIT_EXEC_KEYS = frozenset((
    "core.pager", "core.fsmonitor", "core.sshcommand", "core.editor",
    "core.hookspath", "core.gitproxy", "core.askpass", "diff.external",
    "credential.helper", "sequence.editor", "gpg.program",
    "uploadpack.packobjectshook", "protocol.allow",
))
GIT_EXEC_KEY_SUFFIXES = (".textconv", ".command", ".driver", ".cmd",
                         ".helper", ".program")
# pagers that only display
SAFE_PAGERS = frozenset(("", "cat", "less", "more"))
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
TEMP_VAR_NAMES = frozenset(("TMPDIR", "TMP", "TEMP"))
# `d=$(mktemp -d) && cp a "$d/"`: a variable assigned from mktemp in the same
# command is a temp directory too
MKTEMP_ASSIGN = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)=\$\(\s*mktemp\b")
VAR_PREFIX = re.compile(r"^\$(?:\{([A-Za-z_][A-Za-z0-9_]*)\}|([A-Za-z_][A-Za-z0-9_]*))")
_mktemp_vars = set()


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


def _tokenize(command, strip_heredocs=True):
    text = _strip_heredocs(command) if strip_heredocs else command
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
    if not target:
        return False
    if ".." in re.split(r"[/\\]", target):
        return False  # /tmp/../home/x is not under /tmp
    match = VAR_PREFIX.match(target)
    if match:
        name = match.group(1) or match.group(2)
        rest = target[match.end():]
        if name in TEMP_VAR_NAMES or name in _mktemp_vars:
            return rest == "" or rest[0] in "/\\"
        return False
    prefixes = list(TEMP_PREFIXES)
    for name in sorted(TEMP_VAR_NAMES):
        value = os.environ.get(name)
        if value:
            prefixes.append(value.rstrip("/\\") + "/")
            prefixes.append(value.rstrip("/\\") + "\\")
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


def _short_cluster(arg, value_letters):
    """Parse one `-abc` cluster: (flag letters, value letter or None, value).

    The first letter in `value_letters` takes the rest of the cluster as its
    value; if nothing follows, the value is the next word (returned as None).
    """
    flags = []
    for position in range(1, len(arg)):
        letter = arg[position]
        if letter in value_letters:
            rest = arg[position + 1:]
            return flags, letter, (rest if rest else None)
        flags.append(letter)
    return flags, None, None


def _short_option_values(args, letter, value_letters):
    """Every value given to short option `letter`, in any cluster form."""
    values = []
    for index, arg in enumerate(args):
        if not arg.startswith("-") or arg.startswith("--") or len(arg) < 2:
            continue
        _, found, value = _short_cluster(arg, value_letters)
        if found == letter:
            if value is None:
                value = args[index + 1] if index + 1 < len(args) else ""
            values.append(value)
    return values


def _long_option_values(args, long_name, min_prefix):
    """Values of a GNU long option, accepting unambiguous abbreviations."""
    values = []
    for index, arg in enumerate(args):
        if not arg.startswith("--"):
            continue
        name, eq, value = arg.partition("=")
        if len(name) >= min_prefix and long_name.startswith(name):
            if not eq:
                value = args[index + 1] if index + 1 < len(args) else ""
            values.append(value)
    return values


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
                   "--exec-path", "--config-env", "--ref"):
            skip_next = True
            continue
        if arg.startswith("-"):
            continue
        out.append(arg)
    return out


def _git_config_violation(args):
    """`git -c alias.x='!cmd' x` and friends run a program: deny those keys."""
    for index, arg in enumerate(args):
        setting = None
        if arg == "-c" and index + 1 < len(args):
            setting = args[index + 1]
        elif arg.startswith("--config-env="):
            setting = arg.split("=", 1)[1]
        elif arg == "--config-env" and index + 1 < len(args):
            setting = args[index + 1]
        if setting is None:
            continue
        key, _, value = setting.partition("=")
        key = key.lower()
        if (key in ("core.pager",) or key.startswith("pager.")) \
                and value.strip() in SAFE_PAGERS:
            continue
        if key.startswith("alias.") or key in GIT_EXEC_KEYS \
                or key.startswith("pager.") \
                or key.endswith(GIT_EXEC_KEY_SUFFIXES):
            return "`git -c %s` can run a program" % key
    return None


def _git_output_violation(args, sub):
    """`--output=<file>` (diff, log, show, archive) and format-patch write files."""
    writes_to_o = sub in ("format-patch", "archive")
    targets = _long_option_values(args, "--output", 8)
    if sub == "format-patch":
        targets += _long_option_values(args, "--output-directory", 18)
    if writes_to_o:
        targets += _short_option_values(args, "o", "o")
    for target in targets:
        if not _is_temp(target):
            return "`git %s` writes a file (%s)" % (sub, target or "?")
    if sub == "format-patch" and "--stdout" not in args and not targets:
        return "`git format-patch` writes patch files into the tree"
    return None


def _git_verb_after(args, sub):
    """The first word after `sub`, skipping its options (and --ref's value)."""
    try:
        index = args.index(sub) + 1
    except ValueError:
        return ""
    while index < len(args):
        arg = args[index]
        index += 1
        if arg == "--ref":
            index += 1
            continue
        if arg.startswith("-"):
            continue
        return arg
    return ""


def _git_violation(args, positional):
    found = _git_config_violation(args)
    if found:
        return found
    sub = positional[0] if positional else ""
    if sub in GIT_WRITE:
        return "`git %s` changes the repository" % sub
    found = _git_output_violation(args, sub)
    if found:
        return found
    if sub == "hash-object" and any(a == "-w" or (
            a.startswith("-") and not a.startswith("--") and "w" in a)
            for a in args):
        return "`git hash-object -w` writes to the object store"
    if sub == "symbolic-ref" and (len(positional) > 2 or any(
            a in ("-d", "--delete") for a in args)):
        return "`git symbolic-ref` changes a reference"
    if sub in GIT_FLAG_WRITE:
        if any(a in GIT_FLAG_WRITE[sub] for a in args):
            return "`git %s` writes when given those arguments" % sub
        creates = len(positional) >= (3 if sub == "config" else 2)
        if creates and not any(a in GIT_FLAG_READ[sub] for a in args):
            return "`git %s` writes when given those arguments" % sub
    if sub in GIT_SUB_WRITE:
        verb = _git_verb_after(args, sub)
        if verb in GIT_SUB_WRITE[sub]:
            return "`git %s %s` changes the repository" % (sub, verb)
    return None


def _unwrap(command, args):
    """The command a wrapper runs, as a segment of its own (or [])."""
    takes_value = WRAPPERS[command]
    leading = WRAPPER_LEADING_ARGS.get(command, 0)
    index, options_done = 0, False
    while index < len(args):
        arg = args[index]
        if not options_done:
            if arg == "--":
                options_done = True
                index += 1
                continue
            if arg.startswith("-") and len(arg) > 1:
                index += 2 if arg in takes_value else 1
                continue
        if command == "env" and "=" in arg and not arg.startswith("="):
            index += 1
            continue
        if leading:
            leading -= 1
            index += 1
            continue
        break
    return args[index:]


def _env_split_strings(args):
    """`env -S 'cmd args'` runs its value as a command line."""
    scripts = []
    for index, arg in enumerate(args):
        if arg in ("-S", "--split-string"):
            if index + 1 < len(args):
                scripts.append(args[index + 1])
        elif arg.startswith("--split-string="):
            scripts.append(arg.split("=", 1)[1])
        elif arg.startswith("-S") and len(arg) > 2:
            scripts.append(arg[2:])
    return scripts


def _shell_script(args):
    """The script a shell runs with -c (the word after the -c cluster)."""
    for index, arg in enumerate(args):
        if arg.startswith("-") and not arg.startswith("--") and "c" in arg[1:]:
            rest = args[index + 1:]
            if rest and rest[0] == "--":
                rest = rest[1:]
            return rest[0] if rest else ""
    return None


def _file_writer_targets(command, args):
    kind, takes_value = FILE_WRITERS[command]
    value_letters = "".join(v[1] for v in takes_value
                            if len(v) == 2 and v[0] == "-")
    positional, target_dir, every = [], None, False
    index = 0
    while index < len(args):
        arg = args[index]
        index += 1
        if arg == "--":
            positional.extend(args[index:])
            break
        if arg.startswith("--"):
            name, eq, value = arg.partition("=")
            if name == "--target-directory" and command in TARGET_DIR_WRITERS:
                if not eq:
                    value = args[index] if index < len(args) else ""
                    index += 1
                target_dir = value
            elif name == "--reference" and command in ("chmod", "chown", "chgrp"):
                every = True
                if not eq:
                    index += 1
            elif name == "--directory" and command == "install":
                every = True
            elif not eq and name in takes_value:
                index += 1
            continue
        if arg.startswith("-") and len(arg) > 1:
            if command in ("chmod", "chown", "chgrp"):
                continue  # -R, -v, and chmod's -x style modes
            letters = value_letters + ("t" if command in TARGET_DIR_WRITERS else "")
            flags, letter, value = _short_cluster(arg, letters)
            if command == "install" and "d" in flags:
                every = True
            if letter is not None:
                if value is None:
                    value = args[index] if index < len(args) else ""
                    index += 1
                if letter == "t":
                    target_dir = value
            continue
        positional.append(arg)
    if target_dir is not None:
        return [target_dir]
    if every or kind == "all":
        return positional
    if kind == "last":
        return positional[-1:]
    return positional[1:]


def _awk_code(program):
    """The awk program with string and regex literals blanked out.

    What is left is code: a `>` or `|` there is an operator, not data. A `/`
    starts a regex only where an operand cannot precede it.
    """
    out, index, prev = [], 0, ""
    length = len(program)
    while index < length:
        char = program[index]
        if char == '"':
            end = index + 1
            while end < length and program[end] != '"':
                end += 2 if program[end] == "\\" else 1
            out.append('""')
            index, prev = end + 1, '"'
            continue
        if char == "/" and (prev == "" or prev in "(,~!{};&|=:?"):
            end = index + 1
            while end < length and program[end] not in "/\n":
                if program[end] == "\\":
                    end += 1
                elif program[end] == "[":
                    close = program.find("]", end + 2)
                    end = close if close != -1 else length
                end += 1
            out.append("//")
            index, prev = end + 1, "/"
            continue
        if char == "#":
            while index < length and program[index] != "\n":
                index += 1
            continue
        out.append(char)
        if not char.isspace():
            prev = char
        index += 1
    return "".join(out)


# awk writes with `print > "f"`, `print | "cmd"`, `"cmd" | getline` and
# system(); after parentheses collapse, a `>` inside print(...) is a comparison
AWK_WRITE = re.compile(r"\bprintf?\b[^;{}\n]*(>|\|)|\bsystem\s*\(|\|\s*getline")
AWK_SAFE_TARGET = re.compile(r'(>>?|\|)\s*"/dev/(stdout|stderr)"')
AWK_VALUE_OPTIONS = ("-v", "-F", "-f", "-i", "-E", "--assign",
                     "--field-separator", "--file", "--include", "--exec")


def _awk_writes(args):
    if any(a in ("-f", "--file") or a.startswith("--file=") for a in args):
        return False  # the program is in a file the guard does not read
    positional = _positional_skipping(args, AWK_VALUE_OPTIONS)
    if not positional:
        return False
    code = _awk_code(AWK_SAFE_TARGET.sub("", positional[0]))
    previous = None
    while previous != code:
        previous = code
        code = re.sub(r"\([^()]*\)", "()", code)
    return bool(AWK_WRITE.search(code))


def _sed_scripts(args):
    """Script texts of a sed call: -e/--expression values, else the first word."""
    scripts, from_file, positional = [], False, []
    index = 0
    while index < len(args):
        arg = args[index]
        index += 1
        if arg.startswith("--"):
            name, eq, value = arg.partition("=")
            if "--expression".startswith(name) and len(name) >= 4:
                if not eq:
                    value = args[index] if index < len(args) else ""
                    index += 1
                scripts.append(value)
            elif "--file".startswith(name) and len(name) >= 4:
                from_file = True
                if not eq:
                    index += 1
            elif name in ("--line-length",) and not eq:
                index += 1
            continue
        if arg.startswith("-") and len(arg) > 1:
            _, letter, value = _short_cluster(arg, "efl")
            if letter is not None:
                if value is None:
                    value = args[index] if index < len(args) else ""
                    index += 1
                if letter == "e":
                    scripts.append(value)
                elif letter == "f":
                    from_file = True
            continue
        positional.append(arg)
    if not scripts and not from_file and positional:
        scripts.append(positional[0])
    return scripts


def _sed_in_place(args):
    for arg in args:
        if arg.startswith("--"):
            name = arg.split("=", 1)[0]
            if len(name) >= 4 and "--in-place".startswith(name):
                return True
            continue
        if arg.startswith("-") and len(arg) > 1:
            flags, _, _ = _short_cluster(arg, "efl")
            if "i" in flags:
                return True
    return False


def _sed_writes(script):
    """True if a sed script has a w/W/e command or an s///w or s///e flag.

    A small scanner, not a regex: addresses come in too many shapes (`1~2`,
    `/re/I`, `\\,re,`, `!`) for a pattern to list, and a backtracking regex
    over a long argument could outrun the hook's timeout.
    """
    index, length = 0, len(script)

    def skip_blank(i):
        while i < length and script[i] in " \t":
            i += 1
        return i

    def skip_delimited(i, delimiter):
        while i < length and script[i] != delimiter:
            if script[i] == "\\":
                i += 1
            elif script[i] == "\n":
                return i
            i += 1
        return i + 1

    def skip_address(i):
        if i < length and script[i].isdigit():
            while i < length and (script[i].isdigit() or script[i] == "~"):
                i += 1
            return i
        if i < length and script[i] == "$":
            return i + 1
        if i < length and script[i] == "/":
            i = skip_delimited(i + 1, "/")
        elif i + 1 < length and script[i] == "\\":
            i = skip_delimited(i + 2, script[i + 1])
        else:
            return i
        while i < length and script[i] in "IM":
            i += 1
        return i

    while index < length:
        index = skip_blank(index)
        if index >= length:
            break
        if script[index] in ";\n}":
            index += 1
            continue
        index = skip_blank(skip_address(index))
        if index < length and script[index] == ",":
            index = skip_blank(index + 1)
            if index < length and script[index] in "+~":
                index += 1
            index = skip_blank(skip_address(index))
        while index < length and script[index] in "! \t":
            index += 1
        if index >= length:
            break
        command = script[index]
        index += 1
        if command in "wWe":
            return True
        if command == "#":
            while index < length and script[index] != "\n":
                index += 1
        elif command in "sy":
            if index >= length:
                break
            delimiter = script[index]
            index = skip_delimited(index + 1, delimiter)
            index = skip_delimited(index, delimiter)
            if command == "s":
                while index < length and script[index] not in ";\n}":
                    if script[index] in "we":
                        return True
                    index += 1
        elif command in "aicrRL":
            while index < length and script[index] != "\n":
                index += 1
        elif command in "btT:":
            while index < length and script[index] not in ";\n":
                index += 1
    return False


def _positional_skipping(args, takes_value):
    out, skip_next = [], False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg in takes_value:
            skip_next = True
            continue
        if not arg.startswith("-"):
            out.append(arg)
    return out


def _find_exec_commands(args):
    """The commands `find -exec/-execdir/-ok/-okdir` runs, one list each."""
    commands, current = [], None
    for arg in args:
        if current is None:
            if arg in ("-exec", "-execdir", "-ok", "-okdir"):
                current = []
            continue
        if arg in (";", "+", "\;"):
            commands.append(current)
            current = None
            continue
        current.append(arg)
    if current:
        commands.append(current)
    return commands


def _reader_write_violation(command, args):
    """Write options of commands that otherwise only read."""
    if command in ("awk", "gawk", "mawk", "nawk"):
        if "inplace" in args or any(a.startswith("-iinplace") for a in args):
            return "`%s -i inplace` edits files in place" % command
        if _awk_writes(args):
            return "`%s` program writes a file or runs a command" % command
    if command == "sed":
        if _sed_in_place(args):
            return "`sed -i` edits files in place"
        if any(_sed_writes(script) for script in _sed_scripts(args)):
            return "`sed` script writes a file or runs a command"
    if command == "sort":
        targets = _short_option_values(args, "o", "kotST")
        targets += _long_option_values(args, "--output", 3)
        for target in targets:
            if not _is_temp(target):
                return "`sort -o` writes %s" % (target or "a file")
    if command == "yq":
        for arg in args:
            if arg.startswith("--"):
                name = arg.split("=", 1)[0]
                if len(name) >= 4 and "--inplace".startswith(name):
                    return "`yq -i` edits files in place"
            elif arg.startswith("-") and len(arg) > 1:
                flags, _, _ = _short_cluster(arg, "Iopsef")
                if "i" in flags:
                    return "`yq -i` edits files in place"
    if command == "tree":
        for target in _short_option_values(args, "o", "oLIPH"):
            if not _is_temp(target):
                return "`tree -o` writes %s" % (target or "a file")
    if command == "uniq":
        positional = _positional_skipping(args, ("-f", "-s", "-w",
                                                 "--skip-fields",
                                                 "--skip-chars",
                                                 "--check-chars"))
        if len(positional) > 1 and not _is_temp(positional[1]):
            return "`uniq` writes its second argument (%s)" % positional[1]
    if command == "find":
        for index, arg in enumerate(args):
            if arg in ("-fprint", "-fprint0", "-fprintf", "-fls"):
                target = args[index + 1] if index + 1 < len(args) else ""
                if not _is_temp(target):
                    return "`find %s` writes %s" % (arg, target or "a file")
    if command == "time":
        for target in _long_option_values(args, "--output", 5) + \
                _short_option_values(args, "o", "fo"):
            if not _is_temp(target):
                return "`time -o` writes %s" % (target or "a file")
    if command == "date" and any(
        a in ("-s", "--set") or a.startswith("--set=") for a in args
    ):
        return "`date -s` sets the system clock"
    if command == "patch" and not any(
        a in ("--dry-run", "--version", "-v", "--help") for a in args
    ):
        return "`patch` edits files"
    return None


def _nested_violation(command, args, role, depth):
    """Commands that run other commands: check what they run."""
    if command in ("command", "builtin"):
        for arg in args:
            if not arg.startswith("-") or arg == "--":
                break
            if "v" in arg or "V" in arg:
                return None  # `command -v rm` only looks the name up
    if command in WRAPPERS:
        inner = _unwrap(command, args)
        if inner:
            found = _segment_violation(inner, role, depth + 1)
            if found:
                return found
        if command == "env":
            for script in _env_split_strings(args):
                found = _violation(script, role, depth + 1)
                if found:
                    return found
    if command in SHELLS:
        script = _shell_script(args)
        if script:
            return _violation(script, role, depth + 1)
    if command == "eval" and args:
        return _violation(" ".join(args), role, depth + 1)
    if command == "find":
        for inner in _find_exec_commands(args):
            found = _segment_violation(inner, role, depth + 1)
            if found:
                return found
    return None


def _segment_violation(segment, role, depth=0):
    if depth > MAX_DEPTH:
        return "command nesting is too deep to check"
    command = _first_word(segment)
    if not command:
        return None
    if command in DESTRUCTIVE:
        return "`%s` changes files" % command
    args = _args_after(segment, command)
    positional = [a for a in args if not a.startswith("-")]
    sub = positional[0] if positional else ""

    found = _nested_violation(command, args, role, depth)
    if found:
        return found
    if command in FILE_WRITERS:
        for target in _file_writer_targets(command, args):
            if not _is_temp(target):
                return "`%s` writes %s" % (command, target or "a file")
    found = _reader_write_violation(command, args)
    if found:
        return found

    if command == "perl":
        for arg in args:
            if arg == "--in-place" or (
                arg.startswith("-") and not arg.startswith("--") and "i" in arg
            ):
                return "`perl -i` edits files in place"
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


def _violation(command, role, depth=0):
    if depth > MAX_DEPTH:
        return "command nesting is too deep to check"
    _mktemp_vars.update(MKTEMP_ASSIGN.findall(command))
    try:
        tokens = _tokenize(command)
    except ValueError:
        # a heredoc inside a quoted `bash -c '...'` string: stripping its body
        # took the closing quote with it, so read the command as written
        try:
            tokens = _tokenize(command, strip_heredocs=False)
        except ValueError:
            return None  # unparsable (an unbalanced quote): do not block
    for segment in _segments(tokens):
        found = _segment_violation(segment, role, depth)
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
