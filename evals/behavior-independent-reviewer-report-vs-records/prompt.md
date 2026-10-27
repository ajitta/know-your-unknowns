---
description: "independent-reviewer, called by name on a non-code deliverable: a pilot report whose figures contradict the records beside it"
tags: [behavior, en, agent, independent-reviewer, noncode]
runs: 3
max_turns: 12
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Agent, Task]
fixture: fixture
---

Use the independent-reviewer agent to check our pilot report before it goes to the
Neighbourhood Fund committee next month. Everything is in this folder: plan.md is the
approved plan with the done criteria and the outcome, pilot-report.md is the report,
the three CSVs are our own records, and DEVIATIONS.md is the deviation log. Show me the
reviewer's report.
