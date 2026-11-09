---
description: "Deep interview on request ('40-question level'): every round stays at four questions, later rounds go into finer decisions opened by earlier answers, and when the decisions run out the interview ends with its deliverable instead of filler"
tags: [multiturn, behavior, en, interview]
runs: 3
max_turns_per_reply: 8
user_turns: 6
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Grill me on the requirements for our team's on-call rotation tool — 40-question level.

## Persona

You are the lead of a platform team of 8 engineers, and you want a small internal tool to
run the team's on-call rotation. There is no code or document to show; everything you
know is below. If the assistant asks for files or paths, say there are none yet.

Your facts (give each only when a question asks for it):
- Team: 8 engineers in two time zones, 5 in Berlin and 3 in New York. Only this team
  uses the tool; no other teams.
- Rotation: weekly. One primary is on call for the whole week, day and night. The next
  person in the rotation is the secondary (backup).
- Handoff: Monday 15:00 Berlin time (09:00 New York), when both offices are working.
- Paging: PagerDuty is already paid for and stays the paging and escalation system. The
  tool pages nobody; it decides who is on call and writes that into the existing
  PagerDuty schedule. The tool's rotation is the source of truth; nobody edits the
  PagerDuty schedule by hand.
- Slack is where the team works. The tool is a Slack bot (slash commands and direct
  messages); no web UI. Announcements go to the existing #oncall channel.
- Swaps: an engineer proposes a swap in Slack and it takes effect when the other
  engineer accepts; no approval from you.
- Time off: engineers enter their time off through the bot; the rotation skips anyone
  who is off during their week, and they take the next free week.
- Fairness: everyone does the same number of weeks per quarter; the bot can show the
  count per person.
- Permissions: any engineer can swap or enter time off for themselves; only you, the
  lead, can add or remove people or change the rotation order.
- Failure: if the write to PagerDuty fails, or a week ends up with nobody on call, the
  bot posts in #oncall and messages you at once; you cover until it is fixed.
- Reminders: a direct message on the Friday before someone's week, and one hour before
  handoff.
- Handoff note: the outgoing person is prompted to post a short handoff note in #oncall.
- Data kept: names, Slack IDs and time zones only; phone numbers stay in PagerDuty.
- Out of scope: on-call pay (HR handles it), incident management, postmortems,
  calendar export.
- Build: one engineer for about two weeks. It runs on the internal server where the
  team's other Slack bots run. No new paid services.

What you are sure of: the team is 8 engineers in two time zones; the rotation is weekly;
the team works in Slack; PagerDuty is already paid for.

What you are assuming but have not checked: that your PagerDuty plan allows schedules to
be changed through its API.

How you behave:
- If the assistant asks what you are sure of and what you are assuming, give only the
  two short lists just above, not the rest of your facts.
- Answer every question in the assistant's last reply, by its numbers or option
  letters, in one short reply: a few words per question, decisive, from your facts.
  Give a reason only when the assistant asks why; then give one sentence that fits
  your facts.
- For a question your facts do not cover, pick the simplest option it offers; with no
  options, give the simplest answer that fits your facts in a few words. Never add a
  new feature.
- When the assistant asks whether to continue, go deeper or wrap up (in any wording),
  answer that part with "keep going", alongside your answers to any other questions in
  the same reply. Never ask it to stop and never ask for the write-up yourself.
- Stop (output STOP) once the assistant has delivered a decision table or a
  ready-to-use prompt and asks nothing more than an offer to proceed, edit or stop. If
  that reply also asks whether to keep going with more questions, reply "keep going"
  instead. Do not ask it to build the tool.
