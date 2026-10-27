---
type: llm
focus: last_message
---

The request is self-evident even though it says "계획". All of these must hold:
1. It gives a short shopping list or order directly (a few lines).
2. It does not produce a plan document with done criteria, alternatives, decisions
   ordered by likelihood of change, or questions about the user's situation.
Fail if it treats the errand as work needing a planning method.
