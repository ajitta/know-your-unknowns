---
name: brainstorm
description: >
  Brainstorm the intervention — spread ~10 codebase-grounded candidates, from a
  ship-this-afternoon fix to a quarter-long bet. Use on "brainstorm interventions",
  "show me options", or when a problem is named with no approach chosen.
  NOT for UI/design variants — use prototypes.
argument-hint: "<problem to solve> [constraints: timeline/people/budget]"
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

Jumping on the first solution leaves the rest of the solution space unknown. The user picks; the model draws the space.

## Iron Rules

1. **Implement nothing yet.** Output is a map of solutions, not a solution.
2. Spread candidates **across time horizons and approaches**, not 10 near-duplicates.

## Procedure

1. Get the problem definition and constraints (timeline, people, cost) from `$ARGUMENTS` and the conversation. If they are empty or vague, ask back once for a measurable statement: which metric, how bad, since when, for whom. One round only.
2. When a codebase is in scope, search it for machinery that already exists but sits disconnected, before generating candidates in step 3.

   a. Search the codebase yourself or spawn the `unknowns:unknowns-scout` agent. No Agent tool → search the codebase yourself.

   b. When you spawn the scout, the packet overrides the scout's default output (blindspot cards and an improved prompt). The packet asks the scout to return an **inventory**, one row per existing mechanism that bears on the problem, with the columns `path` / what it does today / what is missing to wire it in / evidence / status (confirmed / inferred). No cards, no prompt draft.

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
5. Arrange the candidates by **impact × effort**, so quick wins and big bets stand out at a glance.
6. After the user selects, turn the chosen interventions into **structured next steps**, down to each one's first execution prompt (or experiment design).

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-brainstorm-<slug>.html`; else markdown with the same structure. On every rung, end the turn with the assembled reply as plain text in chat.

Layout: cards on a time axis (ship this afternoon → quarter-long bet), with a toggle to the impact × effort matrix.

Reaction control: a **resonate checkbox** on each card; the checked cards assemble into a copyable "proceed with these, in this order".

Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Related

After the user picks interventions, hand off by what is still open:

| Still open | Skill |
|---|---|
| The form is in question | **prototypes** |
| Spec finalization | **interview** |
| Implementation plan | **plan** |
