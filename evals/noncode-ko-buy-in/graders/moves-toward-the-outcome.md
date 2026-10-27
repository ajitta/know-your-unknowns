---
type: llm
focus: last_message
---

The reply prepares for approval by surfacing what the approver does not know and
will object to, aiming at the outcome (an approval that sticks). All of these must
hold:
1. It names what the finance director likely does not know or will object to, with
   evidence or a source for each answer.
2. It treats the director's priorities and the company's unwritten norms as unknown to
   it, asking the user or listing them to find out, rather than asserting them.
3. It states limitations (e.g. tax or legal points to confirm) and who signs off.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
