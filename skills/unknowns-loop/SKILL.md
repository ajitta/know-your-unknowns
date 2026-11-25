---
name: unknowns-loop
description: >
  Run the know-your-unknowns workflow end to end, ending with an outcome check. Use only
  on "unknowns loop" or "know your unknowns". A bare "loop" is NOT this.
---

# Unknowns Loop — operating loop for working with strong models

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

With strong models the bottleneck is keeping the **map** (the plan) matched to the **territory** (the situation itself: the domain, the people involved, the rules, the material, a codebase when there is one). The gap is **the unknowns**, on the user's side and on yours. This loop surfaces them cheaply before the work, logs them during it, and checks after it, when you largely produced the work, that the user can explain the result, and always that the result achieved the outcome.

## Sequence

1. **A request clear to both of you skips the loop.** When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange. A request that is not clear to both of you, including one whose read-back exposed a mismatch, goes on to step 2, and the skill the routing named runs at its stage in step 3 whatever that stage's When column says.

2. **Done criteria, in one exchange.** Fix the outcome (what the user is ultimately after), the done criteria, what already works and must not break, and the allowed cost and change scope. Without done criteria, the volume of output gets mistaken for progress.

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.

   The loop's first reply after step 1 names the stages below in run order, marks the current one, and states the outcome, the done criteria, what already works and must not break, and the allowed cost and change scope, or asks for them.

3. **Before the work**, in this order:

   | Stage | Run | When |
   |---|---|---|
   | a. Investigate | the **blindspot** skill; the **teach-me** skill first when the user cannot yet describe the task, and after the **blindspot** skill when the user can describe the task but lacks the field's vocabulary | always, unless its question is already answered |
   | b. Decide | the **interview** skill | requirements leave decisions open (structure, harm, compatibility, cost, taste) |
   | c. Shape | the **brainstorm** skill | the approach is undecided |
   | | the **prototypes** skill | the user will know the form when they see it |
   | | the **reference** skill | there is an example to emulate |
   | d. Test the riskiest assumption | state the most uncertain assumption the approach rests on, with its success and failure criteria, then run the **cheapest probe that tests only that assumption** (a spike, a phone call, a pilot, a sample) | the approach rests on an unproven assumption |
   | e. Plan | the **tweakable-plan** skill, quoting step 2's done criteria | always, unless its question is already answered |

   Each stage's deliverable (improved prompt, decisions, requirements, probe result) is the next stage's input. Skip any stage whose question is already answered, and say so.

   Show each stage's own result (stages a–e) in a reply before the next stage builds on it. After the stage's own ending (its question, draft or approval request), name the next stage. When that reply asks the user something, the next stage starts after the user's reply; a question the user skips stays open, and the next stage carries it as an assumption.

   Stage d: when you can run the probe (a spike, a sample you can draw), run it yourself. When only the user can run it (a phone call, a pilot), ask the user to run it, with its success and failure criteria. Judge the result against those criteria in a reply before stage e; when the user does not run the probe, stage e plans on the assumption, marked untested.

   A result that appears only inside a later stage's deliverable (the investigation's findings as notes in the plan) is lost to the user's review. A probe costs minutes; the same assumption found wrong after the work costs the work built on it.

   Without a tool, do the step in the conversation and say what could not be checked.

4. **During the work**: the **deviation-log** skill logs each deviation from the plan in the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work, otherwise the file the user names or `DEVIATIONS.md` beside the deliverable). Each entry's **Response chosen** says what the work now does about the deviation, including any part still to be done and when, not only the state the deviation left.

5. **After the work**:

   a. **Verify**: check the result against step 2's done criteria, what already works and must not break, and the allowed cost and change scope, marking each met, partial or missing with its evidence (a test run, a command's printed result, `file:line`, a document section, a confirmation from the person responsible).

   b. When you largely produced the work, the **quiz** skill, so the user can explain the work in a handoff; when reviewers or stakeholders must approve the work, the **buy-in** skill.

   c. **Outcome check**, with the user: ask whether the result achieved the outcome from step 2, not only whether it meets the done criteria. Name any gap between the result and the outcome, and what would close it, and let the user decide whether the work is finished. The check is a short exchange in the conversation.
