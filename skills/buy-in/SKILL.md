---
name: buy-in
description: >
  The buy-in doc — after implementation, produce a ship-readiness pitch that leads
  with a working demo, pre-answers likely reviewer objections with evidence, states
  known limitations, and names the stakeholders who must sign off. This skill should
  be used when the user says "buy-in 문서", "설득 문서 만들어줘", "리뷰 준비",
  "머지 승인 준비해줘", "pitch this work", or before requesting review/approval/merge
  of significant work.
argument-hint: "[target work/PR] [audience: team/reviewers]"
---

# Buy-in — Reviewer Persuasion Doc (The Buy-In Doc)

Implementation done, but **others' approval** remains an unknown. Know what reviewers
will ask in advance — it becomes known. Original "The Buy-In Doc": show working demo
first, preempt reviewer objections with evidence, name who must sign off.
`/unknowns:quiz` validates **my understanding**; buy-in prepares **others' trust**.

## Procedure

1. From `$ARGUMENTS`, identify target work and audience (reviewers, team, decision-makers).
2. **Demo first**: working result at top of doc — execution output, screenshot/GIF,
   interactive demo operable inside the doc if possible.
3. **Preempt objections**: anticipate ~5 questions/objections reviewers would raise,
   answer each with **evidence** (test results, benchmark numbers, code locations,
   design rationale). No unsupported rebuttals — no evidence, move it to limitations.
4. **Known limitations and unresolved unknowns**: if IMPLEMENTATION_NOTES.md exists,
   pull recorded deviations and unresolved risks here. Not hiding is the basis of trust.
5. **Sign-off list**: name people/teams needing to approve, with roles, and assign
   what each must check.
6. **Rollback plan**: one paragraph on how to revert if things break.

## Output Format (HTML first)

**Single-file interactive HTML**: top demo (animation, execution example),
expandable card per objection (objection → evidence), limitations section, sign-off
checklist (check each item → **assembles into review-comment draft**). Inline CSS/JS,
no external dependencies.
No viewer available, or target is a PR body — fall back to markdown with same structure.

## Integration

- Run `/unknowns:quiz` before writing — work the user can't explain can't be
  defended in a buy-in doc either.
- independent-reviewer agent's verification results (including "verified" list) are
  the strongest evidence for objection responses.
