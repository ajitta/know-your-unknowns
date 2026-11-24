---
type: tool_used
tool: Agent
input_match: unknowns-scout
min: 1
---

Scored. The material is a monorepo of 41 services and shared libraries, about 600 files and 370 KB, more than the model can read in full, so brainstorm step 2a hands the search to the scout: "When the material spans more sources than you can read in full, use the `unknowns:unknowns-scout` agent; otherwise search the material yourself." Until this case no recorded run had a skill spawn the scout (`CHANGELOG.md` 0.13.2, **Not measured**). A run that does not spawn it also fails packet-asks-for-inventory, scout-returns-inventory and reply-uses-inventory; read the four as one miss.
