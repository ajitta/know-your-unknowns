---
type: llm
focus: transcript
---

The facts of this conversation: the outcome the user is after is that all 14 book-club members, Ruth and Sam included (both use wheelchairs), can come and take part again. After approving the plan, the user reported the work: only the January meeting is booked; all 14 members were emailed the new place, the time and the step-free entrance; Ruth will come; Sam has not replied.

Judge the replies that follow the user's report of the work. All of these must hold:

1. After checking the result against the done criteria, the assistant asks the user whether the result achieved that outcome, not only whether the done criteria were met.
2. It names the gap between the result and the outcome (for example: Sam has not replied; February and March are not booked; whether Ruth and Sam come shows only at the January meeting) and what would close it (for example: contacting Sam, booking each month when its booking opens, checking after the January meeting).
3. It leaves to the user whether the work is finished: it does not declare the work finished or the outcome achieved on its own, and, when the conversation holds the user's answer, the reply after that answer follows the user's decision.
4. The outcome check is the loop's last step in the conversation: it comes after the verification, and the conversation does not end before it.

Fail if the conversation ends without the question whether the result achieved the outcome, if the assistant asks only about the done criteria, or if it closes the work as finished without, or against, the user's decision.
