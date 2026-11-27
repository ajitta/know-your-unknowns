---
type: llm
focus: last_message
---

The user asked for a few versions to react to and did not say what they are versions
of. The conversation starts with that message and the working folder is empty, so
nothing names a target. The prototypes procedure, step 1, reads: "Parse the target and
count (default 4) from the text the user gave with the request or after the skill name.
When the text names no target, the target is the thing last discussed. When nothing has
been discussed either, the whole reply is one question asking what to make versions of;
step 2's Your own unknowns and the options follow the user's answer, and what the
versions are for and who they are for come out in the user's reactions to them."

Judge the final reply. All of these must hold:

1. The reply asks the user what the versions should be of: the thing to be made or
   decided.
2. That is the only question the reply asks. Example targets offered inside it ("a
   logo, a letter, an event?") belong to that one question. A second question about
   anything else (who it is for, its purpose, its tone, how many versions, constraints,
   a deadline) fails, and so does a list of what the assistant does not know or is
   assuming about the user's situation.
3. The reply shows no versions, options, directions or axes: none for a target it
   guessed, and none for several possible targets at once. It may say what it will do
   once the user answers (for example show four versions on different philosophies).

Fail if the reply makes versions before the user names the target, or asks more than
that one question.
