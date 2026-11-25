---
description: "English trigger phrase for the unknowns-loop skill since 0.15.0: 'unknowns loop'"
tags: [trigger, en, unknowns-loop, upload-build-only]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

We need per-organisation rate limiting on the public API. The shape is not settled
and it touches the gateway, the billing plan table and the public docs.
Run the unknowns loop on this.
