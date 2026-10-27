---
type: llm
focus: transcript
---

Before the reactions become a spec, the skill checks whether the option set covered the
space. Judge the assistant replies after the user's first reactions to the options.
All of these must hold:

1. A triad is run at some point in the conversation: the assistant shows (or names)
   three options and asks which two feel alike and how the third differs.
2. After the user's triad answer, the assistant turns it into a named construct (for
   example "calm vs busy") and has the user place every option on it (for example
   1-5), or asks the user to.
3. The assistant makes an explicit saturation call before treating the reactions as
   final: it either offers more options (about two) along the axis still splitting the
   user's opinion, or states that the last options drew no new reactions and the set
   is covered, with that reason.
4. Only after this check does it convert the reactions into a requirements list.

Fail if, after the user reacts, the assistant goes straight to a requirements list or
a final design with no triad and no saturation call, or if the conversation ends with
the user's reactions never acted on.
