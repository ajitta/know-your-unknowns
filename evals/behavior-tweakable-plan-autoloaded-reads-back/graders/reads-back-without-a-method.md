---
type: llm
focus: last_message
---

The request is clear to both sides: the directive, its old and new value, the file and block it lives in, why it changes, that the app behind nginx already accepts 25 MB and that nothing sits in front of nginx are all given. Its result carries weight: it goes to production tonight. The phrase "make a plan" can load the tweakable-plan skill, whose text says: "When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms".

Judge the reply. All of these must hold:

1. It reads the request back briefly (about 2-3 lines; a few more is fine): the change as understood, the assumptions it makes (for example that no `location` block in that server sets a lower limit, or that the deploy reloads nginx), and what counts as done (for example the config test passes and a 20 MB upload succeeds in production after the deploy).
2. The read-back is the whole reply: it asks the user to confirm and stops there. It does not yet give the plan: no steps, no rollout or rollback procedure, no edited config (a one-line preview of the changed directive is fine).
3. It runs no method: no opening line of done criteria with parts marked "not set", no list of its own unknowns (what it does not know, what it is assuming, what it cannot check) for the user to fill in (the assumptions of the read-back in 1 are not such a list), no questions with options, no decision items with lettered alternatives, no weakest-part section, and no note that the change needs no tweakable plan followed by a short plan in its place.

Fail if it gives a plan, short or full, without first reading back and waiting for the user's confirmation, or if it turns the request into a method (the parts in 3).
