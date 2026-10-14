---
name: buy-in
description: >
  The buy-in doc — a ship-readiness pitch that leads with a working demo, pre-answers
  reviewer objections with evidence, states limitations, and names who must sign off.
  Use when the user says "buy-in doc", "prep me for review",
  or before requesting review/approval/merge.
argument-hint: "[target work/PR] [audience: team/reviewers]"
---

# Buy-in — Reviewer Persuasion Doc (The Buy-In Doc)

Implementation is done, but others' approval is still unknown. Find out in advance what reviewers will ask, and it becomes known.

The **quiz** skill validates my understanding; buy-in prepares others' trust.

## Procedure

1. Identify the target and the inputs:

   a. Identify the target work and audience (reviewers, team, decision-makers) from `$ARGUMENTS`. No arguments → this session's implemented work, audience = reviewers.

   b. Take as inputs the plan/spec, the prototype, and IMPLEMENTATION_NOTES.md.
2. **Demo first**: put the working result at the top of the doc: execution output, screenshot/GIF, or an interactive demo inside the doc if possible. Target read time: 90 seconds.
3. **Preempt objections**:

   a. Anticipate ~5 questions/objections reviewers would raise.

   b. Answer each with **evidence**.

   c. Give every answer a reference the reviewer can follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run, file:line).

   d. No unsupported rebuttals: when an answer has no evidence, move it to the known limitations (step 5).
4. **Spec at a glance**: an area / decision / ref table, one row per settled decision.
5. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here. Not hiding is the basis of trust.
6. **Sign-off list**: name the people/teams who must approve, with roles, and what each must check.
7. **Rollback plan**: one paragraph on how to revert if things break.

## Output

When the target is a PR body, use markdown directly, same structure. Otherwise follow this ladder:

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-buy-in-<slug>.html`; else markdown with the same structure. On every rung, end the turn with the assembled reply as plain text in chat.

Reaction control: a sign-off checklist, one checkbox per approver item. The sign-off checklist assembles into a review-comment draft ("Reply with a ✓ on your piece").

Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Related

- Run the **quiz** skill before writing this doc: work the user can't explain can't be defended in a buy-in doc either.
- The `unknowns:independent-reviewer` agent (spawned with the Agent tool) produces the strongest evidence for objection responses, including its "verified" list.

  No Agent tool → use the fresh-thread substitute in `${CLAUDE_PLUGIN_ROOT}/skills/loop/references/surfaces.md` — and never present an unreviewed doc as reviewed.
