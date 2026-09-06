---
type: tool_used
tool: Skill
input_match: unknowns:brainstorm
min: 0
max: 0
arm: both
---

brainstorm advertises "show me options"; prototypes owns UI and design
variants. A UI layout request must land on prototypes (or a plain design
answer), never on the intervention brainstormer.

`min: 0` + `max: 0` + `arm: both` is the documented form of a must-NOT-fire
check. In the without-plugin arm the skill cannot exist, so this grader passes
trivially there; the outcome grader beside it is what carries the delta.
