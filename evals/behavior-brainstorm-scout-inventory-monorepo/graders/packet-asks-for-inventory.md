---
type: llm
focus: trace
weight: 0
---

Judge the packet: the `prompt` the assistant passed in the Agent tool call that spawned the unknowns-scout agent (`subagent_type` `unknowns:unknowns-scout`), among the run's tool calls. If the run made no such call, the verdict is PASS: this indicator judges the packet only when one was sent, and searching the material directly conforms. If it made several, every packet must meet the criteria.

The user's message was:

<<<
Brainstorm interventions for our involuntary churn. Subscriptions cancelled after a failed card payment are 3.1% of active subscribers a month, up from 1.9% a year ago, and finance wants it under 2% by the end of March. We have two engineers on it for the quarter and no budget for new vendors. This folder is our platform monorepo, about 40 services plus shared libraries; look through it for anything we already have.
>>>

The brainstorm skill's step 2b: "When you spawn the scout, the packet overrides the scout's default output (its finding table and improved prompt draft). The packet gives the scout the problem statement, the constraints and where to search, and asks it to return an **inventory**, one row per existing mechanism that bears on the problem, with the columns where it is / what it does today / what is missing to put it to use / evidence / status (confirmed / inferred); the scout is done when its procedure is done and every mechanism it found has a row."

1. The packet gives the problem statement with its current figure (subscriptions cancelled after a failed card payment, 3.1% of active subscribers a month; the 1.9% of a year ago may be left out) and the constraints the user gave (under 2% by the end of March, two engineers for the quarter, no new vendors).
2. The packet says where to search: the repository, or named parts of it.
3. The packet asks for an inventory with one row per existing mechanism that bears on the problem, and names its five columns: where it is, what it does today, what is missing to put it to use, evidence, and status (confirmed or inferred). Other words for a column count when they mean the same.
4. The packet says when the scout is done: once its procedure is done and every mechanism it found has a row, or plain words to that effect.
5. The packet asks for the inventory as the return, and does not also ask for an improved prompt draft or for the scout's default finding table (the table with Kind and Why it bites columns). Asking for the Needs checking, Questions to answer and Information still needed lists as well is fine.

When a packet was sent, fail if any criterion is not met.
