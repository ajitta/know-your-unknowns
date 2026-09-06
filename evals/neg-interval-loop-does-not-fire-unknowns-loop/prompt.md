---
description: "Built-in collision: 'loop this every 5 minutes' must not fire the unknowns loop"
tags: [negative, conflict, en, loop]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

loop this every 5 minutes: check whether the staging deploy has finished and tell me
the moment it does.
