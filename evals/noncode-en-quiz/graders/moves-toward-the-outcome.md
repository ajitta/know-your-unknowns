---
type: llm
focus: last_message
---

The reply checks that the user can explain and defend the analysis, aiming at the
outcome (the user can answer the board) rather than restating the analysis. All of
these must hold:
1. It briefly explains the analysis's structure, key decisions and weak points first,
   including what the user must verify themselves.
2. It asks questions that test applied understanding (what would you say if a board
   member asked..., what changes if the rumoured competitor opens), not rote recall.
3. It does not reveal the answers before the user has answered: no option is marked
   as correct and no answer key is shown in the reply.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
