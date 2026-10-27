---
name: plan
description: >
  The tweakable plan — a plan sorted by likelihood-of-tweaking, not execution order,
  so the most changeable decisions get reviewed first. Use on "plan this", "make a plan",
  "tweakable plan".
  Not native plan mode: writes a reviewable pre-implementation document.
---

# Plan — The Tweakable Plan (sorted by tweak likelihood)

A plan's purpose is to **pull the points where the user would intervene forward**, not to list steps in execution order. Even if the user stops reading partway down, they have already seen every decision that matters. The plan ends at the user's approval or change requests; the build starts from the approved plan.

## Iron Rules

1. **Execution order ≠ presentation order.** Present by tweak likelihood; execution order appears only as a number on each item.
2. Every decision carries **considered alternatives** — a decision without alternatives cannot be reviewed.

## Procedure

1. Confirm the spec from the text the user gave with the request or after the skill name plus the conversation context (blindspot findings, interview decisions).

   a. With no argument, that context is the whole input.

   b. When the spec has big gaps, suggest the **interview** skill before planning.
2. **Done criteria first**: the document opens with one line stating the purpose, the done criteria, the existing behavior that must not break, and the allowed cost and change scope, filled from context (quote the **loop** skill's step 1 when it ran). Write "not set" for any part the context does not give, and ask for it in the reply lines of step 7. Without done criteria, nobody can judge whether the build conforms.
3. **Size gate**: when the change creates or modifies ≤2 files and carries no schema, interface, or UX-contract decision, say it needs no tweakable plan and reply with only the done-criteria line and the implementation steps in execution order, one line each: a change this small has no decision worth a review document, and a shortened copy of the document is still the document.
4. Split work into items of two kinds:

   | Item type | Covers | Trait |
   |---|---|---|
   | **Decision items** | schema/data model, public interfaces (API, types), UX contracts, dependency choices, migration approach | high blast radius if changed |
   | **Mechanical items** | e.g. CRUD, wiring, boilerplate | follow automatically once the decisions are set |
5. Order and fill the decision items.

   a. **Sort decision items by tweak likelihood × blast radius** and place them first, ahead of the mechanical items.

   b. Give each decision item: chosen option / alternatives considered + why rejected / scope affected if this decision changes / **verification method** / **what breaks if this is wrong**.

   c. Render every new or changed public type or schema as **annotated code**: the declaration itself, plus numbered notes, one per field choice worth arguing with.
6. Put mechanical items at the back, each with a 1-line summary and its verification, and the details below them.
7. Flag the weakest part, then close.

   a. Flag the **weakest part of this plan** (the decision resting on the thinnest evidence).

   b. Close with **2–3 pre-written reply lines**: the highest-leverage tweaks, ready to copy, edit, and send.

## Output

Each numbered decision item lists lettered alternatives and asks for **approve / request-change**; selections assemble into a reply like "item 3 → alternative B, rest approved", with mechanical work after the decisions; a missing pick is undecided.
