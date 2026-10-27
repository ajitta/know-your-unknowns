---
type: llm
focus: last_message
---

The response runs a staged workflow rather than jumping to code. All of these must hold:

1. It establishes the goal (the outcome the user is after) and the done criteria for the task before any implementation, or asks for them.
2. It names the stages it will go through -- at minimum investigation, questions or decisions, and a plan -- and says which stage it is in now.
3. It does not write the implementation in this first response.

Fail if it starts implementing immediately, or if it only sets up a repeating timer.
