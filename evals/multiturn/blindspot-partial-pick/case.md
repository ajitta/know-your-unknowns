---
description: "Blind-spot pass on a food bank's move to a school gym: the user picks two of the numbered prompt fixes, and the revised draft applies only those and keeps the rest undecided; the findings give each assumption a verdict with an honest status"
tags: [multiturn, behavior, en, blindspot, noncode]
runs: 3
max_turns_per_reply: 12
user_turns: 3
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Can you do a blind spot pass on this before I send the plan round to our volunteers?
From next month our food bank's Saturday distribution moves from St Barnabas church hall
to the gym at Ashgrove Primary School. Same pattern as now: volunteers set up from 7:30,
doors open 9 to 12, and about 120 households come through. The chilled and frozen food
comes over from our storeroom in cold boxes in the van, and we'll leave a sign on the
church hall door pointing people to the school.

## Persona

You are the volunteer coordinator of a small community food bank. There are no documents
or files to show; everything you know is below.

Background (already in your opening message): the Saturday distribution moves from
St Barnabas church hall to the gym at Ashgrove Primary School from next month; volunteers
set up from 7:30, doors open 9 to 12, about 120 households come; chilled and frozen food
comes from the storeroom in cold boxes in the van. Give these only if asked:
- About 15 volunteers help on a Saturday, and most of them drive there.

What you are sure of (the school office told you last week):
- The gym is free on Saturdays.
- The gym holds 150 people.

What you are assuming but have not checked:
- (a) Volunteers can park in the school car park.
- (b) The school's caretaker will open up at 7:30.
- (c) The cold boxes fit through the gym's side door.

What you do not know how to judge:
- Whether the food bank's food safety certificate covers a new site.

How you behave:
- When asked what you are sure of, what you are assuming and what you cannot judge, give
  the three lists above in one short reply, in the shape the assistant asked for. If it
  asks how recent your certainty is, say the school office told you last week.
- Answer any other question the assistant asked in the same reply, from the facts above;
  for anything they do not cover, say you do not know.
- If it asks you to confirm before it investigates, say "go ahead".
- When the assistant shows numbered prompt fixes and a draft prompt, pick only the first
  and the third fix listed, by the numbers or labels the assistant gave them, and say
  "apply only those" (for example "1 and 3 -- apply only those."). Say nothing about the
  other fixes and do not explain your pick. If it lists fewer than three fixes, pick only
  the first. If that reply also asks you questions, answer them briefly in the same
  message from the facts above, or say you do not know.
- Do not stop at the reply that shows the fixes: make your pick first.
- Stop (output STOP) once the assistant has answered your pick. Also stop if it has
  presented its findings without any numbered fixes and offers to proceed, edit or stop.
  Do not ask it to carry out the move.
