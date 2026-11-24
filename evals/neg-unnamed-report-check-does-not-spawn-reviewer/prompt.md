---
description: "Agent collision, non-code review: an unnamed request to have a subagent independently check a report's figures against the records, in a folder that also holds the plan and the deviation log, must not spawn independent-reviewer or unknowns-scout or load an unknowns skill (the material of behavior-independent-reviewer-report-vs-records without the agent's name)"
tags: [negative, conflict, agent, en, independent-reviewer, noncode]
runs: 3
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, Task]
---

Have a subagent independently check the figures in pilot-report.md against our records
(the three CSVs in this folder) before I send the report to the Neighbourhood Fund
committee.
