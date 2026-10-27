---
type: llm
focus: last_message
---

The reply reads the reference and shows its reading back for correction before
building on it, aiming at the outcome (a policy that fits this library). All of these
must hold:
1. It summarises the reference's intent and sorts its parts: what to keep, what to
   adapt to a smaller library with one paid staff member, what to leave out, and what
   could be better.
2. It shows how each clause would map to the user's library, numbered so the user can
   correct a row, and marks which mappings rest on guesses about the user's library
   (or asks about them).
3. It asks the user to confirm or correct the reading before writing the final policy.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
