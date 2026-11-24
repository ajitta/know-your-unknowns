---
type: llm
focus: trace
weight: 0
---

Indicator; reported, not scored. Judge the packet: the `prompt` of the Agent tool call that spawned the independent-reviewer agent. If the run made no such call, the verdict is PASS: this indicator judges a packet only when one was sent.

The buy-in skill's step 4b says to leave out "the producer's own summary, so the review checks the work rather than the narrative". The user's own words and records (criteria, plan, log, status as claims) are sources, not the producer's summary.

1. The packet holds no judgement of the assistant's own on whether the done criteria are met or the outcome is reached (for example "the project is essentially on track"), and no text from a doc the assistant drafted.

Fail if criterion 1 is not met. A fail here is a miss of step 4b's existing clause, recorded on its own; it is not a loss of sources.
