---
type: llm
focus: last_message
---

The reply checks that the user understands the lease review well enough to act on
it tomorrow, aiming at the outcome (a safe signing) rather than restating it. All of
these must hold:
1. It briefly explains the review's key points and what the user must check themselves
   first.
2. It asks applied questions (what to do if the landlord refuses the clause, what the
   numbers mean for risk), not rote recall.
3. It does not reveal the answers before the user has answered: no option is marked as
   correct and no answer key is shown in the reply.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
