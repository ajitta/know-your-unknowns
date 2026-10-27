---
name: prototypes
description: >
  Divergent prototype fan-out — N (default 4) prototypes with clearly different
  design philosophies to react to. Use when the user says "divergent prototypes",
  "design options", or cannot say what they want
  ("know it when I see it") for a UI, dashboard, or API design.
---

# Prototypes — Divergent Prototype Fan-out (Design Directions)

People can't describe what they want but **can judge when they see it** (unknown knowns).

## Iron Rules

1. **Prototypes are tools to elicit reactions.** The skill ends at the confirmed requirements list.
2. Options must have **clearly different design philosophies — not small variations**.

## Procedure

1. Parse the target and count (default 4) from the text the user gave with the request or after the skill name. With no request text, the target is the thing last discussed and the count is 4.
2. Make options differ along these axes:
   - Information structure (what shows first)
   - User flow (operation order)
   - Visual density (dense vs whitespace)
   - Interaction mode (click/drag/keyboard/automatic)
   - Implementation complexity (simple-robust vs rich-complex)
3. Attach to each option: **name + one-line design philosophy + pros/cons + when it fits**.

   When a runnable prototype is needed, write the prototype code to files and give the user the run instructions. Keep the comparison and requirements in the conversation.

   Without a tool, do the step in the conversation and say what could not be checked.
4. Collect reactions on **both poles**: on every skip, ask what *would* have made it a steal.

   A skip is not the inverse of a steal: a construct is a **bipolar pair**, the contrast pole carries as much information as the pole users volunteer, and it is the one they volunteer least.
5. **Saturation check** before converting to spec:

   a. Before the saturation call in 5c, run one **triad**: show three options and ask which two feel alike and how the third differs. Run it whether reactions stall ("they all look fine") or keep coming; when they stall earlier, run it then.

   b. The triad's answer is a construct nobody volunteered (e.g. "calm vs. busy"). Have the user place **every** option on that construct (1–5), leaving the scores to the user: a score you suggest gets confirmed, not judged.

   c. Saturation call: if the last option shown still drew new reactions, the set was too small — offer 2 more along the axis still splitting opinion.

   Steal/skip only harvests constructs the user can already name; placing every option on the triad's construct makes it an axis the requirements can name instead of a one-off remark. Stop when no new constructs appear; a fixed N says nothing about whether the option space is covered.
6. Convert reactions into an **explicit requirements list**: the taste the user couldn't verbalize (unknown knowns) becomes spec.

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
- When the thing to build is code architecture, present approaches to the same feature (e.g. event-driven vs polling vs push) side by side as minimal skeletons.
- If the user asks for "wild", widen the distance between philosophies.
