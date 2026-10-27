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

Without a tool, do the step in the conversation and say what could not be checked.

## Procedure — Part 2: Six-Question Gate

1. Prepare **6 questions**; pass = **all 6 correct**.

   Question priority, highest first:

   | Priority | Question type | Example |
   |---|---|---|
   | 1 | incident response | "X dies — where do you look first" |
   | 2 | design rationale | "why B, not A" |
   | 3 | behavior prediction | "given this input, what result" |
   | — | rote recall | avoid |

   Each question is a call the user would have to make right during an incident or a review, not trivia.

   If a deviation log exists — the `IMPLEMENTATION_NOTES.md` file, or the log restated in this conversation — include at least 1 quiz question on its recorded deviations.

   a. Five are multiple choice. Keep answer keys hidden until the user has answered: format every option the same way, with no bold, tick or other mark on the correct one. Give every option of a question similar length and detail, so the key cannot be read from the options' form: when the correct option carries a cause, a consequence or a remedy, give each distractor one too.

   b. The sixth is a **teach-back** in plain text, not a choice: "Explain to a reviewer, in your own words, <the change's riskiest decision>."

   c. Commit to the 2–3 points (and change sites) a correct teach-back explanation must mention **before** reading the answer: write them to `.unknowns/<YYYY-MM-DD>-quiz-<slug>-key.md` before asking. Keep the key out of the questions and reply until the user has answered.

   Picking the right option only shows recognition; saying it unprompted is what the user will have to do in the PR. Writing the key file before asking and quoting it when grading makes the key provably predate the answer.

2. Ask the prepared questions. Ask the five multiple-choice questions as 4 + 1, splitting a batch across calls when the question tool accepts fewer questions. Ask the teach-back separately in plain text.
3. Grade answers.

   a. Grade the teach-back against those points, and quote the key file when grading.

   b. For each wrong or blank answer, name the **exact change site (file:line)** to re-read. If the change site is unavailable, mark it unverified.

4. For each wrong or blank answer, re-explain only those parts, then offer a retry: one new question of the same type on each missed part only, prepared, asked and graded by the rules of steps 1–3, not a new six-question set. A retry that gets every missed part right brings the score to 6/6.
5. Close the gate by score:

   | Score | What to do |
   |---|---|
   | 6/6 | Passed. When the work needs reviewer approval, suggest the **buy-in** skill. |
   | Below 6/6 | The result stays "not yet" — list the sections to re-read and offer the retry from step 4. |

## Output

Answers per question type:

| Question | Reply | Key | Graded |
|---|---|---|---|
| Multiple choice | numbered options | hidden until the user answers | in the conversation, with the change site to re-read for each wrong answer |
| Teach-back | the user's own words | hidden until the user answers | in the conversation, against the preselected 2–3 points |

After grading in step 3, assemble the answers + teach-back + score + missed-sections block as copyable text.
