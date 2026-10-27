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

1. **The pass ends at the improved prompt**: the investigation exists to help the user write a better prompt, and implementation starts from the user's next prompt.

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

   c. Restate the three lists verbatim in your reply before investigating, or say the user skipped them. Step 4 marks findings against them, so they must exist before any finding does.

2. Choose how to investigate by scope:

   | Scope of the task (not the size of the repo) | How to investigate |
   |---|---|
   | The task spans the codebase or many modules | Use the `unknowns:unknowns-scout` agent. |
   | The task touches a few files | Investigate directly. |

   When you spawn the scout, hand it a packet:

   - the user's original prompt, verbatim
   - ② what the user is assuming, to check first
   - the context sources
   - the target area and its entry points
   - what to return: a finding table and an improved prompt draft

   When the scout returns, map its rows onto the card kinds in step 3.

   Investigate in this order: ②'s assumptions, then any given sources (git history, docs, specific modules), then the rest. Look for each assumption in the given sources first.

   Without a tool, do the step in the conversation and say what could not be checked.

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

   b. After the contrast, show the cards. Each card holds: kind, finding, why it bites, evidence, status, recommended action. Mark each finding that none of the user's three lists mentioned as **new to you**, so the user sees what the pass taught them rather than recalling it afterwards.

   c. Sort the cards by **likelihood × blast radius**: how likely *this task* is to hit the finding, times how much breaks if it does. A severe landmine in code the task never touches ranks below a modest convention every new line must follow.

5. End with an **improved prompt draft** that reflects the findings. The draft names the execution order and ends with an explicit checkpoint ("stop and show me the plan before writing code"). Present the draft as the prompt to paste next; the user's prompt-fix picks edit it.

6. Suggest the next skill:

   - When undecided items that could change the architecture surface, suggest the **interview** skill next.
   - When ③ has items and teach-me has not run for this task yet, or the user lacks the unfamiliar domain's vocabulary itself, suggest the **teach-me** skill.

## Output

Reaction: a numbered, copyable **prompt fix** per finding card; the user's selected numbers assemble into the improved prompt draft; a missing pick is undecided.

## Scope

Not limited to application code: specs, migrations, infra and vendor integrations also have landmines and unwritten conventions. The subject is always a **specific codebase, plan or system** and its blind spots. If the gap is the user's **vocabulary** for an unfamiliar field, use the **teach-me** skill instead. Running both is fine: when the user cannot yet describe the task, run **teach-me** first; otherwise run **blindspot** first and hand its ③ list (where the user does not know how to judge) to teach-me.
