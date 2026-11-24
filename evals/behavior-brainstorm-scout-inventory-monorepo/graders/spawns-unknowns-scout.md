---
type: tool_used
tool: Agent
input_match: unknowns-scout
min: 0
weight: 0
---

Indicator only; reported, not scored (`min: 0` passes either way and `weight: 0` keeps it out of the score). It shows whether brainstorm step 2a handed the search to the unknowns-scout agent. The material is a monorepo of 41 services and shared libraries, about 600 files and 370 KB; in the 0.13.3 round the one run spawned the scout, the first recorded run in which a skill did. The owner ruled on 2026-11-24 that "more sources than you can read in full" (blindspot step 2, brainstorm step 2a) is the model's own judgment of what it can read: a direct investigation that reaches the result conforms, a spawn conforms too, and no case asserts a spawn from the size of the material. The scored outcome is builds-on-existing-mechanisms; packet-asks-for-inventory, scout-returns-inventory and reply-uses-inventory are indicators that judge the scout path when a run takes it.
