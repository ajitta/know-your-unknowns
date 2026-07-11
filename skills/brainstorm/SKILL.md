---
name: brainstorm
description: >
  Brainstorm the intervention — map the whole solution space before committing to one
  approach. Generates ~10 candidate interventions spread across a time/effort horizon,
  with impact, risk, and a selection UI that assembles picks into a structured next
  step. This skill should be used when the user says "brainstorm interventions",
  "spread out solution candidates", "not sure what to do", "show me options",
  "브레인스토밍", "해법 후보 펼쳐줘", "뭘 해야 할지 모르겠어", "옵션 보여줘", or names
  a problem (churn, slow builds, flaky tests, low conversion) without having chosen
  an approach.
argument-hint: "<problem to solve> [constraints: timeline/people/budget]"
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

Implement the first solution on receipt of a problem and **the rest of the solution space stays unknown**. Original "Brainstorm the Intervention": for a churn problem, spread 10 strategies on a timeline from apply-today to quarter-scale bets, with resonate checks assembling into a structured response. User picks; model draws the space.

## Iron Rules

1. **Implement nothing yet.** Output is a map of solutions, not a solution.
2. Not 10 near-duplicates — spread candidates **diverse in time horizon and approach**.

## Procedure

1. Get problem definition and constraints (timeline, people, cost) from `$ARGUMENTS`. If problem definition is vague, ask back briefly — one round only (in measurable form: "what is how bad").
2. Generate **~10** candidate interventions, spread across the time axis: immediate (today) / short-term (1–2 weeks) / mid-term (quarter) / long-term bets.
3. Attach to each candidate: **name / one-line description / expected impact (what improves, by how much) / effort-cost / key risks / how to measure success**.
4. Present arranged by **impact × effort** — quick wins and big bets distinguishable at a glance.
5. After user selection: convert chosen interventions into **structured next steps** — down to each intervention's first execution prompt (or experiment design).

## Output Format (HTML first)

**Single-file interactive HTML**: candidates as cards on a time-axis timeline (immediate → long-term), toggle to impact×effort matrix view, per-card **resonate checkbox** — checked items **auto-assemble at bottom into a copyable "proceed with these, in this order" structured response**. CSS/JS inline, no external dependencies. If no viewer available, fall back to markdown: per-horizon tables + selection guidance.

## Follow-ups

- After picking interventions: form in question → `/unknowns:prototypes`; spec finalization → `/unknowns:interview`; implementation plan → `/unknowns:plan`.
