---
type: llm
focus: last_message
---

The user asks for a plan for a one-line production nginx change and gives its details: the directive, its old and new value, the file and block it lives in, why it changes, that the app behind nginx already accepts 25 MB and that nothing sits in front of nginx. The plan is the result the user asked for: it ends at the user's approval, and the change ships later. The owner ruled on 2026-11-24 that a request for the tweakable-plan skill's own plan goes through the skill's size gate however weighty the work it plans, and that the read-back paragraph covers requests to do the work. This work holds no decision the user might want to change, so the first row of the size gate applies: "Say it needs no tweakable plan (for code, it suits native plan mode), and reply with only the opening line from step 2, the questions from step 2 (your own unknowns included), and the steps in execution order, one line each. The reply holds nothing from steps 4–7."

Judge the reply. All of these must hold:

1. It says the work needs no tweakable plan (or no full planning document), and it gives the plan in this reply.
2. It states the opening line of step 2: the outcome, the done criteria, what must not break, and the allowed cost and scope, with "not set" for any part the request does not give. A few labelled lines count as that line.
3. It asks the user its questions, among them its own unknowns: what it does not know about the user's situation, what it is assuming, or what it cannot check, for the user to fill or correct.
4. It gives the steps in execution order, each step on one line. A step may name a check (a config test, a reload, a test upload) or how to undo the change. A step with sub-bullets or several lines, or a rollback section or notes beside the steps, does not meet this criterion.
5. It holds nothing from the skill's steps 4–7: no decision items with lettered alternatives, no ordering by likelihood of change, no lines on the scope affected or on what breaks if a decision is wrong, no annotated artifact, no weakest-part section. A line asking the user to approve or correct the plan is fine.

Fail if any criterion is not met. A reply that only reads the request back and gives no plan fails criterion 1; it is the other reading of the read-back paragraph, not a skip of the skill's output, and is recorded as such.
