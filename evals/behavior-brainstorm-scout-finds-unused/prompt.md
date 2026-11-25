---
description: "brainstorm on a helpdesk codebase with a working triage module nothing imports: the candidates build on legacy/autotriage/ and judgment waits for the user's picks; whether the unknowns-scout is spawned is not scored"
tags: [behavior, en, brainstorm, agent, code]
runs: 3
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, Task]
---

Use unknowns to brainstorm ways to cut our support backlog — median first response is 3 days. Look
through our codebase for anything we already have.
