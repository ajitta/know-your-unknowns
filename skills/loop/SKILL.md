---
name: loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan →
  implement → verify → quiz) on significant or ambiguous work. Use on "unknowns loop",
  "run the operating loop", "know your unknowns".
  A bare "loop" means the built-in interval runner, not this skill.
argument-hint: "<task description> | status | resume"
---

# Unknowns Loop — operating loop for working with strong models

Core principle: **the bottleneck with strong models is not the model — it's the
user's ability to keep the map (plan) matched to the territory (reality). That gap
is the unknowns.** Designing the explore → question → plan → implement → log
deviations → verify loop matters more than one good prompt.
Origin: the 11 "Know your unknowns" examples; the loop itself is a plugin extension —
see ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/talk-source.md.

Output: Artifact tool → `.unknowns/<YYYY-MM-DD>-loop-<slug>.html` → markdown.
Each stage's artifact keeps its own skill's reaction control; the loop's own control is the
per-stage checkpoint, which assembles into the `.unknowns/loop.json` tracker.
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Steps (10 — scale down by size)

### 1. Define value & done criteria
Fix with user before starting: purpose / value to user / done criteria /
existing behavior that must never break / allowed cost & change scope.
**Without success criteria, implementation volume gets mistaken for progress.**

### 2. Blind-spot investigation → the **blindspot** skill
Investigate only, no implementation. Find unknown unknowns, conflict points,
regression risks; produce improved prompt. If the **domain itself** is unfamiliar
(requests vague because terms unknown), run the **teach-me** skill alongside.

### 3. Interview → the **interview** skill
Architecture-changing questions first, max 4 per round.

### 4. Explore solutions & shape (as needed)
- **What to do** undecided → the **brainstorm** skill (solution-space map)
- Can't describe **what it should look like** in words → the **prototypes** skill (divergent mockups)
- Has **example to emulate** → the **reference** skill (reference analysis)

### 5. Risky-assumption prototype (as needed)
Before full implementation, build **minimal prototype verifying only the most
uncertain technical assumption**. State the assumption and success/failure
criteria first.

### 6. Plan → the **plan** skill
Tweakable plan sorted by **probability of revision**, not execution order.
Decisions needing user input (schema, interfaces, UX contracts) go on top.
The plan's done-criteria section quotes step 1 — do not ask those questions again.

### 7. Implement + deviation log → apply the **notes** skill rules
Log anything not in the plan; stop and ask on decisions touching architecture,
user-visible behavior, data, or security. Everything else inside this stage: keep going —
put status notes in the same message as the next action, and do not stop to report a
finished plan item or offer to continue. The stage-boundary checkpoint is where the user
steers. If the conversation was compacted, re-invoke
the **notes** skill (and this skill for the step list) before continuing implementation.

### 8. Independent verification → `unknowns:independent-reviewer` agent
Spawn it with the Agent tool (`subagent_type: unknowns:independent-reviewer`). **Never a
fork or `/subtask`** — those inherit the implementer's context, which is the one thing
this step exists to exclude. Hand the agent: done criteria (step 1 / the plan's done-criteria section), the approved plan
(step 6), the `IMPLEMENTATION_NOTES.md` path, the diff range / touched files, how to
run the tests, and a list of the **claims** the work rests on (facts about APIs, data or
the domain, and reasoning the design depends on) for the reviewer's claim-type check. **Never hand it the implementer's own summary.**
No Agent tool in this session (Desktop/web chat, mobile) → hand the user that same packet
to paste into a **new conversation**, and say the review is standing in for the agent.
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/surfaces.md

### 9. Comprehension check & handoff → the **quiz** skill
Verify user can explain this work in a PR or handoff. If the work needs reviewer
or stakeholder **approval**, also run the **buy-in** skill.

### 10. Value review
Judge by real value, not code quality: whose problem shrank and which / how much
faster / reasons it might go unused / metrics / removal condition. **Building is
easier, generating value is still hard.**
Also fix, with the user, **how the result will be checked in reality** (what to look at)
and **when** (a date they choose — there is no default, it depends on the work).
Close by capturing one scorecard row — ask the user whether this surfaced something they
did not know and whether it changed a decision, then append the row to
`.unknowns/scorecard.md`. Never answer those two for them, and write the row even when
both answers are no. Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/scorecard.md

## Scale-down criteria

- **Small fix** (1–2 files, clear spec): step 1 in one line (the done criteria, stated, not
  asked) plus the step-7 rules (notes) — no tracker, no checkpoints.
- **Medium work**: 1 (one exchange) → 2 → 3 → 6 → 7 → 9.
- **Large or unfamiliar work**: all steps, with 4 and 5 only as needed.
- Step 1 runs in every tier — for a small fix as that one line. Unsure which tier → ask
  the user, then record the choice.

## Loop status (survives compaction, /resume, new sessions)

Keep `.unknowns/loop.json` — `{task, tier, stage, status, baseline, decisions[], artifacts[]}` — and
rewrite it at every stage boundary. **Write it first when the loop starts**, with
`status: "active"`, before step 1's exchange — a compaction inside the first stage should
still find it. `status` is `active` while the loop runs, `done` after its last step,
`stopped` when the user chooses stop; `resume` (or the user confirming an old tracker is
unfinished) sets it back to `active`. Keep every field on each rewrite. The plugin's
compaction hook points back at the loop only while it is `active`, so a running loop must
say so and a finished one must not. Close each stage with one AskUserQuestion checkpoint
(continue / skip ahead / stop) and record the answer there. **One stop per boundary**:
a stage skill's own closing offer (blindspot, interview, teach-me: proceed / edit / stop;
plan and reference: approve / revise) is not asked separately — fold its options into this
checkpoint as a single question, e.g. "continue with this prompt / edit it first / skip
ahead / stop". No AskUserQuestion tool → ask
the same three options as a numbered question and wait for the answer.
Nowhere durable to write the tracker (chat sessions, mobile) → restate the whole tracker
as a fenced JSON block at each stage boundary, so the newest message always holds it;
${CLAUDE_PLUGIN_ROOT}/skills/loop/references/surfaces.md has the rest.

- Argument `status`: read the file; report tier, current stage, steps remaining.
- Argument `resume`: read the file, set `status` to `active`, continue from the recorded stage.
- Any other argument text is the task description.
- No argument: if `.unknowns/loop.json` is `active`, name its task and stage in one line and
  confirm before resuming — an abandoned loop stays `active` until someone says stop, and a
  confirmed "no" sets it to `stopped`. Otherwise (no file,
  `done`, `stopped`, or an older file without `status`) ask for the task first — offering to
  resume the old one only if the user says it is unfinished.
- On every start, read `.unknowns/scorecard.md` if it exists. Any row whose recheck date has
  passed and whose reality check is still empty is raised **before** the new task: ask
  the user what they saw and fill the cell. This is the only thing that reads that column;
  without it the date is a promise nobody keeps.

## Operating principles (compressed)

1. Define purpose. 2. Find blind spots before implementing. 3. Make the model ask
questions. 4. Give references and prototypes instead of words. 5. Sort plans by
probability of revision. 6. Log unknowns and plan deviations. 7. Verify with tests
and independent review. 8. Confirm user can explain the result. 9. Deliverables in
reactable form. 10. Measure real value, not code volume.
