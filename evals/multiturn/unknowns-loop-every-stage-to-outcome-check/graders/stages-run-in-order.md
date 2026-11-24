---
type: llm
focus: transcript
---

The facts of this conversation: the user asked for the operating loop on a small non-code task. Their 14-member book club moves its monthly meetings from a cafe with two steps at the door to the public library's free community room, so that all members, including Ruth and Sam, who use wheelchairs, can come and take part again. The user had already chosen the library room and said they would do the booking and the emails themselves. The move rests on assumptions nobody had checked when the conversation began (that the room is free on second Thursdays, 7:00-8:30 pm; that the library is open that late; that Ruth and Sam can get in on their own), which the user lists as unchecked when asked.

The loop's stages before the work, in run order, are: investigate (a blind-spot pass on the plan: findings and an improved prompt); decide (questions on decisions the requirements leave open); shape (options, versions or a reference, for an approach not yet chosen); test the riskiest assumption (state the most uncertain assumption with what result would confirm it and what would refute it, then the cheapest check of only that assumption, such as a phone call); plan (a plan the user approves). After them come the work, a verification against the done criteria and an outcome check.

Judge the whole conversation. All of these must hold:

1. The first reply names the loop's stages in run order (in any wording; the steps after the work may be grouped) and marks which one is current. When the first reply is only a read-back of the request, the next reply does this instead.
2. Each of the five stages before the work either runs, with its own result shown in a reply, or is named as skipped with a reason (for example "Shape: skipped, you have already chosen the library room"). Investigate and plan run. Test the riskiest assumption runs, because the move rests on those unchecked assumptions: before the plan, a reply names the assumption it tests with what result would confirm it and what would refute it, and asks the user for a check of it, and a later reply, still before the plan, takes up the result of that check. When that check was asked for during an earlier stage, the stage may be named as already answered, but the assumption that check tested and its result must still appear before the plan.
3. The stages come in that order: the investigation's findings come before any plan; the result of the assumption check comes before the plan; the plan comes before the assistant handles the user's report of the work; the verification and the outcome check come after that report.
4. No stage is merged into another: no stage's result appears only inside a later stage's deliverable (for example the investigation's findings given only as notes inside the plan), and the plan is not presented before the result of the assumption check it depends on. Two stages may share a reply when each one's own result appears there in order.

Fail if a stage before the work disappears without being named as skipped, if the plan comes before the investigation's findings or before the result of the assumption check, or if a stage is merged into another as item 4 describes.
