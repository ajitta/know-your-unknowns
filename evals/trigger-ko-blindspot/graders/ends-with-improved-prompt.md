---
type: llm
focus: last_message
---

The response is a blind-spot pass, not an implementation. The pass opens by asking the
user, once, what they are sure of, what they are assuming and where they cannot judge,
and investigates after the answer or a skip; a single reply may therefore hold either
the opening question or the whole pass. Both of these must hold:

1. It writes no code and proposes no diff or patch for the task.
2. It is one of these two:

   A. **The opening question:** it asks for those three lists (sure of / assuming /
      cannot judge), in any wording, and waits for the answer. A risk it flags while
      asking is fine.

   B. **The whole pass:** it separates what the user asked for from what the task
      actually involves; it names specific risks -- regressions, unwritten conventions
      the code enforces, a mechanism the request has no word for, or an earlier
      attempt -- rather than generic advice like "add tests" or "be careful"; each risk
      says why it bites (the concrete consequence of missing it); and it ends with a
      rewritten version of the user's request that the user could paste back as the
      next prompt.

Fail if the response starts implementing; if it answers with risks or advice but
neither asks for the three lists nor ends with a rewritten prompt; or if it asks
clarifying questions other than the three lists and stops there.
