---
type: llm
focus: last_message
---

The response treats the supplied example as a map to understand, not an answer to copy. All of these must hold:

1. It states what the reference is actually doing and why -- the mechanism or principle behind it -- before proposing anything.
2. It names which parts transfer to the user's own context and which do not, with the reason for each.
3. It checks its reading with the user, or states the assumptions it is working from, before implementing.

Fail if it immediately writes an implementation that mimics the reference without explaining the mechanism.
