---
type: llm
focus: last_message
---

The reply reads the reference and shows its reading back for correction before
building on it, aiming at the outcome (rules that fit this small school). All of these
must hold:
1. It summarises the reference's intent and sorts its clauses: keep, adapt to a
   120-pupil school, leave out, improve.
2. It maps each clause to the user's school in numbered rows the user can correct, and
   marks or asks which mappings rest on guesses about the user's school.
3. It asks the user to confirm or correct the reading before the final rules.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
