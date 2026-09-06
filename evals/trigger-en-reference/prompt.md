---
description: "English trigger phrase for the reference skill: 'use this as a reference'"
tags: [trigger, en, reference]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

Here is how Linear does command-palette search: one input, fuzzy matching across
issues, projects and people, results grouped by kind, keyboard-only navigation, and
the palette stays open so actions can be chained.

Our admin console today has a plain text box over a single `users` table that does a
server-side LIKE query on every keystroke and navigates away on Enter.
Use this as a reference for our search box.
