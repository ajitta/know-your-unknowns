# Scorecard capture — the plugin's only measurement

Referenced by the `loop` skill's value review (step 10) and the `quiz` wrap-up, the two points where a piece of work ends and the user still remembers what happened.

Background: `docs/value-contract.md` promises this plugin earns its place only when it surfaces something the user did not know **and** that changes a decision. That claim is worthless without recorded rows, and asking days later produces fiction.

## What to do

1. **Check eligibility, then ask the two questions.** Do not ask twice for one piece of work. Apply these conditions before asking or writing:

   | Case | What to do |
   |---|---|
   | The loop already captured a row at step 10 for this piece of work | The quiz wrap-up says so and skips the capture instead of asking again. |
   | The user abandoned the work | Skip the capture entirely. |
   | No unknowns skill actually did anything in the run | Skip the capture entirely. |

   Otherwise, capture the row as follows.

   a. When blindspot recorded the user's pre-investigation lists (sure of / assuming / cannot judge — in `loop.json` `baseline` or the blindspot output), show the findings next to those lists before asking the questions in step 1c, marking each finding that no list mentioned. The question is then about that marked set, not a recollection.

   b. Record in **Baseline** whether this row was `compared` or had `none`.

   c. **Never answer these for the user.** Only they can say whether they already knew something. A row you invented is worse than no row: it corrupts the one signal the plugin has about its own value.

   Ask the user these two questions in one round, splitting tool calls only if the tool requires it:

   - "Did this surface something you did not already know?" — options: yes / no.
   - "Did it change a decision?" — options: yes / no.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

   d. Follow up in free text for the one-line "what", only for answers that were yes.

   The findings go next to the lists before the questions because memory of what one "already knew" drifts toward yes once the answer has been seen.

2. **Append the row.**

   a. Append the row to `.unknowns/scorecard.md` in the current project, creating the file with the two header lines below if it does not exist. Write the row **even when both answers are no.** The value contract's demotion and removal conditions fire only on recorded zeros, so a skipped no-row silently protects a skill that is not earning its place.

   b. Offer once to add `.unknowns/` to `.gitignore`.

   No file system → print the record in the chat as Markdown and say to save it as `.unknowns/scorecard.md`. Include the header and all saved rows so the user can save the whole updated scorecard; see `surfaces.md` in this folder.

## File format

```markdown
| # | Date | Task | Skills used | Learned something? | Changed a decision? | Note | Recheck on | Reality check | Baseline |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-06 | <task in one line> | blindspot → plan | yes — <what they did not know> | no | <note> | 2026-10-06 — <what to look at> | | compared |
```

- Number rows sequentially from the existing file.
- Keep each cell to one line.
- **Recheck on** comes from the loop's value review: the date the user chose and what to look at.
- Leave **Reality check** empty; the loop fills it when it starts after the Recheck on date.
- The quiz wrap-up leaves Recheck on and Reality check empty unless the user names a date.

**Older files.** New columns are only ever added at the **end**, so an existing file is migrated by extending the header and separator lines alone: append whichever of Recheck on, Reality check, Baseline it lacks, in that order. Never insert a column mid-table or move existing cells; filling an empty Reality check cell is fine. A shifted row silently moves every answer under the wrong heading.

When the value contract's ratio is computed, report `compared` rows separately — they are the ones a changed mind cannot have rewritten (see `docs/value-contract.md`).
