---
type: llm
focus: last_message
---

The reply interviews the user before deciding the study design, asking for what only
the user can know. All of these must hold:
1. It asks questions and does not hand back a finished research design.
2. It asks at most 4 questions in this reply, each with a one-line reason. This is
   round 1, so the questions are open questions about the user's situation; options for
   the decisions may wait for a later round.
3. A question asking what the user is sure of and what they are assuming may come
   first. The other questions come in order of what a wrong decision would break: the research
   question's scope and design, and constraints that cannot be undone (ethics approval,
   access to participants, timeline), before minor choices.
4. The questions target what only the user can know: the advisor's expectations, their
   access, time, interests and constraints.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
