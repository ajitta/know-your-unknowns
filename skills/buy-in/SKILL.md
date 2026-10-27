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

   a. Run the **quiz** skill before writing this doc: work the user can't explain can't be defended in a buy-in doc either.

   b. Identify the target work and audience (reviewers, team, decision-makers) from the text the user gave with the request or after the skill name. No arguments → this session's implemented work, audience = reviewers.

   c. Take as inputs the plan/spec, the prototype, and IMPLEMENTATION_NOTES.md.

   Without a tool, do the step in the conversation and say what could not be checked.
2. **Demo first**: put the working result at the top of the doc: execution output, screenshot/GIF, or a link to a runnable demo when available. Keep the demo readable in 90 seconds, so a reviewer sees the work running before reading the rest.
3. **Preempt objections**:

   a. Anticipate ~5 questions/objections reviewers would raise.

   b. Answer each with **evidence**.

   c. Give every answer a reference the reviewer can follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run, file:line).

   d. No unsupported rebuttals: when an answer has no evidence, move it to the known limitations (step 5).

   e. Use the `unknowns:independent-reviewer` agent to check evidence for objection responses, including its "verified OK" list. Hand it the done criteria, the approved plan, the `IMPLEMENTATION_NOTES.md` path, the diff range or touched files, how to run the tests, and the claims the work rests on; leave out the implementer's own summary.
4. **Spec at a glance**: an area / decision / ref table, one row per settled decision.
5. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here. Not hiding is the basis of trust.
6. **Sign-off list**: name the people/teams who must approve, with roles, and what each must check.
7. **Rollback plan**: one paragraph on how to revert if things break.

## Output

Reaction: a numbered sign-off checklist, one item per approver. Ask for the item numbers approved or needing changes; assemble the answers into a review-comment draft ("Reply with a ✓ on your piece"); a missing pick is undecided.
