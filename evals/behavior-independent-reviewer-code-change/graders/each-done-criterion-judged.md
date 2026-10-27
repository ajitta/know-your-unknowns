---
type: llm
focus: trace
---

Judge the review the independent-reviewer agent handed back (the final reply counts only where it reproduces that review).

The review covers a code change against PLAN.md's five done criteria: (1) `--format csv` prints CSV with the header `category,total`; (2) every total has two decimals; (3) a month with no expenses prints the header row only; (4) the default text output is unchanged; (5) unit tests cover the CSV output.
1. Each of the five criteria is marked met, partial or missing (or plainly equivalent words such as "not met").
2. No criterion is skipped or merged into a general remark.
