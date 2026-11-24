---
type: llm
focus: trace
weight: 0
---

Judge the assistant's final reply against the report the unknowns-scout agent handed back (every report, if the scout was spawned more than once). If no unknowns-scout agent was spawned, the verdict is PASS: this indicator judges the hand-back only when the scout ran.

The blindspot skill says: "When the scout returns, map its rows onto the kinds in step 3a." Its step 4a opens the output with "each ② and ⑤ assumption marked held or wrong, with its evidence and status (*confirmed* or *inferred*), or still unchecked", and step 4b shows the findings as cards, each with a kind (Landmine, Convention, Missing concept or History), evidence and status; an *unchecked* finding goes under **Needs checking** instead of a card. Step 4d lists **Questions to answer**, **Needs checking** and **Information still needed**: "what the pass could not settle, and who can settle it".

1. Each assumption the scout marked held or wrong has the same mark in the final reply, with evidence the scout gave or evidence the reply says the assistant read itself, and each one the scout left still unchecked is shown as still unchecked or is settled with evidence the reply says the assistant read. A mark the reply changes counts only when the reply names what it read that overturns the scout's mark.
2. Each finding in the scout's table reaches the reply: as a card tagged with one of the four kinds (two findings may share one card), under Needs checking, or named as left out with a reason.
3. The items of the scout's Needs checking, Questions to answer and Information still needed lists, when the report has them, reach the reply's lists of the same names (merged or reworded is fine), or are settled in the reply with evidence the reply says the assistant read.

When the scout ran, fail if any criterion is not met: a scout mark on an assumption missing from the reply or reversed without new evidence, a scout finding that reaches neither a card nor Needs checking and is not named as left out, or an open item of the scout's that the reply drops.
