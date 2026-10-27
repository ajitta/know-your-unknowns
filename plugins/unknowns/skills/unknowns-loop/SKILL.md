---
name: unknowns-loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan →
  implement → verify → quiz) on significant or ambiguous work. Use on "unknowns loop",
  "run the operating loop", "know your unknowns".
  A bare "loop" means the built-in interval runner, not this skill.
---

# Unknowns Loop — operating loop for working with strong models

With strong models the bottleneck is keeping the **map** (the plan) matched to the **territory** (the code, the domain, the people who approve). The gap is **the unknowns**. This loop surfaces them cheaply before the build, logs them during it, and checks after it that the user can explain the result.

## Sequence

1. **Done criteria, in one exchange.** Fix the purpose, the done criteria, the existing behavior that must not break, and the allowed cost and change scope. Without done criteria, implementation volume gets mistaken for progress.

   The first reply names the stages below in run order, marks the current one, and states the done criteria or asks for them.

2. **Before the build**, in this order:

   | Stage | Run | When |
   |---|---|---|
   | a. Investigate | the **blindspot** skill; the **teach-me** skill first when the user cannot yet name the domain's terms | always |
   | b. Decide | the **interview** skill | requirements leave decisions open (architecture, data, compatibility, performance, taste) |
   | c. Shape | the **brainstorm** skill / the **prototypes** skill / the **reference** skill | the approach is undecided / the user will know the form when they see it / there is an example to emulate |
   | d. Test the riskiest assumption | state the most uncertain technical assumption with its success and failure criteria, then build a **minimal probe that verifies only that assumption** | the plan rests on an unproven technical assumption |
   | e. Plan | the **plan** skill, quoting step 1's done criteria | always |

   Each stage's deliverable (improved prompt, decisions, requirements, probe result) is the next stage's input. Skip a stage whose question is already answered, and say so.

   A probe costs minutes; the same assumption found wrong after the build costs the work built on it. Without a tool, do the step in the conversation and say what could not be checked.

3. **During the build**: the **deviation-log** skill logs each deviation from the plan in `IMPLEMENTATION_NOTES.md`.

4. **After the build**:

   a. **Verify**: check the result against step 1's done criteria, marking each met, partial or missing with its evidence (test run, output, `file:line`). Mark a criterion met when its evidence shows the required outcome.

   b. The **quiz** skill, so the user can explain the work in a PR or handoff; also the **buy-in** skill when reviewers or stakeholders must approve it.
