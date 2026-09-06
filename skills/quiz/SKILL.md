---
name: quiz
description: >
  Post-work comprehension quiz — explain what changed, then quiz the user so they can
  represent the work in a PR or handoff. Use when the user says "quiz me",
  "test my understanding", "퀴즈", "내가 이해했는지 확인해줘", or right before
  creating or merging a PR for work the model largely implemented.
argument-hint: "[target work/PR scope]"
---

# Quiz — Post-Work Comprehension Check (Stay in the Loop)

Even delegated work, **user must be able to explain the result**.
Origin: Quiz Me Before I Merge — see skills/loop/references/talk-source.md.

## Procedure — Part 1: Explain First

Before quiz, explain concisely — anchor each explained behavior with **Where: file:line**:

1. **Overall structure** of changes (what created/changed, where)
2. **Top 3 design decisions** and why
3. **Most likely failure points** (if wrong, where does it surface first)
4. What **user must verify themselves** (what model cannot guarantee)

## Procedure — Part 2: Six-Question Gate

1. Ask **6 questions**; pass = **all 6 correct**. AskUserQuestion takes at most 4
   questions per call, so split the round into 4 + 2.
2. Question priority: **incident response** ("X dies — where do you look first") >
   **design rationale** ("why B, not A") > **behavior prediction** ("given this input, what result") >
   rote recall (avoid). Not trivia — each is a call the user would have to make right
   during an incident or a review.
3. Grade answers. Each wrong or blank one names the **exact change site (file:line)**
   to re-read; re-explain only those parts, then offer a retry.
4. If IMPLEMENTATION_NOTES.md exists, include at least 1 quiz question on its recorded deviations.
5. At 6/6 emit the **cleared to merge** checklist: understanding verified (6/6), CI
   green, migration/rollout reviewed, merge style, what to watch after deploy.
   Below 6/6 the doc stays "not yet" — list the sections to re-read.

## Output

Ladder: Artifact tool → `.unknowns/<YYYY-MM-DD>-quiz-<slug>.html` → markdown, same structure.
Reaction control = answer buttons per question, key embedded so the page self-grades and
a wrong answer scrolls to the change site; assembles into the cleared-to-merge checklist
plus a copyable answers + score + missed-sections block the user pastes back, which
step 3 and the wrap-up then run on.
Details: skills/loop/references/output-routing.md

## Wrap-Up: Handoff Summary

After quiz, present handoff summary — assume another dev takes over tomorrow:
structure summary / key decisions / how to run & test / incident check order / remaining risks.
If user wants, convert to PR body draft; if work needs reviewer approval,
suggest writing a `/unknowns:buy-in` (or `/buy-in` for copied installs) doc.
