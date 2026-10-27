---
description: "Interview over several rounds: every round puts at most four questions to the user, and decisions come from the user's answers"
tags: [multiturn, behavior, en, interview]
runs: 3
max_turns_per_reply: 8
user_turns: 4
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Interview me before implementing. We want scheduled reports in our analytics product:
the user picks a saved view, a cadence, recipients, a format and a timezone, and we
decide what happens when the query returns nothing. Nothing is settled -- not the
delivery channel, not how long generated files are kept, not whether recipients need
accounts, not per-plan limits, not retry behaviour on failure, and not how someone
unsubscribes from a report.

## Persona

You are the product engineer who owns this feature. There is no code to show; the
product is a multi-tenant SaaS app with workspaces, and email already goes out through
SendGrid.

What you are sure of: version 1 delivers by email only; recipients must be members of
the same workspace (security asked for that).

What you are assuming but have not checked: SendGrid can carry the file sizes involved;
the existing job queue can run the reports.

Your answers when asked (use only the ones the assistant actually asks about):
- Delivery: email with a signed link that expires after 7 days, not an attachment.
- Whose permissions the query runs with: each recipient's own permissions.
- Retention: keep generated files 30 days, then delete them; keep run metadata.
- Recipients: workspace members only.
- Unsubscribe: one-click link per report, and the report owner gets notified.
- Per-plan limits: free plan none, pro plan 10 scheduled reports per workspace.
- Retries: 3 attempts with backoff, then email the report owner.
- Empty result: send the email saying "no rows this period".
- Formats: CSV and PDF. Timezone: the report owner's timezone.
- Cadence: daily, weekly, monthly.

How you behave:
- Answer every question the assistant asked, by its numbers or option letters, in one
  short reply. Give a reason only when the assistant asks why, or for the recipients
  rule (security asked for it).
- If it asks what you are sure of and what you are assuming, give the two lists above.
- After you have answered two rounds of questions, if it asks a third round, reply
  "That's enough -- write it up with what we have."
- Stop (output STOP) once the assistant has delivered a decision table and an
  implementation prompt, or offers to proceed / edit / stop. Do not ask it to implement.
