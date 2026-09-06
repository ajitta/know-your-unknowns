---
name: buy-in
description: >
  The buy-in doc — a ship-readiness pitch that leads with a working demo, pre-answers
  reviewer objections with evidence, states limitations, and names who must sign off.
  Use when the user says "buy-in doc", "prep me for review", "설득 문서 만들어줘",
  "리뷰 준비", or before requesting review/approval/merge.
argument-hint: "[target work/PR] [audience: team/reviewers]"
---

# Buy-in — Reviewer Persuasion Doc (The Buy-In Doc)

Implementation done, but **others' approval** remains an unknown. Know what reviewers
will ask in advance — it becomes known.
`/unknowns:quiz` (or `/quiz` for copied installs) validates **my understanding**;
buy-in prepares **others' trust**.
Origin: The Buy-In Doc — see skills/loop/references/talk-source.md.

## Procedure

1. From `$ARGUMENTS`, identify target work and audience (reviewers, team, decision-makers).
   No arguments → this session's implemented work, audience = reviewers.
   Inputs: the plan/spec, the prototype, and IMPLEMENTATION_NOTES.md.
2. **Demo first**: working result at top of doc — execution output, screenshot/GIF,
   interactive demo operable inside the doc if possible. Target read time: 90 seconds.
3. **Preempt objections**: anticipate ~5 questions/objections reviewers would raise,
   answer each with **evidence**, and give every answer a reference the reviewer can
   follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run, file:line).
   No unsupported rebuttals — no evidence, move it to limitations.
4. **Spec at a glance**: area / decision / ref table, one row per settled decision.
5. **Known limitations and unresolved unknowns**: if IMPLEMENTATION_NOTES.md exists,
   pull recorded deviations and unresolved risks here. Not hiding is the basis of trust.
6. **Sign-off list**: name people/teams needing to approve, with roles, and assign
   what each must check.
7. **Rollback plan**: one paragraph on how to revert if things break.

## Output

Ladder: Artifact tool → `.unknowns/<YYYY-MM-DD>-buy-in-<slug>.html` → markdown, same
structure (use markdown directly when the target is a PR body).
Reaction control = sign-off checklist, one checkbox per approver item; assembles into a
review-comment draft ("Reply with a ✓ on your piece").
Details: skills/loop/references/output-routing.md

## Integration

- Run `/unknowns:quiz` before writing — work the user can't explain can't be
  defended in a buy-in doc either.
- The `unknowns:independent-reviewer` agent (spawned with the Agent tool) produces the
  strongest evidence for objection responses, including its "verified" list.
