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
Origin: Four Design Directions / Mock before you wire — see skills/loop/references/talk-source.md.

## Iron Rules

1. **Never start final implementation.** Prototypes are tools to elicit reactions.
2. Options must have **clearly different design philosophies — not small variations**.

## Procedure

1. Parse target and count (default 4) from `$ARGUMENTS`; if empty, target = the thing
   last discussed, count 4.
2. Make options differ along these axes:
   - Information structure (what shows first)
   - User flow (operation order)
   - Visual density (dense vs whitespace)
   - Interaction mode (click/drag/keyboard/automatic)
   - Implementation complexity (simple-robust vs rich-complex)
3. Attach to each option: **name + one-line design philosophy + pros/cons + when it fits**.
4. Collect reactions on **both poles**. A skip is not the inverse of a steal — on every skip
   ask what *would* have made it a steal. Kelly's repertory grid (1955) elicits a construct as
   a **bipolar pair**; the contrast pole carries as much information as the pole users
   volunteer, and it is the one they volunteer least.
5. **Saturation check** before converting to spec: if the last option shown still drew new
   reactions, the set was too small — offer 2 more along the axis still splitting opinion.
   Kelly's stopping rule is "until no new constructs appear"; a fixed N says nothing about
   whether the option space is covered.
6. Convert reactions into an **explicit requirements list** — taste they couldn't verbalize
   (unknown knowns) becomes spec.
7. Proceed to real implementation only after the combined option is confirmed.

## Output

Artifact tool if available → else `.unknowns/<YYYY-MM-DD>-prototypes-<slug>.html` → else
markdown (also when HTML is unnatural: static document, API design); always echo the
assembled reply in chat.
Each option — and each element inside it — carries **steal / skip chips**, with a one-tap
**"would steal if…"** field revealed on skip (step 4); selections assemble into a
**requirements list** ("option 2's layout + option 4's colors…").
Details: skills/loop/references/output-routing.md

## Variants

- **Mock before you wire** — when the interaction itself is the question (toolbar
  position, click flow): no real code, a **clickable mockup** with layout toggles and
  A/B choice buttons. State in the page that everything is **fake data and nothing
  reads from the real app**, and name the file and flag where real wiring would live.
  Add an "open questions I'd rather not guess" list, one A/B(/C) chip row per question,
  feeding the same self-filling copyable reply template.
- Works for code architecture too: present approaches to the same feature
  (e.g. event-driven vs polling vs push) side by side as minimal skeletons.
- If user asks for "wild", widen the distance between philosophies.
