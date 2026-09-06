# Scorecard capture — the plugin's only measurement

Referenced by the `loop` skill's value review (step 10) and the `quiz` wrap-up, the two
points where a piece of work ends and the user still remembers what happened.

Background: `docs/value-contract.md` promises this plugin earns its place only when it
surfaces something the user did not know **and** that changes a decision. That claim is
worthless without recorded rows, and asking days later produces fiction.

## What to do

1. Ask the user with **one** `AskUserQuestion` call carrying exactly these two questions
   (the tool's hard cap is 1–4):
   - "Did this surface something you did not already know?" — options: yes / no.
   - "Did it change a decision?" — options: yes / no.
   Follow up in free text for the one-line "what", only for answers that were yes.
2. **Never answer these for the user.** Only they can say whether they already knew
   something. A row you invented is worse than no row: it corrupts the one signal the
   plugin has about its own value.
3. Append the row to `.unknowns/scorecard.md` in the current project, creating the file
   with the two header lines below if it does not exist. Offer once to add `.unknowns/`
   to `.gitignore`.
4. Write the row **even when both answers are no.** The value contract's demotion and
   removal conditions fire only on recorded zeros, so a skipped no-row silently protects
   a skill that is not earning its place.

## File format

```markdown
| # | Date | Task | Skills used | Learned something? | Changed a decision? | Note |
|---|------|------|-------------|--------------------|---------------------|------|
| 1 | 2026-09-06 | <task in one line> | blindspot → plan | yes — <what they did not know> | no | <note> |
```

Number rows sequentially from the existing file. Keep each cell to one line.

## When to skip

Do not ask twice for one piece of work: if the loop already captured a row at step 10,
the quiz wrap-up says so instead of asking again. Skip the capture entirely for work the
user abandoned, and for a run where no unknowns skill actually did anything.
