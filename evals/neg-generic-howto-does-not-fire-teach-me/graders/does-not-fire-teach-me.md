---
type: tool_used
tool: Skill
input_match: unknowns:teach-me
min: 0
max: 0
arm: both
---

`teach me` is a two-word generic English phrase, so teach-me's trigger surface
overlaps every ordinary "teach me how to X" request. The skill is for a domain
whose *vocabulary* the user cannot yet name — the state where they cannot state a
precise request. This prompt is the opposite: the terms are known, the answer is
known, and the user has already specified the two techniques and the output format.

`min: 0` + `max: 0` + `arm: both` is the documented form of a must-NOT-fire check.
This case exists because `docs/trigger-matrix.md` lists this exact overfire direction
under "남은 위험" and nothing measured it.
