---
type: llm
focus: last_message
---

The request is clear to both sides, but its result carries weight (a notice to all 80
staff). All of these must hold:
1. The reply reads the request back briefly (about 2-3 lines; a few more is fine): the
   notice as understood, the assumptions it makes (for example the tone, who it goes
   to, what stays the same), and what counts as done.
2. It asks the user to confirm before writing the notice, and does not yet deliver the
   full notice.
3. It runs no method: no rounds of questions with options, no lists of unknowns, no plan
   document, no alternative drafts to choose from.
Fail if it delivers the whole notice without a read-back, or if it turns the request
into a method (the parts in 3).
