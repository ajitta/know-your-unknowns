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

Even delegated work, **user must be able to explain the result**.
Origin: Quiz Me Before I Merge — see ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/talk-source.md.

## Procedure — Part 1: Explain First

Before quiz, explain concisely — anchor each explained behavior with **Where: file:line**:

1. **Overall structure** of changes (what created/changed, where)
2. **Top 3 design decisions** and why
3. **Most likely failure points** (if wrong, where does it surface first)
4. What **user must verify themselves** (what model cannot guarantee)

## Procedure — Part 2: Six-Question Gate

1. Ask **6 questions**; pass = **all 6 correct**. Five are multiple choice — AskUserQuestion
   takes at most 4 per call, so ask 4 + 1. The sixth is a **teach-back** in plain text, not
   a choice: "Explain to a reviewer, in your own words, <the change's riskiest decision>."
   Picking the right option only shows recognition; saying it unprompted is what the user
   will have to do in the PR. Grade it against the 2–3 points (and change sites) a correct
   explanation must mention, fixed **before** reading the answer.
2. Question priority: **incident response** ("X dies — where do you look first") >
   **design rationale** ("why B, not A") > **behavior prediction** ("given this input, what result") >
   rote recall (avoid). Not trivia — each is a call the user would have to make right
   during an incident or a review.
3. Grade answers. Each wrong or blank one names the **exact change site (file:line)**
   to re-read; re-explain only those parts, then offer a retry.
4. If a deviation log exists — the `IMPLEMENTATION_NOTES.md` file, or the log restated in
   this conversation — include at least 1 quiz question on its recorded deviations.
5. At 6/6 emit the **cleared to merge** checklist: quiz passed (6/6 — say "self-graded"
   when the page graded it and the user reported the score), CI
   green, migration/rollout reviewed, merge style, what to watch after deploy.
   Below 6/6 the doc stays "not yet" — list the sections to re-read.

## Output

Ladder: Artifact tool → `.unknowns/<YYYY-MM-DD>-quiz-<slug>.html` → markdown, same structure.
Reaction control = answer buttons per multiple-choice question, key embedded so the page
self-grades and a wrong answer scrolls to the change site; the teach-back gets a text box
and **no key on the page** — it is graded in the conversation. Assembles into the
cleared-to-merge checklist plus a copyable answers + teach-back + score + missed-sections
block the user pastes back, which step 3 and the wrap-up then run on.
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Wrap-Up: Handoff Summary

After quiz, present handoff summary — assume another dev takes over tomorrow:
structure summary / key decisions / how to run & test / incident check order / remaining risks.
If user wants, convert to PR body draft; if work needs reviewer approval,
suggest writing a **buy-in** doc.

Then capture one scorecard row — ask whether this work surfaced something the user did
not know and whether it changed a decision, and append it to `.unknowns/scorecard.md`.
Never answer those for them; write the row even when both answers are no. Skip it if the
**loop** skill's value review already captured one for this work.
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/scorecard.md
