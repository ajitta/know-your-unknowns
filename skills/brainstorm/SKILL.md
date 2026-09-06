---
name: brainstorm
description: >
  Brainstorm the intervention — spread ~10 codebase-grounded candidates from
  ship-this-afternoon to quarter-long bet. Use on "brainstorm interventions",
  "show me options", "브레인스토밍", "해법 후보 펼쳐줘", "옵션 보여줘", or a problem
  named with no approach chosen. NOT for UI/design variants — use prototypes.
argument-hint: "<problem to solve> [constraints: timeline/people/budget]"
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

Jumping on the first solution leaves **the rest of the solution space unknown**.
The user picks; the model draws the space.
Origin: Brainstorm the Intervention — see skills/loop/references/talk-source.md.

## Iron Rules

1. **Implement nothing yet.** Output is a map of solutions, not a solution.
2. Not 10 near-duplicates — spread candidates **diverse in time horizon and approach**.

## Procedure

1. Get problem definition and constraints (timeline, people, cost) from `$ARGUMENTS` +
   conversation context. If empty or vague, ask back once for a measurable statement:
   which metric, how bad, since when, for whom — one round only.
2. When a codebase is in scope, **search it first** (or spawn the `unknowns:unknowns-scout`
   agent with the Agent tool) for machinery that already exists but sits disconnected —
   the cheapest candidates are usually wiring, not building.
3. Generate **~10** candidate interventions, spread across the time axis: ship this
   afternoon / short-term (1–2 weeks) / mid-term (quarter) / quarter-long bets.
4. Attach to each candidate: **name / one-line description / expected impact (what
   improves, by how much) / effort size (S/M/L/XL) / key risks / how to measure success**,
   plus **`Found in code — <path>`** when it builds on machinery already in the repo.
5. Present arranged by **impact × effort** (a plugin extension of the source's single
   time axis) — quick wins and big bets distinguishable at a glance.
6. After user selection: convert chosen interventions into **structured next steps** —
   down to each intervention's first execution prompt (or experiment design).

## Output

Artifact tool if available → else `.unknowns/<YYYY-MM-DD>-brainstorm-<slug>.html` → else
markdown; always echo the assembled reply in chat.
Cards on a time axis (ship this afternoon → quarter-long bet) with a toggle to the
impact × effort matrix; each card's **resonate checkbox** assembles into a copyable
"proceed with these, in this order".
Details: skills/loop/references/output-routing.md

## Follow-ups

- After picking interventions: form in question → `/unknowns:prototypes` (or
  `/prototypes` for copied installs); spec finalization → `/unknowns:interview`;
  implementation plan → `/unknowns:plan`.
