---
description: "Deliverable check: when the user skips the up-front lists, a blind-spot pass must end with a prompt the user can paste back"
tags: [behavior, en, blindspot]
runs: 3
max_turns: 10
timeout_seconds: 360
allowed_tools: [Read, Glob, Grep, Skill]
---

Do a blind spot pass on this before I start. I am adding soft delete to our documents
table: a deleted_at timestamp, and every existing query gets WHERE deleted_at IS NULL.
There are about 30 queries across the API, a nightly export job, and a search indexer
that reads the table directly.

Skip the up-front questions: I have no lists of what I am sure of or assuming. You cannot
see our repo, so work from this description.
