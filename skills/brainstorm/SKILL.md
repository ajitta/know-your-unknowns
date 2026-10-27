---
name: brainstorm
description: >
  Brainstorm the intervention — spread ~10 codebase-grounded candidates, from a
  ship-this-afternoon fix to a quarter-long bet. Use on "brainstorm interventions",
  "show me options", or when a problem is named with no approach chosen.
  NOT for UI/design variants — use prototypes.
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

Jumping on the first solution leaves the rest of the solution space unknown. The user picks; the model draws the space.

## Iron Rules

1. **The output is a map of solutions, not a solution.** It ends at the user's assembled selection.
2. Spread candidates **across time horizons and approaches**, not 10 near-duplicates.

## Procedure

1. Get the problem definition and constraints (timeline, people, cost) from the text the user gave with the request or after the skill name and the conversation. If they are empty or vague, ask back once for a measurable statement: which metric, how bad, since when, for whom. One round only. If the answer is still vague or the user skips, generate the candidates anyway and state the assumed metric and constraints above them.
2. When a codebase is in scope, search it for machinery that already exists but sits disconnected, before generating candidates in step 3.

   a. Search the codebase yourself or use the `unknowns:unknowns-scout` agent.

   b. When you spawn the scout, the packet overrides the scout's default output (blindspot cards and an improved prompt). The packet asks the scout to return an **inventory**, one row per existing mechanism that bears on the problem, with the columns `path` / what it does today / what is missing to wire it in / evidence / status (confirmed / inferred). No cards, no prompt draft.

   Without a tool, do the step in the conversation and say what could not be checked.

   The cheapest candidates are usually wiring, not building.
3. Generate **~10** candidate interventions, spread across the time axis: ship this afternoon / short-term (1–2 weeks) / mid-term (quarter) / quarter-long bets.
4. Attach these fields to each candidate:
   - name
   - one-line description
   - expected impact: what improves, by how much
   - effort size: S/M/L/XL
   - key risks
   - how to measure success
   - `Found in code — <path>`, when the candidate builds on machinery already in the repo
5. Ask which candidate numbers **resonate**; the selected numbers assemble into a copyable "proceed with these, in this order"; a missing pick is undecided.

## Output

Layout: numbered cards on a time axis (ship this afternoon → quarter-long bet).

## Related

After the user picks interventions, hand off by what is still open:

| Still open | Skill |
|---|---|
| The form is in question | **prototypes** |
| Spec finalization | **interview** |
| Implementation plan | **plan** |
