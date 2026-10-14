---
name: prototypes
description: >
  Divergent prototype fan-out — N (default 4) prototypes with clearly different
  design philosophies to react to. Use when the user says "divergent prototypes",
  "design options", or cannot say what they want
  ("know it when I see it") for a UI, dashboard, or API design.
argument-hint: "<thing to build> [count, default 4]"
---

# Prototypes — Divergent Prototype Fan-out (Design Directions)

People can't describe what they want but **can judge when they see it** (unknown knowns).

## Iron Rules

1. **Never start final implementation.** Prototypes are tools to elicit reactions.
2. Options must have **clearly different design philosophies — not small variations**.

## Procedure

1. Parse the target and count (default 4) from `$ARGUMENTS`. If `$ARGUMENTS` is empty, the target is the thing last discussed and the count is 4.
2. Make options differ along these axes:
   - Information structure (what shows first)
   - User flow (operation order)
   - Visual density (dense vs whitespace)
   - Interaction mode (click/drag/keyboard/automatic)
   - Implementation complexity (simple-robust vs rich-complex)
3. Attach to each option: **name + one-line design philosophy + pros/cons + when it fits**.
4. Collect reactions on **both poles**: on every skip, ask what *would* have made it a steal.

   A skip is not the inverse of a steal. Kelly's repertory grid (1955) elicits a construct as a **bipolar pair**; the contrast pole carries as much information as the pole users volunteer, and it is the one they volunteer least.
5. **Saturation check** before converting to spec:

   a. When reactions stall ("they all look fine") or before the saturation call, run one **triad** — Kelly's own elicitation: show three options and ask which two feel alike and how the third differs.

   b. The triad's answer is a construct nobody volunteered (e.g. "calm vs. busy"). Have the user place **every** option on that construct (1–5).

   c. Saturation call: if the last option shown still drew new reactions, the set was too small — offer 2 more along the axis still splitting opinion.

   Steal/skip only harvests constructs the user can already name; placing every option on the triad's construct makes it an axis the requirements can name instead of a one-off remark. Kelly's stopping rule is "until no new constructs appear"; a fixed N says nothing about whether the option space is covered.
6. Convert reactions into an **explicit requirements list**: the taste the user couldn't verbalize (unknown knowns) becomes spec.
7. Proceed to real implementation only after the combined option is confirmed.

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-prototypes-<slug>.html`; else markdown with the same structure. On every rung, end the turn with the assembled reply as plain text in chat.
Use markdown also when HTML is unnatural (static document, API design).

- Each option — and each element inside it — carries **steal / skip chips**.
- On skip, a one-tap **"would steal if…"** field is revealed (step 4).
- Selections assemble into a **requirements list** ("option 2's layout + option 4's colors…").

Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Variants

- **Mock before you wire** — when the interaction itself is the question (toolbar position, click flow):
  - No real code: build a **clickable mockup** with layout toggles and A/B choice buttons.
  - State in the page that everything is **fake data and nothing reads from the real app**, and name the file and flag where real wiring would live.
  - Add an "open questions I'd rather not guess" list, one A/B(/C) chip row per question, feeding the same self-filling copyable reply template.
- When the thing to build is code architecture, present approaches to the same feature (e.g. event-driven vs polling vs push) side by side as minimal skeletons.
- If the user asks for "wild", widen the distance between philosophies.
