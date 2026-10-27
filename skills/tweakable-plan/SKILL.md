---
name: tweakable-plan
description: >
  The tweakable plan — for any work, a plan sorted by likelihood of change, not
  execution order, so the decisions the user is most likely to change are reviewed
  first, each with alternatives. Use on "plan this", "make a plan", "tweakable plan".
  Not native plan mode: a reviewable document before the work starts. Clear to both: no
  skill or method; if weighty (ships, is sent, hard to undo), first read back request,
  assumptions and what done means in 2–3 lines; a mismatch goes to teach-me, interview
  or blindspot.
---

# Tweakable Plan — sorted by tweak likelihood

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

A plan's purpose is to **pull the points where the user would intervene forward**, not to list steps in execution order. Even if the user stops reading partway down, they have already seen every decision that matters. The plan ends at the user's approval or change requests; the work starts from the approved plan.

## Iron Rules

1. **Execution order ≠ presentation order.** Present by tweak likelihood; execution order appears only as a number on each item.
2. Every decision carries **considered alternatives** — a decision without alternatives cannot be reviewed.

## Procedure

1. Confirm the spec from the text the user gave with the request or after the skill name plus the conversation context (blindspot findings, interview decisions).

   a. With no argument, that context is the whole input.

   b. When the spec has big gaps, suggest the **interview** skill before planning.
2. **Done criteria first**: the document opens with one line stating the purpose (the outcome the user is after), the done criteria, what already works and must not break, and the allowed cost and change scope, filled from context (quote the **unknowns-loop** skill's step 2 when it ran). Write "not set" for any part the context does not give, and ask the user for it in the same reply. Without done criteria, nobody can judge whether the work conforms.

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.
3. **Size gate**: when the work holds no decision the user might want to change (in code, e.g. ≤2 files and no schema, interface or UX-contract decision; elsewhere, e.g. one step with a fixed format, date and budget), say it needs no tweakable plan (for code, it suits native plan mode), and reply with only the done-criteria line, its questions from step 2, and the steps in execution order, one line each: work this small has no decision worth a review document, and a shortened copy of the document is still the document.
4. Split work into items of two kinds:

   | Item type | Covers | Trait |
   |---|---|---|
   | **Decision items** | what other parts build on, e.g. in code: schema/data model, public interfaces (API, types), UX contracts, dependency choices, migration approach; elsewhere: format, venue, method, budget split, who is involved | high blast radius if changed |
   | **Mechanical items** | e.g. CRUD, wiring and boilerplate in code; bookings, mailings and formatting elsewhere | follow automatically once the decisions are set |
5. Order and fill the decision items.

   a. **Sort decision items by tweak likelihood × blast radius** and place them first, ahead of the mechanical items.

   b. Give every decision item, the last as fully as the first, these labeled lines: chosen option / alternatives considered + why rejected / scope affected if this decision changes / **verification method** / **what breaks if this is wrong**. A decision missing a line cannot be reviewed on that line.

   c. Render the central artifact others build on as an **annotated artifact**: every new or changed public type or schema as annotated code in code work; otherwise the budget table, run sheet, survey instrument or outline itself. Add numbered notes, one per choice worth arguing with, each naming the alternative it beat.
6. Put mechanical items at the back, each with a 1-line summary and its verification, and the details below them.
7. Flag the weakest part, then close.

   a. Flag the **weakest part of this plan** (the decision resting on the thinnest evidence).

   b. Close with **2–3 pre-written reply lines**: the highest-leverage tweaks, ready to copy, edit, and send.

## Output

Each numbered decision item lists lettered alternatives and asks for **approve / request-change**; selections assemble into a reply like "item 3 → alternative B, rest approved", with mechanical work after the decisions; a missing pick is undecided.
