---
type: llm
focus: transcript
---

The quiz in this conversation is a six-question gate on a school field trip plan: five
multiple-choice questions and one teach-back that asks the user to explain something in
their own words. The simulated user was set to answer the second and the fourth
multiple-choice questions wrongly and everything else as the plan supports; on the first
retry, to answer the new question for the second question's part right and the new
question for the fourth question's part wrong again; and on any later retry, to answer
everything right. Read the conversation for what the assistant actually marked right
and wrong; this paragraph says only what the user was set to do.

The quiz skill says, after grading: "For each wrong or blank answer, re-explain only the
part of the work that answer missed, then offer a retry: one new question per wrong or
blank answer only, in the same format (multiple choice or teach-back), of the same
question type and on the same part of the work, prepared, asked and graded by the rules
of steps 1–3, not a new six-question set."

Find the first grading: the assistant reply that first grades the user's answers to the
six questions. Then find each retry: the new questions the assistant asks after a
grading below 6/6. All of these must hold:

1. The first retry asks exactly one new question for each question the first grading
   marked wrong or blank, and none for a question it marked right. It is not a new set
   of six questions.
2. Each retry question has the format of the question it stands in for (multiple choice
   for a multiple-choice miss, an explain-in-your-own-words question for a teach-back
   miss), asks the same type of question as that one (what to do when something goes
   wrong, why one choice was made over another, or what happens in a given case), and is
   about the same part of the plan as that question.
3. Each retry question is new: not the missed question repeated with the same wording
   and the same options.
4. Every later retry, after a grading that still marks some retry answers wrong, asks
   one new question for each answer still marked wrong and none for a part whose latest
   answer was marked right.

Fail if a retry asks a question about a part the user had already answered right, asks
more or fewer questions than there are answers marked wrong or blank, changes a missed
question's format, type or part of the plan, repeats a missed question unchanged, or
starts a new six-question quiz; or if no retry is asked in the conversation (for example
because the first grading gave 6/6).
