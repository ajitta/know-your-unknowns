---
name: blindspot
description: >
  Blind-spot pass — investigate unknown unknowns BEFORE implementation. This skill
  should be used when the user says "blind spot pass", "blindspot", "what am I missing",
  "do a blind-spot investigation", "find my unknowns", "unknown unknowns",
  "사각지대 조사해줘", "내가 놓친 게 뭐지", "내가 모르는 게 뭐지", or is about to start
  work in an unfamiliar domain, library, or codebase area and wants to discover what
  they are missing before writing a fuller prompt or spec. Do NOT trigger for routine
  tasks the user clearly understands.
argument-hint: "<task description or target area> [context sources: git/docs/slack etc.]"
---

# Blindspot Pass — Blind-Spot Investigation

Before implementation, find the **gap between the map (plan/prompt) and the territory
(actual codebase, domain, constraints)**.
Original source: Thariq Shihipar — "I'm working on X that I know nothing about. Do a blind-spot
pass to help me figure out my relevant unknown unknowns and help me prompt better."

## Iron Rules

1. **Do not implement yet.** No code changes while this skill is active.
2. End goal of the investigation: help the user **write a better prompt**.

## Procedure

1. Parse task description and context sources from `$ARGUMENTS`. If sources given
   (git history, docs, specific modules, etc.), investigate those first.
2. Scope codebase-wide or large → delegate to **unknowns-scout agent**.
   Scope is a few files → investigate directly with Read/Grep/Glob.
3. Compile these 6:
   - **Assumptions** the user is likely missing
   - Expected **unknown unknowns** (decision points absent from the plan)
   - **Potential conflicts** with existing structure/conventions
   - **Regression-prone areas** if changed (incl. test coverage)
   - **Questions to answer** before implementation
   - **Information needed** to sharpen the prompt
4. Present sorted by **importance × impact**.
5. End with an **improved prompt draft** reflecting the findings — the core
   deliverable of this skill.
6. If undecided items that could change architecture surface, suggest continuing
   with `/unknowns:interview`. If the user lacks the unfamiliar domain's vocabulary
   itself, suggest `/unknowns:teach-me`.

## Output Format (HTML First)

In renderable environments (Cowork, artifact viewer), build a **single-file interactive
HTML**: 1 finding = 1 card (category, finding, why it matters, recommended action), each
card with a copyable **"prompt fix"** button reflecting that finding; selecting cards
**auto-assembles the selected fixes into an improved prompt draft** at the bottom.
Inline CSS/JS, no external dependencies.
Viewer-less CLI environment → fall back to same-structure markdown table + prompt draft.

## Scope

Not limited to code. Applies equally to learning new fields (e.g. color grading,
payments, auth, physics engines) — the model often knows the field better than the
user; the goal is to elicit that.
