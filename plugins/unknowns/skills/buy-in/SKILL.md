---
name: buy-in
description: >
  The buy-in doc — before asking someone to approve the work, surface what the approvers
  do not know and will object to, answer each point with evidence, state the limitations,
  and name who signs off. Any approval: a director signing a policy, a funder, a client,
  a committee, a code reviewer. Use when the user says "buy-in doc", "prep me for review",
  "get sign-off", or before requesting review, approval or merge. Self-evident requests are done directly.
---

# Buy-in — Approvers' Unknowns Doc (The Buy-In Doc)

This skill serves the **Blind** cell (Johari window, adapted: the user does not know what you know), and surfaces the approvers' gaps. A self-evident request, where both of you already know what to do (the **Open** cell), is done directly, without this method.

The work is done, but the approvers have not seen what the user has, and the user does not yet know how they will react. Approval turns on what the approvers do not know, so the doc finds those gaps and fills them with evidence before the meeting, not in it.

## Procedure

1. Identify the target and the inputs:

   a. Identify the target work and the approvers (reviewers, a director, a funder, a client, a committee) from the text the user gave with the request or after the skill name. No arguments → this session's finished work, approvers = its reviewers.

   b. Take as inputs the plan or spec, the prototype or draft, and the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work).

   Without a tool, do the step in the conversation and say what could not be checked.
2. **Map the approvers' unknowns**:

   a. For each approver, list what they do not know about the work that their decision depends on, and the objections they are likely to raise (~5 in total).

   b. Ask the user what they know about each approver that you cannot: their priorities, past objections, what they are measured on, the unwritten politics around the decision. Mark each point that neither of you knows as a question to find out before asking for approval, with who could answer it.
3. **Lead with the result shown**: open with what the work does or delivers, shown rather than described (a running demo or screenshot for software; a sample, an excerpt, a pilot result or a budget table otherwise), so an approver sees the result before reading the rest. When nothing can be shown, say so and list it under the known limitations (step 5).
4. **Answer each unknown and objection with evidence**:

   a. Answer each item from step 2 with **evidence**, and give every answer a reference the approver can follow (spec §, deviation log entry date, metric, source document, test run, `file:line`).

   b. Use the `unknowns:independent-reviewer` agent to check the evidence, including its "verified OK" list. Hand it the done criteria, the outcome, the approved plan, the deviation log, the deliverable (for code, the diff range or touched files and how to run the tests), and the claims the work rests on; leave out the producer's own summary, so the review checks the work rather than the narrative.

   c. Move every answer that has no evidence, or whose evidence the reviewer could not confirm, to the known limitations (step 5).
5. **Known limitations and unresolved unknowns**: if a deviation log exists (file or in-conversation), pull its recorded deviations and unresolved risks here, with the questions from step 2b nobody could answer yet. Not hiding is the basis of trust.
6. **Who signs off**: name the people or teams who must approve, with roles, and what each will check.

## Output

Reaction: number the approvers' unknowns, objections, limitations and sign-off entries; the user marks each keep or revise and answers the step 2b questions they can, and the answers assemble into the final doc; a missing pick is undecided.
