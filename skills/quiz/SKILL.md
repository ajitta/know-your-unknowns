---
name: quiz
description: >
  Post-work comprehension quiz — explain what changed, then quiz the user so they can
  represent the work in a PR or handoff. Use when the user says "quiz me",
  "test my understanding", or right before
  creating or merging a PR for work the model largely implemented.
---

# Quiz — Post-Work Comprehension Check (Stay in the Loop)

Even when the work was delegated, **the user must be able to explain the result**.

## Procedure — Part 1: Explain First

Before the quiz, explain concisely, anchoring each explained behavior with **Where: file:line**:

1. **Overall structure** of the changes (what was created/changed, where)
2. **Top 3 design decisions** and why
3. **Most likely failure points** (if something is wrong, where it surfaces first)
4. What the **user must verify themselves** (what the model cannot guarantee)

No file access → use the supplied diff, code excerpts, and deviation log. Ask for missing material before quizzing on it, and mark unavailable change sites unverified rather than inventing `file:line` references.

## Procedure — Part 2: Six-Question Gate

1. Prepare **6 questions**; pass = **all 6 correct**.

   Question priority, highest first:

   | Priority | Question type | Example |
   |---|---|---|
   | 1 | incident response | "X dies — where do you look first" |
   | 2 | design rationale | "why B, not A" |
   | 3 | behavior prediction | "given this input, what result" |
   | — | rote recall | avoid |

   No trivia: each question is a call the user would have to make right during an incident or a review.

   If a deviation log exists — the `IMPLEMENTATION_NOTES.md` file, or the log restated in this conversation — include at least 1 quiz question on its recorded deviations.

   a. Five are multiple choice. Keep answer keys hidden until the user has answered.

   b. The sixth is a **teach-back** in plain text, not a choice: "Explain to a reviewer, in your own words, <the change's riskiest decision>."

   c. Commit to the 2–3 points (and change sites) a correct teach-back explanation must mention **before** reading the answer: write them to `.unknowns/<YYYY-MM-DD>-quiz-<slug>-key.md` before asking. Keep the key out of the questions and reply until the user has answered.

   No file system → choose the points before asking without showing them; the key cannot be committed to a file in advance.

   Picking the right option only shows recognition; saying it unprompted is what the user will have to do in the PR. Writing the key file before asking and quoting it when grading makes the key provably predate the answer.

2. Ask the prepared questions. Ask the five multiple-choice questions as 4 + 1, splitting a batch across calls when the question tool accepts fewer questions. Ask the teach-back separately in plain text.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.
3. Grade answers.

   a. Grade the teach-back against those points, and quote the key file when grading. No file system → grade anyway, say in the grading message that the points were not committed to a file in advance, and print the key as Markdown only after the answer, saying to save it as `.unknowns/<YYYY-MM-DD>-quiz-<slug>-key.md`.

   b. For each wrong or blank answer, name the **exact change site (file:line)** to re-read. If the change site is unavailable, mark it unverified instead of inventing a reference.

4. For each wrong or blank answer, re-explain only those parts, then offer a retry.
5. Close the gate by score:

   | Score | What to do |
   |---|---|
   | 6/6 | Emit the **cleared to merge** checklist below. |
   | Below 6/6 | The result stays "not yet" — list the sections to re-read. |

   The cleared-to-merge checklist:
   - quiz passed (6/6, graded in the conversation)
   - CI green
   - migration/rollout reviewed
   - merge style
   - what to watch after deploy

## Output

Deliver Markdown in the conversation, keeping this skill's structure. End the turn with the assembled reply as Markdown in the conversation.

Answers per question type:

| Question | Reply | Key | Graded |
|---|---|---|---|
| Multiple choice | numbered options | hidden until the user answers | in the conversation, with the change site to re-read for each wrong answer |
| Teach-back | the user's own words | hidden until the user answers | in the conversation, against the preselected 2–3 points |

After grading in step 3, assemble the answers + teach-back + score + missed-sections block as copyable text. Include the cleared-to-merge checklist only at 6/6; otherwise keep the "not yet" result and retry. Then run the wrap-up in the same reply; the assembled reply ends with the wrap-up.

For numbered reactions and reply assembly, read references/output-routing.md.

## Wrap-Up: Handoff Summary

After the quiz, present a handoff summary, assuming another dev takes over tomorrow: structure summary / key decisions / how to run & test / incident check order / remaining risks.

- If the user wants, convert the handoff summary to a PR body draft.
- If the work needs reviewer approval, suggest writing a **buy-in** doc.

Then capture one scorecard row:

1. When the **loop** skill's value review already captured a scorecard row for this work, say so and skip the remaining scorecard steps instead of asking again. Otherwise, ask whether this work surfaced something the user did not know, and whether it changed a decision.
2. Append the row to `.unknowns/scorecard.md`.

   No file system → print the record in the chat as Markdown and say to save it as `.unknowns/scorecard.md`.

Never answer those two questions for the user; write the row even when both answers are no.

Details: references/scorecard.md
