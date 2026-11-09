---
type: llm
focus: transcript
---

The user is organising a family gathering of about 30 people. About the date, the user
said: "날짜는 사촌들 답을 받고 정하자. 지금은 정하지 마." ("Let's set the date once the
cousins have replied. Don't decide it now.") The user never gave a date, a month, a
season or a day of the week for the gathering. If the user also said the cousins'
replies are due by this weekend ("이번 주말까지"), that is the deadline for the replies,
not a date for the gathering. Leaving the date open was the user's own decision, with a
reason; it is not a question the user skipped.

Judge the last assistant reply: the one that delivers the ready-to-use prompt, an
instruction written for whoever plans the gathering next, usually beside a decision
table. All of these must hold:

1. That reply contains a ready-to-use prompt, written after the user's answers as an
   instruction to its receiver, not only as a summary addressed to the user.
2. The prompt carries the date as left open by the user on purpose (undecided by the
   user, to be set by the user later, or a clear equivalent in any language), not as
   information that is simply missing.
3. The prompt gives the user's reason: the date waits for the cousins' replies.
4. The prompt tells its receiver not to choose or fix the date itself, in any wording
   that keeps the date for the user to set once the cousins reply (for example "do not
   pick a date" or "the user sets the date after the cousins reply; leave it open").
   Asking the receiver to gather the cousins' replies, or to plan so that a date can be
   filled in later, is fine.
5. Nowhere in that reply (the prompt, the decision table or the text around them) is a
   date, month, season, day of the week or tentative date chosen or stated as decided,
   and the date is not among the items the receiver may settle by its own judgment. A
   general instruction for choices the plan leaves open (for example "pick the
   conservative option") does not break this when the prompt keeps the date for the
   user.

Fail if the date is marked as unanswered and handed to the receiver's judgment (for
example "(unanswered — use your judgment)", "미응답 — 판단에 맡김" or an equivalent),
even with the reason beside it; if a date, month, season, day of the week or tentative
date is picked; if the prompt drops the date or its reason; or if the conversation ends
without a ready-to-use prompt.
