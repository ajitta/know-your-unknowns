---
name: blindspot
description: >
  Blind-spot pass — investigate unknown unknowns before implementation and turn them
  into a better prompt. Use when the user says "blind spot pass", "what am I missing",
  "unknown unknowns", or before work in an
  unfamiliar codebase area. Not for routine, well-understood tasks.
argument-hint: "<task description or target area> [context sources: git/docs/slack etc.]"
---

# Blindspot Pass — Blind-Spot Investigation

Before implementation, find the **gap between the map (plan/prompt) and the territory
(actual codebase, domain, constraints)**.
Origin: Blindspot Pass — see skills/loop/references/talk-source.md

## Iron Rules

1. **Do not implement yet.** No code changes while this skill is active.
2. End goal of the investigation: help the user **write a better prompt**.

## Procedure

1. Parse task description and context sources from `$ARGUMENTS`. Empty → the task
   currently under discussion; if there is none, ask one question first. If sources are
   given (git history, docs, specific modules, etc.), investigate those first.
2. Scope codebase-wide or large → spawn the `unknowns:unknowns-scout` agent with the
   Agent tool. Hand it a packet: the user's original prompt verbatim, the context
   sources, the target area and its entry points, and what to return (finding table +
   improved prompt draft); map its rows onto the card kinds below.
   Scope is a few files → investigate directly with Read/Grep/Glob.
3. Compile findings, each tagged with a kind:
   - **Landmine** — touching this breaks something non-obvious (regression risk, fragile
     or missing tests, a module mid-migration)
   - **Convention** — an unwritten rule the codebase enforces
   - **Missing concept** — a mechanism the user's prompt has no word for
   - **History** — an earlier or reverted attempt at this exact task
   Also collect the **questions to answer** and the **information still needed** to
   sharpen the prompt.
4. Lead with the contrast: **What you asked for** (the task as the user framed it, and why
   it sounds small) vs **What you're actually walking into**, with a tally by kind
   ("4 landmines, 2 conventions, 1 missing concept, 1 reverted attempt"). Then the cards —
   kind, finding, **why it bites**, recommended action — sorted by **importance × impact**.
5. End with an **improved prompt draft** reflecting the findings — the core deliverable of
   this skill. It names the execution order and ends with an explicit checkpoint
   ("stop and show me the plan before writing code").
6. Offer with one AskUserQuestion: proceed with this prompt now / edit it first / stop here.
7. If undecided items that could change architecture surface, suggest continuing with
   `/unknowns:interview` (or `/interview` for copied installs). If the user lacks the
   unfamiliar domain's vocabulary itself, suggest `/unknowns:teach-me`.

## Output

Artifact tool → publish the page; else `.unknowns/<YYYY-MM-DD>-blindspot-<slug>.html`; else markdown.
Reaction control: a copyable **prompt fix** per card; selected fixes assemble into the improved prompt draft.
Details: skills/loop/references/output-routing.md

## Scope

Not limited to application code — specs, migrations, infra and vendor integrations all
have landmines and unwritten conventions worth mapping before you touch them.
The subject is always a **specific codebase, plan or system** and its blind spots.
If the gap is the user's **vocabulary** for an unfamiliar field, that is
`/unknowns:teach-me` (or `/teach-me` for copied installs), not this skill. Running both
is fine: teach-me first for the words, blindspot for the territory.
