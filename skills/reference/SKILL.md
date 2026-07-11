---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer. Analyze
  reference code, mockups, or docs and prove comprehension before implementing. This
  skill should be used when the user provides reference material and says "use this
  as a reference", "레퍼런스로 써", "이 코드처럼 만들어줘", "이거 참고해서", or passes
  example code in another language/system, an HTML mockup, a screenshot, or a
  competitor's UX as the basis for new work.
argument-hint: "<reference file/path/description>"
---

# Reference — A Reference Is Another Map

Best way to give a model a map: **give it another map**.
Source: Thariq Shihipar — "Here's some code that represents what I want. It could be
in a different system or language. Read this code, understand it, and use that to
start your work." One working example beats hundreds of lines of explanation.

## Iron Rule

**Reference is not an answer to copy verbatim — it is material for understanding intent and behavior.**
Before implementing, **prove comprehension** — the semantics map from the original "Point at a Reference".

## Procedure

1. Read reference to the end; summarize **intent, core behavior, invariants**.
2. Present 4-category analysis:
   - **Behaviors to preserve** — the reference's reason to exist
   - **Parts to transform for current environment** — language/framework/scale differences
   - **Unnecessary or dangerous parts** — must not be brought into this project
   - **Parts improvable beyond the reference** — where we can do better
3. For port/transform work, also present **proof of comprehension (semantics map)**:
   key reference excerpts ↔ new-environment counterparts side by side, including
   gotcha points where behavior subtly differs and an edge-case table.
4. Contrast with current project conventions (code style, dependencies, test
   approach); present an **application plan**.
5. Start implementation after user confirmation. Record intentional deviations
   from the reference per `/unknowns:notes` rules.

## Output Format (HTML First)

Large analysis (many files, language port): **single-file interactive HTML** —
side-by-side comparison (reference excerpt ↔ counterpart plan), gotcha notes,
edge-case table, UI where per-item **approve/request-change selections assemble
into a reply**. No viewer available: fall back to markdown with same structure
(4-category analysis + semantics map comparison + gotcha/edge-case table).
Small analysis: markdown suffices.

## What Can Be a Reference

Existing implementation code, same algorithm in another language, working HTML
mockup, competitor product UX, past project design docs, test code,
screenshots/video, actual example of desired output. E.g., an HTML mockup as the
map when building a React component.
