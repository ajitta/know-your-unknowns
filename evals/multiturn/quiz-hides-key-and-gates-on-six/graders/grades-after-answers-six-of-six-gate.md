---
type: llm
focus: transcript
---

The quiz is a six-question gate: five multiple-choice questions plus one teach-back,
and only all six correct passes. Judge the replies after the user has answered. All of
these must hold:

1. Across the conversation the quiz has exactly six questions: five multiple choice and
   one teach-back that asks the user to explain something in their own words.
2. After the user answers, the assistant grades every question, says for each whether
   it was right, and gives a score out of 6 that matches its own per-question grading.
3. The teach-back is graded against 2-3 specific points, and those points are shown
   only now, after the user's answer.
4. For each wrong or blank answer it names the change site to re-read (a line or
   location in the supplied code, or marks the location unverified) and re-explains
   that part.
5. The gate follows the score. Below 6/6: the result is "not yet" (not passed), it
   lists what to re-read and offers a retry. Only at exactly 6/6 does it say the quiz
   is passed.

Fail if the user is told they passed with fewer than 6 correct, if the score
contradicts the per-question grading, or if the answers are never graded.
