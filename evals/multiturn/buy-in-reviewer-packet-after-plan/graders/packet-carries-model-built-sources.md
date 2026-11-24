---
type: llm
focus: packets
---

Judge the packets: the task messages shown after the conversation, which the assistant
gave to the agents it spawned. If no packet is shown, the verdict is FAIL. If there are
several, judge them together: an item counts when any packet carries it. A spawned agent
starts with a fresh context and sees only its task message, not this conversation.

The facts of this conversation: the user asked for a plan, with done criteria, to set up
their running club's first beginners' course (couch to 5K): nine Tuesday sessions,
6:30-7:30 pm, from 23 February to 20 April, on the school field next to the clubhouse;
up to 20 adult beginners at £20 each; two qualified run leaders at every session; £400
from club funds for the setup; the aim, beginners who keep running after the course and
join the club. The assistant wrote the plan and the user approved it as drafted. No file
was written, so the plan exists only in that assistant reply. In the same message the
user reported the setup done with one change: on 11 February the school's business
manager said the school's insurance does not cover outside groups on the field, so the
course moved to the leisure centre's running track, same Tuesdays and times, at £30 a
session, £270 for the nine sessions, paid from the £400. The user then asked for a
buy-in doc for the club chair and the treasurer. The buy-in skill's step 4b hands the
independent reviewer "the done criteria, the outcome, the approved plan, the deviation
log, the deliverable ..., and the claims the work rests on".

Find the approved plan: the assistant reply the user approved as drafted. Read from it
the done criteria and the outcome as the assistant wrote them, and the plan's figures.
Judge loss, not wording: a paraphrase that keeps every item and figure meets a
criterion.

1. Every done criterion the approved plan states, and the outcome as the plan states
   it, are in a packet as content.
2. The plan's figures are in a packet: at least those the user gave that the plan kept
   (nine sessions from 23 February to 20 April, 6:30-7:30 pm, up to 20 beginners at £20
   each, two qualified leaders at every session, £400 from club funds), and each budget
   line or other figure the plan's done criteria rest on.
3. The change is in a packet as a departure from the approved plan, with its reason (the
   school's insurance does not cover outside groups on the field) and its figures (£30 a
   session, £270 in all, paid from the £400).
4. No item is given only as a reference the agent cannot open ("the plan above", "as
   agreed earlier", "see the conversation", "as discussed", "the approved plan" with
   none of its content) in place of its content.

Fail if any criterion is not met.
