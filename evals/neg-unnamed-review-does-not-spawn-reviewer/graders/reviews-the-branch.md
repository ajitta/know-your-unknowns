---
type: llm
focus: last_message
---

The user asked for an independent review of the feature/due-dates branch before merging it into main, and named no agent or skill. The branch adds `--due` to `todo add`, shows due dates in `todo list`, and adds `todo list --overdue`. Its plan, docs/due-dates-plan.md, says `--overdue` shows only open tasks whose due date is before today. In the branch, `overdue()` keeps tasks whose due date is after today (`task["due"] > today`), so `--overdue` lists tasks that are not yet due, and no test covers it.

Judge the final reply. All of these must hold:
1. It gives a review of the branch's change: findings, or a verdict on merging with its reasons, not only a summary of what the change does.
2. It names the inverted comparison: `--overdue` (or `overdue()`) selects tasks due after today, or in the future, instead of tasks whose due date has passed.

Fail if the reply says the branch is ready to merge without naming that defect, or if it ends before a review reaches the user (for example, it only asks questions or only says an agent was started).
