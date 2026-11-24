---
type: tool_used
tool: Skill
input_match: "unknowns:"
min: 0
max: 0
arm: both
---

The user asks for a review of a branch, not for a quiz, a buy-in doc or a blind-spot pass, so no unknowns skill should run. The request says "before I merge it", and the quiz skill's description lists merging as a time to use it ("or before merging"); a quiz load here would come from that clause. Read the run's tool calls for the skill that loaded.

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form.
