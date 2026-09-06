---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer, and prove
  comprehension before implementing. Use when the user says "use this as a reference",
  "make it like this", or
  supplies example code, a mockup, or a competitor's UX to build from.
argument-hint: "<reference file/path/description>"
---

# Reference — A Reference Is Another Map

Best way to give a model a map: **give it another map**.
Origin: Point at a Reference — see skills/loop/references/talk-source.md.

## Iron Rule

**Reference is not an answer to copy verbatim — it is material for understanding intent and behavior.**
Before implementing, **prove comprehension** with a semantics map.

## Procedure

1. Read reference to the end; summarize **intent, core behavior, invariants**.
2. Present 4-category analysis:
   - **Behaviors to preserve** — the reference's reason to exist
   - **Parts to transform for current environment** — language/framework/scale differences
   - **Unnecessary or dangerous parts** — must not be brought into this project
   - **Parts improvable beyond the reference** — where we can do better
3. For port/transform work, also present **proof of comprehension (semantics map)**:
   key reference excerpts ↔ new-environment counterparts side by side, gotcha points
   where behavior subtly differs, and an edge-case table with a **Match** column —
   identical / equivalent / changed ("equivalent" = same decision, different surface).
   Number every note and row so a correction can name one.
4. Contrast with current project conventions (code style, dependencies, test
   approach); present an **application plan**.
5. **Sign-off gate — nothing is implemented until the user signs off.** They reply
   `semantics confirmed`, or correct any row by its number ("note 5", "budget
   exhaustion row") and the map is revised before any code. In-session, offer the same
   choice once with AskUserQuestion: implement now / revise the map / stop.
6. On sign-off, **port the reference's existing tests first**, then implement. Record
   intentional deviations from the reference per `/unknowns:notes` (or `/notes` for
   copied installs).

## Output

Artifact tool if available → else `.unknowns/<YYYY-MM-DD>-reference-<slug>.html` → else
markdown; always echo the assembled reply in chat.
Numbered mapping rows (reference excerpt ↔ counterpart plan) and edge-case rows each
carry **approve / request-change**; selections assemble into a `semantics confirmed`
reply or a numbered correction template.
Details: skills/loop/references/output-routing.md

## What Can Be a Reference

Existing implementation code, same algorithm in another language, working HTML
mockup, competitor product UX, past project design docs, test code,
screenshots/video, actual example of desired output. E.g., an HTML mockup as the
map when building a React component.
