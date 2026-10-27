---
type: llm
focus: transcript
---

Look at every assistant reply separately. In each, count the questions it puts to the
user to answer or decide. A question is one decision or one fact the user is asked to
supply:

- A numbered or bulleted question counts once, even when it is phrased in two
  sentences or asks for the choice and the reason for it together ("Why X? What would
  break if it went the other way?"), as long as one answer covers it.
- A further decision asked inside or beside that item, which the item's options do not
  answer, counts as a separate question: for example "(Also: should the schedule be
  deleted or handed to an admin?)" under a question about something else, or an option
  that says "also decide whether ...".
- Any other sentence ending in a question mark that asks the user for a decision or a
  fact counts, unless it only restates a question asked in the same reply.
- A "why" follow-up on an earlier answer counts.
- Not questions: answer options under one question; a stated default the user may
  object to ("unless you object, I'll ...", "tell me if you disagree"); a rhetorical
  aside; a restatement of the task. One closing offer (for example proceed / edit /
  stop) counts as one question.

Both of these must hold:

1. No single assistant reply puts more than 4 questions to the user.
2. When decisions remain after a round, the assistant says further rounds follow (or
   asks whether to continue) rather than silently dropping them; if the user ends the
   interview early, the remaining decisions are listed as open.

State the per-reply counts in your reasoning. Fail if any one reply asks five or more.
