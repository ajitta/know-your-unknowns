---
type: llm
focus: last_message
---

The reply interviews the user before deciding, asking for what only the user can
know. All of these must hold:
1. It asks questions and does not produce a plan, schedule or venue choice yet.
2. It asks at most 4 questions in this reply, each with a one-line reason. This is
   round 1, so the questions are open questions about the user's situation; options for
   the decisions may wait for a later round.
3. A question asking what the user is sure of and what they are assuming may come
   first. The other questions come in order of what a wrong decision would break: the shape of the
   event and things that cannot be undone (budget commitments, who must be able to
   come, accessibility) before details of taste (theme, menu, decorations).
4. The questions target facts and decisions only the user holds (the family's
   constraints, relationships, who pays, priorities), not general trivia.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
