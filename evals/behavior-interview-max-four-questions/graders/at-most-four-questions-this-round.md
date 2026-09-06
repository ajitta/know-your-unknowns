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
4. The four it chose are the highest-blast-radius ones -- architecture, data model,
   or external contract -- not formatting, wording or timezone display.

Fail if five or more decisions are put to the user at once.
