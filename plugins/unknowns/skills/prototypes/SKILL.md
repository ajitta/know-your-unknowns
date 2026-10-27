---
name: prototypes
description: >
  Prototypes in the design-thinking sense — several versions of anything, each on a
  clearly different philosophy, for the user to react to; ends with a confirmed
  requirements list. Use on "divergent prototypes", "design options", "versions to react
  to", or when the user cannot say what they want ("know it when I see it"). Clear to both
  sides: no skill or method.
---

# Prototypes — Divergent Prototype Fan-out (Design Directions)

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

People can't describe what they want but **can judge when they see it** (unknown knowns), and you do not know it either until they react.

## Iron Rules

1. **Prototypes are tools to elicit reactions.** The skill ends at the confirmed requirements list.
2. Options must have **clearly different design philosophies — not small variations**.

## Procedure

1. Parse the target and count (default 4) from the text the user gave with the request or after the skill name. With no request text, the target is the thing last discussed and the count is 4.
2. Make options differ along the axes that fit the subject:

   | Subject | Axes, e.g. |
   |---|---|
   | A screen, dashboard or tool | Information structure (what shows first), user flow (operation order), visual density (dense vs whitespace), interaction mode (click/drag/keyboard/automatic) |
   | A document, plan, policy, event, role, campaign or process | Structure (what comes first), scope (narrow vs broad), tone or register, audience, format |
   | Any | Complexity (simple-robust vs rich-complex) |

   **Your own unknowns**: say what you do not know about the user's situation, what you are assuming, and what you cannot check, and ask the user to fill or correct them.
3. Attach to each option: **name + one-line design philosophy + pros/cons + when it fits**.

   When a runnable or full-length version is needed (a clickable prototype, a whole draft), write it to files and tell the user how to open or run it. Keep the comparison and requirements in the conversation.

   Without a tool, do the step in the conversation and say what could not be checked.
4. Collect reactions on **both poles**: on every skip, ask what *would* have made it a steal.

   A skip is not the inverse of a steal: a construct is a **bipolar pair**, the contrast pole carries as much information as the pole users volunteer, and it is the one they volunteer least.
5. **Saturation check** before building the requirements list:

   a. Before the saturation call in 5c, run one **triad**: show three options and ask which two feel alike and how the third differs. Run it whether reactions stall ("they all look fine") or keep coming; when they stall earlier, run it then.

   b. The triad's answer is a construct nobody volunteered (e.g. "calm vs. busy"). Have the user place **every** option on that construct (1–5), leaving the scores to the user: a score you suggest gets confirmed, not judged.

   c. Saturation call: if the last option shown still drew new reactions, the set was too small — offer 2 more along the axis still splitting opinion.

   Steal/skip only harvests constructs the user can already name; placing every option on the triad's construct makes it an axis the requirements can name instead of a one-off remark. Stop when no new constructs appear; a fixed N says nothing about whether the option space is covered.
6. Convert reactions into an **explicit requirements list**: the taste the user couldn't verbalize (unknown knowns) becomes requirements. Ask the user to confirm the assembled list; the confirmed list is the input to the work.

## Output

- Number every option and element inside it; ask for **steal / skip** by number.
- On skip, ask **"would steal if…"** (step 4).
- Say the set can grow: if the last option shown still draws new reactions, you will offer 2 more along the axis still splitting opinion (step 5c).
- Selections assemble into a **requirements list** ("option 2's layout + option 4's colors…"); a missing pick is undecided.

## Variants

- **Mock before you wire** — when the interaction itself is the question (toolbar position, click flow):

  1. Build a **clickable mockup** using fake data, with layout toggles and A/B choice buttons, kept apart from the real app.
  2. State in the mockup and its description that everything is **fake data and nothing reads from the real app**, and name the file and flag where real wiring would live.
  3. Add an "open questions I'd rather not guess" list, with numbered questions and A/B(/C) options; assemble the answers into the same copyable requirements list.
- When the thing to decide is how something works inside (a code architecture, a process, an organisation), present approaches to the same goal side by side as minimal skeletons (e.g. event-driven vs polling vs push; a central desk vs a rota).
- If the user asks for "wild", widen the distance between philosophies.
