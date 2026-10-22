"""Collision probe for unknowns: which skill/agent fires on generic requests that
should NOT go to unknowns (and positive controls that should).

usage: python3 run.py <arm> [runs] [cell-prefix...]
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
C0 = {
  # --- brainstorm collisions ---
  "b-name-ko": ("NONE", "동네에 새로 여는 빵집 이름 브레인스토밍 해줘."),
  "b-event-ko": ("NONE", "다음 달 팀 워크숍 아이스브레이킹 아이디어 브레인스토밍 좀 해줘."),
  "b-blog-en": ("NONE", "Brainstorm some blog post ideas about learning Rust."),
  "b-idea-ko": ("NONE", "점심 메뉴 추천 앱을 만들고 싶은데, 이 아이디어 같이 브레인스토밍해보자."),
  "b-socratic-ko": ("NONE", "퇴사하고 1인 앱 개발로 먹고살고 싶어. 같이 브레인스토밍하면서 허점 좀 찔러줘."),
  "b-options-ko": ("NONE", "이번 주말에 서울에서 뭐 할지 옵션 보여줘."),
  "b-pos-ko": ("unknowns:brainstorm", "무료에서 유료로 넘어가는 전환율이 두 분기째 2.1%에서 안 움직여. 가입 퍼널, 온보딩\n체크리스트, 페이월 전부 손댈 수 있고 엔지니어 한 명이 6주 동안 붙을 수 있어.\n해법 후보 펼쳐줘."),
  # --- review collisions ---
  "r-pr-ko": ("NONE", "이 PR 리뷰해줘.\n" + DIFF),
  "r-code-en": ("NONE", "Review this function for bugs:\n" + CODE),
  "r-merge-en": ("NONE", "I'm about to merge this PR. Can you review it first?\n" + DIFF),
  "r-refine-ko": ("NONE", "이 초안 다시 검토해서 고쳐줘.\n" + DRAFT),
  "r-design-ko": ("NONE", "이 설정 화면 디자인 리뷰해줘. 왼쪽에 사이드바, 가운데 폼, 오른쪽 위에 저장 버튼이 있고 글씨가 전부 12px이야."),
  "r-done-ko": ("NONE", "인증 리팩터링 다 끝냈어. 머지 전에 한번 검토해줘.\n" + DIFF),
  "r-pos-ko": ("unknowns:buy-in", "저장소를 볼 수 없으니 작업 상태를 여기 적을게. 직접 만든 세션 쿠키를 15분짜리 액세스\n토큰 + 리프레시 로테이션이 있는 서명된 JWT로 옮겼고, 기존 쿠키 경로는 플래그 뒤에서\n한 릴리스 동안 계속 받아. 인증 테스트는 61/61 통과(이전 48개), 부하 테스트는 2,400 req/s\n에서 p99 41ms, 아직 리프레시 토큰 재사용 탐지와 여러 기기 동시 로그아웃은 처리 못 했어.\n배포 전에 시니어 엔지니어 3명한테 승인을 받아야 해. 설득 문서 만들어줘."),
  # --- other generic names ---
  "g-plan-ko": ("NONE", "다음 주 운동 계획 세워줘. 주 3회, 한 번에 40분."),
  "g-quiz-ko": ("NONE", "한국사 퀴즈 5문제 내줘."),
  "g-interview-ko": ("NONE", "내일 백엔드 개발자 면접이야. 모의 인터뷰 해줘."),
  "g-notes-ko": ("NONE", "회의 내용 노트로 정리해줘: 출시일 11/3 확정, QA는 민수, 마케팅 예산 미정."),
  "g-reference-ko": ("NONE", "이 참고문헌을 APA 형식으로 바꿔줘: Kim, 2020, 한국 IT 산업 연구, 서울대출판부."),
}
C = {
  "l-loop-ko": ("agent:unknowns:independent-reviewer", "/unknowns:loop resume — 구현은 이 브랜치(feature/todo-due-dates)에 끝났어. 계획은 docs/features/todo-due-dates/05-plan.md, 요구사항은 01-discovery.md야. 8단계 독립 검증부터 이어서 해줘."),
  "l-buyin-ko": ("INFO", "/unknowns:buy-in 이 브랜치(feature/todo-due-dates) 머지 승인 받을 설득 문서 만들어줘. 계획은 docs/features/todo-due-dates/05-plan.md야."),
}
JOBS = [(c, i) for c in C if (not PREFIX or any(c.startswith(p) for p in PREFIX)) for i in range(1, RUNS + 1)]
OUT = f"{D}/out-loop/{ARM}"
os.makedirs(OUT, exist_ok=True)
os.makedirs(f"{D}/cwd", exist_ok=True)


def claude(prompt, cfg):
    wd = cfg + "/ws"
    shutil.copytree(f"{D}/fixture-feat", wd, symlinks=True)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_CONFIG_DIR"}
    env.update(CLAUDE_CONFIG_DIR=cfg, ENABLE_CLAUDEAI_MCP_SERVERS="false")
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--max-turns", "20", "--permission-mode", "acceptEdits", "--allowedTools", "Bash(git:*)", "Bash(make:*)", "Bash(python3:*)",
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
    shutil.copy(f"{H}/.credentials.json", cfg)
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
        if not model:
            print("EMPTY", cell, i, out[-300:], flush=True); return
        rec = dict(cell=cell, run=i, arm=ARM, expect=C[cell][0], fired=fired, model=model, nskills=ns, text=text[:3000])
        json.dump(rec, open(fn, "w"), ensure_ascii=False, indent=1)
        print(ARM, cell, i, fired, flush=True)
    finally:
        shutil.rmtree(cfg, ignore_errors=True)


with cf.ThreadPoolExecutor(int(os.environ.get("CONC", "4"))) as ex:
    list(ex.map(run, JOBS))
print("DONE", ARM, len(os.listdir(OUT)), "files", flush=True)
