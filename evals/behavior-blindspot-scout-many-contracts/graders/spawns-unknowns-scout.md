---
type: tool_used
tool: Agent
input_match: unknowns-scout
min: 1
---

Scored. The task spans 214 supplier agreements of about 3.8 KB each (about 820 KB in all), written in four layouts whose wording varies from agreement to agreement, so that counting repeated lines does not reduce them to a few documents: more than the model can read in full, so blindspot step 2 hands the investigation to the scout: "The task spans more sources than you can read in full (e.g. a whole codebase or many modules, a large body of documents or records)" → "Use the `unknowns:unknowns-scout` agent." Until this case no recorded run had a skill spawn the scout (`CHANGELOG.md` 0.13.2, **Not measured**). A run that does not spawn it also fails packet-carries-both-sides-assumptions, scout-marks-each-assumption and reply-uses-scout-rows; read the four as one miss.
