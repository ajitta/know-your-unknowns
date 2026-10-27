---
type: llm
focus: last_message
---

The reply logs the deviation as a structured entry in a deviation log, aiming at the
outcome (the user can later judge the call). All of these must hold:
1. It writes the entry to a file (a deviation log beside the proposal, or a file the
   user named) or, without a writing tool, presents the entry and says it could not be
   saved.
2. The entry separates what happened (the situation, what the plan said, what was
   chosen) from the reasoning (why, alternatives considered, the risk if wrong).
3. It names what only the user can judge (e.g. how reviewers or the foundation will
   read the merged aim) as a follow-up rather than asserting it.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
