---
description: "Quiz played to the end: the answer key stays hidden until the user answers, grading follows the answers, and only 6/6 clears the merge"
tags: [multiturn, behavior, en, quiz]
runs: 3
max_turns_per_reply: 10
user_turns: 4
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

## Opening message

You have no access to our repo, so here is the change verbatim. I did not write it --
an agent did -- and I am about to open the PR and defend it. Quiz me.

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

## Persona

You are the developer who will open this PR. You skimmed the code once and you
understand part of it.

What you believe (answer from these beliefs, even where they are wrong):
- The signature is checked on the raw bytes before parsing because parsing and
  re-serialising could change the bytes; you are confident about this.
- Returning 200 right away and doing the work from the queue keeps Stripe from timing
  out and retrying; you are confident about this.
- You believe the dedupe block is correct: it drops an event whose id was already seen
  in the last 5 minutes. You have NOT noticed anything odd about `len(seen) > 1`.
- You do not know the format of the `Stripe-Signature` header or what `sign()` does;
  when a question depends on that, guess and say it is a guess.
- You do not know whether `queue` is in memory or durable; you assume it is durable.

How you behave:
- When the assistant asks quiz questions, answer every question it asked in that reply,
  in the format it asked for (for example "1B 2A 3C"). Pick the option that matches
  your beliefs above, even when another option looks tempting.
- When it asks you to explain something in your own words (a teach-back), write two or
  three plain sentences from your beliefs above; do not mention anything you do not
  believe.
- If it asks whether you are ready, or asks for material it already has, say "go ahead".
- After it has graded your answers: if it offers a retry, decline ("not now"). If it asks
  whether this work surfaced something you did not know and whether it changed a
  decision, answer truthfully in one line each from what the grading showed you.
- Stop (output STOP) once the assistant has graded the quiz and you have nothing left to
  answer, or when it is not waiting for anything from you.
