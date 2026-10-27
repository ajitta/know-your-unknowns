---
name: interview
description: >
  Pre-implementation interview — the model asks the user the questions that turn
  known unknowns into decisions, biggest blast radius first. Use when the user says
  "interview me", "ask me questions before implementing",
  or requirements are incomplete and implementation has not started.
---

# Interview — Pre-Implementation Interview

When requirements are incomplete, **the model interviews the user** before anyone implements.

## Question Priority (blast radius, fixed)

1. Questions whose answer **changes the whole architecture**
2. Questions that could cause **data loss / security problems** (the *data* tier below)
3. **Compatibility with external APIs / existing code**
4. Questions affecting **performance / operating cost**
5. UI taste, minor implementation details (last)

## Procedure

1. Find the gaps.

   a. Investigate the conversation and codebase before listing gaps. From the text the user gave with the request or after the skill name and conversation context, list spec gaps (known unknowns), leaving out any gap the conversation or codebase already answers. With no request text, use the spec under discussion; with no spec under discussion either, ask once what to interview about.

   b. When the user has not yet said what they are sure of and what they are assuming, make that the first question of round 1; a list of what is still open does not say it. Settled items are not asked again, and stated assumptions become questions of their own.
2. Ask the round.

   a. Ask **max 4 questions per round**, in priority order, with 2–4 options each. Each question asks for one decision: a further decision tucked under it ("Also: …?") or into one of its options counts toward the 4, so move it to the next round when the round is full. When the question tool takes fewer questions or options, split the round across calls; the round still totals at most four.

   b. Attach a **one-line reason why it matters** to each question.
   c. Give each option a short consequence (tradeoff) note.
3. Collect the answers before updating the spec in step 4.
4. After the answers:

   a. On answers, restate the decisions as an **updated spec summary**.

   b. When undecided items remain, propose the next round.

   c. **Ladder once on the load-bearing answers**: an architecture or data answer that came without a reason gets one "why" follow-up at the top of the next round ("what would break for you if it went the other way?"), asked open, without options, so the reason is the user's own. Follow-ups count toward the round's 4 questions. When no undecided items remain, the follow-ups make up the next round on their own. The reason, not the choice, is what lets a later deviation be judged — the reason fills the decision table's rationale column.
5. When the user wants a deep interview (e.g. "40-question level"), repeat rounds in the same order: architecture → data → compatibility → performance → taste.

## Final Deliverables

When the interview ends, present two things:

1. **Decision table** with the columns radius (architecture / data / compatibility / performance / taste), question, decision, rationale, left undecided.
2. **Ready-to-use implementation prompt**: a complete instruction with all decisions applied. In the prompt:

   - Mark skipped questions "(unanswered — use your judgment)". A question that was asked but not answered is a skipped question: its options and any reason for it stay out of the fixed decisions.
   - Declare the architecture and data decisions **fixed**.
   - Close with "start with a short plan, then implement".
   - Include: "Where the plan leaves a choice open or the code conflicts with a fixed decision, pick the conservative option and log the deviation in IMPLEMENTATION_NOTES.md."

   The skill's purpose is that the user copies this prompt to start implementation.
