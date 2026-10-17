#!/usr/bin/env python3
"""Generate HTML-page runs for the unknowns plugin and record token usage.
Usage: PLUGIN=<checkout> OUTDIR=<dir> RUNS=5 WORKERS=3 python3 run_html.py case1,case2
Each run gets a fresh cwd under $TMPROOT (default ./tmp); the pages it writes are copied to OUTDIR.
"""
import json, os, subprocess, sys, tempfile, shutil, glob, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.environ["PLUGIN"]; OUT = os.environ["OUTDIR"]
RUNS = int(os.environ.get("RUNS", "1")); WORKERS = int(os.environ.get("WORKERS", "3"))
MODEL = os.environ.get("M", "claude-opus-5-5")
TMPROOT = os.path.abspath(os.environ.get("TMPROOT", "tmp"))
os.makedirs(OUT, exist_ok=True)
env = dict(os.environ); env.pop("CLAUDE_CONFIG_DIR", None); env["ANTHROPIC_MODEL"] = MODEL
TOOLS = "Skill,Read,Write,Edit,Bash,Glob,Grep"

def gen(case, i):
    path = f"{OUT}/{case}.{i}.json"
    if os.path.exists(path):
        return
    prompt = open(f"{HERE}/cases/{case}.md").read().strip()
    cwd = tempfile.mkdtemp(prefix=f"kyu-{case}-", dir=TMPROOT)
    cmd = ["claude", "-p", prompt, "--plugin-dir", PLUGIN, "--output-format", "stream-json",
           "--verbose", "--allowedTools", TOOLS, "--max-turns", "40"]
    try:
        p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=1800)
        stdout, stderr = p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        stdout, stderr = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "TIMEOUT"
    tools, result = [], {}
    for line in stdout.splitlines():
        try: ev = json.loads(line)
        except Exception: continue
        if ev.get("type") == "result": result = ev
        msg = ev.get("message")
        if isinstance(msg, dict) and msg.get("role") == "assistant":
            for c in msg.get("content", []) or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    inp = c.get("input", {})
                    tools.append({"name": c["name"], "input": {k: (str(v)[:300]) for k, v in inp.items()},
                                  "size": {k: len(str(v)) for k, v in inp.items()}})
    pages = sorted(glob.glob(f"{cwd}/.unknowns/**/*.html", recursive=True)) + sorted(glob.glob(f"{cwd}/*.html"))
    saved = []
    for j, pg in enumerate(pages):
        dst = f"{OUT}/{case}.{i}.page{j}.html"; shutil.copy(pg, dst); saved.append(os.path.relpath(pg, cwd))
    rec = {"case": case, "run": i, "usage": result.get("usage", {}), "cost": result.get("total_cost_usd"),
           "turns": result.get("num_turns"), "duration_ms": result.get("duration_ms"),
           "is_error": result.get("is_error"), "last": result.get("result", ""),
           "tools": tools, "pages": saved, "err": stderr[-800:]}
    json.dump(rec, open(path, "w"), ensure_ascii=False, indent=1)
    shutil.rmtree(cwd, ignore_errors=True)
    print(case, i, "out_tok", rec["usage"].get("output_tokens"), "cost", rec["cost"], "pages", saved, flush=True)

os.makedirs(TMPROOT, exist_ok=True)
jobs = [(c, i) for c in sys.argv[1].split(",") for i in range(RUNS)]
with cf.ThreadPoolExecutor(WORKERS) as ex:
    for f in cf.as_completed([ex.submit(gen, c, i) for c, i in jobs]):
        f.result()
