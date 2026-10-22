import json, glob, os, sys, collections, math
D = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else "out-fx2"


def fisher(a, b, c, d):
    # two-sided Fisher exact for [[a,b],[c,d]]
    n = a + b + c + d; r1 = a + b; c1 = a + c
    def p(x):
        return math.comb(r1, x) * math.comb(n - r1, c1 - x) / math.comb(n, c1)
    p0 = p(a); lo = max(0, c1 - (n - r1)); hi = min(r1, c1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= p0 + 1e-12))


res = collections.defaultdict(lambda: collections.defaultdict(list))
for f in glob.glob(f"{D}/{OUT}/*/*.json"):
    r = json.load(open(f))
    unk = [x for x in r["fired"] if "unknowns" in str(x)]
    exp = r["expect"]
    if exp == "NONE":
        ok = not unk
    elif exp.startswith("INFO"):
        ok = None
    else:
        ok = bool(r["fired"]) and r["fired"][0] == exp or exp in r["fired"]
    res[r["cell"]][r["arm"]].append((ok, r["fired"][:2]))
for cell in sorted(res):
    line = [cell]
    cnt = {}
    ARMS = ["base"] + sorted({a for c in res.values() for a in c} - {"base"})
    for arm in ARMS:
        v = res[cell].get(arm, [])
        p = sum(1 for o, _ in v if o); cnt[arm] = (p, len(v))
        fired = collections.Counter(str(x[1][0]) if x[1] else "-" for x in v)
        line.append(f"{arm} {p}/{len(v)} {dict(fired)}")
    if all(cnt[a][1] for a in cnt):
        (pb, nb), (pv, nv) = cnt["base"], cnt[ARMS[-1]]
        line.append("p=%.4f" % fisher(pb, nb - pb, pv, nv - pv))
    print(" | ".join(line))
