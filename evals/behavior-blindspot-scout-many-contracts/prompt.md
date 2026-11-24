---
description: "Blind-spot pass over 214 supplier agreements, more than the model can read in full: the pass spawns the unknowns-scout with both sides' assumptions and asks for a held or wrong verdict on each, and the final reply carries the scout's verdicts and findings"
tags: [behavior, en, blindspot, agent, noncode]
runs: 3
max_turns: 40
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Bash, Skill, Agent, Task]
---

Can you do a blind spot pass on our plan to pay all our suppliers at 60 days instead of 30 from 1 April 2027? We run twelve garden centres, and the longer terms would carry us through the spring stock build without using the overdraft. Finance would write to every supplier in January. Skip the up-front questions, here are my lists.

Sure of: we have 214 supplier agreements, and all of them are in contracts/.
Assuming: (a) every agreement lets us change the payment terms by giving written notice; (b) every supplier is on 30-day terms today.
Can't judge: how much pushback to expect from the small growers.

Our purchasing policies are in policies/ and the purchasing manager's notes are in notes/.
