---
description: "Agent collision, investigation: an unnamed request to have a subagent investigate a codebase before implementation must not spawn unknowns-scout or independent-reviewer or load an unknowns skill (0.9.2 cell s-pre-en, with a named search target in place of 'for risks')"
tags: [negative, conflict, agent, en, unknowns-scout, code]
runs: 3
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Task]
---

Before I implement a SQLite backend for todo.py, have a subagent investigate the
codebase first: I need everything that reads or writes todo.json.
