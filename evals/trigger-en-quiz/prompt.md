---
description: "English trigger phrase for the quiz skill: 'quiz me'"
tags: [trigger, en, quiz]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

You have no access to our repo, so here is the change verbatim. I did not write it —
an agent did — and I am about to open the PR and defend it. Quiz me.

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
