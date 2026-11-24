---
type: tool_used
tool: Agent
input_match: unknowns-scout
min: 0
weight: 0
---

Indicator only; reported, not scored (`min: 0` passes either way and `weight: 0` keeps it
out of the score). It shows whether the pass handed the investigation to the
unknowns-scout agent. The blindspot skill uses the scout when the
task spans more sources than the model can read in full, and twenty-two short policy
documents can be read in full. `behavior-blindspot-scout-many-contracts` is the case built
to make the skill spawn the scout. The scored
outcome is assumption-verdicts-with-evidence.
