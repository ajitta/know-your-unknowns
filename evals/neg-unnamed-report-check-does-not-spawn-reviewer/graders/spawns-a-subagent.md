---
type: tool_used
tool: Agent
min: 0
weight: 0
---

Indicator only; reported, not scored (`min: 0` passes either way and `weight: 0` keeps it out of the score). It shows whether the run spawned any subagent, as the user asked. When it did, the two agent guards were exercised: the run chose an agent, and it was not an unknowns one. When it did not, the check was done directly and the guards say little about routing.
