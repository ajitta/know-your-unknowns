---
paths:
  - "skills/**/*.md"
  - "agents/**/*.md"
---
# Writing skill and agent text

Skill and agent text is read by the model first and by maintainers second. Fix a hard-to-read passage by restructuring it, not by cutting words: a model that loses the reason for a step tends to skip the step.

## Steps

1. **One step, one action.** When a step holds several actions (parse input, ask, record, investigate), split it into sub-steps `a.`, `b.`, `c.` under the same number, so references to later step numbers stay valid.

   A lead line that groups the sub-steps adds nothing: no "only", no new verb. "Suggest another skill only in these cases:" added a restriction, and "Record the answers." suggested writing a file. Use a neutral lead ("Suggest the next skill:", "After the answers:") or none.

   A limit that covered the whole step ("Investigate only, no implementation") goes on its own line before `a.`, not inside `a.`.
2. **Write steps in execution order.** A word like "first" or "before" must name what it comes before. Two sentences that each claim to go first are a defect. The order includes what happens after a delegate returns: what you send the scout comes before what you do with its rows.
3. **Condition before action.** Write "When run as a **loop** stage, fold these options into the stage checkpoint", not "Run as a loop stage, this is not a separate question". A missing tool or surface goes last among the step's instructions, in one form: `No <tool or surface> → <what to do instead>`. The reason (rule 4) comes after it.

   Keep the original wording when the arrow form would force one reading: "No A or B →" means neither is available, while "Where they are unavailable" may mean either. A chain of fallbacks (an output ladder) keeps its chain form.
4. **Keep the reason, once, at the end of the step.** One sentence saying why the step exists, after the instructions. Background (a paper, a method's history) goes after the instructions too, or into a references file, never between two instructions.

## Structure

5. **Tables for parallel items, cases and states.** When several items each get their own handling (① sure of / ② assuming / ③ can't judge), or a field moves through states (`active` → `done` / `stopped`), give each one a row: name, when, what to do. Do not list the items and then refer back to them by number in prose.

   A cell states only what the prose stated. Write "—" rather than invent a definition the original never gave, and mark an example list "e.g." so the column does not read as complete.
6. **No paragraph-sized bullet.** A bullet or sentence that carries several conditions in parentheses (when the hook runs, when it doesn't, what to do in each case) becomes a short list or a table.
7. **Don't hard-wrap prose.** One line per paragraph or list item; let the editor wrap it. Split a line by what it carries (rule 6), not by its length. Don't reflow untouched text; convert a paragraph when you edit it.

   Inside a list item, split with a blank line and a new paragraph indented to the item's text, as here. A table inside a list item is indented the same way. Lines meant as separate items need a blank line or a list marker between them: consecutive lines with neither render as one paragraph.

## Wording

8. **Allow only one reading.** Spell out what happens when the user skips or declines ("If the user skips, run a full investigation; a skip never stops the pass"), not a phrase like "never block on it".
9. **One name per concept across all skills and agents.** Decided names: *kind* (blindspot cards and the scout's `Kind` column map 1:1), *done criteria*, *stage checkpoint*, `## Iron Rules`, `## Related` for a section pointing at other skills.

   A shared term needs the same definition too, not only the same name. Do not reuse a defined term as a generic table header: `| Kind |` in notes and plan collided with blindspot's *kind*, so those tables use `Entry` and `Item type`.
10. **Bold marks a term the reader must find again**, not a whole sentence. A short hard prohibition may stay bold as a whole (**Never create or edit files in the repository.**). A line with four bold phrases has no emphasis left.
11. **A sentence shared across skills is copied word for word.** Each skill loads alone, so repeating it is fine, but the copies must match so one grep finds and fixes them all. Known shared blocks:
    - the loop-stage sentence (blindspot, interview, reference, teach-me; plan's variant ends "carries the approval.")
    - the scorecard-capture sentence (loop step 10, quiz wrap-up)
    - the four finding kinds and the status labels (unknowns-scout, blindspot)
    - the independent-reviewer packet (loop step 8, `skills/loop/references/surfaces.md`)
    - each skill's Output ladder (`skills/loop/references/output-routing.md` defines it)
12. **Moving a sentence can change its meaning.**
    - Putting it under a sub-bullet or a condition, or taking it out, changes when it applies.
    - Splitting it can strand a qualifier that covered the whole sentence ("same structure", "in the page"). Keep the qualifier where it still covers every part.
    - Inserting a table or list between a sentence and the words that point back at it ("the same three options", "these", "this") changes what they point at. Re-read every such word below an inserted block and name the thing again.
    - Words like *also*, *so*, *otherwise* and pronouns lose what they pointed at when you split a sentence. Repeat the noun instead.

    If the original scope is unclear, keep the sentence where it was, log it as a **Todo for human** in `IMPLEMENTATION_NOTES.md`, and ask the user.

## Verify

13. **Before editing, find text that tests quote.** Grep `tests/` for phrases from the file and keep them word for word: `tests/test_agent_readonly_guard.py` quotes the reviewer's Bash allowances. Grep `docs/` and `README*.md` too before renaming a heading or renumbering anything they cite.
14. **After editing, prove behavior did not change.**
    - Run `python -m unittest discover -s tests` and `claude plugin validate .`.
    - Read all of `git diff --word-diff=plain`, not just the start: every removed instruction must reappear somewhere.
    - That check says nothing about scope. In the 2026-10-10 rewrite, all five behavior changes passed it. For each moved or split sentence, compare what it covers before and after (rule 12).
    - Have someone who did not write the change make that comparison against `git show HEAD:<file>`, without the writer's explanation.
    - Run that skill's evals through `evals/run-manual.py`; `--verify` alone checks only the eval suite's structure. A file with no eval (`independent-reviewer` has none) was not tested with a model, so say so.

## Rewriting many files

15. **Decide shared names and sentences before splitting the work.** Rules 9 and 11 cannot be applied one file at a time. Before handing files to separate writers, fix the names and the exact text of every shared block, and give them to each writer. After they finish, check the set as a whole.
16. **A rewording pass fixes wording only.** An inconsistency that existed before the pass (two files giving opposite orders, a packet missing a field, two definitions of one kind) is a behavior decision. Log it as a **Todo for human** and leave the text as it was.
