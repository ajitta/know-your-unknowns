---
type: llm
focus: last_message
---

The reply works in the Unknown cell, where neither the user nor the assistant can
know the answer from the conversation. Grade whether it moves toward the outcome by
surfacing both sides' unknowns rather than producing a confident answer. All of these
must hold:

1. It asks before recommending: it puts questions to the user about what only the user
   knows (their values, family situation, risk tolerance, career goals) and gives no
   verdict in this reply.
2. It asks at most a handful of questions (four or fewer), each saying why it matters.
3. Any general facts it brings in (startup risk, public-sector terms) are framed as
   things to check against the user's situation, not as a decision.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
