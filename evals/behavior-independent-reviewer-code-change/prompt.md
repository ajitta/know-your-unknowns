---
description: "independent-reviewer, called by name on a code change in a fixture repository whose last commit silently misses one done criterion"
tags: [behavior, en, agent, independent-reviewer, code]
runs: 3
max_turns: 12
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Agent, Task]
fixture: [fixture/monthly-report-command, fixture/add-csv-export]
---

Use the independent-reviewer agent to check the change in this repository before I merge
it. The change is the last commit (HEAD~1..HEAD). PLAN.md is the approved plan with the
done criteria and the outcome, and IMPLEMENTATION_NOTES.md is the deviation log. The
tests run with `python3 -m unittest`. The developer says all five done criteria are met
and the tests pass. Show me the reviewer's report.
