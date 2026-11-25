---
description: "A skill reached by its label (\"tweakable plan\", since 0.15.0; before that the everyday \"make a plan\" loaded it), asked for its own deliverable about weighty work: make a plan for a one-line production config change. The plan is the requested result and ends at the user's approval, so the reply is the size gate's short plan (owner ruling 2026-11-24), not a read-back with no plan and not the full document. Read it only in runs where the skill loaded"
tags: [behavior, size-gate, en, tweakable-plan]
runs: 3
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Make a tweakable plan for tonight's release: raise `client_max_body_size` from `10m` to `25m` in our production nginx config so customers can upload the 20 MB PDFs they keep sending. It is one line in the `server` block of `/etc/nginx/conf.d/app.conf`. The Django app behind nginx already accepts 25 MB (we raised its limit last week), nothing sits in front of nginx, and nothing else changes. It ships with tonight's deploy.
