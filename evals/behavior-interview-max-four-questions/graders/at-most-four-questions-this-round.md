---
type: llm
focus: last_message
---

Count the questions this response puts to the user in this round: every numbered
item, bulleted item or sentence ending in a question mark that asks the user to
decide something. A rhetorical aside or a restatement of the task is not a question.

All of these must hold:

1. The count is 4 or fewer. The prompt deliberately offers at least nine open
   decisions, so asking them all at once is the failure this case exists to catch.
2. The response says or implies that further rounds follow, rather than silently
   dropping the decisions it did not ask about.
3. Each question carries a one-line reason why the answer matters.
4. The questions go after the highest-blast-radius unknowns -- architecture, data, or
   external contract -- not formatting, wording or timezone display.
5. This is round 1, so its questions are open questions about the user's situation
   (what the assistant cannot know or judge from here), without multiple-choice options
   for the decisions; those come in later rounds.

Fail if five or more decisions are put to the user at once.
