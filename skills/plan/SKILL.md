---
name: plan
description: >
  The tweakable plan — write implementation plans sorted by likelihood-of-tweaking,
  not by execution order, so the user reviews the decisions most likely to change
  first. This skill should be used when the user says "plan this", "tweakable plan",
  "sort plan by tweak likelihood", "계획 세워줘", "구현 계획", "수정확률순 계획",
  or when a plan is needed after blindspot/interview and before implementation.
argument-hint: "<task description or confirmed spec>"
---

# Plan — The Tweakable Plan (sorted by tweak likelihood)

Plan's purpose: not execution-order listing but **pulling user-intervention points forward**.
Original "The Tweakable Plan": sort roadmap by **likelihood of tweaking**, not execution
order; attach alternatives to schema decisions; fold mechanical work. Even if user tires
reading top-down, they've already seen every decision that matters.

## Iron rules

1. **Execution order ≠ presentation order.** Present by tweak likelihood; execution order
   appears only as a number on each item.
2. Every decision carries **considered alternatives** — a decision without alternatives
   cannot be reviewed.

## Procedure

1. Confirm spec from `$ARGUMENTS` + conversation context (blindspot findings, interview
   decisions). Big gaps → suggest `/unknowns:interview` first.
2. Split work into items, two kinds:
   - **Decision items** — schema/data model, public interfaces (API, types), UX contracts,
     dependency choices, migration approach: high blast radius if changed
   - **Mechanical items** — follow automatically once decisions set (CRUD, wiring,
     boilerplate)
3. **Sort decision items by tweak likelihood × blast radius**, place first. Each item:
   chosen option / alternatives considered + why rejected / scope affected if this decision
   changes / verification method.
4. Mechanical items folded at back (1-line summary + expand).
5. Required for every step: **verification method** / **expected risks** / **rollback method**.
6. Proceed to implementation only after user approval/change requests update the plan.
   Record mid-implementation deviations per `/unknowns:notes` rules.

## Output format (HTML first)

**Single-file interactive HTML** plan: decision items as cards top-down, each card with
**alternative toggle** (chosen ↔ alternative comparison) and **approve / request-change
selection** — selections **auto-assemble at bottom into a copyable reply** like
"item 3 → alternative B, rest approved". Mechanical work as collapsed sections.
Inline CSS/JS, no external dependencies.
No viewer available → fall back to markdown with same ordering principle (decision table
+ collapsed list).
