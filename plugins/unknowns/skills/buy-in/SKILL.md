---
name: buy-in
description: >
  The buy-in doc — a ship-readiness pitch that leads with a working demo, pre-answers
  reviewer objections with evidence, states limitations, and names who must sign off.
  Use when the user says "buy-in doc", "prep me for review",
  or before requesting review/approval/merge.
---

# Buy-in — Reviewer Persuasion Doc (The Buy-In Doc)

Implementation is done, but others' approval is still unknown. Find out in advance what reviewers will ask, and it becomes known.

The **quiz** skill validates my understanding; buy-in prepares others' trust.

## Procedure

1. Identify the target and the inputs:

   a. Identify the target work and audience (reviewers, team, decision-makers) from the text the user gave with the request or after the skill name. No arguments → this session's implemented work, audience = reviewers.

   b. Take as inputs the plan/spec, the prototype, and IMPLEMENTATION_NOTES.md.

   Without a tool, do the step in the conversation and say what could not be checked.
2. **Lead with the result**: open with what the change does, with a working demo when one is available (execution output, screenshot/GIF, or a link to a runnable demo), so a reviewer sees the work running before reading the rest.
3. **Preempt objections**:

   a. Anticipate ~5 questions/objections reviewers would raise.

   b. Answer each with **evidence**, and give every answer a reference the reviewer can follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run, file:line).

   c. Use the `unknowns:independent-reviewer` agent to check the evidence, including its "verified OK" list. Hand it the done criteria, the approved plan, the `IMPLEMENTATION_NOTES.md` path, the diff range or touched files, how to run the tests, and the claims the work rests on; leave out the implementer's own summary, so the review checks the work rather than the narrative.

   d. Move every answer that has no evidence to the known limitations (step 4).
4. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here. Not hiding is the basis of trust.
5. **Who signs off**: name the people/teams who must approve, with roles, and what each will check.

## Output

Reaction: number the objections, limitations and sign-off entries; the user marks each keep or revise, and the answers assemble into the final doc; a missing pick is undecided.
