---
type: llm
focus: last_message
---

The response interviews the user instead of implementing. All of these must hold:

1. It asks the user questions and does not begin implementing or writing the feature.
2. The questions are ordered by blast radius: architecture or data-model questions come before UI, wording or formatting questions.
3. Each question carries a one-line reason why the answer matters.
4. It puts at most 4 questions to the user in this round.

Fail if it answers its own questions and proceeds, or if it opens with cosmetic questions.
