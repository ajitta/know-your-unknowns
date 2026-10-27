---
type: llm
focus: last_message
---

The response logs the deviation as a structured entry. All of these must hold:

1. It records the situation that was hit, what the plan had said, what was chosen instead, and why.
2. It records the alternatives that were discarded, and the risk or follow-up check if the choice turns out to be wrong.
3. It is a log entry about a decision already taken, not a proposal to change the code now.

Fail if it only acknowledges the change in prose without those fields.
