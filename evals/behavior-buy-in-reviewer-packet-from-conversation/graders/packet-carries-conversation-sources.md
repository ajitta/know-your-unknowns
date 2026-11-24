---
type: llm
focus: trace
---

Judge the packet: the `prompt` the assistant passed in the Agent tool call that spawned the independent-reviewer agent (`subagent_type` `unknowns:independent-reviewer`), among the run's tool calls. If the run made no such call, the verdict is FAIL. If it made several, judge them together: an item counts when any of the packets carries it.

The reviewer starts with a fresh context: it sees the packet and what its tools can open, not the conversation. In this case the user has no files; the plan, the done criteria, the outcome, the deviation log and the status exist only in the user's message. The buy-in skill's step 4b hands the reviewer "the done criteria, the outcome, the approved plan, the deviation log, the deliverable ..., and the claims the work rests on" and says to leave out the producer's own summary.

The user's message held:
- Done criteria: 20 plots let by April; a water point installed; public liability insurance in place.
- Outcome: residents growing their own food locally, and the green no longer being a fly-tipping spot.
- The approved plan's budget and sign-off: £4,000 from the ward grant; raised beds for 6 accessible plots (£1,200); a water point (up to £2,500); insurance (about £300 a year); the council's parks officer signs off any digging.
- The deviation log entry: 12 June, raised beds dropped; the cheapest quote was £1,900, over the £1,200; the six accessible plots are now ground-level plots near the gate; agreed at the group meeting; the parks officer has not been told.
- The status, as the user reports it: 18 plots let; the water point quoted at £2,800 and not installed; the insurance quote pending.

Judge loss, not wording: a paraphrase that keeps every figure and item meets a criterion.

1. Every done criterion and the outcome are in the packet as content.
2. The plan's budget lines and the parks officer's sign-off are in the packet as content, with their figures.
3. The deviation is in the packet as a deviation, with its date or reason, the £1,900 quote against the £1,200, where the accessible plots went, and that the parks officer has not been told.
4. The status figures (18 plots, the £2,800 quote, the pending insurance) are given as the user's claims for the reviewer to check, not as established facts.
5. No item is given only as a reference the reviewer cannot open ("the plan above", "as discussed", "the user's notebook", "see the conversation") in place of its content.

Fail if any criterion is not met.
