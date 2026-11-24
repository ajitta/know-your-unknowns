---
type: llm
focus: transcript
---

The user asked for the operating loop on their community-radio podcast (muddy voices, levels that jump from week to week) and said they know no audio terms. The loop's first stage can hold two deliverables: a blind-spot pass that ends with numbered prompt fixes and an improved prompt, and a vocabulary explainer that offers numbered terms, comparisons or presets. In this conversation the user picks prompt fixes with "Apply fixes 1 and 3." (or "the first one only" when fewer than three were offered) and picks from the explainer with "I'll take items 1 and 2."

First find the two sets of picks. If no assistant reply offered numbered prompt fixes, or no assistant reply offered numbered terms, comparisons or presets to pick from, or the user did not make both sets of picks, write a line "NOT REACHED" directly before the final line and answer OVERALL: FAIL.

Otherwise judge the first assistant reply after both sets of picks that opens a later stage (deciding open questions, shaping the approach, testing the riskiest assumption or making the plan) or hands on the request that stage starts from. Read the earlier replies only to see what each picked fix and each picked term or preset was.

Pass when either holds:

1. The request that reply builds on, or hands on, carries every prompt fix the user picked and every term or preset the user picked, in any wording.
2. The reply names which of the two deliverables it builds on and lists the other deliverable's picks as still to apply.

Fail if it builds on the explainer's draft and leaves out a picked prompt fix, or builds on the improved prompt and leaves out a picked term or preset, without saying so. Fail also if no assistant reply after both sets of picks opens a later stage or hands on its request.
