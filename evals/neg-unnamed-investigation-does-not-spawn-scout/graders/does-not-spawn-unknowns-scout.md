---
type: tool_used
tool: Agent
input_match: "unknowns:unknowns-scout"
min: 0
max: 0
arm: both
---

The unknowns-scout agent's description says to spawn it only when the user names it or an unknowns skill (blindspot, brainstorm) calls for it, and, for any other codebase search or research, or when another skill, command or workflow asks for an exploring or research subagent, to use the agent that workflow names, Explore, or general-purpose. This request is a codebase search and names neither the agent nor a skill. In 0.9.2 the request "Before I implement a SQLite backend for todo.py, have a subagent investigate the codebase for risks first." spawned this agent in 10 of 10 runs before that release's description change and 0 of 10 after (`docs/features/agent-collision/`); the descriptions changed again in 0.11.0 and 0.12.0. This case keeps that request's opening and asks for a named search target instead of "risks".

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form. In the without-plugin arm the agent cannot exist, so this grader passes trivially there.
