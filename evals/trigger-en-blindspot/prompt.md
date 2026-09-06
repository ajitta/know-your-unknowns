---
description: "English trigger phrase for the blindspot skill: 'what am I missing'"
tags: [trigger, en, blindspot]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

You cannot see our repo, so here is the shape of it. Our payments service makes
outbound calls to a card processor (authorise, capture, refund), to a fraud scorer,
and to our own ledger service. I am about to wrap every one of those calls in a
generic retry-with-backoff decorator so transient 502s stop failing checkouts.
I have never touched this part of the codebase. What am I missing?
