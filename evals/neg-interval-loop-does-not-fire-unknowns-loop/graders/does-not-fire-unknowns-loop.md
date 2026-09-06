---
type: tool_used
tool: Skill
input_match: unknowns:loop
min: 0
max: 0
arm: both
---

A bare "loop" with an interval means the built-in interval runner. The
unknowns loop description carries that boundary sentence explicitly, and
this case is what keeps it honest.

`min: 0` + `max: 0` + `arm: both` is the documented form of a must-NOT-fire
check. In the without-plugin arm the skill cannot exist, so this grader passes
trivially there; the outcome grader beside it is what carries the delta.
