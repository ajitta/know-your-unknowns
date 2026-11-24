---
type: llm
focus: transcript
---

The quiz in this conversation is a six-question gate on a school field trip plan: five
multiple-choice questions and one teach-back that asks the user to explain something in
their own words. Only 6/6 passes. The simulated user was set to answer the second and
the fourth multiple-choice questions wrongly; on the first retry, to answer the new
question for the second question's part right and the new question for the fourth
question's part wrong again; and on any later retry, to answer everything right. Read
the conversation for what the assistant actually marked right and wrong; this paragraph
says only what the user was set to do.

The quiz skill says: "Each retry question answered correctly adds one to the score, so a
retry that answers every question correctly brings it to 6/6." Below 6/6, "The result
stays 'not yet' — list the change sites to re-read and offer the retry"; at 6/6,
"Passed."

Follow the score through the conversation. All of these must hold:

1. The first grading gives a score out of 6 that matches its own marks per question, and
   when that score is below 6/6 the result is "not yet" (not passed).
2. At least one retry is asked, answered by the user and graded.
3. After each graded retry, the new score equals the score before that retry plus the
   number of retry answers the assistant marked right in that grading. Answers marked
   right earlier keep their points, a retry answer marked wrong adds nothing, and the
   score never goes above 6/6.
4. While any part missed in the first grading still has its latest answer marked wrong,
   the score is below 6/6 and the result is "not yet" (not passed); the reply names
   where in the plan to re-read for each part still missed (a section, a heading or a
   line of the plan) and offers another retry.
5. The assistant says the quiz is passed, or gives a score of 6/6, only after every part
   missed in the first grading has an answer it marked right; once that is so, the score
   is 6/6 and the result is passed.

Fail if a score after a retry is not the earlier score plus the retry answers marked
right; if the user is told they passed, or scored 6/6, while a missed part's latest
answer is marked wrong; if a score below 6/6 is called a pass; or if no retry is graded.
