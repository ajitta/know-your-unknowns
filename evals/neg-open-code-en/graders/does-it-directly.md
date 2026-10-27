---
type: llm
focus: last_message
---

The request is self-evident. All of these must hold:
1. It returns the function with `tmp` renamed to `total` everywhere.
2. It does not ask clarifying questions, list unknowns, propose a plan or run a
   workflow.
Fail if it does anything other than the rename (plus at most one short sentence).
