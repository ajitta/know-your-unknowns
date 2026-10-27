---
type: llm
focus: last_message
---

The reply teaches the field's vocabulary so the user can make precise requests,
aiming at the outcome (a renovation they are happy with, briefed precisely). All of
these must hold:
1. It gives a short mental model of the renovation work in order (what comes before
   what) and picks the few decision axes the user must decide on.
2. It maps the user's everyday words to the trade's terms, with an example request
   for each.
3. It gives criteria the user can use to judge quotes or finished work.
4. It ends with a more precise version of the user's request, or asks which terms to
   include.
5. It leaves the user's taste, budget and the contractor's practices to the user or
   marks them as assumptions instead of deciding them.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
