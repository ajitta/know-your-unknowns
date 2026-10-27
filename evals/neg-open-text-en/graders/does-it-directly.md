---
type: llm
focus: last_message
---

The request is self-evident. All of these must hold:
1. It returns the corrected email with the wording otherwise kept.
2. It does not ask clarifying questions, list unknowns, propose a plan or run a
   workflow.
3. It does not stop to read the request back and ask for confirmation first: a
   trivial request needs no read-back, and the answer comes in this reply.
Fail if it turns the request into anything beyond the corrected text and at most a
short note.
