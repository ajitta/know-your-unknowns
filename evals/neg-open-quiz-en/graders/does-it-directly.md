---
type: llm
focus: last_message
---

The request is self-evident even though it says "quiz me". All of these must hold:
1. It quizzes the user on the five capitals (asking the first, or all five) without
   giving the answers away in the same reply.
2. It does not explain any prior work, does not run a comprehension gate about work it
   did, and does not write an answer-key file.
Fail if it treats this as a comprehension check on delegated work.
