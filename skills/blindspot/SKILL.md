---
name: blindspot
description: >
  Blind-spot pass — investigate unknown unknowns before implementation and turn them
  into a better prompt. Use when the user says "blind spot pass", "what am I missing",
  "unknown unknowns", or before work in an
  unfamiliar codebase area — run it even when you could answer directly, because the
  deliverable is the improved prompt, not the answer. Not for routine, well-understood tasks.
argument-hint: "<task description or target area> [context sources: git/docs/slack etc.]"
---
# Blindspot Pass — Blind-Spot Investigation

Before implementation, find the **gap between the map (plan/prompt) and the territory
(actual codebase, domain, constraints)**.

## Iron Rules

1. **Do not implement yet.** Make no code changes while this skill is active.
2. End goal of the investigation: help the user **write a better prompt**.

## Procedure

1. Parse the task description and context sources from `$ARGUMENTS`. Empty → the task
   under discussion; if there is none, ask one question first. Investigate any given
   sources (git history, docs, specific modules) first.
   **Before investigating, ask once** (one AskUserQuestion, or one message) for three
   lists: ① what the user is already sure of, ② what they are assuming, ③ where they do
   not know how to judge. ① narrows the scope; ask how recent that certainty is.
   ② is the **first** thing to check, not something to skip. ③ points at the
   **teach-me** skill. A skip means a full investigation; never block on it.
   Record the three lists **verbatim before investigating**: in `.unknowns/loop.json` as
   `baseline` when a loop runs, otherwise restated in your reply right then. The output's
   first section copies them later. They are the before-picture the scorecard compares
   findings against, so they must exist before any finding does.
2. Scope codebase-wide or large → spawn the `unknowns:unknowns-scout` agent with the
   Agent tool. Hand it a packet: the user's original prompt verbatim, the context
   sources, the target area and its entry points, and what to return (finding table +
   improved prompt draft). Map its rows onto the card kinds below.
   Scope is a few files → investigate directly with Read/Grep/Glob. No Agent tool in this
   session → investigate directly too, and say the scope was narrowed to one pass
   (${CLAUDE_PLUGIN_ROOT}/skills/loop/references/surfaces.md).
3. Compile findings, each tagged with a kind:
   - **Landmine** — touching this breaks something non-obvious (regression risk, fragile
     or missing tests, a module mid-migration)
   - **Convention** — an unwritten rule the codebase enforces
   - **Missing concept** — a mechanism the user's prompt has no word for
   - **History** — an earlier or reverted attempt at this exact task
   Each finding also carries **evidence** (`file:line`, commit hash, or doc URL) and a
   **status**: *confirmed* (you read it), *inferred* (follows from what you read, or from
   how such systems usually work — say which), or *unchecked*. Keep unchecked items out of
   the cards and the tally; list them under **Needs checking**. Also collect the
   **questions to answer** and the **information still needed** to sharpen the prompt.
4. Lead with the contrast: **What you asked for** (the task as the user framed it, and why
   it sounds small) vs **What you're actually walking into**, with a tally by kind
   ("4 landmines, 2 conventions, 1 missing concept, 1 reverted attempt"). Then the cards —
   kind, finding, **why it bites**, evidence, status, recommended action — sorted by
   **likelihood × blast radius**: how likely *this task* is to hit it, times how much breaks
   if it does. A severe landmine in code the task never touches ranks below a modest
   convention every new line must follow.
5. End with an **improved prompt draft** that reflects the findings — the core
   deliverable of this skill. It names the execution order and ends with an explicit checkpoint ("stop and show me the plan
   before writing code").
6. Offer with one AskUserQuestion: proceed with this prompt now / edit it first / stop here. Run as a **loop** stage, this is not a separate question: the loop's stage checkpoint carries these options.
7. If undecided items that could change the architecture surface, suggest the
   **interview** skill next. If the user lacks the unfamiliar domain's vocabulary itself,
   suggest the **teach-me** skill.

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-blindspot-<slug>.html`; else markdown.
Reaction control: a copyable **prompt fix** per card; selected fixes assemble into the improved prompt draft.
Details: ${CLAUDE_PLUGIN_ROOT}/skills/loop/references/output-routing.md

## Scope

Not limited to application code: specs, migrations, infra and vendor integrations also
have landmines and unwritten conventions. The subject is always a **specific codebase,
plan or system** and its blind spots. If the gap is the user's **vocabulary** for an
unfamiliar field, use the **teach-me** skill instead. Running both is fine: teach-me
first for the words, blindspot for the territory.
