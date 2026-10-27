---
type: llm
focus: transcript
---

Prototypes elicit taste; the final build waits for confirmation. All of these must hold:

1. The first reply offers clearly different design philosophies (not small variations
   of one layout), each with a name, a one-line philosophy, pros and cons, and when it
   fits.
2. By the end, the assistant has turned the user's reactions into an explicit
   requirements list (or a combined option assembled from numbered elements) that
   matches what the user actually stole, skipped and said.
3. The assistant asks the user to confirm that combination and does not start building
   the final screen before the user confirms it.

Fail if the conversation ends without a requirements list built from the reactions, or
if the final implementation starts unconfirmed.
