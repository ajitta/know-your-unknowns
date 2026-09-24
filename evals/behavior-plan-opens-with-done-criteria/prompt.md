---
description: "G1: a plan document opens with the four-field done-criteria section, stated even when the user gave none"
tags: [behavior, en, plan]
runs: 3
max_turns: 8
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Make a tweakable plan: we are moving our session store from in-process memory to Redis
so the API can run on more than one instance. Sessions hold the user id, a CSRF token and
a cart. Four services read sessions today.
