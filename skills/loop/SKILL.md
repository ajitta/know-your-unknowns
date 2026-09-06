---
name: loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan →
  implement → verify → quiz) on significant or ambiguous work. Use on "unknowns loop",
  "run the operating loop", "know your unknowns", "운영 루프로 진행", "풀 루프로 해줘".
  A bare "loop"/"루프 돌려줘" means the built-in interval runner.
argument-hint: "<task description> | status | resume"
---

# Unknowns Loop — operating loop for working with strong models

Core principle: **the bottleneck with strong models is not the model — it's the
user's ability to keep the map (plan) matched to the territory (reality). That gap
is the unknowns.** Designing the explore → question → plan → implement → log
deviations → verify loop matters more than one good prompt.
Origin: the 11 "Know your unknowns" examples; the loop itself is a plugin extension —
see skills/loop/references/talk-source.md.

Output: Artifact tool → `.unknowns/<YYYY-MM-DD>-loop-<slug>.html` → markdown.
Each stage's artifact keeps its own skill's reaction control; the loop's own control is the
per-stage checkpoint, which assembles into the `.unknowns/loop.json` tracker.
Details: skills/loop/references/output-routing.md

## Steps (10 — scale down by size)

### 1. Define value & done criteria
Fix with user before starting: purpose / value to user / done criteria /
existing behavior that must never break / allowed cost & change scope.
**Without success criteria, implementation volume gets mistaken for progress.**

### 2. Blind-spot investigation → `/unknowns:blindspot` (or `/blindspot` for copied installs)
Investigate only, no implementation. Find unknown unknowns, conflict points,
regression risks; produce improved prompt. If the **domain itself** is unfamiliar
(requests vague because terms unknown), run `/unknowns:teach-me` alongside.

### 3. Interview → `/unknowns:interview`
Architecture-changing questions first, max 4 per round.

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
user-visible behavior, data, or security. If the conversation was compacted, re-invoke
`/unknowns:notes` (and this skill for the step list) before continuing implementation.

### 8. Independent verification → `unknowns:independent-reviewer` agent
Spawn it with the Agent tool (`subagent_type: unknowns:independent-reviewer`). **Never a
fork or `/subtask`** — those inherit the implementer's context, which is the one thing
this step exists to exclude. Hand the agent: done criteria (step 1), the approved plan
(step 6), the `IMPLEMENTATION_NOTES.md` path, the diff range / touched files, and how to
run the tests. **Never hand it the implementer's own summary.**

### 9. Comprehension check & handoff → `/unknowns:quiz`
Verify user can explain this work in a PR or handoff. If the work needs reviewer
or stakeholder **approval**, also produce a `/unknowns:buy-in` doc.

### 10. Value review
Judge by real value, not code quality: whose problem shrank and which / how much
faster / reasons it might go unused / metrics / removal condition. **Building is
easier, generating value is still hard.**
Close by capturing one scorecard row — ask the user whether this surfaced something they
did not know and whether it changed a decision, then append the row to
`.unknowns/scorecard.md`. Never answer those two for them, and write the row even when
both answers are no. Details: skills/loop/references/scorecard.md

## Scale-down criteria

- **Small fix** (1–2 files, clear spec): step-7 rules (notes) only — no loop needed.
- **Medium work**: 1 (one exchange) → 2 → 3 → 6 → 7 → 9.
- **Large or unfamiliar work**: all steps, with 4 and 5 only as needed.
- Step 1 runs in every tier. Unsure which tier → ask the user, then record the choice.

## Loop status (survives compaction, /resume, new sessions)

Keep `.unknowns/loop.json` — `{task, tier, stage, decisions[], artifacts[]}` — and rewrite
it at every stage boundary. Close each stage with one AskUserQuestion checkpoint
(continue / skip ahead / stop) and record the answer there.

- Argument `status`: read the file; report tier, current stage, steps remaining.
- Argument `resume`: read the file; continue from the recorded stage.
- Any other argument text is the task description.
- No argument: resume `.unknowns/loop.json` if it exists, otherwise ask for the task first.

## Operating principles (compressed)

1. Define purpose. 2. Find blind spots before implementing. 3. Make the model ask
questions. 4. Give references and prototypes instead of words. 5. Sort plans by
probability of revision. 6. Log unknowns and plan deviations. 7. Verify with tests
and independent review. 8. Confirm user can explain the result. 9. Deliverables in
reactable form. 10. Measure real value, not code volume.
