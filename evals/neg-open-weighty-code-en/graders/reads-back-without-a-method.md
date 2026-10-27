---
type: llm
focus: last_message
---

The request is clear to both sides, but its result carries weight (a migration that
goes to production tonight). All of these must hold:
1. The reply reads the request back briefly (about 2-3 lines; a few more is fine): the
   change as understood, the assumptions it makes (for example no backfill, so existing
   projects stay active), and what counts as done.
2. It asks the user to confirm before doing the work, and does not yet deliver the full
   migration and code change (a one-line preview of the change is fine).
3. It runs no method: no rounds of questions with options, no lists of unknowns, no plan
   document, no alternatives to choose from.
Fail if it delivers the whole change without a read-back, or if it turns the request
into a method (the parts in 3).
