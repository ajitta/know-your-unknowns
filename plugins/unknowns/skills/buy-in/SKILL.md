---
name: buy-in
description: >
  The buy-in doc — before asking for approval of any work, surface what the approvers do
  not know and will object to, answer each point with evidence, state the limitations,
  and name who signs off. Use on "buy-in doc", "prep me for review", "get sign-off", or
  before requesting review, approval or merge. Clear to both: no skill or method; if
  weighty (ships, is sent, hard to undo), first read back request, assumptions and what
  done means in 2–3 lines; a mismatch goes to teach-me, interview or blindspot.
---

# Buy-in — The Buy-In Doc

This skill serves what the user does not know and you do, and surfaces the approvers' gaps.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

The work is done, but the approvers have not seen what the user has, and the user does not yet know how they will react. Approval turns on what the approvers do not know, so the doc finds those unknowns and answers them with evidence before the meeting, not in it.

## Procedure

1. Identify the target and the inputs:

   a. Identify the target work and the approvers (reviewers, a director, a funder, a client, a committee) from the text the user gave with the request or after the skill name. No arguments → this session's finished work, approvers = its reviewers.

   b. Take as inputs the done criteria and the outcome the work is for, the approved plan or spec, the deliverable (the prototype, draft or change), and the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work).

   Without a tool, do the step in the conversation and say what could not be checked.
2. **Map the approvers' unknowns**:

   a. For each approver, list what they do not know about the work that their decision depends on, and the objections they are likely to raise (~5 in total).

   b. Ask the user what they know about each approver that you cannot: their priorities, past objections, what they are measured on, the unwritten politics around the decision. Mark each point that neither of you knows as a question to find out before asking for approval, with who could answer it.
3. **Lead with the result shown**: open with what the work does or delivers, shown rather than described (a running demo or screenshot for software; a sample, an excerpt, a pilot result or a budget table otherwise), so an approver sees the result before reading the rest. When nothing can be shown, say so and list it under the known limitations (step 5).
4. **Answer each unknown and objection with evidence**:

   a. Answer each item from step 2 with **evidence**, and give every answer a reference the approver can follow (spec §, deviation log entry date, metric, source document, test run, `file:line`).

   b. Use the `unknowns:independent-reviewer` agent to check the evidence, including its "verified OK" list. Hand it the done criteria, the outcome, the approved plan, the deviation log, the deliverable (for code, the diff range or touched files and how to run the tests), and the claims the work rests on; leave out the producer's own summary, so the review checks the work rather than the narrative.

   c. Move every answer that has no evidence, or whose evidence the independent-reviewer agent could not confirm, to the known limitations (step 5).
5. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here, with the questions from step 2b nobody could answer yet. Not hiding is the basis of trust.
6. **Who signs off**: name the people or teams who must approve, with roles, and what each will check.

## Output

Reaction: number the approvers' unknowns, objections, limitations and sign-off entries; the user marks each keep or revise and answers the step 2b questions they can, and the kept entries and the user's answers assemble into the final doc; a missing pick is undecided.
