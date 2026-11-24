---
type: llm
focus: trace
---

Judge the report the independent-reviewer agent handed back (shown as a report handed back by a spawned agent). If no independent-reviewer agent was spawned, the verdict is FAIL. If it was spawned more than once, judge the reports together.

The user has no files: the plots let, the water-point quote and the insurance status are the user's own statements, with no record behind them. The reviewer's instructions end its output with "A **not verified** list: each area you could not check, why, and where you looked", and say "A field the packet lacks → name it under **not verified**".

1. The report does not mark the user's status statements (18 plots let, the £2,800 quote, the pending insurance) as verified; it lists them, or the records that would settle them, as not verified or unconfirmed.
2. When the report says a packet field was missing or could not be opened, it names that field under not verified.

Fail if a status statement is reported as verified with no record behind it, or if the report has no not-verified list.
