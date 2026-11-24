---
type: tool_used
tool: Skill
input_match: "unknowns:"
min: 0
max: 0
arm: both
---

The user asks for a search with a named target (everything that reads or writes todo.json), not for a blind-spot pass or a plan, so no unknowns skill should run. A blindspot or tweakable-plan load here would come from "Before I implement …". Read the run's tool calls for the skill that loaded.

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form.
