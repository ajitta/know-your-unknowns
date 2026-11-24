---
type: tool_used
tool: Agent
input_match: "unknowns:independent-reviewer"
min: 0
max: 0
arm: both
---

The independent-reviewer agent's description says to spawn it only when the user names it or an unknowns skill (buy-in) calls for it, and to send any other code, PR, document or "independent" review to the agent the workflow names, or general-purpose. This request names neither the agent nor a skill. In 0.9.2 the same request about a similar branch ("Get an independent review of the … branch before I merge it.") spawned this agent in 10 of 10 runs before that release's description change and 0 of 10 after (`docs/features/agent-collision/`); the descriptions changed again in 0.11.0 and 0.12.0.

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form. In the without-plugin arm the agent cannot exist, so this grader passes trivially there.
