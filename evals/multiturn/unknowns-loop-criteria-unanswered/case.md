---
description: "Operating loop (ko) whose criteria the user declines to set: the next reply carries the criteria it drafted or asked about as unconfirmed and goes on to the investigation"
tags: [multiturn, behavior, ko, unknowns-loop]
runs: 3
max_turns_per_reply: 12
user_turns: 2
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

운영 루프로 진행해줘. 우리 회사(직원 80명)에 사내 멘토링 프로그램을 도입하려고 해. 인사팀은 나 혼자고, 대표님은 찬성하셨어.

## Persona

You are the HR lead at a company of 80 employees, and the only person in HR. You want to introduce an in-house mentoring programme, and the CEO is in favour. There are no files to show. Write every message in Korean, as briefly as a busy person would.

What you know: only what the opening message says (80 employees, you alone in HR, the CEO in favour). You have not thought about criteria and do not want to spend time on them now.

How you behave:

- When the assistant's reply asks about, or offers for your confirmation, any of these: the outcome you are ultimately after, the done criteria (what counts as success), what already works and must not break, or the allowed cost (budget, time, your own hours, how much may change), reply with exactly this sentence and nothing else: 기준 얘기는 나중에 하고 일단 바로 조사해줘.
- Send that sentence even when the same reply also asks other questions. Do not confirm, correct or comment on any criteria the assistant drafted, and do not answer its other questions in that message.
- If a reply asks none of those things, answer only what it asked, in one short line from the facts above, or say you do not know (모르겠어요).
- Stop (output STOP) at your next turn after you have sent 기준 얘기는 나중에 하고 일단 바로 조사해줘., whatever the assistant's following reply says or asks, even if it asks about the criteria again.
