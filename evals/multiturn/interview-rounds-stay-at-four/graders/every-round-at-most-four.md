---
type: llm
focus: transcript
---

Look at every assistant reply separately. In each, count the questions it puts to the
user to answer or decide: every numbered or bulleted question and every sentence ending
in a question mark that asks the user for a decision or a fact. A "why" follow-up on an
earlier answer counts. Answer options under one question are not extra questions, and
one closing offer (for example proceed / edit / stop) counts as one question. A
rhetorical aside or a restatement of the task is not a question.

Both of these must hold:

1. No single assistant reply puts more than 4 questions to the user.
2. When decisions remain after a round, the assistant says further rounds follow (or
   asks whether to continue) rather than silently dropping them; if the user ends the
   interview early, the remaining decisions are listed as open.

State the per-reply counts in your reasoning. Fail if any one reply asks five or more.
