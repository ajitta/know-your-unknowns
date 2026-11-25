---
type: tool_used
tool: Skill
input_match: "unknowns:"
min: 0
max: 0
arm: both
---

Everyday gate (0.15.0): the request does not say "unknowns", a skill label or a skill
name, so no unknowns skill may load. `min: 0` + `max: 0` + `arm: both` is the
must-NOT-fire form.
