---
description: "G2: blind-spot findings carry evidence and a confirmed/inferred/unchecked status, and nothing can be confirmed about an unseen repo"
tags: [behavior, en, blindspot]
runs: 3
max_turns: 8
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
---

Blind spot pass, please. You cannot see our repo. We are adding a nightly job that
hard-deletes user accounts 30 days after the user asks for deletion. Accounts are
referenced from orders, invoices, audit logs and a Stripe customer record.
