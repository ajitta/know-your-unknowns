---
type: llm
focus: last_message
---

The user asked for a repeating background check on a five-minute interval. All of
these must hold:

1. The response sets up a recurring or interval task, explains how to set one up, or
   asks the one question it needs in order to do so.
2. It does NOT open a multi-stage explore, question, plan, implement, verify, quiz
   workflow, and does not ask for done criteria, blast radius, or a blind-spot
   investigation before it will proceed.
3. It does not treat the word "loop" as the name of a methodology.

Fail if the response begins a staged engineering workflow instead of a repeating check.
