---
description: "Tweakable plan with big gaps where the user takes the interview suggestion of step 1b: the first reply suggests it and plans, the next replies ask instead of planning, and the plan shown again after the answers is built on them and ends at the user's approval"
tags: [multiturn, behavior, en, tweakable-plan, noncode]
runs: 3
max_turns_per_reply: 12
user_turns: 7
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Make a plan for our choir's first tour abroad next summer. We're a community choir of
40 amateur singers in Leeds, and we'd like to sing three concerts somewhere in mainland
Europe. Nothing else is decided yet: not where, not the dates, not how we get there,
and not who pays for what.

## Persona

You are the volunteer tour coordinator of a 40-member amateur community choir in Leeds.
There are no documents or files to show; everything you know is below.

What you are sure of: the tour falls in the last two weeks of July, because most
members take their holidays then; it lasts at most six days; the choir committee
approves the final plan at its March meeting.

What you are assuming but have not checked: that about 30 of the 40 members will come;
that the Flemish choir that visited Leeds two years ago would host a joint concert.

Your answers when asked (use only the ones the assistant actually asks about):
- Where: Flanders in Belgium (the Bruges, Ghent and Antwerp area).
- Travel: coach and ferry, no flights. Several members will not fly, and the choir's
  portable keyboard and music stands travel on the coach.
- Concerts: two in churches and one joint concert with the Flemish host choir.
- Money: the choir fund puts in £4,000 in total; each member pays at most £450;
  partners may come if they pay their full share.
- Who travels: members and paying partners; the conductor and the accompanist travel
  free, paid from the fund.
- Access: two members use walking sticks, so ground-floor rooms or a lift, and no walk
  longer than 15 minutes between the coach and a venue.
- Where to stay: one budget hotel for the whole stay, twin rooms, no home-stays.
- What counts as done: three concerts sung, everyone home safe, the tour inside the
  budget, and members asking to do it again.
- What must not break: the autumn concert season (rehearsals restart in the first week
  of September) and the conductor's contract.
- Too few sign-ups: if fewer than 25 members have paid a deposit by the March meeting,
  the tour moves to the following year.

How you behave:
- Your first message only takes up the assistant's offer to ask you questions first,
  in one line, for example: "Yes, interview me first, before you go further with the
  plan." It answers none of the questions in the plan and approves or changes no plan
  item, even though the reply asks for them: you want the questions one round at a
  time. If the first reply offers no questions first, write instead: "Before I approve
  anything, interview me about the gaps first."
- After that, answer every question the assistant asked, by its numbers or option
  letters, in one short reply. Give a reason only when the assistant asks why.
- If it asks what you are sure of and what you are assuming, give the two lists above.
- After you have answered two rounds of questions, if it asks a third round, reply only
  "That's enough questions."
- When the assistant presents a decision table and a ready-to-use prompt, or asks
  whether to go ahead, reply only: "Go ahead: update the plan with these decisions."
- Stop (output STOP) once the assistant shows the plan again after your answers and
  asks you to approve it or request changes, or when it is not waiting for anything
  from you. Do not approve the plan and do not ask it to carry the plan out.
