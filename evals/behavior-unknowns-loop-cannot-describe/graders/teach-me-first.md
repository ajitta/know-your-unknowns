---
type: llm
focus: last_message
---

The user asked to run the staged working loop on a task they cannot describe: the
company's photo work was suddenly handed to them, they have heard it involves "보정"
(correction) and "리터칭" (retouching), and they say they cannot explain what they are
supposed to do. Judge the reply, in whatever language it is written, by what each step
does rather than what it is called.

The reply passes when, before any investigation of the photo work itself, it places a
step that teaches the user the basic words and picture of photo work (for example what
correction and retouching each are, the order the work usually goes in, and the choices
the user will have to make), in one of two ways:
1. It sets out the stages the work will go through, in order, and the teaching step comes
   before the investigation.
2. It starts the work with that teaching, delivering it or beginning it.

Investigation here means hunting for the photo work's risks, gaps or blind spots, or
asking the user what they are sure of, what they are assuming and what they cannot judge
about it. Settling the goal, what counts as done, what must not break and the limits, and
the assistant saying what it does not know about the user's situation, may come before
both and are not investigation. A term glossed in passing inside the investigation is not
a teaching step.

Fail if the reply goes straight to investigating the photo work with no teaching step
placed first, if the teaching step comes only alongside or after the investigation, or if
there is none.
