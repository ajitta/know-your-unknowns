---
description: "unknowns-scout, called by name before a planned change on a Flask service: requirements.txt pins pydantic 1.10.13 while PLAN.md names pydantic 2 APIs as the codebase's own, and the report checks the pinned version"
tags: [behavior, en, agent, unknowns-scout, code]
runs: 3
max_turns: 12
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, Task]
---

I'm starting on PLAN.md on Monday. Before I do, use the unknowns-scout agent to go through
this repo and tell me what could bite me.
