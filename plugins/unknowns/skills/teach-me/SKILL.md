---
name: teach-me
description: >
  Teach me my unknowns — an interactive explainer for a domain's vocabulary and mental
  model, so vague requests become precise. Use on "teach me", "make me an explainer",
  or when the user cannot name
  what they want. Blindspot investigates a codebase; teach-me teaches vocabulary.
---

# Teach Me — Domain Vocabulary Explainer (Teach Me My Unknowns)

Vague requests ("make it better") usually stem from **missing vocabulary**, not missing taste. This skill fills the **concept/terminology gap** among unknown unknowns.

## Iron Rules

1. **Do not start the work yet.** Teach first, so the user can make the request precise.
2. Teach **only vocabulary needed for decisions**, not an encyclopedia — start from the axes the user must choose on in this task.

## Procedure

1. Parse the input.

   a. Parse the domain, goal and current level from the text the user gave with the request or after the skill name.

   b. With no request text, take the domain of the work under discussion; if the domain is still unclear, ask once, briefly.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.
2. Open with the **mental model**: the domain's pipeline in 3–5 ordered stages (color grading: ingest → correct → grade → match). The pipeline is there so the user knows what comes before what — correction first, then the creative look.
3. Pick 3–7 **decision axes** the user will decide on in this task (e.g. color grading: exposure / white balance / contrast curve / saturation vs naturalness / look).
4. Build a **vocabulary ladder**: per axis, everyday word → expert term. Give each term:
   - 1 example sentence of "what you can request with this term"
   - one source (a doc, standard or reference text)

   Mark any term whose usage you are not sure of as *unverified* rather than defining it confidently. No source access → use the supplied reference text and mark any source or usage you could not check as unverified. A precise term can make a wrong premise sound right.
5. Show what each concept changes.

   a. Show a **before/after comparison** per concept — same subject with vs without the concept applied. Build it by domain:

   | Domain | Comparison |
   |---|---|
   | Visual | Numbered Markdown before/after descriptions of the same subject, naming the visible differences. If a real photo is essential, ask the user for a file and refer to its visible regions without inventing an image. |
   | Code/writing | Comparison examples. |

   b. Add 2–3 named presets (e.g. flat / corporate clean / cinematic teal-orange), with a description of each whole look and its settings.
6. Give **what good looks like**: 4–6 judging criteria stated in the new vocabulary (e.g. "skin tones stay believable", "blacks are rich but not crushed"). Keep this step even when trimming for size. These criteria buy later revision rounds: judging criteria transfer far better than production vocabulary, because recognising a bad result is cheaper than knowing which axis to move.
7. Close with the payoff.

   a. Write a **precise-request draft**: the user's original request rewritten in the new vocabulary.

   b. The user picks items and adjusts values/direction; the result becomes the next prompt.

   c. Offer once: use this request now / edit it first / stop here. When run as a **loop** stage, do not ask this separately: the loop's stage checkpoint carries these options.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

## Output

Deliver Markdown in the conversation, keeping this skill's structure. End the turn with the assembled reply as Markdown in the conversation.
Reaction: number the concepts, before/after comparisons, and presets. Ask which numbers to **include in my request** and which settings to change; assemble the answers into the precise-request draft.

For numbered reactions and reply assembly, read references/output-routing.md.

## Limits — what this can and cannot deliver

- Vocabulary hands over a **request**, not fluency: expect the user's *next* request to be markedly more precise, not the terms wielded unaided across revision rounds 2–4. Success is convergence across those rounds, not the quality of the first rewritten request.
- When revisions stop converging, hand off to the **interview** skill to lock decisions rather than teaching more vocabulary. Revisions that stop converging mark this skill's ceiling, not the user's mistake.

## Related

- Codebase blind spots: use the **blindspot** skill — teach-me covers blind spots in domain **concepts**. Running both is fine: when the user cannot yet describe the task, run **teach-me** first; otherwise run **blindspot** first and hand its ③ list (where the user does not know how to judge) to teach-me.
- If requirements still diverge after gaining vocabulary, lock decisions with the **interview** skill.
