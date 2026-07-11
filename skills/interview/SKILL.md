---
name: interview
description: >
  Pre-implementation interview — the model interviews the user to convert known
  unknowns into decisions. This skill should be used when the user says "interview me",
  "인터뷰해줘", "질문해줘" (before implementation), "ask me questions about the spec",
  "스펙 질문", or when requirements are visibly incomplete and implementation has not
  started yet. Prioritize architecture-changing questions first.
argument-hint: "[task/spec description] [priority hint]"
---

# Interview — Pre-Implementation Interview

Requirements incomplete? Don't implement yet — **model interviews user**.
Source: Thariq Shihipar — more context in questions is better. Especially
"prioritize questions that would change the architecture."

## Question Priority (fixed)

1. Questions whose answer **changes the whole architecture**
2. Questions that could cause **data loss / security problems**
3. **Compatibility with external APIs / existing code**
4. Questions affecting **performance / operating cost**
5. UI taste, minor implementation details (last)

## Procedure

1. From `$ARGUMENTS` and conversation context, list spec gaps (known unknowns).
2. Ask **max 5 questions per round**, in priority order. Attach a
   **one-line reason why it matters** to each question.
3. If AskUserQuestion tool available, use it for multiple-choice questions. Give each
   option a short consequence (tradeoff) note.
4. On answers: re-present decisions as an **updated spec summary**; if undecided
   items remain, propose next round.
5. If user wants a deep interview (e.g. "40-question level"), repeat rounds while
   keeping architecture → data → compatibility → performance → taste order.

## Final Deliverables

When interview ends, present two things (deliverables from the original "The Interview"):

1. **Decision table** — question / decision / rationale / left undecided.
2. **Ready-to-use implementation prompt** — complete instruction with all decisions
   applied. User copying this to start implementation is the skill's purpose.

## Never

- Ask questions already answered in conversation/codebase (investigate first).
- Start from priority 5 (taste).
- Start implementing on guesses without the interview.
