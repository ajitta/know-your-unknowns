---
description: "English trigger phrase for the deviation-log skill since 0.15.0: 'deviation log'"
tags: [trigger, en, deviation-log]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

The plan said to keep export job status in Redis with a 24h TTL. Redis is not
provisioned in staging, so I put the status in the existing jobs table behind a status
column instead. Record it in the deviation log.
