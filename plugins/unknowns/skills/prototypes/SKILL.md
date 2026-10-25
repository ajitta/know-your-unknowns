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

1. **Start final implementation only after the combined option is confirmed.** Prototypes are tools to elicit reactions.
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

   When a runnable prototype is needed and the host can write files, write the prototype code to files and give the user the run instructions. Keep the comparison and requirements in Markdown in the conversation. Record prototype decisions that depart from the plan in `IMPLEMENTATION_NOTES.md` before ending the turn; apply the **notes** skill's logging criteria and escalation rules. No file system → show the prototype code or a labeled mockup description and the deviation record as Markdown for the user to save, naming each intended file. No execution tool → say the prototype has not been run and ask for the user's execution result before treating it as verified.
4. Collect reactions on **both poles**: on every skip, ask what *would* have made it a steal.

   A skip is not the inverse of a steal. Kelly's repertory grid (1955) elicits a construct as a **bipolar pair**; the contrast pole carries as much information as the pole users volunteer, and it is the one they volunteer least.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.
5. **Saturation check** before converting to spec:

   a. When reactions stall ("they all look fine") or before the saturation call, run one **triad** — Kelly's own elicitation: show three options and ask which two feel alike and how the third differs.

   b. The triad's answer is a construct nobody volunteered (e.g. "calm vs. busy"). Have the user place **every** option on that construct (1–5).

   c. Saturation call: if the last option shown still drew new reactions, the set was too small — offer 2 more along the axis still splitting opinion.

   Steal/skip only harvests constructs the user can already name; placing every option on the triad's construct makes it an axis the requirements can name instead of a one-off remark. Kelly's stopping rule is "until no new constructs appear"; a fixed N says nothing about whether the option space is covered.
6. Convert reactions into an **explicit requirements list**: the taste the user couldn't verbalize (unknown knowns) becomes spec.
7. Proceed to real implementation only after the combined option is confirmed.

   When work departs from the plan, append the deviation to IMPLEMENTATION_NOTES.md before ending the turn. Stop and ask before changes to architecture, user-visible behavior, data, or security. No file system → print the record in the chat as Markdown and say to save it as IMPLEMENTATION_NOTES.md.

## Output

Deliver Markdown in the conversation with the same structure. End the turn with the assembled reply as Markdown in the conversation.

- Number every option and element inside it; ask for **steal / skip** by number.
- On skip, ask **"would steal if…"** (step 4).
- Selections assemble into a **requirements list** ("option 2's layout + option 4's colors…").

For numbered reactions and reply assembly, read references/output-routing.md.

## Variants

- **Mock before you wire** — when the interaction itself is the question (toolbar position, click flow):

  1. Build a **clickable mockup** using fake data when the host can write prototype code, with layout toggles and A/B choice buttons; do not wire it to the real app. No file system → show the states and transitions as numbered Markdown mockups. No execution tool → say the click flow has not been run and ask the user to run it before claiming it works.
  2. State in the mockup and its Markdown description that everything is **fake data and nothing reads from the real app**, and name the file and flag where real wiring would live.
  3. Add an "open questions I'd rather not guess" list, with numbered questions and A/B(/C) options; assemble the answers into the same copyable requirements list.
- When the thing to build is code architecture, present approaches to the same feature (e.g. event-driven vs polling vs push) side by side as minimal skeletons.
- If the user asks for "wild", widen the distance between philosophies.
