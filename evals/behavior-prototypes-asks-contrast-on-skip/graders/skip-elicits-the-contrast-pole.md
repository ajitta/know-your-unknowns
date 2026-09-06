---
type: llm
---

The reply presents several divergent design directions for the user to react to.
Both of these must hold:

1. The reaction mechanism offers more than accept/reject. On a rejected option or
   element, the user is asked what *would* have made it acceptable — a "would steal
   if…" field, an equivalent prompt, or an explicit written instruction to say so.
2. It does not merely tell the user to describe what they want in free text; the
   contrast is attached to a specific rejected option or element.

Fail if skips are only recorded as rejections, with no route for the user to say what
would have changed the verdict.
