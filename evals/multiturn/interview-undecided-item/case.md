---
description: "Interview where the user leaves one item open on purpose (ko): the date waits for the cousins' replies, and the ready-to-use prompt carries it as the user's open item, with that reason, and tells the receiver not to pick a date"
tags: [multiturn, behavior, ko, interview, noncode]
runs: 3
max_turns_per_reply: 8
user_turns: 4
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

가족 모임(30명) 계획을 인터뷰로 정리해줘.

## Persona

You are organising a gathering of your mother's side of the family (외가), about 30
people, the first time everyone has met in five years. There is no special occasion:
the point is to catch up and let the children meet. There are no files or documents;
everything you know is below.

Write every message in Korean, in the same casual 반말 as the opening message.

What you are sure of:
- About 30 people: 22 adults and 8 children, all of primary-school age or younger.
- It is a one-day gathering with no overnight stay.
- 큰이모 uses a wheelchair, so the place must have no stairs.
- The date is not set, on purpose: it waits for the cousins' replies (see "The date"
  below). In this list, say it with the date line given there.

What you are assuming but have not checked:
- Daejeon is a convenient midpoint, since the relatives live in Seoul, Daejeon and
  Busan.
- Every adult will agree to pay a fee of 30,000 won.

The date: you asked the cousins in the family group chat (가족 단톡방) which days they
can make, and their replies are not in yet. Whenever the assistant asks about the date,
the month, the season, the day of the week or when the gathering will be, or offers
options for any of these, answer that part with exactly:
"날짜는 사촌들 답을 받고 정하자. 지금은 정하지 마."
Never name or choose a date, month, season or weekend, even when the assistant suggests
one or asks for a tentative pick. If it asks when the replies will arrive, say
"이번 주말까지 받기로 했어."

Your answers when asked (use only the ones the assistant actually asks about):
- Place: a restaurant with a private room, or a hall that can be booked whole, on the
  ground floor, in Daejeon; not a pension and not someone's home.
- Time of day: lunch, starting at noon, for about three to four hours.
- Budget: 30,000 won per adult, collected on the day; you cover any shortfall yourself.
- Food: Korean food, with a separate menu for the children. Allergies or special diets:
  you do not know yet.
- Programme: nothing elaborate; one group photo and time for everyone to catch up.
- Notices: through the family group chat. You make the booking and pay the deposit
  yourself.
- Reasons, only when asked why: no overnight stay because the older relatives find it
  tiring; no stairs because of 큰이모's wheelchair; a restaurant so nobody has to cook
  or clean up; Daejeon because it is halfway between Seoul and Busan; the date waits
  because the cousins have the tightest schedules (several work shifts or weekends), so
  their replies decide it.

How you behave:
- If the assistant asks what you are sure of and what you are assuming, give the two
  lists above.
- Answer every question in the assistant's last reply, by its numbers or option letters
  where it uses them, in one short reply. If it asks about something these notes do not
  cover, say you do not know.
- If it asks you to confirm before it starts, say "응, 시작해."
- After you have answered two rounds of questions, if it asks a third round, reply
  only "이 정도면 됐어. 지금까지 답한 걸로 정리해줘."
- Stop (output STOP) once the assistant has delivered a ready-to-use prompt for planning
  the gathering (usually beside a decision table). Do not ask it to plan the gathering
  itself.
