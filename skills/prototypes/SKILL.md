---
name: prototypes
description: >
  Divergent prototype fan-out — generate N (default 4) prototypes with clearly
  different design philosophies so the user can react to them. This skill should be
  used when the user says "divergent prototypes", "design options", "give me
  different designs", "design
  directions", "프로토타입 여러 개", "시안 4개", "다양한 디자인으로 보여줘", or cannot
  articulate what they want ("know it when I see it", "보면 안다") for a UI,
  dashboard, document, or API design.
argument-hint: "<thing to build> [count, default 4]"
---

# Prototypes — Divergent Prototype Fan-out (Design Directions)

People can't describe what they want but **can judge when they see it** (unknown knowns).
Source: Thariq Shihipar — "I have no visual taste. Make me an HTML page with four
widely different design decisions so I can react to them."

## Iron Rules

1. **Never start final implementation.** Prototypes are tools to elicit reactions.
2. Options must have **clearly different design philosophies — not small variations**.

## Procedure

1. Parse target and count (default 4) from `$ARGUMENTS`.
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

## Output Format (HTML first)

Build a **single-file interactive HTML** that switches between the N options for
comparison. Include the device from "Four Design Directions": each option (or
individual element within it) gets **steal / skip chips**, and selections
**auto-assemble at the bottom into a copyable reply template** (requirements-list
draft like "option 2's layout + option 4's colors…"). Inline CSS/JS, no external
dependencies.
If in a viewer-less CLI environment, or HTML is unnatural (static document, API
design), fall back to markdown presenting options side by side in the same format —
still ask steal/skip reactions per item and assemble them into a requirements draft.

If interaction itself is the question (toolbar position, click flow, etc.), use the
source's "Mock before you wire" approach: no real code — a **clickable mockup**
with layout toggles and A/B choice buttons to collect reactions.

## Variants

- Works for code architecture too: present approaches to the same feature
  (e.g. event-driven vs polling vs push) side by side as minimal skeletons.
- If user asks for "wild", widen the distance between philosophies.
