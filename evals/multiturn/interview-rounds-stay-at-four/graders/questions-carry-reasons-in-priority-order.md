---
type: llm
focus: transcript
weight: 0.5
---

Each round's questions are ordered by blast radius and justified. All of these must
hold:

1. Every question the assistant asks carries a one-line reason why the answer matters
   (a short "why it matters" line or an equivalent clause).
2. Every option under a question carries a short consequence or tradeoff note. A
   free-text "other" option needs none.
3. Within each round, questions come in blast-radius order: architecture, then data
   loss or security, then compatibility with external APIs or existing code, then
   performance or operating cost, then taste and minor details. The first round starts
   with the highest-radius open decisions, and no taste question comes before an open
   higher-radius one in the same round. A "why" follow-up on an earlier answer belongs
   at the top of a round and is exempt from this ordering; judge the order of the rest.
   Judge each question's radius by what it decides, not by the label the assistant
   gives it.

Fail if any question has no reason, or if a round puts a lower-radius question before
a higher-radius one.
