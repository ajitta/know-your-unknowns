---
type: tool_used
tool: Skill
input_match: unknowns:blindspot
min: 0
max: 0
arm: both
---

blindspot investigates a codebase or plan for unknown unknowns; teach-me
teaches a domain's vocabulary. "I do not know these words" is teach-me's
territory, and the two skills sit next to each other in the trigger matrix.

`min: 0` + `max: 0` + `arm: both` is the documented form of a must-NOT-fire
check. In the without-plugin arm the skill cannot exist, so this grader passes
trivially there; the outcome grader beside it is what carries the delta.
