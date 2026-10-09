---
name: quiz
description: >
  Post-work comprehension quiz — explain what changed, then quiz the user so they can
  represent the work in a PR or handoff. Use when the user says "quiz me",
  "test my understanding", or right before
  creating or merging a PR for work the model largely implemented.
argument-hint: "[target work/PR scope]"
---

# Quiz — Post-Work Comprehension Check (Stay in the Loop)

Even when the work was delegated, **the user must be able to explain the result**.

## Procedure — Part 1: Explain First

Before the quiz, explain concisely, anchoring each explained behavior with **Where: file:line**:

1. **Overall structure** of the changes (what was created/changed, where)
2. **Top 3 design decisions** and why
3. **Most likely failure points** (if something is wrong, where it surfaces first)
4. What the **user must verify themselves** (what the model cannot guarantee)

## Procedure — Part 2: Six-Question Gate

1. Ask **6 questions**; pass = **all 6 correct**.

   a. Five are multiple choice. AskUserQuestion takes at most 4 per call, so ask 4 + 1.

   b. The sixth is a **teach-back** in plain text, not a choice: "Explain to a reviewer, in your own words, <the change's riskiest decision>."

   c. Commit to the 2–3 points (and change sites) a correct teach-back explanation must mention **before** reading the answer: write them to `.unknowns/<YYYY-MM-DD>-quiz-<slug>-key.md` before asking.

   d. Grade the teach-back against those points, and quote the key file when grading. Nothing writable → grade anyway, and say in the grading message that the points were not committed in advance.

   Picking the right option only shows recognition; saying it unprompted is what the user will have to do in the PR. Writing the key file before asking and quoting it when grading makes the key provably predate the answer.
2. Question priority, highest first:

   | Priority | Question type | Example |
   |---|---|---|
   | 1 | incident response | "X dies — where do you look first" |
   | 2 | design rationale | "why B, not A" |
   | 3 | behavior prediction | "given this input, what result" |
   | — | rote recall | avoid |

   No trivia: each question is a call the user would have to make right during an incident or a review.
3. Grade answers.

   a. For each wrong or blank answer, name the **exact change site (file:line)** to re-read.

   b. Re-explain only those parts, then offer a retry.
4. If a deviation log exists — the `IMPLEMENTATION_NOTES.md` file, or the log restated in this conversation — include at least 1 quiz question on its recorded deviations.
5. Close the gate by score:

   | Score | What to do |
   |---|---|
   | 6/6 | Emit the **cleared to merge** checklist below. |
   | Below 6/6 | The doc stays "not yet" — list the sections to re-read. |

   The cleared-to-merge checklist:
   - quiz passed (6/6 — say "self-graded" when the page graded it and the user reported the score)
   - CI green
   - migration/rollout reviewed
   - merge style
   - what to watch after deploy

## Output

Ladder: Artifact tool → `.unknowns/<YYYY-MM-DD>-quiz-<slug>.html` → markdown, same structure.

Reaction controls per question type:

| Question | Reaction control | Key | Graded |
|---|---|---|---|
| Multiple choice | answer buttons | embedded, so the page self-grades and a wrong answer scrolls to the change site | on the page |
| Teach-back | a text box | **no key on the page** | in the conversation |

The reaction controls assemble into the cleared-to-merge checklist plus a copyable answers + teach-back + score + missed-sections block the user pastes back, which step 3 and the wrap-up then run on.

Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Wrap-Up: Handoff Summary

After the quiz, present a handoff summary, assuming another dev takes over tomorrow: structure summary / key decisions / how to run & test / incident check order / remaining risks.

- If the user wants, convert the handoff summary to a PR body draft.
- If the work needs reviewer approval, suggest writing a **buy-in** doc.

Then capture one scorecard row, unless the **loop** skill's value review already captured one for this work:

1. Ask whether this work surfaced something the user did not know, and whether it changed a decision.
2. Append the row to `.unknowns/scorecard.md`.

Never answer those two questions for the user; write the row even when both answers are no.

Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/scorecard.md
