---
type: llm
focus: last_message
---

The reply logs the deviation as a structured entry, aiming at the outcome (the user
can judge the change and its risks later). All of these must hold:
1. It writes the entry to a file (a deviation log beside the event plan, or a file the
   user named) or, without a writing tool, presents the entry and says it could not be
   saved.
2. The entry separates what happened (situation, what the plan said, what was chosen)
   from the reasoning (why, alternatives, risk if wrong).
3. It flags the accessibility risk (no elevator) and what only the user can judge or
   check (who attends, the school's conditions) as follow-ups.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
