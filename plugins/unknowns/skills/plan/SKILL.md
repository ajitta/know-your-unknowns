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

A plan's purpose is to **pull the points where the user would intervene forward**, not to list steps in execution order. Even if the user stops reading partway down, they have already seen every decision that matters.

## Iron Rules

1. **Execution order ≠ presentation order.** Present by tweak likelihood; execution order appears only as a number on each item.
2. Every decision carries **considered alternatives** — a decision without alternatives cannot be reviewed.

## Procedure

1. Confirm the spec from `$ARGUMENTS` plus the conversation context (blindspot findings, interview decisions).

   a. With no argument, that context is the whole input.

   b. When the spec has big gaps, suggest the **interview** skill before planning.
2. **Done criteria first**: the document opens with a fixed four-field done-criteria section: **purpose / done criteria / existing behavior that must never break / allowed cost & change scope**.

   a. Fill the section from context. When the loop's step 1 already fixed these fields, quote them instead of asking again.

   b. When any field is still empty, ask one AskUserQuestion round.

   c. If the user skips, write "done criteria not set — the reviewer cannot judge conformance" in the section; never drop it silently.

   The independent reviewer's packet starts from this section.
3. **Size gate**: when the task touches ≤2 files and carries no schema, interface, or UX-contract decision:

   a. Say so and defer to native plan mode instead of writing this document.

   b. State the done criteria in one line even when deferring.
4. Split work into items of two kinds:

   | Item type | Covers | Trait |
   |---|---|---|
   | **Decision items** | schema/data model, public interfaces (API, types), UX contracts, dependency choices, migration approach | high blast radius if changed |
   | **Mechanical items** | e.g. CRUD, wiring, boilerplate | follow automatically once the decisions are set |
5. Order and fill the decision items.

   a. **Sort decision items by tweak likelihood × blast radius** and place them first, ahead of the mechanical items.

   b. Give each decision item: chosen option / alternatives considered + why rejected / scope affected if this decision changes / verification method.

   c. Render every new or changed public type or schema as **annotated code**: the declaration itself, plus numbered notes, one per field choice worth arguing with.
6. Fold mechanical items at the back (1-line summary + expand).
7. Required for every step: **verification method** / **expected risks** / **rollback method**.
8. Flag the weakest part, then close.

   a. Flag the **weakest part of this plan** (the decision resting on the thinnest evidence).

   b. Close with **2–3 pre-written reply lines**: the highest-leverage tweaks, ready to copy, edit, and send.
9. Gate implementation on the user's response.

   a. Proceed to implementation only after the user's approval or change requests have updated the plan. When run as a **loop** stage, do not ask this separately: the loop's stage checkpoint carries the approval.

   b. Record mid-implementation deviations per the **notes** skill rules.

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-plan-<slug>.html`; else markdown with the same structure. On every rung, end the turn with the assembled reply as plain text in chat.

Each decision card carries an **alternative toggle** and an **approve / request-change** control; selections assemble into a reply like "item 3 → alternative B, rest approved", with mechanical work collapsed.

Before writing HTML, read how to build the page from the template: references/output-routing.md
