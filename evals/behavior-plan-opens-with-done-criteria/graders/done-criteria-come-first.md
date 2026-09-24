---
type: llm
focus: last_message
---

The plan skill must open with a done-criteria section before any decision items. All of
these must hold:

1. Before the first decision item, the response has a section covering purpose, done
   criteria, existing behavior that must not break, and allowed cost or change scope.
2. Where the user did not give one of those, the response either asks for it or says
   plainly that it is not set -- it does not silently invent a firm criterion and present
   it as agreed.

Fail if the decision items come first, or if the done criteria are missing entirely.
