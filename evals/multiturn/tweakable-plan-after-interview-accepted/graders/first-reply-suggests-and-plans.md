---
type: llm
focus: transcript
---

The user asked for a plan for their choir's first tour abroad and said almost nothing
was decided: not where, not the dates, not how they travel, not who pays for what. The
tweakable plan's step 1b reads: "When the spec has big gaps, suggest the interview skill
and plan in the same reply, listing each gap under Your own unknowns in step 2; the plan
does not wait for an answer to the suggestion."

Judge the assistant's first reply only. All of these must hold:

1. It suggests settling the gaps through an interview: a round of questions for the
   user about them, whether or not it names an interview skill. Taking up the
   suggestion is left to the user.
2. The same reply gives the plan, without waiting for an answer to that suggestion: the
   plan opens with the outcome and the done criteria, and then gives decision items,
   each with the alternatives it considered. The suggestion may come before or after
   the plan.
3. Each big gap in the request (where, the dates, how they travel, who pays for what)
   appears in a list of what the assistant does not know, is assuming or cannot check,
   and the reply asks the user to fill or correct that list.

Fail if the first reply stops at the suggestion with no plan, if it gives the plan with
no suggestion of an interview, or if a big gap is missing from that list.
