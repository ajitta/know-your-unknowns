---
type: llm
focus: last_message
---

The user asked a well-specified CSS question and named the output they want. All of
these must hold:

1. It answers the question — a flexbox snippet and a grid snippet that actually
   centre a child on both axes.
2. It does NOT teach the vocabulary of a domain, build a mental model or an ordering
   of concepts, and does NOT hand back a list of decisions the user must now make
   before they can ask properly.
3. It does not open a staged workflow or ask for the task's blast radius, done
   criteria or constraints before answering.

Fail if the response turns a known-answer question into a vocabulary lesson, or if it
asks clarifying questions instead of answering.
