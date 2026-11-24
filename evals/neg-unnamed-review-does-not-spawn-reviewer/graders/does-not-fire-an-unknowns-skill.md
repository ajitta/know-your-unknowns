---
type: tool_used
tool: Skill
input_match: "unknowns:"
min: 0
max: 0
arm: both
---

The user asks for a review of a branch, not for a quiz, a buy-in doc or a blind-spot pass, so no unknowns skill should run. The request says "before I merge it". The quiz skill's description listed merging as a time to use it ("or before merging") through 0.13.2; the next release removed that clause, so no description asks for a quiz here. Read the run's tool calls for the skill that loaded.

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form.
