---
description: "In Claude Code the unknowns loop runs only when the user names it (/unknowns:unknowns-loop): its plain trigger phrase does not load it"
tags: [negative, en, unknowns-loop]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

We need per-organisation rate limiting on the public API. The shape is not settled
and it touches the gateway, the billing plan table and the public docs.
Run the operating loop on this.
