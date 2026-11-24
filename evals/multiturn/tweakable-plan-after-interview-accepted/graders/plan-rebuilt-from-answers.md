---
type: llm
focus: transcript
---

The user asked for a plan for their choir's first tour abroad. The assistant's first
reply gave a plan and suggested questions first; the user took the suggestion, answered
the questions, and then said "Go ahead: update the plan with these decisions." (or the
assistant showed the plan again without being told to). The tweakable plan says: "The
plan ends at the user's approval; on change requests, revise the named items and every
item that builds on them and show the plan again", and its step 1 builds the plan from
the conversation context, the interview's decisions included.

Find the revised plan: the first assistant reply after the user's answers that shows
the plan again. If no reply after the user's answers shows the plan again, fail. Judge
that reply against the user's messages before it. All of these must hold:

1. It is the plan itself shown again, not only a list of what changed: it opens with
   the line on the outcome, the done criteria, what must not break and the allowed cost
   and change scope, and its decision items come ahead of the mechanical (routine)
   items.
2. Every decision the user gave in an answer appears as the chosen option of the item
   it settles (for example coach and ferry with no flights, Flanders, £4,000 from the
   fund and at most £450 a member, members and paying partners only, one budget hotel
   with ground-floor rooms or a lift). Only answers the user actually gave count; check
   each against the user's messages. No item still rests on a guess an answer replaced
   (for example a cost or a schedule built on flights after the user chose the coach),
   and nothing the user answered is still listed as unknown or "not set".
3. What the user never gave stays marked: a part of the opening line that the
   conversation did not give reads "not set" (step 2: "Write 'not set' for any part the
   context does not give") rather than a value the assistant chose, and the assistant's
   remaining assumptions are listed as its own, not presented as the user's decisions.
4. Every decision item, the last as fully as the first, lists its considered
   alternatives lettered A, B, ..., each with why it was rejected, the items the user
   settled in the interview included.
5. The reply ends at the user's approval: it asks the user to approve or request
   changes by item, and it does not go on to carry the plan out (for example writing
   the letters to venues or the sign-up message to members).

Fail if no plan is shown again after the answers, if the plan shown again contradicts
or leaves out an answer the user gave, or if it presents a choice the user never made
as the user's decision.
