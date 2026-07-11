---
name: loop
description: >
  Know-your-unknowns operating loop — orchestrate the full explore → question →
  prototype → plan → implement-with-notes → verify → quiz → value-check workflow for
  significant or ambiguous work. This skill should be used when the user says "unknowns
  loop", "know your unknowns", "운영 루프로 진행", "풀 루프로 해줘", "field guide"/"필드
  가이드"(legacy name), or starts a substantial/ambiguous feature and wants the whole
  methodology applied end to end. NOT for running a prompt repeatedly on an
  interval/schedule or polling — a bare "loop"/"루프 돌려줘" without the unknowns
  context likely means a generic recurring-task runner, not this skill. For a single
  technique, use the individual skills instead (blindspot, teach-me, interview,
  prototypes, brainstorm, reference, plan, notes, quiz, buy-in).
argument-hint: "<task description>"
---

# Unknowns Loop — operating loop for working with strong models

Core principle: **the bottleneck with strong models is not the model — it's the
user's ability to keep the map (plan) matched to the territory (reality). That gap
is the unknowns.** Designing the explore → question → plan → implement → log
deviations → verify loop matters more than one good prompt.
Background and source: see `references/talk-source.md`.

Deliverable principle: any deliverable the user must **see and react to**
(investigation results, mockups, plans, buy-in docs) is built as single-file
interactive HTML with reaction-assembly UI when possible. No viewer available →
fall back to markdown with same structure.

## Steps (default 10 — scale down by size)

### 1. Define value & done criteria
Fix with user before starting: purpose / value to user / done criteria /
existing behavior that must never break / allowed cost & change scope.
**Without success criteria, implementation volume gets mistaken for progress.**

### 2. Blind-spot investigation → `/unknowns:blindspot`
Investigate only, no implementation. Find unknown unknowns, conflict points,
regression risks; produce improved prompt. If the **domain itself** is unfamiliar
(requests vague because terms unknown), run `/unknowns:teach-me` alongside.

### 3. Interview → `/unknowns:interview`
Architecture-changing questions first, max 5 per round.

### 4. Explore solutions & shape (as needed)
- **What to do** undecided → `/unknowns:brainstorm` (solution-space map)
- Can't describe **what it should look like** in words → `/unknowns:prototypes` (divergent mockups)
- Has **example to emulate** → `/unknowns:reference` (reference analysis)

### 5. Risky-assumption prototype (as needed)
Before full implementation, build **minimal prototype verifying only the most
uncertain technical assumption**. State the assumption and success/failure
criteria first.

### 6. Plan → `/unknowns:plan`
Tweakable plan sorted by **probability of revision**, not execution order.
Decisions needing user input (schema, interfaces, UX contracts) go on top.

### 7. Implement + deviation log → apply `/unknowns:notes` rules
Log anything not in the plan; stop and ask on decisions touching architecture,
user-visible behavior, data, or security.

### 8. Independent verification → **independent-reviewer agent**
Run separate review that does not trust the implementer's account. Separate
implementation and review contexts when possible (using the agent is the separation).

### 9. Comprehension check & handoff → `/unknowns:quiz`
Verify user can explain this work in a PR or handoff. If the work needs reviewer
or stakeholder **approval**, also produce a `/unknowns:buy-in` doc.

### 10. Value review
Judge by real value, not code quality: whose problem shrank and which / how much
faster / reasons it might go unused / metrics / removal condition. **Building is
easier, generating value is still hard.**

## Scale-down criteria

- **Small fix** (1–2 files, clear spec): step-7 rules (notes) only — no loop needed.
- **Medium work**: 2 → 3 → 6 → 7 → 9.
- **Large or unfamiliar work**: full 10 steps.
- Unsure → ask user which level to run.

## Operating principles (compressed)

1. Define purpose. 2. Find blind spots before implementing. 3. Make the model ask
questions. 4. Give references and prototypes instead of words. 5. Sort plans by
probability of revision. 6. Log unknowns and plan deviations. 7. Verify with tests
and independent review. 8. Confirm user can explain the result. 9. Deliverables in
reactable form. 10. Measure real value, not code volume.
