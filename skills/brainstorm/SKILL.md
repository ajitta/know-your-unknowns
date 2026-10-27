---
name: brainstorm
description: >
  Brainstorm the intervention — for a named problem in any domain, spread ~10 candidate
  interventions from a fix for this afternoon to a quarter-long bet without judging them,
  then size the ones the user picks. Use on "brainstorm interventions", "show me
  options", or when a problem is named with no approach chosen. NOT for variants of one
  design — use prototypes. Clear to both sides: no skill or method.
---

# Brainstorm — Solution-Space Map (Brainstorm the Intervention)

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

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

   Ranking, pruning, sizing and any recommendation wait for the user's picks (steps 4–5). Judging while generating keeps the first safe ideas and stops the list before the unexpected ones (Osborn: defer judgment, go for quantity).
4. End the reply by asking which candidate numbers **resonate**; those are the picks.
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
