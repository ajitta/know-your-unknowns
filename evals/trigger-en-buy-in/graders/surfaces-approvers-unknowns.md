---
type: llm
focus: last_message
---

The response prepares the work for approval by surfacing what the approvers do not know and will object to. All of these must hold:

1. It leads with what the work does, or shows it working, rather than with implementation detail; when nothing can be shown, it says so.
2. It names what the approvers do not know or will object to, and answers each with evidence rather than assertion.
3. It states the limitations or known gaps explicitly, including what neither the user nor the assistant knows yet about the approvers' reaction (as questions to find out or to ask the user).
4. It names who has to sign off, or asks who the approvers are.

Fail if it is only a summary of the diff or a persuasive pitch with no open points, or if it omits limitations.
