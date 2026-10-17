#!/usr/bin/env python3
"""Compare base vs var HTML runs: output tokens, cost, bytes written, page checks.
Usage: python3 analyze.py b6   (reads b6-base/ b6-var/ and b6-*.checks.jsonl)"""
import json, glob, sys, math, statistics as st, itertools, os

pre = sys.argv[1]

def mwu_p(a, b):
    """Two-sided Mann-Whitney U p-value, exact by permutation of ranks (small n)."""
    allv = a + b
    ranks = {}
    for i, v in enumerate(sorted(allv)):
        ranks.setdefault(v, []).append(i + 1)
    r = {v: sum(x) / len(x) for v, x in ranks.items()}
    ra = sum(r[v] for v in a)
    n1, n2 = len(a), len(b)
    u = ra - n1 * (n1 + 1) / 2
    mu = n1 * n2 / 2
    allr = [r[v] for v in allv]
    obs = abs(u - mu)
    cnt = tot = 0
    for comb in itertools.combinations(range(n1 + n2), n1):
        s = sum(allr[i] for i in comb) - n1 * (n1 + 1) / 2
        tot += 1
        if abs(s - mu) >= obs - 1e-9:
            cnt += 1
    return cnt / tot

def load(arm):
    out = {}
    for f in sorted(glob.glob(f"{pre}-{arm}/*.json")):
        r = json.load(open(f))
        if not r.get("usage"):
            print("NO USAGE", f, r.get("err", "")[-200:]); continue
        if "session limit" in (r.get("last") or "") or "hit your limit" in (r.get("last") or ""):
            print("LIMIT", f); continue
        w = sum(t.get("size", {}).get("content", 0) + t.get("size", {}).get("new_string", 0)
                for t in r["tools"] if t["name"] in ("Write", "Edit"))
        # the saved page carries the template's marker; commands are truncated, so they can miss it
        rendered = any("<!-- unknowns-page -->" in open(f"{pre}-{arm}/{r['case']}.{r['run']}.page{j}.html", encoding="utf-8").read()
                       for j in range(len(r["pages"])))
        reads = sum(1 for t in r["tools"] if t["name"] == "Read")
        u = r["usage"]
        out.setdefault(r["case"], []).append(dict(out=u["output_tokens"], think=u.get("output_tokens_details", {}).get("thinking_tokens", 0),
            cost=r["cost"] or 0, wrote=w, rendered=rendered, turns=r["turns"], pages=len(r["pages"]), reads=reads, run=r["run"]))
    return out

base, var = load("base"), load("var")
def med(x): return st.median(x) if x else float("nan")
rows = []
for case in sorted(set(base) | set(var)):
    a, b = base.get(case, []), var.get(case, [])
    print(f"\n## {case}  n={len(a)}/{len(b)}")
    for k in ("out", "think", "wrote", "cost", "turns"):  # wrote = characters of Write content + Edit new_string
        xa, xb = [r[k] for r in a], [r[k] for r in b]
        p = mwu_p(xa, xb) if xa and xb else float("nan")
        ch = (med(xb) - med(xa)) / med(xa) * 100 if med(xa) else float("nan")
        print(f"  {k:6} base med {med(xa):>9.1f} [{min(xa) if xa else 0:.0f}-{max(xa) if xa else 0:.0f}]  var med {med(xb):>9.1f} [{min(xb) if xb else 0:.0f}-{max(xb) if xb else 0:.0f}]  Δ {ch:+.0f}%  MWU p={p:.3f}")
    print(f"  pages base {sum(r['pages']>0 for r in a)}/{len(a)}  var {sum(r['pages']>0 for r in b)}/{len(b)}  var rendered via script {sum(r['rendered'] for r in b)}/{len(b)}")
tot = lambda d, k: sum(r[k] for v in d.values() for r in v)
nb, nv = sum(map(len, base.values())), sum(map(len, var.values()))
print(f"\nTOTAL cost base ${tot(base,'cost'):.2f} ({nb} runs)  var ${tot(var,'cost'):.2f} ({nv} runs)")
print(f"mean out tokens base {tot(base,'out')/nb:.0f}  var {tot(var,'out')/nv:.0f}")
print(f"mean chars written base {tot(base,'wrote')/nb:.0f}  var {tot(var,'wrote')/nv:.0f}")
for arm in ("base", "var"):
    path = f"{pre}-{arm}.checks.jsonl"
    if not os.path.exists(path):
        continue
    cs = [json.loads(l) for l in open(path)]
    keys = ["dark", "focus", "motion", "lang", "replyBox", "defaultReply", "reacts", "copyButton"]
    summary = {k: sum(bool(c[k]) for c in cs) for k in keys}
    summary["jsErrors"] = sum(bool(c["jsErrors"]) for c in cs)
    summary["remote"] = sum(c["remote"] > 0 for c in cs)
    print(arm, f"pages={len(cs)}", summary)
