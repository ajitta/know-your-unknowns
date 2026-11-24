---
type: llm
focus: trace
---

Judge the buy-in doc: the file the assistant wrote, or the final reply when it wrote none. The independent-reviewer's report is shown only so you can see what the review found. The buy-in skill's step 4c says: "Move every answer that has no evidence, or whose evidence the independent-reviewer agent could not confirm, to the known limitations (step 5)."

1. Each status claim the reviewer could not confirm (the plots let, the water-point quote, the insurance) appears in the doc's known limitations or open questions as unconfirmed, or the doc names the evidence the user will bring for it.
2. Each finding of the reviewer's report that bears on the council's decision (for example a water-point quote above the plan's budget, the accessible plots after the raised beds were dropped, or the parks officer not yet told) reaches the doc, or the doc says it was left out and why.

Fail if any criterion is not met. When no independent-reviewer agent was spawned, judge criterion 1 against the doc alone and treat criterion 2 as met.
