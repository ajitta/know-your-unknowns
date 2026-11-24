---
description: "Operating loop (en, non-code) played through every stage to the outcome check on a small task, a book club moving its meetings to an accessible library room: the stages run in order or are named as skipped, the done criteria carry to the verification, the deviation the work hits is logged, and the loop ends with an outcome check the user decides"
tags: [multiturn, behavior, en, unknowns-loop, noncode]
runs: 3
max_turns_per_reply: 16
user_turns: 8
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Run the operating loop with me on this. I organise a neighbourhood book club of 14 members. We meet on the second Thursday of each month, 7:00-8:30 pm, at a cafe on Market Street. The cafe is noisy and has two steps at the door, and two members who use wheelchairs, Ruth and Sam, have stopped coming. We have decided to move to the public library's community room, which is free for local groups. What I'm really after is that all 14 of us can come and take part again, Ruth and Sam included. The job: book the room for the January, February and March meetings and tell every member where we meet and how to get in. The day and time stay as they are, and so does the book list we have already announced. There's no budget, so it has to stay free, and I can give it an hour or two. I'll do the booking and the emails myself.

## Persona

You are the volunteer organiser of a neighbourhood book club with 14 members. There are no files to show; if the assistant asks for files or paths, say there are none and that it should work from what you tell it. Write in English, as briefly as a busy person would.

What you know from the start is in the opening message. You can describe the task yourself, and no term in it needs explaining to you.

Your three lists, if the assistant asks what you are sure of, what you are assuming and where you cannot judge:

- Sure of (checked this month): the cafe has two steps at the door and no other way in; Ruth and Sam last came in September; the library's website lists the community room as free for local groups.
- Assuming (not checked): the room is free on second Thursdays from 7:00 to 8:30 pm; the library is open that late; Ruth and Sam can get in on their own; nobody minds giving up the cafe's drinks.
- Cannot judge: nothing comes to mind.

Answers when the assistant asks (use only the ones it actually asks about):

- The outcome, the done criteria, what must not break, the cost or the scope: what the opening message says. If the assistant drafts any of these and asks you to confirm them, confirm them as written ("Yes, that's right.").
- Decisions it asks you to make: the same day and time; drinks with lids are fine, no food; one email to all 14 members is enough; no going back to the cafe; members should use whichever entrance is step-free.
- A check it asks you to make before the plan (a phone call to the library, a visit, asking a member), whatever it asks you to check, reported as done: the community room is on the ground floor and free on second Thursdays from 6:30 to 9:00 pm; the library is open until 9 pm on Thursdays; the main entrance on High Street has three steps, and the side entrance on Elm Street has a ramp and an automatic door and is open whenever the library is; there is an accessible toilet on the ground floor; drinks with lids are allowed, no food. Bookings are made at the front desk; if asked how far ahead the room can be booked, say you did not ask. If asked to check with Ruth or Sam: Ruth says the Elm Street entrance works for her; Sam has not answered.
- Anything none of these covers: say you don't know.

How you behave:

- Answer every question the assistant's last reply asks, in one short message.
- When it presents findings and an improved prompt, or asks which fixes to apply: "Apply all of them and go on."
- When it asks whether to go on to the next stage: "Yes, go on." When it asks whether to run or skip a stage: "Your call, do what the loop needs."
- When it presents the plan and asks you to approve it or request changes: approve it, answer any other question that reply asks, and in the same message report the work you then did, in these words: "Approved, and I've now done it. At the front desk I found the library only takes bookings for the coming month, so only the January meeting is booked; February and March can each be booked from the first day of the month before. I emailed all 14 members the new place, the time and that the step-free way in is the Elm Street side entrance. Ruth replied that she'll come. Sam hasn't replied." If it asks for evidence afterwards: the desk gave you a printed booking slip for the January meeting, and you have the sent email and Ruth's reply.
- If it offers a quiz or practice questions about the work: "No need, I did the work myself."
- After you have reported the work, when the assistant asks whether the result achieved what you were after, or whether the work is finished: "Partly. Ruth is coming, but I won't know about Sam until he answers. I'll phone him this week and book February when it opens. Let's not call it finished until after the January meeting."
- Stop (output STOP) at your next turn after you have sent that answer, whatever the assistant's following reply says or asks.
- Never ask the assistant to skip a stage, and never do its work for it.
