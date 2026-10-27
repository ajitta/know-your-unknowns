---
paths:
  - "skills/**/*.md"
  - "claude-code/agents/**/*.md"
---
# Writing skill and agent text

Skill and agent text is read by the model first and by maintainers second. Rule 0 decides what the plugin is for, rule 17 decides what stays in the text, and the other rules decide how it reads. Fix a hard-to-read passage that rule 17 keeps by restructuring it, not by cutting words: a model that loses the reason for a step tends to skip the step.

## Purpose

0. **The plugin serves three of the four cells of what the user and the AI know about a task, in any domain.** The cells are the Johari window's panes, adapted: self = the user, others = the AI, and the knowledge is about the task at hand, not about oneself. The pane names below are for developer documents; shipped text (skills, agents, descriptions, the plugin README) describes each cell in plain words, and each README names the panes once, where it credits the source.

   | Cell (user : AI) | Pane | Plain words in shipped text | What happens without the method | What the skills do | Skills |
   |---|---|---|---|---|---|
   | known : known | **Open** | what both of you know | The request is self-evident and the AI does it well. | Out of scope: do the request directly, without the method. | — |
   | unknown : known | **Blind** | what the user does not know and you do | The AI may build it right, but the user (or an approver) cannot judge it. | Surface the user's or the approvers' gaps. | teach-me, quiz, buy-in |
   | known : unknown | **Hidden** | what you do not know and the user does | The user keeps correcting the AI until the result comes out. | Ask or read back what the AI does not know or cannot judge, before deciding. | interview, reference |
   | unknown : unknown | **Unknown** | what neither the user nor you know yet | Output appears, but it is unlikely to achieve the outcome. The widest cell. | Surface both sides' unknowns: the user's and the AI's own. | blindspot, brainstorm, prototypes, deviation-log, tweakable-plan, unknowns-loop |

   **Output** is the artifact the AI produces; the **outcome** is the achievement that matches the user's ultimate intent. A result can meet every done criterion and still miss the outcome, so the last check, made with the user, is "did it achieve the outcome".

   Every skill decision follows this rule. Write methods, examples, triggers and deliverables for any domain (research, policy, events, hiring, personal decisions, code), with code as one example among several. A step earns its place when it moves the unknowns of the cell its skill serves toward the outcome.

   Reason: an AI-assisted task goes wrong where one side does not know what the other knows, or neither knows yet. The open cell needs no method, and every method sentence read there competes with the request.

## Steps

1. **One step, one action.** When a step holds several actions (parse input, ask, record, investigate), split it into sub-steps `a.`, `b.`, `c.` under the same number, so references to later step numbers stay valid.

   A lead line that groups the sub-steps adds nothing: no "only", no new verb. "Suggest another skill only in these cases:" added a restriction, and "Record the answers." suggested writing a file. Use a neutral lead ("Suggest the next skill:", "After the answers:") or none.

   A limit that covered the whole step ("Investigate only, no implementation") goes on its own line before `a.`, not inside `a.`.
2. **Write steps in execution order.** A word like "first" or "before" must name what it comes before. Two sentences that each claim to go first are a defect. The order includes what happens after a delegate returns: what you send the scout comes before what you do with its rows.
3. **Condition before action.** Write "When the scope is codebase-wide, use the scout", not "Use the scout; this applies to codebase-wide scope". A skill that needs a tool says what to do without it in one line, at most once per skill and worded the same everywhere (rule 11): "Without a tool, do the step in the conversation and say what could not be checked." Do not write per-host branches (no file system, no question tool, no sub-agent): the model already adapts to the tools it has, and a branch it never takes is read on every run.
4. **Keep the reason, once, at the end of the step.** One sentence saying why the step exists, after the instructions. Background (a paper, a method's history) goes after the instructions too, or into a references file, never between two instructions.

## Structure

5. **Tables for parallel items, cases and states.** When several items each get their own handling (① sure of / ② assuming / ③ can't judge), or a finding takes one of several statuses (*confirmed* / *inferred* / *unchecked*), give each one a row: name, when, what to do. Do not list the items and then refer back to them by number in prose.

   A cell states only what the prose stated. Write "—" rather than invent a definition the original never gave, and mark an example list "e.g." so the column does not read as complete.
6. **No paragraph-sized bullet.** A bullet or sentence that carries several conditions in parentheses (when the hook runs, when it doesn't, what to do in each case) becomes a short list or a table.
7. **Don't hard-wrap prose.** One line per paragraph or list item; let the editor wrap it. Split a line by what it carries (rule 6), not by its length. Don't reflow untouched text; convert a paragraph when you edit it.

   Inside a list item, split with a blank line and a new paragraph indented to the item's text, as here. A table inside a list item is indented the same way. Lines meant as separate items need a blank line or a list marker between them: consecutive lines with neither render as one paragraph.

## Wording

8. **Allow only one reading.** Spell out what happens when the user skips or declines ("If the user skips, run a full investigation; a skip never stops the pass"), not a phrase like "never block on it".
9. **One name per concept across all skills and agents.** Decided names: *kind* (blindspot cards and the scout's `Kind` column map 1:1), *done criteria*, *deviation* (an entry in the deviation log, `IMPLEMENTATION_NOTES.md` by default), *output* and *outcome* (Korean 산출물 and 성과; plain "outcome", with no qualifier), the cells in the plain words of rule 0's table (the pane names *Open*, *Blind*, *Hidden* and *Unknown* only in developer documents and once per README, credited as adapted from the Johari window), "did it achieve the outcome" for the final check, `## Iron Rules`, `## Related` for a section pointing at other skills.

   Refer to another skill only as the **name** skill (bold name, then "skill"), and write a skill's own name only in its frontmatter and title. A file then holds each skill name in one form, so a later rename is one search and replace.

   A shared term needs the same definition too, not only the same name. Do not reuse a defined term as a generic table header: `| Kind |` in deviation-log and tweakable-plan collided with blindspot's *kind*, so those tables use `Entry` and `Item type`.
10. **Bold marks a term the reader must find again**, not a whole sentence. A short rule the whole skill turns on may stay bold as a whole (**Execution order ≠ presentation order.**). A line with four bold phrases has no emphasis left.
11. **A sentence shared across skills is copied word for word.** Each skill loads alone, so repeating it is fine, but the copies must match so one grep finds and fixes them all. Known shared blocks:
    - the four finding kinds and the status labels (unknowns-scout, blindspot)
    - the independent-reviewer packet fields (buy-in, independent-reviewer)
    - the cell line and the Open line at the top of every skill body ("This skill serves <the cell in plain words>, …"; "A self-evident request, where both of you already know what to do, is done directly, without this method."), and "Self-evident requests are done directly." at the end of every skill description
    - the **Your own unknowns** sentence (brainstorm, prototypes, tweakable-plan, unknowns-loop)
    - the deviation log's default file ("the deviation log (`IMPLEMENTATION_NOTES.md` by default for code work)")
    - the missing-tool line ("Without a tool, do the step in the conversation and say what could not be checked.")
    - the reaction sentence's ending ("; a missing pick is undecided.") — each skill names its own items and deliverable
    - the blindspot ↔ teach-me order sentence (blindspot Scope, teach-me Related)
12. **Moving a sentence can change its meaning.**
    - Putting it under a sub-bullet or a condition, or taking it out, changes when it applies.
    - Splitting it can strand a qualifier that covered the whole sentence ("same structure", "in the page"). Keep the qualifier where it still covers every part.
    - Inserting a table or list between a sentence and the words that point back at it ("the same three options", "these", "this") changes what they point at. Re-read every such word below an inserted block and name the thing again.
    - Words like *also*, *so*, *otherwise* and pronouns lose what they pointed at when you split a sentence. Repeat the noun instead.

    If the original scope is unclear, keep the sentence where it was, log it as a **Todo for human** in `IMPLEMENTATION_NOTES.md`, and ask the user.

## Verify

13. **Before editing, find text that tests quote.** Grep `tests/` for phrases from the file. Tests pin what the package depends on: packaging, a portable build, trigger phrases, and the method's measured steps. When an authorized change removes a sentence a test quotes, rewrite the test to check what still matters instead of keeping the sentence for the test's sake. Grep `docs/` and `README*.md` too before renaming a heading or renumbering anything they cite.
14. **After editing, prove behavior did not change.**
    - Run `python -m unittest discover -s tests` and `claude plugin validate --strict plugins/unknowns` and `claude plugin validate --strict .`.
    - Read all of `git diff --word-diff=plain`, not just the start: every removed instruction must reappear somewhere.
    - That check says nothing about scope. In the 2026-10-10 rewrite, all five behavior changes passed it. For each moved or split sentence, compare what it covers before and after (rule 12).
    - Have someone who did not write the change make that comparison against `git show HEAD:<file>`, without the writer's explanation.
    - Run that skill's evals through `evals/run-manual.py`; `--verify` alone checks only the eval suite's structure. A file with no eval (`independent-reviewer` has none) was not tested with a model, so say so.

## Rewriting many files

15. **Decide shared names and sentences before splitting the work.** Rules 9 and 11 cannot be applied one file at a time. Before handing files to separate writers, fix the names and the exact text of every shared block, and give them to each writer. After they finish, check the set as a whole.
16. **A rewording pass fixes wording only.** An inconsistency that existed before the pass (two files giving opposite orders, a packet missing a field, two definitions of one kind) is a behavior decision. Log it as a **Todo for human** and leave the text as it was.

## What the text is for

17. **Every sentence makes the model do the method.** The plugin exists to surface and resolve the unknowns of rule 0's three cells: investigate the gap between the plan and the territory, teach the missing words, show alternatives to react to, ask what the AI cannot know or judge, put the AI's own unknowns next to the user's, label what is confirmed and what is assumed, log where the work departed from the plan, check that the user can explain the result, and check with the user that the result achieved the outcome. Keep a sentence only when it makes the model do one of those moves, or when one of them needs it (input, hand-off to another skill, the user's reaction).

    Cut guard prose:
    - prohibitions and stop-and-ask fences ("Never …", "Stop and ask before …")
    - read-only contracts, temporary-directory rules, never-commit and never-install lines
    - `tools:` allow-lists on agents
    - identity lines ("You are a …")
    - git workflow (a branch per agent, automatic commits, `isolation: worktree`)

    State the target behavior instead of the ban: "This pass ends at the improved prompt", not "Do not implement". Agents inherit every tool and may write code, tests and scripts and use git.

    Reason: a sentence guarantees nothing. A user who needs enforcement builds it into their own harness (permission modes, hooks, sandboxes), which does the job a sentence cannot, while every guard sentence is read on every run and competes with the method for the model's attention.
