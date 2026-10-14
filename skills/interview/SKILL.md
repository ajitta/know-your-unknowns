---
name: interview
description: >
  Pre-implementation interview — the model asks the user the questions that turn
  known unknowns into decisions, biggest blast radius first. Use when the user says
  "interview me", "ask me questions before implementing",
  or requirements are incomplete and implementation has not started.
argument-hint: "[task/spec description] [priority hint]"
---

# Interview — Pre-Implementation Interview

When requirements are incomplete, don't implement yet: **the model interviews the user**.

## Question Priority (blast radius, fixed)

1. Questions whose answer **changes the whole architecture**
2. Questions that could cause **data loss / security problems**
3. **Compatibility with external APIs / existing code**
4. Questions affecting **performance / operating cost**
5. UI taste, minor implementation details (last)

## Procedure

1. Find the gaps.

   a. From `$ARGUMENTS` and conversation context, list spec gaps (known unknowns). No arguments → use the spec under discussion; no spec under discussion either → ask once what to interview about.

   b. When the user has not yet said what they are sure of and what they are assuming, make that the first question of round 1: settled items are not asked again, and stated assumptions become questions of their own.
2. Ask the round.

   a. Ask **max 4 questions per round**, in priority order. The cap is AskUserQuestion's hard cap: 1-4 questions, 2-4 options each.

   b. Attach a **one-line reason why it matters** to each question.
3. When the AskUserQuestion tool is available, use it for multiple-choice questions. Give each option a short consequence (tradeoff) note.
4. After the answers:

   a. On answers, restate the decisions as an **updated spec summary**.

   b. When undecided items remain, propose the next round.

   c. **Ladder once on the load-bearing answers**: an architecture or data answer that came without a reason gets one "why" follow-up at the top of the next round ("what would break for you if it went the other way?"). Follow-ups count toward the round's 4 questions. The reason, not the choice, is what lets a later deviation be judged — the reason fills the decision table's rationale column.
5. When the user wants a deep interview (e.g. "40-question level"), repeat rounds in the same order: architecture → data → compatibility → performance → taste.

## Final Deliverables

When the interview ends, present two things:

1. **Decision table** with the columns radius (architecture / data / ux / polish), question, decision, rationale, left undecided.
2. **Ready-to-use implementation prompt**: a complete instruction with all decisions applied. In the prompt:

   - Mark skipped questions "(unanswered — use your judgment)".
   - Declare the architecture and data decisions **fixed**, with "if anything later conflicts with them, flag it before writing code".
   - Close with "start with a short plan, then implement".

   The skill's purpose is that the user copies this prompt to start implementation.

Then offer in one AskUserQuestion: proceed with this prompt now / let me edit it / stop here. When run as a **loop** stage, do not ask this separately: the loop's stage checkpoint carries these options.

## Iron Rules

- Never ask questions already answered in the conversation or codebase: investigate the conversation and codebase before asking.
- Never start from priority 5 (taste).
- Never start implementing on guesses without the interview.
