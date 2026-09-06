---
description: "English trigger phrase for the buy-in skill: 'buy-in doc'"
tags: [trigger, en, buy-in]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

You cannot see our repo, so here is the state of the work. I have moved us off
hand-rolled session cookies onto signed JWTs: a 15-minute access token plus refresh
rotation, with the old cookie path still accepted behind a flag for one release.
The auth suite is 61/61 green (was 48 tests), a load test held 2,400 req/s with a
p99 of 41 ms, and I have not yet handled refresh-token reuse detection or logout
across devices. Three senior engineers have to approve it before it ships.
Write me a buy-in doc.
