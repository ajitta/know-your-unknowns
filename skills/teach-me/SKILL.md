---
name: teach-me
description: >
  Teach me my unknowns — an interactive explainer for a field's vocabulary and mental
  model, in any field, so vague requests become precise. Use on "teach me", "make me an
  explainer", or when the user cannot name what they want or judge the result. Blindspot
  investigates a specific situation; teach-me teaches a field's vocabulary. Clear to
  both: do it without a skill, after a 2–3-line read-back (request, assumptions, what
  done means) if weighty; a mismatch goes to teach-me, interview or blindspot.
---

# Teach Me — Domain Vocabulary Explainer (Teach Me My Unknowns)

This skill serves what the user does not know and you do, and surfaces the user's gaps.

When you and the user both seem to understand the request, do it without this method: if its result carries weight, first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

Vague requests ("make it better") usually stem from **missing vocabulary**, not missing taste. This skill fills the **concept/terminology gap** among unknown unknowns.

## Iron Rules

1. **Teach first; the work starts from the precise request.** The user needs the words before the request can be precise.
2. Teach **only vocabulary needed for decisions**, not an encyclopedia — start from the axes the user must choose on in this task.

## Procedure

1. Parse the input.

   a. Parse the domain, goal and current level from the text the user gave with the request or after the skill name.

   b. With no request text, take the domain of the work under discussion; if the domain is still unclear, ask once, briefly.
2. Open with the **mental model**: the domain's pipeline in 3–5 ordered stages (color grading: ingest → correct → grade → match). The pipeline is there so the user knows what comes before what — correction first, then the creative look.
3. Pick 3–7 **decision axes** the user will decide on in this task (e.g. color grading: exposure / white balance / contrast curve / saturation vs naturalness / look).
4. Build a **vocabulary ladder**: per axis, everyday word → expert term. Give each term:
   - 1 example sentence of "what you can request with this term"
   - one source (a doc, standard or reference text)

   Mark any term whose usage or source you could not check as *unverified* rather than defining it confidently. A precise term can make a wrong premise sound right.
5. Show what each decision axis changes.

   a. Show a **before/after comparison** per decision axis — same subject at two contrasting settings on that axis. Build it by domain:

   | Domain | Comparison |
   |---|---|
   | Visual | Numbered Markdown before/after descriptions of the same subject, naming the visible differences. If a real photo is essential, ask the user for a file and refer to its visible regions. |
   | Text, code or process | Comparison examples. |

   b. Add 2–3 named presets (e.g. flat / corporate clean / cinematic teal-orange), with a description of each whole look and its settings.
6. Give **what good looks like**: 4–6 judging criteria stated in the new vocabulary (e.g. "skin tones stay believable", "blacks are rich but not crushed"). Keep this step even when trimming for size. These criteria buy later revision rounds: judging criteria transfer far better than production vocabulary, because recognising a bad result is cheaper than knowing which axis to move.
7. Close with the payoff.

   a. Write a **precise-request draft**: the user's original request rewritten in the new vocabulary. Mark every detail the user did not give (their taste, their numbers, their situation) as an assumption to confirm, so the draft does not decide for them.

   b. The user picks items and adjusts values/direction; the result becomes the next prompt.

## Output

Reaction: number the terms, before/after comparisons, and presets. Ask which numbers to **include in my request** and which settings to change; assemble the answers into the precise-request draft; a missing pick is undecided.

## Related

- Blind spots in a specific plan, system or situation: use the **blindspot** skill — this skill covers blind spots in a field's **concepts**. Running both is fine: when the user cannot yet describe the task, run **teach-me** first; otherwise run **blindspot** first and hand its ③ list (where the user does not know how to judge) to teach-me.
- If requirements still diverge after gaining vocabulary (revisions stop converging), lock decisions with the **interview** skill rather than teaching more vocabulary.
