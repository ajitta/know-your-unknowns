---
name: blindspot
description: >
  Blind-spot pass — before work on a plan or system in any domain, investigate the
  unknown unknowns on both sides (what the user has not seen, what the AI does not know
  about their situation) and turn them into a better prompt. Use on "blind spot pass",
  "what am I missing", "unknown unknowns", or before work whose territory neither side
  has checked; run it even when you could answer directly, because the deliverable is
  the improved prompt. Clear to both: no skill or method; if weighty (ships, is sent,
  hard to undo), first read back request, assumptions and what done means in 2–3 lines;
  a mismatch goes to teach-me, interview or blindspot.
---
# Blindspot Pass — Blind-Spot Investigation

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

When you and the user both seem to understand the request, do it without this method: if its result carries weight, first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

Before the work starts, find the gap between the **map** (the plan or prompt) and the **territory** (the actual situation: its documents, rules, people, data, or codebase).

## Iron Rules

1. **The pass ends at the improved prompt**: the investigation exists to help the user write a better prompt, and the work starts from the user's next prompt.

## Procedure

1. Start the pass:

   a. Parse the task description and context sources from the text the user gave with the request or after the skill name. With no request text, use the task under discussion. When there is no task under discussion either, ask one question for the task before step 1b.

   b. Before investigating, ask once for the user's three lists, and put your own three lists next to them:

   | List | Whose | What to do with it |
   |---|---|---|
   | ① What the user is already sure of | the user's | It narrows the scope. Ask how recent that certainty is. |
   | ② What the user is assuming | the user's | It is the **first** thing to check (step 2), not something to skip. |
   | ③ Where the user does not know how to judge | the user's | It points at the **teach-me** skill. |
   | ④ What you do not know about the user's situation | yours | Each item is a question only the user can answer; it goes under **Questions to answer**. |
   | ⑤ What you are assuming | yours | Check it alongside ② (step 2). |
   | ⑥ What you cannot check from here | yours | It goes under **Needs checking**, with who or what could check it. |

   If the user skips, run a full investigation; a skip never stops the pass. The three-list question and your own three lists are the whole opening reply: every finding, the most urgent included, follows the answer or the skip.

   c. Restate the user's three lists verbatim in your reply before investigating, or say the user skipped them, and update your own lists with the answers. Step 4 marks findings against the user's lists, so they must exist before any finding does.

2. Choose how to investigate by scope:

   | Scope of the task (not the size of the material) | How to investigate |
   |---|---|
   | The task spans many sources (a whole codebase or many modules, a large body of documents or records) | Use the `unknowns:unknowns-scout` agent. |
   | The task touches a few files or documents | Investigate directly. |

   When you spawn the scout, hand it a packet:

   - the user's original prompt, verbatim
   - ② what the user is assuming and ⑤ what you are assuming, to check first
   - the context sources
   - the target area and where to start in it
   - what to return: a finding table and an improved prompt draft

   When the scout returns, map its rows onto the card kinds in step 3.

   Investigate in this order: ② and ⑤ (the assumptions on both sides), then any given sources (documents, data, history, a codebase), then the rest. Look for each assumption in the given sources first.

   Without a tool, do the step in the conversation and say what could not be checked.

3. Compile the findings:

   a. Tag each finding with a **kind**:

   | Kind | What it is |
   |---|---|
   | Landmine | Touching this breaks something non-obvious (a regression risk, a rule with penalties, a dependency mid-change, fragile or missing checks). |
   | Convention | An unwritten rule the territory enforces (a codebase, an organisation, a funder, a community). |
   | Missing concept | A mechanism the user's prompt has no word for. |
   | History | A past attempt, reversal or dead end that explains why things are the way they are. |

   b. Give each finding **evidence** (`file:line`, commit hash, doc URL, or a section, clause or record the user can open) and a **status**:

   | Status | Meaning |
   |---|---|
   | *confirmed* | You read it. |
   | *inferred* | It follows from what you read, or from how such situations usually work. Say which. |
   | *unchecked* | You have not checked it. |

   Keep unchecked items out of the cards and the tally; list them under **Needs checking**.

   c. Besides the findings, collect the **questions to answer** (④ and new ones) and the **information still needed** to sharpen the prompt.

4. Present the findings:

   a. Open the output with the user's three lists from step 1c and your own three lists as updated, each of your ⑤ assumptions marked confirmed, refuted or still unchecked. Then lead the findings with the contrast: **What you asked for** (the task as the user framed it, and why it sounds small) vs **What you're actually walking into**, with a tally by kind ("4 landmines, 2 conventions, 1 missing concept, 1 history finding").

   b. After the contrast, show the cards. Each card holds: kind, finding, why it bites, evidence, status, recommended action. Mark each finding that none of the user's three lists mentioned as **new to you**, so the user sees what the pass taught them rather than recalling it afterwards.

   c. Sort the cards by **likelihood × blast radius**: how likely *this task* is to hit the finding, times how much breaks if it does. A severe landmine in a part the task never touches ranks below a modest convention every new piece of the work must follow.

   d. After the cards, list **Questions to answer**, **Needs checking** and **Information still needed**: what the pass could not settle, and who can settle it.

5. End with an **improved prompt draft** that reflects the findings and the user's answers to the questions. The draft names the execution order and ends with an explicit checkpoint ("stop and show me the plan before doing the work"). Present the draft as the prompt to paste next; the user's prompt-fix picks edit it.

6. Suggest the next skill:

   - When undecided items that could change the shape of the work surface, suggest the **interview** skill next.
   - When ③ has items and teach-me has not run for this task yet, or the user lacks the unfamiliar domain's vocabulary itself, suggest the **teach-me** skill.

## Output

Reaction: a numbered, copyable **prompt fix** per finding card; the user's selected numbers assemble into the improved prompt draft; a missing pick is undecided.

## Scope

Not limited to code: a funding call, a policy, an event, a study, infrastructure and vendor integrations all have landmines and unwritten conventions. The subject is always a **specific plan, system or situation** and its blind spots. If the gap is the user's **vocabulary** for an unfamiliar field, use the **teach-me** skill instead. Running both is fine: when the user cannot yet describe the task, run **teach-me** first; otherwise run **blindspot** first and hand its ③ list (where the user does not know how to judge) to teach-me.
