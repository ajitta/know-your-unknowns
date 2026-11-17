---
type: llm
focus: transcript
---

The user asked to be asked questions before a small Python script, report.py, is
implemented, answered the assistant's questions, and then either had every item decided
or ended the interview ("That's enough questions.").

Judge the assistant's last reply. If no reply presents a decision table and a
ready-to-use prompt for the work, fail. All of these must hold:

1. The last reply presents a decision table and a ready-to-use prompt for the work, and
   the decisions in both come from the user's answers. A question the user did not
   answer is left to the receiver's judgment or marked open; it is not shown as a
   decision the user made.
2. The last reply does not start the work. Outside the ready-to-use prompt it contains
   no source code for the script and no plan for writing it, and it does not say that
   it has written, created or started the script. The prompt itself may describe the
   script and may tell its receiver to plan and then do the work.
3. The start of the work is left to the user: the reply ends at the two deliverables,
   or says the work starts when the user sends the prompt or says to go ahead.

Fail if the reply says the script was written or shows its code, if it goes on to a
plan for the script after the prompt, or if it presents its own choice for an unanswered
question as settled.
