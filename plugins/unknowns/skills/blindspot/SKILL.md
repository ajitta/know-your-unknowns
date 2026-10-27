---
name: blindspot
description: >
  Blind-spot pass — investigate unknown unknowns before implementation and turn them
  into a better prompt. Use when the user says "blind spot pass", "what am I missing",
  "unknown unknowns", or before work in an
  unfamiliar codebase area — run it even when you could answer directly, because the
  deliverable is the improved prompt, not the answer. Not for routine, well-understood tasks.
---
# Blindspot Pass — Blind-Spot Investigation

Before implementation, find the gap between the **map** (plan/prompt) and the **territory** (actual codebase, domain, constraints).

## Iron Rules

1. **Do not implement yet.** Make no code changes while this skill is active.
2. End goal of the investigation: help the user **write a better prompt**.

## Procedure

1. Start the pass:

   a. Parse the task description and context sources from the text the user gave with the request or after the skill name. With no request text, use the task under discussion. When there is no task under discussion either, ask one question for the task before step 1b.

   b. Before investigating, ask once for three lists:

   | List | What to do with it |
   |---|---|
   | ① What the user is already sure of | It narrows the scope. Ask how recent that certainty is. |
   | ② What the user is assuming | It is the **first** thing to check (step 2), not something to skip. |
   | ③ Where the user does not know how to judge | It points at the **teach-me** skill. |

   If the user skips, run a full investigation; a skip never stops the pass.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

   c. Record the three lists verbatim, before investigating:

   - When a loop runs, record them in `.unknowns/loop.json` as `baseline`.
   - Otherwise, restate them in your reply right then.

   No file system → print the record in the chat as Markdown and say to save it as the baseline for `.unknowns/loop.json`.

   The three lists are the before-picture the scorecard compares findings against, so they must exist before any finding does.

2. Choose how to investigate by scope:

   | Scope | How to investigate |
   |---|---|
   | Codebase-wide or large | Use `unknowns:unknowns-scout` when the host can start a sub-agent of that name. |
   | A few files | Investigate directly with the available read and search tools. |

   When you spawn the scout, hand it a packet:

   - the user's original prompt, verbatim
   - ② what the user is assuming, to check first
   - the context sources
   - the target area and its entry points
   - what to return: a finding table and an improved prompt draft

   When the scout returns, map its rows onto the card kinds in step 3.

   Investigate in this order: ②'s assumptions, then any given sources (git history, docs, specific modules), then the rest. Look for each assumption in the given sources first.

   Keep the scout pass read-only: never create or modify files, run implementation commands, or invent findings. Read available history records; hand history questions that require unavailable tools back to the caller. No sub-agent → do the pass yourself as a separate step and label it "Scout pass performed by the assistant"; say what one pass could not cover. No file access or search tools → investigate the supplied material and list missing sources under **Needs checking**. Details: references/surfaces.md

3. Compile the findings:

   a. Tag each finding with a **kind**:

   | Kind | What it is |
   |---|---|
   | Landmine | Touching this breaks something non-obvious (regression risk, fragile or missing tests, a module mid-migration). |
   | Convention | An unwritten rule the codebase enforces. |
   | Missing concept | A mechanism the user's prompt has no word for. |
   | History | A past attempt, revert or hairy dead end that explains why the code looks this way. |

   b. Give each finding **evidence** (`file:line`, commit hash, or doc URL) and a **status**:

   | Status | Meaning |
   |---|---|
   | *confirmed* | You read it. |
   | *inferred* | It follows from what you read, or from how such systems usually work. Say which. |
   | *unchecked* | You have not checked it. |

   Keep unchecked items out of the cards and the tally; list them under **Needs checking**.

   c. Besides the findings, collect the **questions to answer** and the **information still needed** to sharpen the prompt.

4. Present the findings:

   a. Open the output with the three lists from step 1c. Then lead the findings with the contrast: **What you asked for** (the task as the user framed it, and why it sounds small) vs **What you're actually walking into**, with a tally by kind ("4 landmines, 2 conventions, 1 missing concept, 1 history finding").

   b. After the contrast, show the cards. Each card holds: kind, finding, why it bites, evidence, status, recommended action.

   c. Sort the cards by **likelihood × blast radius**: how likely *this task* is to hit the finding, times how much breaks if it does. A severe landmine in code the task never touches ranks below a modest convention every new line must follow.

5. End with an **improved prompt draft** that reflects the findings. The draft names the execution order and ends with an explicit checkpoint ("stop and show me the plan before writing code"). The draft is the core deliverable of this skill.

6. Offer once: proceed with this prompt now / edit it first / stop here. When run as a **loop** stage, do not ask this separately: the loop's stage checkpoint carries these options.

   Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

7. Suggest the next skill:

   - When undecided items that could change the architecture surface, suggest the **interview** skill next.
   - When ③ has items and teach-me has not run for this task yet, or the user lacks the unfamiliar domain's vocabulary itself, suggest the **teach-me** skill.

## Output

Deliver Markdown in the conversation, keeping this skill's structure. End the turn with the assembled reply as Markdown in the conversation.
Reaction: a numbered, copyable **prompt fix** per finding card; the user's selected numbers assemble into the improved prompt draft.

For numbered reactions and reply assembly, read references/output-routing.md.

## Scope

Not limited to application code: specs, migrations, infra and vendor integrations also have landmines and unwritten conventions. The subject is always a **specific codebase, plan or system** and its blind spots. If the gap is the user's **vocabulary** for an unfamiliar field, use the **teach-me** skill instead. Running both is fine: when the user cannot yet describe the task, run **teach-me** first; otherwise run **blindspot** first and hand its ③ list (where the user does not know how to judge) to teach-me.
