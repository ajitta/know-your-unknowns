---
type: llm
focus: transcript
---

The user coordinates a food bank whose Saturday distribution moves from a church hall to
a school gym. The assistant was to present its findings with numbered prompt fixes and a
draft prompt; the user would then pick only some of the fix numbers (normally the first
and the third listed) and say "apply only those". Read the picked numbers from that user
message; every other fix is unpicked: the user neither accepted nor rejected it.

Judge the assistant's reply to that pick. All of these must hold:

1. The reply contains a revised draft of the prompt.
2. The revised draft applies each picked fix: what that fix asked for is in the draft.
3. Every fix the user did not pick is named in that reply, by its number or its content,
   as undecided, still open, or a clear equivalent that leaves the choice to the user.
   Naming an unpicked fix as rejected, dropped or removed does not count.
4. No unpicked fix is applied: the draft does not tell the model to do what an unpicked
   fix asked for as a settled step. Listing an unpicked fix as undecided, inside or below
   the draft, is allowed.

Fail if the user was never given numbered fixes to pick from, if the reply to the pick
leaves out an unpicked fix or names it as anything but undecided or open, or if it
applies an unpicked fix anyway.
