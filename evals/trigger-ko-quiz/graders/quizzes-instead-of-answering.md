---
type: llm
focus: last_message
---

The response prepares the user to defend the work to someone else. All of these must hold:

1. It first explains what changed and why, in terms the user could repeat to a reviewer.
2. It then asks the user questions about the change and stops for answers instead of answering them itself.
3. The questions test understanding of the decisions and their consequences (why this design, what breaks if X), not trivia about names or line numbers.

Fail if it answers its own questions, or if it never asks any.
