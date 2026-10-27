---
type: llm
focus: last_message
---

The response is a reviewable pre-implementation plan ordered for review, not for execution. All of these must hold:

1. The items the user is most likely to want changed -- schema, interfaces, contracts, migration approach -- appear first, before mechanical or boilerplate work.
2. Each of those items lists the alternatives that were considered and why they were rejected.
3. Each item carries how it would be verified and what happens if it turns out wrong (risk or rollback).
4. It does not start implementing.

Fail if the plan is simply a chronological list of steps, or if any decision appears without alternatives.
