---
type: llm
focus: last_message
---

The response is a pre-implementation investigation, not an implementation. All of these must hold:

1. It writes no code and proposes no diff or patch for the task.
2. It separates what the user asked for from what the task actually involves, and it names specific risks -- regressions, unwritten conventions the code enforces, a mechanism the request has no word for, or an earlier attempt -- rather than generic advice like "add tests" or "be careful".
3. Each risk says why it bites: the concrete consequence of missing it.
4. It ends with a rewritten version of the user's request that the user could paste back as the next prompt.

Fail if the response starts implementing, or if it is only a list of clarifying questions with no rewritten prompt.
