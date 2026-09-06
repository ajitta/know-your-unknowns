---
type: tool_used
tool: Skill
input_match: unknowns:brainstorm
---

Trigger indicator only. `tool: Skill` with no `arm:` is reported under
`--ablation with-without` and excluded from the score in both arms, so it can
never move the delta on its own. The scored check is the outcome grader.
