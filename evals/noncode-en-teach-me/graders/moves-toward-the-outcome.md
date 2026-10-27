---
type: llm
focus: last_message
---

The reply teaches the field's vocabulary so the user can make a precise request,
aiming at the outcome (a brief the roaster can act on). All of these must hold:
1. It gives a short mental model of the field (an ordered pipeline from farm or
   processing to roast to cup) and picks the few decision axes this brief turns on.
2. It maps everyday words ("smooth", "sour") to expert terms the user can use, with an
   example of a request using each.
3. It gives criteria for judging the result (how to tell a good sample from a bad one).
4. It ends by asking which terms, comparisons or presets to put into the request,
   before writing the rewritten request: a finished rewrite made before the user picks
   fails this criterion.
5. It is honest about what it cannot know: the user's taste and the roaster's beans
   are left to the user or marked as assumptions, and doubtful terms are marked
   rather than asserted.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
