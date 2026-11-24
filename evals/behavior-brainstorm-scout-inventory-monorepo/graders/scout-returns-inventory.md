---
type: llm
focus: trace
---

Judge the report the unknowns-scout agent handed back (shown as a report handed back by a spawned agent). If no unknowns-scout agent was spawned, the verdict is FAIL. If it was spawned more than once, every report must meet the criteria.

The scout's instruction: "**The packet can change the return shape.** If the caller asks for a different output (for example the **brainstorm** skill's inventory of what already exists but is not used for the problem), return exactly that instead of the table and the prompt draft below. The investigation rules still apply: evidence, status labels, and only what you found; keep the **Needs checking**, **Questions to answer** and **Information still needed** lists in any return shape."

1. The report is an inventory: one row or entry per existing mechanism, each giving where it is, what it does today, what is missing to put it to use, its evidence and its status (confirmed or inferred).
2. The report has no default finding table (rows with Kind and Why it bites) and no improved prompt draft.
3. Each row's evidence is something the user can open: a file path, with or without a line number, or a commit.
4. The report keeps the Needs checking, Questions to answer and Information still needed lists: each appears, with its items or marked as having none.

Fail if any criterion is not met.
