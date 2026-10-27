---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer: read it, show
  the user your reading, and get it corrected before building on it. Use on "use this as
  a reference", "make it like this", or when the user supplies an example to build from.
  Clear to both: no skill or method; if weighty (ships, is sent, hard to undo), first
  read back request, assumptions and what done means in 2–3 lines; a mismatch goes to
  teach-me, interview or blindspot.
---

# Reference — A Reference Is Another Map

This skill serves what you do not know and the user does: before building on a reference, it reads back your reading of it for the user to correct.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

## Iron Rules

1. A reference is **not an answer to copy verbatim**; it is material for understanding intent and behavior.
2. Before building on it, **prove comprehension** with a semantics map: the user knows why they chose this reference, and your reading of it is the part they can correct.

## Procedure

1. Read and summarize the reference:

   a. Read the reference to the end.

   b. Summarize its **intent, core behavior, invariants**.

   Without a tool, do the step in the conversation and say what could not be checked.

2. Present a 4-category analysis:

   | Category | What goes in it |
   |---|---|
   | **Behaviors to preserve** | The reference's reason to exist. |
   | **Parts to transform for the current environment** | Differences of context, e.g. language, framework, scale, audience, jurisdiction, budget. |
   | **Unnecessary or dangerous parts** | Left out of this work, with the reason. |
   | **Parts improvable beyond the reference** | Where we can do better. |

3. Before building anything on the reference, a port or adaptation included, present **proof of comprehension (semantics map)**. The semantics map holds:

   - key reference excerpts ↔ new-environment counterparts, side by side
   - gotcha notes where behavior subtly differs
   - an edge-case table with a **Match** column: identical / equivalent / changed ("equivalent" = same decision, different surface)

   Number every note and row so a correction can name one. Give each row the reference location it came from (`file:line`, section, or timestamp) so the user can check the reading against the source. Mark each counterpart that rests on a guess about the user's context (which behaviors they want kept, the local facts the reference does not show) as *assumed*, so the user corrects those first.

4. Contrast and plan:

   a. Contrast it with the current work's conventions (e.g. house style, tools and dependencies, how the work is checked).

   b. Present an **application plan** that first carries over how the reference checks itself (its tests, checklists or acceptance criteria), so the new version is checked against the reference's own behavior.

5. **Sign-off gate**: the user replies `semantics confirmed`, or corrects any row by its number ("note 5", "budget exhaustion row"). On a correction, revise the semantics map and show it again. The skill ends at sign-off; the signed-off map and application plan are the input to the build.

## Output

Numbered mapping rows (key reference excerpt ↔ new-environment counterpart) and edge-case rows each carry **approve / request-change**; selections assemble into a `semantics confirmed` reply or a numbered correction template; a missing pick is undecided.

## What Can Be a Reference

Another organisation's policy, a past proposal or report, a contract or form template, a competitor's product or event, existing code, the same algorithm in another language, a working HTML mockup, test code, screenshots/video, an actual example of the desired output. For example, a neighbouring city's grant guidelines as the map for your own call, or an HTML mockup when building a React component.
