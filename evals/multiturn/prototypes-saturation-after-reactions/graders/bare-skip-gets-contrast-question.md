---
type: llm
focus: transcript
---

A skip is not the inverse of a steal. In the first reaction the simulated user skips
some items with a bare "skip" and no reason. All of these must hold:

1. For the items the user skipped without saying why, the assistant's next reply asks
   what would have made that specific item a steal (a "would steal if..." question
   attached to the skipped option or element), unless the user already said it. An
   element of an option the user skipped as a whole may be folded into the question
   about that option.
2. When the user answers, the answer shows up later as a requirement or constraint in
   the assistant's summary (for example light rather than dark, short labels rather than
   sentences), not just as a rejected option.
3. Reactions are collected by the numbers the assistant gave the options and elements.

Fail if skips are only recorded as rejections, or if the assistant never asks about a
bare skip.
