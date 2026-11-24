---
description: "Read-back paragraph in a skill that loaded on its own, not by name (non-code): 'get sign-off' in a request, clear to both sides, for an email sent today whose reply releases a payment; the reply reads back in 2-3 lines and waits, with no email and no buy-in doc. Read it only in runs where the skill loaded"
tags: [behavior, open-cell, readback, en, buy-in, noncode]
runs: 3
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Help me get sign-off from my manager, Priya, on renewing our team's design-software licence. Write the email I'll send her today: 12 seats at $15 per seat per month, billed yearly ($2,160), the same plan, seat count and price she approved last year. It renews on 1 December, and finance pays the invoice once she replies "approved".
