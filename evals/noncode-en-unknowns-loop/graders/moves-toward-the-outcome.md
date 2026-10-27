---
type: llm
focus: last_message
---

The reply runs a staged workflow toward the outcome rather than jumping to a plan.
All of these must hold:
1. It establishes the purpose (what the user is ultimately after) and the done
   criteria, or asks for them.
2. It names the stages it will go through (investigation, questions or decisions, a
   plan, the work, a check of the result) and says which stage it is in.
3. It states what it does not know about the user's situation (the building's rules,
   the volunteers, liability) or asks, instead of assuming.
4. It does not deliver the finished plan in this first reply.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
