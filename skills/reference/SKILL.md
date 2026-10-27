---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer, and prove
  comprehension before implementing. Use when the user says "use this as a reference",
  "make it like this", or
  supplies example code, a mockup, or a competitor's UX to build from.
---

# Reference — A Reference Is Another Map

The best way to give a model a map: **give it another map**.

## Iron Rules

1. A reference is **not an answer to copy verbatim**; it is material for understanding intent and behavior.
2. Before implementing, **prove comprehension** with a semantics map.

## Procedure

1. Read and summarize the reference:

   a. Read the reference to the end.

   b. Summarize its **intent, core behavior, invariants**.

   No file access or browsing tool → ask the user to paste the reference or its relevant excerpts; label any missing portions unverified before continuing.

2. Present a 4-category analysis:

   | Category | What goes in it |
   |---|---|
   | **Behaviors to preserve** | The reference's reason to exist. |
   | **Parts to transform for the current environment** | Language/framework/scale differences. |
   | **Unnecessary or dangerous parts** | Must not be brought into this project. |
   | **Parts improvable beyond the reference** | Where we can do better. |

3. For port/transform work or before implementing any reference-based work, present **proof of comprehension (semantics map)**. The map holds:

   - key reference excerpts ↔ new-environment counterparts, side by side
   - gotcha points where behavior subtly differs
   - an edge-case table with a **Match** column: identical / equivalent / changed ("equivalent" = same decision, different surface)

   Number every note and row so a correction can name one. Give each row the reference location it came from (`file:line`, section, or timestamp) so the user can check the reading against the source.

4. Contrast and plan:

   a. Contrast it with the current project's conventions (code style, dependencies, test approach).

   b. Present an **application plan**.

5. **Sign-off gate — nothing is implemented until the user signs off.**

   a. The user replies `semantics confirmed`, or corrects any row by its number ("note 5", "budget exhaustion row"). On a correction, the map is revised before any code.

   b. Offer this choice once: implement now / revise the map / stop. When run as a **loop** stage, do not ask this separately: the loop's stage checkpoint carries these options.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

6. On sign-off:

   Record intentional deviations from the reference per the **notes** skill. When work departs from the plan, append the deviation to IMPLEMENTATION_NOTES.md before ending the turn. Stop and ask before changes to architecture, user-visible behavior, data, or security.

   a. **Port the reference's existing tests first**, before implementing.

   b. Implement within the logging and stop-and-ask limits at the start of step 6.

   No file system → print the record in the chat as Markdown and say to save it as IMPLEMENTATION_NOTES.md; show proposed code as Markdown code blocks for the user to save and do not claim the code was applied. No execution tool → give verification commands and keep their results unverified until the user supplies evidence.

## Output

Deliver Markdown in the conversation, keeping this skill's structure. End the turn with the assembled reply as Markdown in the conversation.

Numbered mapping rows (key reference excerpt ↔ new-environment counterpart) and edge-case rows each carry **approve / request-change**; selections assemble into a `semantics confirmed` reply or a numbered correction template.

For numbered reactions and reply assembly, read references/output-routing.md.

## What Can Be a Reference

Existing implementation code, the same algorithm in another language, a working HTML mockup, a competitor's product UX, past project design docs, test code, screenshots/video, an actual example of the desired output. For example, an HTML mockup as the map when building a React component.
