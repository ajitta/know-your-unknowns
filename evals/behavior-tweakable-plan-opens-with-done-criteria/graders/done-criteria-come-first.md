---
type: llm
focus: last_message
---

The plan skill must open with its done criteria before any decision items. All of these
must hold:

1. Before the first decision item, the response states what must be true for the work
   to count as done, and what existing behavior must not break. A heading, a table or a
   single line all count; the form does not matter.
2. Where the user did not give a criterion, the response either asks for it or says
   plainly that it is not set -- it does not silently invent a firm criterion and present
   it as agreed.

Fail if the decision items come first, or if the done criteria are missing entirely.
