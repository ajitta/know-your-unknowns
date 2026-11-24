---
type: llm
focus: last_message
---

The user's whole message was: "Use the reference skill. Use this as a reference for the
volunteer handbook I'm writing for our food bank." Nothing came with it: there was no earlier conversation and
no attachment, and the working folder was empty, so the message neither names nor
contains a reference. The reference skill says: "Take the reference from the text the
user gave with the request or after the skill name, or from the conversation; when
neither names or contains a reference, ask one question for it."

Judge the reply. All of these must hold:

1. It asks the user for the reference: to paste or share it, or to say what or where it
   is. Alternatives for how to supply it inside that one question ("paste it or give me
   the file name") count as one question.
2. It asks nothing else: no second question, for example about the handbook's readers,
   its length, its sections or the food bank.
3. It does not read a reference it does not have: no summary of a reference's intent,
   behaviour or rules, no list of what to keep, change or leave out, no side-by-side
   mapping and no application plan.
4. It does not build the handbook: no draft, outline or list of sections, and no generic
   or typical handbook offered in place of the user's reference.

A short note on what happens once the reference arrives (for example that the assistant
will show its reading of it for correction before drafting) is fine, and so is saying
that nothing was attached or found in the folder.

Fail if the reply asks more than one question, works from a reference it guessed or made
up, or starts the handbook.
