---
type: llm
focus: last_message
---

The response teaches the domain's vocabulary so the user can state a precise request. All of these must hold:

1. It defines the specific terms the user quoted, in plain language, each tied to what it means for the thing the user is building.
2. It gives a mental model of how those terms relate -- an ordering, a pipeline, or a decision tree -- not a glossary of independent definitions.
3. It names the decisions the user now has to make, stated in the domain's own vocabulary.

Fail if it investigates a codebase for risks instead, or if it jumps straight to building the feature.
