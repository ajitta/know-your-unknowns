---
description: "quiz from the source talk's own request (example #11), with no 'quiz' or 'test my understanding': the description no longer says 'or before merging', so this measures whether the merge-time comprehension request still reaches the skill"
tags: [behavior, en, quiz]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

An agent wrote this change for me and you can't see our repo, so here it is verbatim.
I want to make sure I understand everything that happened in this change before I merge.

```python
@app.post("/hooks/stripe")
def receive(req):
    raw = req.get_data()
    if not hmac.compare_digest(sign(raw, SECRET), req.headers["Stripe-Signature"]):
        return "", 400                      # verify before parsing
    event = json.loads(raw)
    if seen.setdefault(event["id"], time.time()) < time.time() - 300:
        del seen[event["id"]]               # 5-minute dedupe window
    elif len(seen) > 1:
        return "", 200                      # already handled
    queue.put(event)
    return "", 200                          # ack now, work later
```
