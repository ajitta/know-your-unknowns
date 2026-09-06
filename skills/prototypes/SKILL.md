---
name: prototypes
description: >
  Divergent prototype fan-out — N (default 4) prototypes with clearly different
  design philosophies to react to. Use when the user says "divergent prototypes",
  "design options", "시안 4개", "프로토타입 여러 개", or cannot say what they want
  ("know it when I see it", "보면 안다") for a UI, dashboard, or API design.
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
4. After user reacts: convert chosen elements into an **explicit requirements list** —
   taste they couldn't verbalize (unknown knowns) becomes spec.
5. Proceed to real implementation only after the combined option is confirmed.

## Output

Artifact tool if available → else `.unknowns/<YYYY-MM-DD>-prototypes-<slug>.html` → else
markdown (also when HTML is unnatural: static document, API design); always echo the
assembled reply in chat.
Each option — and each element inside it — carries **steal / skip chips**; selections
assemble into a **requirements list** ("option 2's layout + option 4's colors…").
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
