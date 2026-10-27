---
type: llm
focus: last_message
---

The reply maps the solution space for the user to pick from, aiming at the outcome
(membership that recovers) rather than one answer. All of these must hold:
1. It lists roughly 8 or more distinct candidate interventions (more is fine: they
   are generated before judging) spanning effort, from
   something doable this week to a longer bet.
2. Each candidate says in a line what it would change. Judgment is deferred: the
   reply does not rank, score or prune the candidates before the user picks (effort,
   risks and how to measure success come with the picks).
3. It names what it does not know about this choir (why members left, who they are)
   or the assumed cause, and asks or states it, rather than presenting one diagnosis
   as fact.
4. It asks which candidates resonate instead of picking one.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
