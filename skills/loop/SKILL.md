---
name: loop
description: >
  Run the know-your-unknowns workflow end to end (explore → question → plan →
  implement → verify → quiz) on significant or ambiguous work. Use on "unknowns loop",
  "run the operating loop", "know your unknowns".
  A bare "loop" means the built-in interval runner, not this skill.
---

# Unknowns Loop — operating loop for working with strong models

Core principle: the bottleneck with strong models is not the model — it's the user's ability to keep the map (plan) matched to the territory (reality). That gap is **the unknowns**. Designing the explore → question → plan → implement → log deviations → verify loop matters more than one good prompt.

Deliver Markdown in the conversation with the same structure. End the turn with the assembled reply as Markdown in the conversation.

Each stage keeps its own skill's numbered reactions; the loop's own reaction is the stage checkpoint, whose answer updates the `.unknowns/loop.json` tracker. For numbered reactions and reply assembly, read references/output-routing.md.

## Steps (10 — scale down by size)

### 1. Define value & done criteria

Fix these with the user before starting:

- purpose
- value to user
- done criteria
- existing behavior that must never break
- allowed cost & change scope

Without done criteria, implementation volume gets mistaken for progress.

Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

### 2. Blind-spot investigation → the **blindspot** skill

Investigate only, no implementation.

a. Find unknown unknowns, conflict points and regression risks; produce an improved prompt.

b. If the domain itself is unfamiliar (requests are vague because the terms are unknown), run the **teach-me** skill before the blindspot pass; otherwise hand blindspot's ③ list to teach-me afterwards.

### 3. Interview → the **interview** skill

Architecture-changing questions first, max 4 per round.

### 4. Explore solutions & shape (as needed)

| When | Run | It gives |
|---|---|---|
| What to do is undecided | the **brainstorm** skill | solution-space map |
| Can't describe what it should look like in words | the **prototypes** skill | divergent mockups |
| Has an example to emulate | the **reference** skill | reference analysis |

### 5. Risky-assumption prototype (as needed)

a. State the most uncertain technical assumption and the prototype's success/failure criteria.

b. Before full implementation, build a **minimal prototype that verifies only that assumption**.

No file system → show the prototype code and success/failure criteria in Markdown for the user to save and run. No execution tool → ask the user to run the probe and supply its output; keep the assumption unverified until evidence arrives.

### 6. Plan → the **plan** skill

- Write a tweakable plan sorted by **probability of revision**, not execution order.
- Decisions needing user input (schema, interfaces, UX contracts) go on top.
- The plan's done-criteria section quotes step 1 — do not ask those questions again.

### 7. Implement + deviation log → apply the **notes** skill rules

a. Log anything not in the plan. When work departs from the plan, append the deviation to IMPLEMENTATION_NOTES.md before ending the turn. Check for deviations at each stage boundary. Apply the **notes** skill's logging criteria and escalation rules.

b. Stop and ask before changes to architecture, user-visible behavior, data, or security.

c. Everything else inside this stage: keep going. Put status notes in the same message as the next action, and do not stop to report a finished plan item or offer to continue. The stage checkpoint is where the user steers.

d. If the conversation was compacted, re-invoke the **notes** skill (and this skill for the step list) before continuing implementation.

No skill-loading tool → apply the logging criteria and escalation rules stated here: log design, behavior, or compatibility decisions and differences from the plan; skip trivial syntax, formatting, and naming changes. No file system → print the record in the chat as Markdown and say to save it as IMPLEMENTATION_NOTES.md; show proposed code as Markdown code blocks for the user to save and do not claim the code was applied. No execution tool → give verification commands and mark the result unverified until the user supplies evidence.

### 8. Independent verification → `unknowns:independent-reviewer` agent

a. Use `unknowns:independent-reviewer` when the host can start a sub-agent of that name. Start a fresh context that does not inherit the implementer's narrative.

b. Hand the agent this packet:

- done criteria (step 1 / the plan's done-criteria section)
- the approved plan (step 6)
- the `IMPLEMENTATION_NOTES.md` path
- the diff range / touched files
- how to run the tests
- a list of the **claims** the work rests on (facts about APIs, data or the domain, and reasoning the design depends on), for the reviewer's claim-type check

c. **Never hand it the implementer's own summary.**

Keep the review read-only: never edit or commit repository files or write outside a temporary directory. Check plan/spec conformance, recorded deviations, tests-pass-but-reality-fails cases, verified OK areas, and factual and reasoning claims against their evidence. Run available tests, lint and builds only when they can obey that read-only contract; report checks you cannot run.

No sub-agent → hand the user the same packet to paste into a new conversation, and say that review stands in for the agent. The independent verification stage stays pending until that review returns. Use the same read-only contract. Details: references/surfaces.md

### 9. Comprehension check & handoff → the **quiz** skill

a. Verify the user can explain this work in a PR or handoff.

b. If the work needs reviewer or stakeholder **approval**, also run the **buy-in** skill.

### 10. Value review

a. Judge by real value, not code quality:

- whose problem shrank, and which one
- how much faster
- reasons it might go unused
- metrics
- removal condition

b. Fix, with the user, **how the result will be checked in reality** (what to look at) and **when** (a date they choose — there is no default, it depends on the work).

c. Close by capturing one scorecard row: ask the user whether this surfaced something they did not know and whether it changed a decision, then append the row to `.unknowns/scorecard.md`. Never answer those two questions for the user; write the row even when both answers are no. Details: references/scorecard.md

No file system → print the record in the chat as Markdown and say to save it as `.unknowns/scorecard.md`.

Building is easier, generating value is still hard.

## Scale-down criteria

| Tier | Steps |
|---|---|
| **Small fix** (1–2 files, clear spec) | Step 1 in one line (the done criteria, stated, not asked) plus the step-7 rules (notes) — no tracker, no checkpoints. |
| **Medium work** | 1 (one exchange) → 2 → 3 → 6 → 7 → 9 |
| **Large or unfamiliar work** | All steps, with 4 and 5 only as needed. |

Step 1 runs in every tier — for a small fix as that one line.

Unsure which tier → ask the user, then record the choice.

## Loop status (survives compaction, /resume, new sessions)

For medium and large work, apply the tracker and checkpoint rules in this section; small fixes have neither.

Keep `.unknowns/loop.json` — `{task, tier, stage, status, baseline, decisions[], artifacts[]}` — and rewrite it at every stage boundary. Keep every field on each rewrite.

**Write it first when the loop starts**, with `status: "active"`, before step 1's exchange — a compaction inside the first stage should still find it.

| `status` | Set when |
|---|---|
| `active` | The loop starts and while it runs; `resume`, or the user confirming an old tracker is unfinished, sets it back to `active` |
| `done` | After the loop's last step |
| `stopped` | The user chooses stop; also a confirmed "no" to resuming an `active` tracker (see No argument below) |

At each stage boundary, state the task, tier, stage, and status in the conversation. When work departs from the plan, append the deviation to IMPLEMENTATION_NOTES.md before ending the turn. After compaction or on resume, read the tracker before continuing; no automatic reminder restores the loop for you.

Close each stage with one question-tool checkpoint (continue / skip ahead / stop) and record the answer there.

**One stop per boundary.** When a stage skill runs as a **loop** stage, do not ask its own closing offer separately: fold its options into this stage checkpoint as a single question, e.g. "continue with this prompt / edit it first / skip ahead / stop". The stage skills' own closing offers:

| Stage skill | Its own closing offer |
|---|---|
| blindspot, interview, teach-me | proceed / edit / stop |
| plan | approve / revise |
| reference | implement now / revise the map / stop |

Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

No file system → print the record in the chat as Markdown and say to save it as `.unknowns/loop.json`. Include every tracker field, restate the whole tracker at each stage boundary, and use that record for status and resume; references/surfaces.md has the rest.

### Arguments

| Argument | What to do |
|---|---|
| `status` | Read the file; report tier, current stage, steps remaining. |
| `resume` | Read the file, set `status` to `active`, continue from the recorded stage. |
| Any other text | It is the task description. |
| None | See No argument below. |

No argument:

- `.unknowns/loop.json` is `active` → name its task and stage in one line and confirm before resuming. An abandoned loop stays `active` until someone says stop, and a confirmed "no" sets it to `stopped`.
- Otherwise (no file, `done`, `stopped`, or an older file without `status`) → ask for the task first, offering to resume the old one only if the user says it is unfinished.

### On every start

On every start, read `.unknowns/scorecard.md` if it exists. Any row whose recheck date has passed and whose reality check is still empty is raised **before** the new task: ask the user what they saw and fill the cell.

No file system → read the scorecard record supplied in the conversation and print the updated record as Markdown for the user to save as `.unknowns/scorecard.md`. No supplied tracker or scorecard → ask for the saved record when status, resume, or a reality check depends on it; never invent the missing history.

This is the only thing that reads that column; without it the date is a promise nobody keeps.
