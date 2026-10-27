---
name: interview
description: >
  The interview — before deciding anything, the model asks the user, in rounds of at most
  four, what it cannot know or judge about their situation (constraints, people,
  priorities, local rules, the decisions only they can make), biggest blast radius first,
  and ends with a decision table and a ready prompt. Any domain: a study design, an
  event, a policy, a hire, a feature. Use when the user says "interview me", "ask me
  questions before implementing", "ask me before you decide", or requirements are
  incomplete and the work has not started. Self-evident requests are done directly.
---

# Interview — Before-Deciding Interview

This skill serves what you do not know and the user does: before deciding, it asks what you cannot know or judge about the user's situation. A self-evident request, where both of you already know what to do, is done directly, without this method.

When requirements are incomplete, **the model interviews the user** before anything is decided: the answers sit with the user, and a decision made without them is a guess about their situation.

## Question Priority (blast radius: what a wrong decision breaks, fixed)

1. **Structure**: answers that change the shape of the whole work (the architecture of a system, the format of an event, the design of a study)
2. **Irreversible harm**: answers that could cause loss or harm that cannot be undone (data loss or a security problem, money spent, legal exposure, people affected; the *harm* tier below)
3. **Compatibility**: fit with what already exists and depends on it (external APIs and existing code, commitments, other people's plans, rules in force)
4. **Cost**: ongoing cost and performance (operating cost, time, budget, effort)
5. **Taste**: taste and minor details (last)

## Procedure

1. Find the gaps.

   a. Investigate the conversation and the available material (documents, data, a codebase) before listing gaps. From the text the user gave with the request or after the skill name and conversation context, list the gaps only the user can fill: decisions that are theirs, and facts about their situation you cannot know or judge from here (constraints, the people involved, local rules, priorities). Leave out any gap the conversation or material already answers. With no request text, use the spec under discussion; with no spec under discussion either, ask once what to interview about.

   b. When the user has not yet said what they are sure of and what they are assuming, make that the first question of round 1; a list of what is still open does not say it. Settled items are not asked again, and stated assumptions become questions of their own.
2. Ask the round.

   a. Ask **max 4 questions per round**, in priority order, with 2–4 options each. Each question asks for one decision: a further decision tucked under it ("Also: …?") or into one of its options counts toward the 4, and so does a request for a fact (a file path, a date, a headcount), so move it to the next round when the round is full. When the question tool takes fewer questions or options, split the round across calls; the round still totals at most four.

   b. Attach a **one-line reason why it matters** to each question.
   c. Give each option a short consequence (tradeoff) note.
3. Collect the answers before updating the spec in step 4.
4. After the answers:

   a. On answers, restate the decisions as an **updated spec summary**.

   b. When undecided items remain, propose the next round.

   c. **Ladder once on the load-bearing answers**: a structure or harm answer that came without a reason gets one "why" follow-up at the top of the next round ("what would break for you if it went the other way?"), asked open with its why-it-matters line and no options, so the reason is the user's own. Follow-ups count toward the round's 4 questions. When no undecided items remain, the follow-ups make up the next round on their own. The reason, not the choice, is what lets a later deviation be judged — the reason fills the decision table's rationale column.
5. When the user wants a deep interview (e.g. "40-question level"), repeat rounds in the same order: structure → harm → compatibility → cost → taste.

## Final Deliverables

When the interview ends, present two things:

1. **Decision table** with the columns radius (structure / harm / compatibility / cost / taste), question, decision, rationale, left undecided.
2. **Ready-to-use prompt for the work**: a complete instruction with all decisions applied. In the prompt:

   - Mark skipped questions "(unanswered — use your judgment)". A question that was asked but not answered is a skipped question: its options and any reason for it stay out of the fixed decisions.
   - Declare the structure and harm decisions **fixed**.
   - Close with "start with a short plan, then do the work".
   - Include: "Where the plan leaves a choice open or the work conflicts with a fixed decision, pick the conservative option and log the deviation in the deviation log (IMPLEMENTATION_NOTES.md for code work, otherwise the file the user names or DEVIATIONS.md beside the deliverable)."
