---
description: "Reference carried past its semantics map: the user corrects one row by its number, and the reply must revise the application-plan items built on that row"
tags: [multiturn, behavior, en, reference, noncode]
runs: 3
max_turns_per_reply: 8
user_turns: 3
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Use this as a reference: Northfield's small grants guidelines, below. Make ours like this
for Riverside's new Neighbourhood Small Grants (grants of 500 to 3,000 pounds, first round
this spring).

> **Northfield Community Small Grants: guidelines**
> 1. Who can apply: registered charities based in Northfield. Give your charity number on the form.
> 2. Grants: 500 to 5,000 pounds for projects that bring neighbours together.
> 3. What you send: the application form, last year's audited accounts, and a project budget.
> 4. Payment: the full grant is paid into the organisation's bank account within 30 days of the award.
> 5. Assessment: a panel of three councillors scores each bid out of 20 (need 8, reach 6, value 6); bids under 12 are declined.
> 6. Reporting: a one-page report and receipts for spending over 100 pounds, within 3 months of the project ending.
> 7. Deadlines: one round a year, closing 31 January.

## Persona

You are the community grants officer at Riverside council. There are no files to show;
everything you know is below.

Facts you know (give them only when asked):
- Budget: 40,000 pounds a year, two rounds a year (spring and autumn).
- The panel: three councillors and two residents.
- You want to keep Northfield's scoring out of 20 and the one-page report.
- Who may apply: registered charities AND unregistered resident groups of at least three residents. An unregistered group applies through a fiscal sponsor, the Riverside Community Foundation, which receives and holds the money for the group.

How you behave:
- If the assistant asks questions before showing its reading, answer only what it asked, from the facts above, in one short reply. Do not volunteer the eligibility fact yet.
- When the assistant shows its reading of the reference with numbered rows or notes, correct exactly one: the row (or note) about who can apply. Name it by the number the assistant gave it, for example "Row 2 is wrong: we also fund unregistered resident groups of at least three residents; they apply through a fiscal sponsor, the Riverside Community Foundation, which receives the money for them." Say nothing about what else that changes; leave that to the assistant. Approve the other rows.
- If the assistant shows a revised reading and plan and asks you to confirm, reply "semantics confirmed".
- Stop (output STOP) once the assistant has answered your correction with a revised reading and plan, or after you have replied "semantics confirmed". Do not ask it to draft the guidelines.
