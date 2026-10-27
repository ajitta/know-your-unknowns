---
name: brainstorm
description: >
  Brainstorm the intervention — spread ~10 candidate interventions for a named problem,
  grounded in what already exists, from a fix for this afternoon to a quarter-long bet,
  for the user to pick from. Any problem: falling sales, low turnout, a slow process,
  churn in a product. Use on "brainstorm interventions", "show me options", or when a
  problem is named with no approach chosen. NOT for variants of one design — use
  prototypes. Self-evident requests are done directly.
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns. A self-evident request, where both of you already know what to do, is done directly, without this method.

Jumping on the first solution leaves the rest of the solution space unknown. The user picks; the model draws the space.

## Iron Rules

1. **The output is a map of solutions, not a solution.** It ends at the user's assembled selection.
2. Spread candidates **across time horizons and approaches**, not 10 near-duplicates.

## Procedure

1. Get the problem definition and constraints (timeline, people, cost) from the text the user gave with the request or after the skill name and the conversation. If they are empty or vague, ask back once for a measurable statement: which metric, how bad, since when, for whom. One round only. If the answer is still vague or the user skips, generate the candidates anyway and state the assumed metric and constraints above them.

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.

   When you ask back for the problem statement, put these in the same round.
2. Before generating candidates in step 3, look for what already exists but is not used for this problem: in a codebase, machinery that sits disconnected; elsewhere, resources, programs, people or partnerships already in reach.

   a. Search the material yourself or use the `unknowns:unknowns-scout` agent.

   b. When you spawn the scout, the packet overrides the scout's default output (blindspot cards and an improved prompt). The packet asks the scout to return an **inventory**, one row per existing mechanism that bears on the problem, with the columns where it is / what it does today / what is missing to put it to use / evidence / status (confirmed / inferred). No cards, no prompt draft.

   Without a tool, do the step in the conversation and say what could not be checked.

   The cheapest candidates are usually connecting what exists, not building.
3. Generate **~10** candidate interventions with judgment deferred, spread across the time axis (this afternoon / short-term (1–2 weeks) / mid-term (quarter) / quarter-long bets) and across approaches, the unlikely ones included. Give each only:
   - name
   - one-line description: what it would change
   - `Already exists — <where>`, when the candidate builds on something step 2 found

   Ranking, scoring and pruning wait for step 5. Judging while generating keeps the first safe ideas and stops the list before the unexpected ones (Osborn: defer judgment, go for quantity).
4. Ask which candidate numbers **resonate**.
5. At selection, attach these fields to each picked candidate:
   - expected impact: what improves, by how much
   - effort size: S/M/L/XL
   - key risks
   - how to measure success: the sign that it moved the stated problem, not only that it was done

   The picked numbers assemble into a copyable "proceed with these, in this order"; a missing pick is undecided.

## Output

Layout: numbered cards on a time axis (this afternoon → quarter-long bet).

## Related

After the user picks interventions, hand off by what is still open:

| Still open | Skill |
|---|---|
| The form is in question | **prototypes** |
| Decisions only the user can make | **interview** |
| The plan for the work | **tweakable-plan** |
