---
type: llm
focus: last_message
---

The reply is a plan ordered for the user's review, aiming at the outcome (a garden
that opens and is used) rather than a chronological checklist. All of these must hold:
1. It opens with the purpose and done criteria, or asks for the parts it cannot know
   (marking them "not set" or asking).
2. The decisions the user is most likely to change (e.g. how plots are allocated, the
   agreement with the city, costs and who pays, water) come first, each with
   alternatives considered and what breaks if it is wrong.
3. Routine steps come after the decisions.
4. It labels its own assumptions (costs, the city's terms, timings) as assumptions or
   asks about them.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
