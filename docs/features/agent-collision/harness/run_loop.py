"""Collision probe for unknowns: which skill/agent fires on generic requests that
should NOT go to unknowns (and positive controls that should).

usage: python3 run_loop.py <arm> [runs] [cell-prefix...]
  arm = name of a dir under arms/ holding the unknowns tree (base, var, ...)
Companion plugins dia + design are loaded in every arm (the owner's install set).
"""
import shlex, json, os, shutil, subprocess, tempfile, sys, concurrent.futures as cf

D = os.path.dirname(os.path.abspath(__file__))
ARM = sys.argv[1]
RUNS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
PREFIX = sys.argv[3:]

DIFF = """```diff
--- a/src/auth/session.py
+++ b/src/auth/session.py
@@ def refresh(token):
-    if token.expired:
-        return None
+    if token.expired and not token.grace:
+        raise SessionExpired(token.user_id)
     return issue(token.user_id)
```"""
CODE = """```python
def avg(xs):
    total = 0
    for x in xs:
        total += x
    return total / len(xs)
```"""
DRAFT = "초안: 우리 서비스는 2019년에 출시됐고 월 사용자 300만 명으로 국내 1위다. 따라서 해외 진출도 무조건 성공한다."

# cell -> (expect, prompt). expect: "NONE" = no unknowns skill/agent may fire;
# "unknowns:x" = that skill must fire; "INFO:..." = recorded only.
C = {
  "l-loop-ko": ("agent:unknowns:independent-reviewer", "/unknowns:loop resume — 구현은 이 브랜치(feature/todo-due-dates)에 끝났어. 계획은 docs/features/todo-due-dates/05-plan.md, 요구사항은 01-discovery.md야. 8단계 독립 검증부터 이어서 해줘."),
  "l-buyin-ko": ("INFO", "/unknowns:buy-in 이 브랜치(feature/todo-due-dates) 머지 승인 받을 설득 문서 만들어줘. 계획은 docs/features/todo-due-dates/05-plan.md야."),
}
JOBS = [(c, i) for c in C if (not PREFIX or any(c.startswith(p) for p in PREFIX)) for i in range(1, RUNS + 1)]
# Pass the current access token as an env var; never copy the credentials file into
# probe config dirs: the copies refresh on their own and wiped the main login once.
TOKEN = (os.environ.get("CLAUDE_CODE_OAUTH_TOKEN") or
         json.load(open(os.path.expanduser("~/.claude/.credentials.json")))["claudeAiOauth"]["accessToken"])
MODEL = os.environ.get("MODEL", "claude-opus-5-5")
OUT = f"{D}/out-loop/{ARM}"
os.makedirs(OUT, exist_ok=True)
os.makedirs(f"{D}/cwd", exist_ok=True)


def claude(prompt, cfg):
    wd = cfg + "/ws"
    shutil.copytree(f"{D}/fixture-feat", wd, symlinks=True)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_CONFIG_DIR"}
    env.update(CLAUDE_CONFIG_DIR=cfg, ENABLE_CLAUDEAI_MCP_SERVERS="false", CLAUDE_CODE_OAUTH_TOKEN=TOKEN)
    cmd = ["claude", "-p", prompt, "--model", MODEL, "--output-format", "stream-json", "--verbose", "--max-turns", "20", "--permission-mode", "acceptEdits", "--allowedTools", "Bash(git:*)", "Bash(make:*)", "Bash(python3:*)",
           "--plugin-dir", f"{D}/arms/{ARM}", "--plugin-dir", f"{D}/arms/dia", "--plugin-dir", f"{D}/arms/design"]
    return subprocess.run(cmd, cwd=wd, env=env, capture_output=True, text=True, timeout=900).stdout


def parse(out):
    fired, text, model, nskills = [], "", None, None
    for line in out.splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") == "system" and e.get("subtype") == "init":
            model = e.get("model"); nskills = len(e.get("skills", []) or [])
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "tool_use":
                    if c.get("name") == "Skill":
                        fired.append(c["input"].get("skill"))
                    elif c.get("name") in ("Task", "Agent"):
                        fired.append("agent:" + str(c["input"].get("subagent_type")))
        if e.get("type") == "result":
            text = e.get("result") or ""
    return fired, text, model, nskills


def run(job):
    cell, i = job
    fn = f"{OUT}/{cell}-{i}.json"
    if os.path.exists(fn):
        return
    cfg = tempfile.mkdtemp(prefix="cc-", dir=os.environ.get("TMPDIR"))
    H = os.path.expanduser("~/.claude")
    for n in ("CLAUDE.md",):
        shutil.copy(f"{H}/{n}", cfg)
    for n in ("superclaude", "commands", "agents", "hooks", "output-styles", ".superclaude_hooks"):
        if os.path.isdir(f"{H}/{n}"):
            shutil.copytree(f"{H}/{n}", f"{cfg}/{n}")
    os.makedirs(f"{cfg}/skills")
    for n in ("sc-author", "sc-prompt"):
        shutil.copytree(f"{H}/skills/{n}", f"{cfg}/skills/{n}")
    s = json.load(open(f"{H}/settings.json")); s.pop("enabledPlugins", None)
    deny = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "probe harness: the agent dispatch was recorded and not run. Do not dispatch another agent; reply with one line naming the agent you chose."}}
    s.setdefault("hooks", {}).setdefault("PreToolUse", []).insert(0, {"matcher": "Agent|Task", "hooks": [{"type": "command", "command": "echo " + shlex.quote(json.dumps(deny))}]})
    json.dump(s, open(f"{cfg}/settings.json", "w"))
    try:
        out = claude(C[cell][1], cfg)
        fired, text, model, ns = parse(out)
        if "Failed to authenticate" in text:
            print("AUTH FAILURE - aborting", cell, i, flush=True); os._exit(3)
        if not model:
            print("EMPTY", cell, i, out[-300:], flush=True); return
        rec = dict(cell=cell, run=i, arm=ARM, expect=C[cell][0], fired=fired, model=model, nskills=ns, text=text[:3000])
        json.dump(rec, open(fn, "w"), ensure_ascii=False, indent=1)
        print(ARM, cell, i, fired, flush=True)
    finally:
        shutil.rmtree(cfg, ignore_errors=True)


with cf.ThreadPoolExecutor(int(os.environ.get("CONC", "2"))) as ex:
    list(ex.map(run, JOBS))
print("DONE", ARM, len(os.listdir(OUT)), "files", flush=True)
