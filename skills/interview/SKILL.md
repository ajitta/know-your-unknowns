---
name: interview
description: >
  Pre-implementation interview — the model asks the user the questions that turn
  known unknowns into decisions, biggest blast radius first. Use when the user says
  "interview me", "ask me questions before implementing", "인터뷰해줘", "스펙 질문",
  or requirements are incomplete and implementation has not started.
argument-hint: "[task/spec description] [priority hint]"
---

# Interview — Pre-Implementation Interview

Requirements incomplete? Don't implement yet — **model interviews user**.
Origin: The Interview — see skills/loop/references/talk-source.md.

## Question Priority (blast radius, fixed)

1. Questions whose answer **changes the whole architecture**
2. Questions that could cause **data loss / security problems**
3. **Compatibility with external APIs / existing code**
4. Questions affecting **performance / operating cost**
5. UI taste, minor implementation details (last)

## Procedure

1. From `$ARGUMENTS` and conversation context, list spec gaps (known unknowns).
   No arguments → the spec under discussion; if none, ask once what to interview about.
2. Ask **max 4 questions per round** (AskUserQuestion hard cap: 1-4 questions,
   2-4 options each), in priority order. Attach a **one-line reason why it matters**
   to each question.
3. If AskUserQuestion tool available, use it for multiple-choice questions. Give each
   option a short consequence (tradeoff) note.
4. On answers: re-present decisions as an **updated spec summary**; if undecided
   items remain, propose next round.
5. If user wants a deep interview (e.g. "40-question level"), repeat rounds while
   keeping architecture → data → compatibility → performance → taste order.

## Final Deliverables

When interview ends, present two things:

1. **Decision table** — radius (architecture / data / ux / polish) / question /
   decision / rationale / left undecided.
2. **Ready-to-use implementation prompt** — complete instruction with all decisions
   applied. Mark skipped questions "(unanswered — use your judgment)"; declare the
   architecture and data decisions **fixed**, with "if anything later conflicts with
   them, flag it before writing code"; close with "start with a short plan, then
   implement". User copying this to start implementation is the skill's purpose.

Then offer in one AskUserQuestion: proceed with this prompt now / let me edit it /
stop here.

## Never

- Ask questions already answered in conversation/codebase (investigate first).
- Start from priority 5 (taste).
- Start implementing on guesses without the interview.
