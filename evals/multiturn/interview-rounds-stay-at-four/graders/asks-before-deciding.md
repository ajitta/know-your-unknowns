---
type: llm
focus: transcript
---

The interview asks before it decides, and its deliverable is built from the answers.
All of these must hold:

1. Before the user has answered, no reply presents a decision table or implementation
   prompt with the open decisions already filled in by the assistant.
2. After the user's answers, a reply restates the decisions so far as an updated spec
   summary or a decision table.
3. The conversation ends (once the user asks for the write-up, or the decisions are in)
   with a decision table and a ready-to-use implementation prompt. The prompt applies
   the user's actual answers (for example email with an expiring link, workspace
   members only, 30-day file retention), does not contradict any of them, and marks
   decisions that were never asked or answered as unanswered / use judgment rather than
   inventing them.
4. The implementation prompt declares the architecture and data decisions fixed, says to
   flag conflicts before writing code, and ends with starting from a short plan.

Fail if the assistant decides open questions for the user without asking, if the
deliverable contradicts the user's answers, or if the conversation ends without the
decision table and implementation prompt.
