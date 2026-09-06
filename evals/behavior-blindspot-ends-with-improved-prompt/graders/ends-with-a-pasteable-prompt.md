---
type: llm
focus: last_message
---

The deliverable of a blind-spot pass is a better prompt. All of these must hold:

1. The response contains a rewritten version of the user's request, marked as the
   prompt to use next and written as an instruction to the model -- not as a summary
   addressed to the user.
2. That rewritten prompt is the last substantial block of the response: the findings
   come before it, not after.
3. It folds in the specific risks the response just surfaced (for example the nightly
   export job and the search indexer) rather than restating the original request.
4. It ends with an explicit stop-and-review checkpoint, such as showing a plan before
   writing any code.

Fail if the response lists risks but never produces a prompt the user could paste back.
