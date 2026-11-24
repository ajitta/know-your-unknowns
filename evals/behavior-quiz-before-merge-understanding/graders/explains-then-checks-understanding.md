---
type: llm
focus: last_message
---

The user, about to merge a change an agent wrote, asked to make sure they understand
everything that happened in it. Judge the reply. All of these must hold:

1. It explains what the change does and why, in terms the user could repeat to a
   reviewer (signature check before parsing, the dedupe window, acknowledging before the
   work is done).
2. It then checks the user's understanding with questions and stops for the answers,
   instead of answering them itself.
3. The questions are about decisions and their consequences (why this order, what
   happens if a step goes wrong), not trivia such as names or line numbers.

Fail if the reply only explains and asks nothing, or if it answers its own questions.
