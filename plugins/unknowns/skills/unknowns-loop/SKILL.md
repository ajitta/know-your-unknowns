---
name: unknowns-loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan → work →
  verify → quiz → outcome check) on significant or ambiguous work in any domain. Use on
  "unknowns loop", "run the operating loop", "know your unknowns". A bare "loop" means
  the built-in interval runner, not this skill. Clear to both: no skill or method; if
  weighty (ships, is sent, hard to undo), first read back request, assumptions and what
  done means in 2–3 lines; a mismatch goes to teach-me, interview or blindspot.
---

# Unknowns Loop — operating loop for working with strong models

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

With strong models the bottleneck is keeping the **map** (the plan) matched to the **territory** (the situation itself: the domain, the people involved, the rules, the material, a codebase when there is one). The gap is **the unknowns**, on the user's side and on yours. This loop surfaces them cheaply before the work, logs them during it, and checks after it that the user can explain the result and that the result achieved the outcome.

## Sequence

1. **Read back first.** When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange. A request that is not clear to both of you goes on to step 2.

2. **Done criteria, in one exchange.** Fix the outcome (what the user is ultimately after), the done criteria, what already works and must not break, and the allowed cost and change scope. Without done criteria, the volume of output gets mistaken for progress.

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.

   The loop's first reply after step 1 names the stages below in run order, marks the current one, and states the done criteria or asks for them.

3. **Before the work**, in this order:

   | Stage | Run | When |
   |---|---|---|
   | a. Investigate | the **blindspot** skill; the **teach-me** skill first when the user cannot yet name the domain's terms | always |
   | b. Decide | the **interview** skill | requirements leave decisions open (structure, harm, compatibility, cost, taste) |
   | c. Shape | the **brainstorm** skill / the **prototypes** skill / the **reference** skill | the approach is undecided / the user will know the form when they see it / there is an example to emulate |
   | d. Test the riskiest assumption | state the most uncertain assumption the plan rests on, with its success and failure criteria, then run the **cheapest probe that tests only that assumption** (a spike, a phone call, a pilot, a sample) | the plan rests on an unproven assumption |
   | e. Plan | the **tweakable-plan** skill, quoting step 2's done criteria | always |

   Each stage's deliverable (improved prompt, decisions, requirements, probe result) is the next stage's input. Skip a stage whose question is already answered, and say so.

   A probe costs minutes; the same assumption found wrong after the work costs the work built on it. Without a tool, do the step in the conversation and say what could not be checked.

4. **During the work**: the **deviation-log** skill logs each deviation from the plan in the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work).

5. **After the work**:

   a. **Verify**: check the result against step 2's done criteria, marking each met, partial or missing with its evidence (a test run, an output, `file:line`, a document section, a confirmation from the person responsible). Mark a criterion met when its evidence shows the required result.

   b. The **quiz** skill, so the user can explain the work in a handoff; also the **buy-in** skill when reviewers or stakeholders must approve it.

   c. **Outcome check**, with the user: ask whether the result achieved the outcome from step 2, not only whether it meets the done criteria. Name any gap between the two and what would close it, and let the user decide whether the work is finished. The check is a short exchange in the conversation; nothing is scored.
