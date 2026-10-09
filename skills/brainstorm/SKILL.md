---
name: brainstorm
description: >
  Brainstorm the intervention — spread ~10 codebase-grounded candidates from
  ship-this-afternoon to quarter-long bet. Use on "brainstorm interventions",
  "show me options", or a problem
  named with no approach chosen. NOT for UI/design variants — use prototypes.
argument-hint: "<problem to solve> [constraints: timeline/people/budget]"
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

Jumping on the first solution leaves **the rest of the solution space unknown**.
The user picks; the model draws the space.

## Iron Rules

1. **Implement nothing yet.** Output is a map of solutions, not a solution.
2. Spread candidates **across time horizons and approaches**, not 10 near-duplicates.

## Procedure

1. Get the problem definition and constraints (timeline, people, cost) from `$ARGUMENTS`
   and the conversation. If they are empty or vague, ask back once for a measurable
   statement: which metric, how bad, since when, for whom. One round only.
2. When a codebase is in scope, **search it first** (or spawn the `unknowns:unknowns-scout`
   agent where the Agent tool exists) for machinery that already exists but sits
   disconnected. The cheapest candidates are usually wiring, not building. The scout
   returns blindspot cards and an improved prompt by default, so the packet overrides
   that: return an **inventory**, one row per existing mechanism that bears on the
   problem: `path` / what it does today / what is missing to wire it in / evidence /
   status (confirmed / inferred). No cards, no prompt draft.
3. Generate **~10** candidate interventions, spread across the time axis: ship this
   afternoon / short-term (1–2 weeks) / mid-term (quarter) / quarter-long bets.
4. Attach to each candidate: **name / one-line description / expected impact (what
   improves, by how much) / effort size (S/M/L/XL) / key risks / how to measure success**,
   plus **`Found in code — <path>`** when it builds on machinery already in the repo.
5. Arrange them by **impact × effort**, so quick wins and big bets stand out at a glance.
6. After the user selects, turn the chosen interventions into **structured next steps**,
   down to each one's first execution prompt (or experiment design).

## Output

Artifact tool if available → else `.unknowns/<YYYY-MM-DD>-brainstorm-<slug>.html` → else
markdown; always echo the assembled reply in chat.
Cards on a time axis (ship this afternoon → quarter-long bet) with a toggle to the
impact × effort matrix; each card's **resonate checkbox** assembles into a copyable
"proceed with these, in this order".
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Follow-ups

- After picking interventions: the form is in question → the **prototypes** skill; spec finalization → the **interview** skill;
  implementation plan → the **plan** skill.
