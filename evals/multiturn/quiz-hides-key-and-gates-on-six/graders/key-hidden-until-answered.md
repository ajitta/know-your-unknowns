---
type: llm
focus: transcript
---

A quiz must not show its answer key before the user answers. Check the replies that
ask the six gate questions and every reply before the user's answers to them. Retry
questions asked after grading are outside this check. All of these must hold:

1. No such reply states, marks or hints which option is correct for any gate question
   (no "correct: B", no bolded or ticked right option, no "hint: pick the one about
   ...", no telling the user which option to choose).
2. No such reply lists the points a correct teach-back (the explain-in-your-own-words
   question) must mention, or gives a model answer to it.
3. The assistant waits for the user's answers instead of answering its own gate
   questions in the same reply.

The skill explains the change before quizzing by design: the structure, the design
decisions and the most likely failure points come first, and the quiz then checks
whether the user took them in. Do not fail because that explanation covers facts a
question later tests. A reveal is the key itself: which option is correct, or the
teach-back's grading points, presented as such. Wording that appears inside a question
or its options is not a reveal by itself. Two things that single out the correct option
are a reveal: formatting (bold, italics, a tick or a check mark on the correct option and
on none of the others), and a correct option clearly longer or more detailed than every
other option of its question, so that it stands out as the key.

Fail if a gate question's correct option or the teach-back's grading points are shown
before the user's answer.
