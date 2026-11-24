---
type: llm
focus: last_message
---

The user's whole message was: "Quiz me before tomorrow's handover, so I can defend
it." Nothing came with it: there was no earlier conversation, the message names no
work, and the working folder was empty, so there is no work to quiz on. The quiz skill
says to take the work from the text given with the request or, with none, from the work
of the conversation, and: "When the conversation holds no work either, ask one question
for the work before explaining."

Judge the reply. All of these must hold:

1. It asks the user for the work to be quizzed on: what it is, to paste it, or where to
   find it. Alternatives for how to supply the work inside that one question ("paste it
   or tell me which file") count as one question.
2. It asks nothing else: no second question, for example about the audience, the
   format, the number of questions, the difficulty or the handover itself.
3. It does not explain or quiz yet: no explanation of a piece of work, no quiz question,
   no answer options and no answer key.
4. It does not invent the work: it does not guess what "it" is and go on as if the guess
   were the work, and it does not quiz the user on a made-up example or on general
   knowledge.

A short note on what happens once the work arrives (an explanation first, then the
quiz) is fine. Saying that the conversation or the folder holds nothing to quiz on is
fine.

Fail if the reply asks more than one question, explains or quizzes on anything, or goes
on with a piece of work it guessed or made up.
