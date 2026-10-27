---
type: llm
focus: last_message
---

The request is self-evident. All of these must hold:
1. It returns the notice rewritten in polite Korean with the same content; offering a
   second variant is fine.
2. It does not ask clarifying questions before answering, list unknowns, propose a plan
   or run a workflow.
3. It does not stop to read the request back and ask for confirmation first: a
   trivial request needs no read-back, and the answer comes in this reply.
Fail if it withholds the rewrite or turns the request into a method (questions first,
unknowns lists, a plan).
