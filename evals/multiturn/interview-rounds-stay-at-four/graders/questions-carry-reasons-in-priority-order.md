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
   with the highest-radius open questions, and no taste question comes before an open
   higher-radius one in the same round. A "why" follow-up on an earlier answer belongs
   at the top of a round and is exempt from this ordering; judge the order of the rest.
   Judge each question's radius by what it decides, not by the label the assistant
   gives it. When a question fairly fits two levels (for example retry policy as data
   loss or as operating cost, unsubscribe as compatibility with mail-provider rules or
   as a minor detail), accept either level; fail only an order that is inverted under
   every fair reading.
4. When the user has not said what they are sure of and what they are assuming (a list
   of what is still open is not that), round 1 opens with that question. It is exempt
   from the ordering in 3.
5. Round 1 asks open questions about the user's situation, without options; questions
   with options for the decisions come from round 2 on.

Fail if any question has no reason, if a round puts a lower-radius question before
a higher-radius one, if round 1 skips the question required by 4, or if round 1 offers
options for decisions.
