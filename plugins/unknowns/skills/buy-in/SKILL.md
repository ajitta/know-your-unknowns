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

   No file access → use the records supplied in the conversation and ask for missing evidence; mark unsupported claims as limitations in step 5.
2. **Demo first**: put the working result at the top of the doc: execution output, screenshot/GIF, or a link to a runnable demo when available. Target read time: 90 seconds. No access to the result → ask for the result or mark the demo unverified; never invent an execution result.
3. **Preempt objections**:

   a. Anticipate ~5 questions/objections reviewers would raise.

   b. Answer each with **evidence**.

   c. Give every answer a reference the reviewer can follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run, file:line).

   d. No unsupported rebuttals: when an answer has no evidence, move it to the known limitations (step 5).

   e. Use `unknowns:independent-reviewer` when the host can start a sub-agent of that name to check evidence for objection responses, including its "verified" list. Hand it the reviewer packet from references/surfaces.md.

   Keep the review read-only: never edit or commit repository files or write outside a temporary directory. Check plan/spec conformance, recorded deviations, tests-pass-but-reality-fails cases, verified OK areas, and factual and reasoning claims against their evidence. Run available tests, lint and builds only when they can obey that read-only contract; report checks you cannot run. No sub-agent → hand the user the same packet to paste into a new conversation, and say that review stands in for the agent. The independent verification stage stays pending until that review returns. Details: references/surfaces.md
4. **Spec at a glance**: an area / decision / ref table, one row per settled decision.
5. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here. Not hiding is the basis of trust.
6. **Sign-off list**: name the people/teams who must approve, with roles, and what each must check.
7. **Rollback plan**: one paragraph on how to revert if things break.

## Output

Deliver Markdown in the conversation, keeping this skill's structure. End the turn with the assembled reply as Markdown in the conversation.

Reaction: a numbered sign-off checklist, one item per approver. Ask for the item numbers approved or needing changes; assemble the answers into a review-comment draft ("Reply with a ✓ on your piece").

Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

For numbered reactions and reply assembly, read references/output-routing.md.
