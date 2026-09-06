---
name: plan
description: >
  The tweakable plan — a plan sorted by likelihood-of-tweaking, not execution order,
  so the most changeable decisions get reviewed first. Use on "plan this", "make a plan",
  "tweakable plan".
  Not native plan mode: writes a reviewable pre-implementation document.
argument-hint: "<task description or confirmed spec>"
---

# Plan — The Tweakable Plan (sorted by tweak likelihood)

Plan's purpose: not execution-order listing but **pulling user-intervention points forward**.
Even if the user tires reading top-down, they have already seen every decision that matters.
Origin: The Tweakable Plan — see skills/loop/references/talk-source.md.

## Iron rules

1. **Execution order ≠ presentation order.** Present by tweak likelihood; execution order
   appears only as a number on each item.
2. Every decision carries **considered alternatives** — a decision without alternatives
   cannot be reviewed.

## Procedure

1. Confirm spec from `$ARGUMENTS` plus conversation context (blindspot findings,
   interview decisions); with no argument, that context is the whole input. Big gaps →
   suggest `/unknowns:interview` (or `/interview` for copied installs) first.
2. **Size gate**: task touches ≤2 files and carries no schema, interface, or UX-contract
   decision → say so and defer to native plan mode instead of writing this document.
3. Split work into items, two kinds:
   - **Decision items** — schema/data model, public interfaces (API, types), UX contracts,
     dependency choices, migration approach: high blast radius if changed
   - **Mechanical items** — follow automatically once decisions set (CRUD, wiring,
     boilerplate)
4. **Sort decision items by tweak likelihood × blast radius**, place first. Each item:
   chosen option / alternatives considered + why rejected / scope affected if this decision
   changes / verification method. Render every new or changed public type or schema as
   **annotated code** — the declaration itself, plus numbered notes, one per field choice
   worth arguing with.
5. Mechanical items folded at back (1-line summary + expand).
6. Required for every step: **verification method** / **expected risks** / **rollback method**.
7. Flag the **weakest part of this plan** (the decision resting on the thinnest evidence),
   and close with **2–3 pre-written reply lines** — the highest-leverage tweaks, ready to
   copy, edit, and send.
8. Proceed to implementation only after user approval/change requests update the plan.
   Record mid-implementation deviations per `/unknowns:notes` rules.

## Output

Artifact tool → `.unknowns/<YYYY-MM-DD>-plan-<slug>.html` → markdown; highest available rung wins.
Each decision card carries an **alternative toggle** and an **approve / request-change**
control; selections assemble into a reply like "item 3 → alternative B, rest approved",
with mechanical work collapsed.
Details: skills/loop/references/output-routing.md
