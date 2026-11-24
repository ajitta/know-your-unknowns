---
type: llm
focus: transcript
---

The assistant's first reply gave a plan for the choir tour and suggested settling its
gaps through questions first. The user's first message took that suggestion ("interview
me first"), or, if no suggestion was made, asked to be interviewed about the gaps first.
That message answered none of the plan's questions and approved no item.

Judge the assistant replies after that message, up to the first reply that shows the
plan again (or to the end of the conversation if none does). All of these must hold:

1. The reply right after the user's message asks the user questions about the plan's
   gaps: facts about the choir's situation and decisions that are the user's, such as
   the parts the first reply marked "not set" or listed as unknown or assumed. It does
   not answer with the plan again, a longer plan, or the assistant's own choices for
   those gaps.
2. No reply shows the plan again, or a new version of it, before the user has answered
   the questions of criterion 1 or ended the questioning (for example with "That's
   enough questions."). A summary of the user's answers so far, a decision table and a
   ready-to-use prompt are not the plan.

Fail if the assistant meets the user's acceptance with a plan built on its own guesses
instead of questions, or if it shows a revised plan before the user's answers are in.
