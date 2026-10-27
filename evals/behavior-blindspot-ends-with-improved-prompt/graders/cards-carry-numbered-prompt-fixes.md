---
type: llm
focus: last_message
weight: 0.5
---

Each finding card carries its recommended action as a numbered, copyable prompt fix, so
the user can pick fixes by number. All of these must hold:

1. Every finding card ends with a prompt fix: a line the user could paste into the
   prompt, not only advice addressed to the user.
2. The prompt fixes are numbered, so a reply like "fixes 1 and 3" names them.

Fail if any card has no prompt fix, or if the fixes cannot be picked by number.
