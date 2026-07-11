---
name: quiz
description: >
  Post-work comprehension quiz — after finishing significant work, explain what changed
  and quiz the user so they stay in the loop and can represent the work in a PR or
  handoff. This skill should be used when the user says "quiz me", "test my understanding",
  "퀴즈", "내가 이해했는지 확인해줘", or right before creating/merging a PR for work the
  model largely implemented.
argument-hint: "[target work/PR scope]"
---

# Quiz — Post-Work Comprehension Check (Stay in the Loop)

Even delegated work, **user must be able to explain the result**. Source: Thariq Shihipar —
"I like to get it to quiz me about what happened, to make sure I understand what I'm
doing and can represent this work when I'm creating a PR or merging it."

## Procedure — Part 1: Explain First

Before quiz, explain concisely:

1. **Overall structure** of changes (what created/changed, where)
2. **Top 3 design decisions** and why
3. **Most likely failure points** (if wrong, where does it surface first)
4. What **user must verify themselves** (what model cannot guarantee)

## Procedure — Part 2: Quiz

1. Ask **5 questions**. If AskUserQuestion tool available, use multiple-choice.
2. Question priority: **incident response** ("X dies — where do you look first") >
   **design rationale** ("why B, not A") > **behavior prediction** ("given this input, what result") >
   rote recall (avoid).
3. Grade answers; re-explain **only the wrong or blank parts** —
   per "Quiz Me Before I Merge", each wrong answer must point to the exact
   change site to re-review.
4. If IMPLEMENTATION_NOTES.md exists, include at least 1 quiz question on its recorded deviations.

## Output Format (HTML Option)

For big pre-merge changes, may build a **merge-readiness report** as single-file HTML:
change summary (per-file collapsible) + quiz UI; wrong answer scrolls to and highlights the relevant change section.
No viewer available: fall back to markdown with same structure.
Normal cases: in-conversation is enough.

## Wrap-Up: Handoff Summary

After quiz, present handoff summary — assume another dev takes over tomorrow:
structure summary / key decisions / how to run & test / incident check order / remaining risks.
If user wants, convert to PR body draft; if work needs reviewer approval,
suggest writing a `/unknowns:buy-in` doc.
