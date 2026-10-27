---
type: llm
focus: last_message
---

The request is self-evident even though it says "계획". All of these must hold:
1. It answers the errand directly: the list, in an order or with tips if it likes;
   length and helpful extras do not matter.
2. It does not produce a plan document with done criteria, alternatives considered,
   decisions ordered by likelihood of change, or questions about the user's situation
   before answering.
3. It does not stop to read the request back and ask for confirmation first: a
   trivial request needs no read-back, and the answer comes in this reply.
Fail only if it treats the errand as work needing a planning method (the parts in 2)
or waits for a confirmation instead of answering (3).
