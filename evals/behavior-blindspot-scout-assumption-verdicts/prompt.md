---
description: "Blind-spot pass over 22 league policy documents: each assumption the user lists gets a held or wrong verdict with the policy that settles it, and the investigation goes to the unknowns-scout"
tags: [behavior, en, blindspot, agent, noncode]
runs: 3
max_turns: 20
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, Task]
---

Can you do a blind spot pass on moving our registration online? We run a youth football
league, and from next season we want parents to register their kids through an online
form instead of filling in the paper pack at sign-up night. Skip the up-front questions,
here are my lists.

Sure of: the league has 340 players.
Assuming: (a) parents can e-sign the consent form, (b) players registered online are
insured the same way as before.
Can't judge: how long to keep the data.

All our policies are in policies/.
