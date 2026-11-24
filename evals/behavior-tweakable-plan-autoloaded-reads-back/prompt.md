---
description: "Read-back paragraph in a skill that loaded on its own, not by name: 'make a plan' for a one-line production config change clear to both sides; the reply reads back in 2-3 lines and waits, with no plan and no method. Read it only in runs where the skill loaded"
tags: [behavior, open-cell, readback, en, tweakable-plan]
runs: 3
max_turns: 6
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Make a plan for tonight's release: raise `client_max_body_size` from `10m` to `25m` in our production nginx config so customers can upload the 20 MB PDFs they keep sending. It is one line in the `server` block of `/etc/nginx/conf.d/app.conf`. The Django app behind nginx already accepts 25 MB (we raised its limit last week), nothing sits in front of nginx, and nothing else changes. It ships with tonight's deploy.
