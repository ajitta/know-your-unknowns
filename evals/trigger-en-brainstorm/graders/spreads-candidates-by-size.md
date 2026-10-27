---
type: llm
focus: last_message
---

The response maps the solution space for the stated problem. All of these must hold:

1. It lists many distinct candidate interventions -- roughly 8 or more (they are generated before judging) -- not two or three.
2. The candidates span effort sizes: at least one that could ship this afternoon and at least one that is a quarter-scale bet.
3. Each candidate names what it would change.
4. Judgment is deferred: the response does not rank, score, prune or recommend candidates before the user picks (no "if you pick one, take #1").
5. It does not pick one and start implementing.

Fail if there are fewer than 5 candidates, or if every candidate is the same size of effort.
