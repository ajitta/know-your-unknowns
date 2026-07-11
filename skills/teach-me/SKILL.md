---
name: teach-me
description: >
  Teach me my unknowns — build an interactive explainer that teaches the user the
  vocabulary and mental model of an unfamiliar domain, so vague requests become
  precise ones. This skill should be used when the user says "teach me", "가르쳐줘",
  "설명서 만들어줘", "이 분야 용어를 모르겠어", "teach me my unknowns", or asks for
  work in a domain where they cannot yet name what they want (e.g. "영상 더 좋게
  해줘", "make it pop") and better vocabulary would make the request precise.
argument-hint: "<domain/task to learn> [current level]"
---

# Teach Me — Domain Vocabulary Explainer (Teach Me My Unknowns)

Vague requests ("make it better") usually stem from **missing vocabulary**, not missing taste.
From the original "Teach Me My Unknowns": given a vocabulary ladder and before/after
comparisons, a user who knew nothing about color grading turned "make the video nicer"
into precise requests in professional language.
This skill fills the **concept/terminology gap** among unknown unknowns.

## Iron Rules

1. **Do not start the work yet.** Teach first, so the user can make the request precise.
2. Teach **only vocabulary needed for decisions**, not an encyclopedia — start from
   the axes the user must choose on in this task.

## Procedure

1. Parse domain, goal, current level from `$ARGUMENTS`. If unclear, ask once, briefly.
2. Pick 3–7 **decision axes** the user will decide on in this task
   (e.g. color grading: exposure / white balance / contrast curve / saturation vs naturalness / look).
3. Build a **vocabulary ladder**: per axis, everyday word → expert term, each term with
   1 example sentence of "what you can request with this term".
4. Show a **before/after comparison** per concept — same subject with vs without the
   concept applied. Visual domains: real comparison images; code/writing: comparison examples.
5. Finish: present a **precise-request draft rewriting the user's original request in the
   new vocabulary**. User picks items and adjusts values/direction — result becomes the next prompt.

## Output Format (HTML first)

**Single-file interactive HTML** explainer: vocabulary ladder (click term → expand
definition/example), where possible **live before/after sliders/toggles** (real demos via
CSS filter, inline SVG/canvas, etc.), per-concept "include in my request" checkbox →
**precise request prompt auto-assembles** at bottom, copyable. CSS/JS inline, no external
dependencies.
No viewer available: fall back to markdown with vocabulary-ladder table + comparison
explanations + request draft.

## Related

- Codebase blind spots: run `/unknowns:blindspot` first — teach-me covers blind spots in
  domain **concepts**. Running both is fine.
- If requirements still diverge after gaining vocabulary, lock decisions with `/unknowns:interview`.
