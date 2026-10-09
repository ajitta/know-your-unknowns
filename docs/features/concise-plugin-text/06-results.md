---
status: complete
revised: 2026-10-09
---
# Concise plugin text: measurement results

Plan: [05-plan.md](./05-plan.md). Raw eval output: `evals/results/` (git-ignored). Every eval below ran with `ANTHROPIC_MODEL=claude-sonnet-5-5` and `--arm with`.

## Phase 0: baseline

### Installed plugin state (restore target)

`claude plugin list` before the evals: `unknowns@synced` 0.8.2, `Status: ✔ loaded`.
Disable needs the marketplace-qualified name: `claude plugin disable unknowns` fails with "not found in any editable settings scope"; `claude plugin disable unknowns@synced` works and shows `Status: ✘ disabled`.

### Tests and structural check

- `python -m unittest discover -s tests`: `Ran 127 tests`, `OK (skipped=2)`
- `python evals/run-manual.py --verify`: `33 case(s), 74 grader(s), 0 problem(s)`, exit 0

### behavior-* (6 cases × 3 runs)

`evals/results/baseline-behavior/`. The plan said 5 cases; `--list` finds 6, and all 6 ran. Every run reported `model: claude-sonnet-5-5`.

| Case | Mechanical grader | Pass |
|---|---|---|
| blindspot-ends-with-improved-prompt | fires-unknowns-blindspot | 3/3 |
| | labels-the-prompt-draft | 1/3 |
| blindspot-labels-evidence-status | fires-unknowns-blindspot | 3/3 |
| | uses-status-labels | 3/3 |
| interview-max-four-questions | fires-unknowns-interview | 3/3 |
| | no-fifth-numbered-question | 3/3 |
| notes-appends-to-file | fires-unknowns-notes | 3/3 |
| | creates-implementation-notes-file | 3/3 |
| plan-opens-with-done-criteria | fires-unknowns-plan | 3/3 |
| | names-done-criteria | 3/3 |
| prototypes-asks-contrast-on-skip | fires-unknowns-prototypes | 3/3 |

### blindspot `llm` rubrics, hand-scored from `last_message`

| Rubric | Run 1 | Run 2 | Run 3 | Pass |
|---|---|---|---|---|
| ends-with-a-pasteable-prompt | fail | fail | fail | 0/3 |
| claims-nothing-confirmed-unseen | fail | pass | fail | 1/3 |

Five of the six blindspot runs ended at Step 1's "ask once" question for the three lists. They produced no findings and no prompt, so these rubrics fail on the question itself, not on the quality of a pass. The one full pass (labels run 2) labelled every finding *inferred*, kept code-specific items under **Needs checking**, and ended with an improved prompt draft. `labels-the-prompt-draft` passed once because the run 1 question promises "an improved prompt"; `uses-status-labels` passed 3/3 because every question promises *inferred* labels. A headless run can't answer the question, so these four graders mostly measure whether the model asks first, not the pass itself.

## Phase 0.5: caveman-compress pilot (blindspot body)

Result: **fail**. `skills/blindspot/SKILL.md` was reverted with `git checkout`. Phases 1 to 3 use direct editing.

### Steps 1 and 2: caveman run and its deletions

- Command: `CAVEMAN_COMPRESS_MODEL=claude-sonnet-5-5 python -m scripts <scratchpad copy>`, run from the caveman-compress skill directory. `call_claude_cli` passes this value to `claude` as `--model`.
- caveman validation: `Validation passed` on attempt 1. Frontmatter was preserved verbatim.
- The word diff against the original shows only function words were deleted: `the` ×44, `a` ×13, `an` ×5, `is` ×4, `this` ×3, plus `if ... ,` clause openers that became `→`.
- **Deletions that hit the "keep" list: none.** Every number, term, path, substitution, grader phrase and the loop checkpoint sentence (Step 6) survived. One meaning shift that is not on the list: "② becomes the **first** thing to check, not something to skip" became "not skip".
- caveman also removed nothing from the "trim" list: no duplicate sentence, background explanation or nested clause. Apart from dropping articles, the rewrite in Step 3 was a direct edit.

### Step 4: verification

Proof 1 (frontmatter unchanged), Proof 2 (`Ran 127 tests`, `OK (skipped=2)`) and Proof 3 (`0 problem(s)`) passed. The reviewer check was not run, because the eval had already failed.

The eval gap was one run, so each arm ran 3 more times, 6 runs per arm. The extra baseline runs used the original file, swapped back in for the run. Directories: `baseline-behavior` + `baseline-blindspot-2` against `pilot-blindspot` + `pilot-blindspot-2`. Every run reported `claude-sonnet-5-5`.

| Grader | Baseline | Pilot |
|---|---|---|
| fires-unknowns-blindspot (both cases) | 12/12 | 12/12 |
| labels-the-prompt-draft | 3/6 | **0/6** |
| uses-status-labels | 6/6 | 6/6 |
| ends-with-a-pasteable-prompt (hand) | 0/6 | 0/6 |
| claims-nothing-confirmed-unseen (hand) | 3/6 | 3/6 |

All 3 baseline passes of `labels-the-prompt-draft` were runs that stopped at the three-lists question, and in each one the question promised "an improved prompt" or "the improved prompt draft". No pilot question mentioned the deliverable. The likely cause is the deletion of Step 5's "— the core deliverable of this skill" as a duplicate of Iron Rule 2, combined with the rewording of Iron Rule 2. This is inferred: no run isolated that one sentence.

### Step 5: what changes

- The pipeline is not adopted. caveman added nothing beyond dropping articles, and the rewrite built on it regressed a grader.
- Edit-rule addition from the regression (Step 2's list is empty): sentences that name a skill's deliverable or end goal stay, even when they look like duplicates (for example blindspot Iron Rule 2 and Step 5's "core deliverable" clause).
- Measurement limit for Phase 6: in all 12 runs of `ends-with-improved-prompt` (baseline and pilot), the model stopped at Step 1's question. Four of the six blindspot graders therefore score the question message, not a finished pass.

## Phase 3.5: descriptions

Only the brainstorm description changed. It went from 258 to 275 characters, adding the article before "quarter-long bet" and a verb to "or a problem named with no approach chosen". The other 10 skill descriptions and both agent descriptions already read as complete, clear sentences, so they were left alone.

`evals/results/desc-brainstorm/`, all runs `claude-sonnet-5-5`:

| Case | Pass criterion | Result |
|---|---|---|
| trigger-en-brainstorm | fires 2/3 or more | 3/3 |
| trigger-ko-brainstorm | fires 2/3 or more | 3/3 |
| neg-ui-options-does-not-fire-brainstorm | fires 0/3 | 0/3 (all three fired `unknowns:prototypes`) |

## Phase 6: re-measurement after all edits

- `python -m unittest discover -s tests`: `Ran 127 tests`, `OK (skipped=2)`, same as Phase 0.
- `python evals/run-manual.py --verify`: `33 case(s), 74 grader(s), 0 problem(s)`, exit 0.
- `claude plugin validate . --strict` and `claude plugin validate ./.claude-plugin/plugin.json --strict` fail in the working tree on one warning: `CLAUDE.local.md at the plugin root is not loaded as project context`. That file is a personal, git-ignored file. A clean `git archive HEAD` export passes both commands (`✔ Validation passed`).
- Table separator grep (Proof 6): no output.

### behavior-* (6 cases × 3 runs)

`evals/results/final-behavior/`, plus `final-prototypes-rerun/` for one prototypes run that timed out at 420 s after writing its HTML file (not graded). Every graded run reported `claude-sonnet-5-5`.

| Case | Grader | Baseline (Phase 0) | After |
|---|---|---|---|
| blindspot-ends-with-improved-prompt | fires-unknowns-blindspot | 3/3 | 3/3 |
| | labels-the-prompt-draft | 1/3 (3/6 with the Phase 0.5 extra runs) | 1/3 |
| blindspot-labels-evidence-status | fires-unknowns-blindspot | 3/3 | 3/3 |
| | uses-status-labels | 3/3 | 3/3 |
| interview-max-four-questions | fires-unknowns-interview | 3/3 | 3/3 |
| | no-fifth-numbered-question | 3/3 | 3/3 |
| notes-appends-to-file | fires-unknowns-notes | 3/3 | 3/3 |
| | creates-implementation-notes-file | 3/3 | 3/3 |
| plan-opens-with-done-criteria | fires-unknowns-plan | 3/3 | 3/3 |
| | names-done-criteria | 3/3 | 3/3 |
| prototypes-asks-contrast-on-skip | fires-unknowns-prototypes | 3/3 | 3/3 |

Hand-scored blindspot rubrics:

| Rubric | Baseline | After |
|---|---|---|
| ends-with-a-pasteable-prompt | 0/3 (0/6) | 0/3 |
| claims-nothing-confirmed-unseen | 1/3 (3/6) | 2/3 |

Regressions (a grader down by 2 or more of 3 runs): **none**. As in Phase 0, every `ends-with-improved-prompt` run stopped at Step 1's three-lists question, so those two graders still score the question message, not a finished pass. In both full passes (labels runs 1 and 3), every finding was labelled *inferred*, code-specific items sat under **Needs checking**, and the pass ended with an improved prompt draft.

The installed plugin was re-enabled after the evals: `unknowns@synced` 0.8.2, `Status: ✔ loaded`, the same as the Phase 0 record.
