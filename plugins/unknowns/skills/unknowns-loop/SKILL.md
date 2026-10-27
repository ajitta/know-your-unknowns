---
name: unknowns-loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan → do the
  work → verify → quiz → outcome check) on significant or ambiguous work in any
  domain: an event, a study, a policy, a product launch, a feature. Use on "unknowns
  loop", "run the operating loop", "know your unknowns". A bare "loop" means the
  built-in interval runner, not this skill. Self-evident requests are done directly.
---

# Unknowns Loop — operating loop for working with strong models

This skill serves the **Unknown** cell (Johari window, adapted: neither the user nor you know yet), and surfaces both sides' unknowns. A self-evident request, where both of you already know what to do (the **Open** cell), is done directly, without this method.

With strong models the bottleneck is keeping the **map** (the plan) matched to the **territory** (the situation itself: the domain, the people involved, the rules, the material, a codebase when there is one). The gap is **the unknowns**, on the user's side and on yours. This loop surfaces them cheaply before the work, logs them during it, and checks after it that the user can explain the result and that the result achieved the outcome.

## Sequence

1. **Done criteria, in one exchange.** Fix the outcome (what the user is ultimately after), the done criteria, what already works and must not break, and the allowed cost and change scope. Without done criteria, the volume of output gets mistaken for progress.

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.

   The first reply names the stages below in run order, marks the current one, and states the done criteria or asks for them.

2. **Before the work**, in this order:

   | Stage | Run | When |
   |---|---|---|
   | a. Investigate | the **blindspot** skill; the **teach-me** skill first when the user cannot yet name the domain's terms | always |
   | b. Decide | the **interview** skill | requirements leave decisions open (structure, harm, compatibility, cost, taste) |
   | c. Shape | the **brainstorm** skill / the **prototypes** skill / the **reference** skill | the approach is undecided / the user will know the form when they see it / there is an example to emulate |
   | d. Test the riskiest assumption | state the most uncertain assumption the plan rests on, with its success and failure criteria, then run the **cheapest probe that tests only that assumption** (a spike, a phone call, a pilot, a sample) | the plan rests on an unproven assumption |
   | e. Plan | the **tweakable-plan** skill, quoting step 1's done criteria | always |

   Each stage's deliverable (improved prompt, decisions, requirements, probe result) is the next stage's input. Skip a stage whose question is already answered, and say so.

   A probe costs minutes; the same assumption found wrong after the work costs the work built on it. Without a tool, do the step in the conversation and say what could not be checked.

3. **During the work**: the **deviation-log** skill logs each deviation from the plan in the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work).

4. **After the work**:

   a. **Verify**: check the result against step 1's done criteria, marking each met, partial or missing with its evidence (a test run, an output, `file:line`, a document section, a confirmation from the person responsible). Mark a criterion met when its evidence shows the required result.

   b. The **quiz** skill, so the user can explain the work in a handoff; also the **buy-in** skill when reviewers or stakeholders must approve it.

   c. **Outcome check**, with the user: ask whether the result achieved the outcome from step 1, not only whether it meets the done criteria. Name any gap between the two and what would close it, and let the user decide whether the work is finished. The check is a short exchange in the conversation; nothing is scored.
