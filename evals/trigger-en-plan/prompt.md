---
description: "English trigger phrase for the plan skill: 'tweakable plan'"
tags: [trigger, en, plan]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

We are replacing our single-tenant Postgres schema with a tenant_id column on every
table, plus row-level security, plus a migration for the three customers already on the
old shape. Give me a tweakable plan.
