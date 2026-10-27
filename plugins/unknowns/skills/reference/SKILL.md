---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer: read it,
  show the user your reading of it, and get it corrected before building on it. Any
  example: another organisation's policy, a past proposal, a contract template, a
  competitor's product, example code or a mockup. Use when the user says "use this as a
  reference", "make it like this", or supplies an example to build from. Self-evident requests are done directly.
---

# Reference — A Reference Is Another Map

This skill serves the **Hidden** cell (Johari window, adapted: the user knows what you do not), and reads back what you do not know or cannot judge before deciding. A self-evident request, where both of you already know what to do (the **Open** cell), is done directly, without this method.

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
