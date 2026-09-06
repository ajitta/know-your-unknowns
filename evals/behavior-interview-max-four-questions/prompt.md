---
description: "Round-size check: the interview must put at most 4 questions to the user at once"
tags: [behavior, en, interview]
runs: 3
max_turns: 8
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Interview me before implementing. We want scheduled reports in our analytics product:
the user picks a saved view, a cadence, recipients, a format and a timezone, and we
decide what happens when the query returns nothing. Nothing is settled -- not the
delivery channel, not how long generated files are kept, not whether recipients need
accounts, not per-plan limits, not retry behaviour on failure, and not how someone
unsubscribes from a report.
