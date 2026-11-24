---
type: tool_used
tool: Agent
min: 0
weight: 0
---

Indicator only; reported, not scored (`min: 0` passes either way and `weight: 0` keeps it out of the score). It shows whether the run spawned any subagent. When it did, the two agent guards were exercised: the run chose an agent, and it was not an unknowns one. When it did not, the review was done directly and the guards say little about routing. In 0.9.2, in the measured setup with SuperClaude removed, the same request about a similar branch spawned general-purpose in 5 of 5 runs after the description change.
