---
name: teach-me
description: >
  Teach me my unknowns — an interactive explainer for a domain's vocabulary and mental
  model, so vague requests become precise. Use on "teach me", "make me an explainer",
  "가르쳐줘", "설명서 만들어줘", "이 분야 용어를 모르겠어", or when the user cannot name
  what they want. Blindspot investigates a codebase; teach-me teaches vocabulary.
argument-hint: "<domain/task to learn> [current level]"
---

# Teach Me — Domain Vocabulary Explainer (Teach Me My Unknowns)

Vague requests ("make it better") usually stem from **missing vocabulary**, not missing taste.
This skill fills the **concept/terminology gap** among unknown unknowns.
Origin: Teach Me My Unknowns — see skills/loop/references/talk-source.md

## Iron Rules

1. **Do not start the work yet.** Teach first, so the user can make the request precise.
2. Teach **only vocabulary needed for decisions**, not an encyclopedia — start from
   the axes the user must choose on in this task.

## Procedure

1. Parse domain, goal, current level from `$ARGUMENTS`. Empty → the domain of the work
   under discussion; if still unclear, ask once, briefly.
2. Open with the **mental model**: the domain's pipeline in 3–5 ordered stages
   (color grading: ingest → correct → grade → match), so the user knows what comes before
   what — correction first, then the creative look.
3. Pick 3–7 **decision axes** the user will decide on in this task
   (e.g. color grading: exposure / white balance / contrast curve / saturation vs naturalness / look).
4. Build a **vocabulary ladder**: per axis, everyday word → expert term, each term with
   1 example sentence of "what you can request with this term".
5. Show a **before/after comparison** per concept — same subject with vs without the
   concept applied. Visual domains: synthetic inline comparisons (SVG/canvas, or CSS
   filters over two rendered states), never external image URLs; if a real photo is
   essential, ask the user for a file and embed it as a `data:` URI. Code/writing:
   comparison examples. Add 2–3 named presets (e.g. flat / corporate clean / cinematic
   teal-orange) so a whole look can be felt at once, not only single sliders.
6. Give **what good looks like**: 4–6 judging criteria stated in the new vocabulary
   (e.g. "skin tones stay believable", "blacks are rich but not crushed").
7. Close with the payoff — a **precise-request draft rewriting the user's original request
   in the new vocabulary**. User picks items and adjusts values/direction; the result
   becomes the next prompt. Offer with one AskUserQuestion: use this request now / edit it
   first / stop here.

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-teach-me-<slug>.html`; else markdown.
Reaction control: an "include in my request" checkbox per concept (plus live before/after sliders and presets); checked items assemble into the precise-request draft.
Details: skills/loop/references/output-routing.md

## Related

- Codebase blind spots: run `/unknowns:blindspot` (or `/blindspot` for copied installs)
  first — teach-me covers blind spots in domain **concepts**. Running both is fine.
- If requirements still diverge after gaining vocabulary, lock decisions with
  `/unknowns:interview`.
