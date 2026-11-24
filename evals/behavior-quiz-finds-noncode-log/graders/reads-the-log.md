---
type: tool_used
tool: Read
input_match: DEVIATIONS\.md
min: 0
weight: 0
---

Indicator only: reports how often the run opened tournament/DEVIATIONS.md and adds
nothing to the score. When asks-about-a-recorded-deviation fails, it tells a run that
never opened the log (it looked for `IMPLEMENTATION_NOTES.md` only, or for no log) from
one that read the log and still asked nothing about it.
