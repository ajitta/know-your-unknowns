# Sources and verification — Know your unknowns

## Contents

- [Sources](#sources)
- [The 11 "Know your unknowns" examples ↔ plugin mapping](#the-11-know-your-unknowns-examples--plugin-mapping)
- [Per-example source record (prompt + provenance)](#per-example-source-record-prompt--provenance)
- [Shared output format](#shared-output-format)
- [Techniques verified directly from the talk (with timestamps)](#techniques-verified-directly-from-the-talk-with-timestamps)
- [Key concepts from the talk (externally fact-checked)](#key-concepts-from-the-talk-externally-fact-checked)
- [Extensions made while building the plugin](#extensions-made-while-building-the-plugin-not-in-the-sources--design-judgment)

## Sources

This plugin is based on two sources by Thariq Shihipar (Anthropic, Claude Code team):

1. **Talk** — AI Engineer World's Fair 2026 keynote "Field Guide to Fable"
   (2026-06-29 to 07-02, San Francisco). Video: https://www.youtube.com/watch?v=9fubhllmsBU
   (archived: https://web.archive.org/web/20260707181143/https://www.youtube.com/watch?v=9fubhllmsBU)
2. **Example collection** — "Know your unknowns" (companion page to the blog post
   "The unreasonable effectiveness of HTML", 11 interactive examples):
   https://thariqs.github.io/html-effectiveness/unknowns/
   (archived: https://web.archive.org/web/20260708043037/https://thariqs.github.io/html-effectiveness/unknowns/)
   Parent page: https://thariqs.github.io/html-effectiveness/
   (archived: https://web.archive.org/web/20260708043027/https://thariqs.github.io/html-effectiveness/)

Re-verified 2026-07-11 against the live page source: the research doc's
single-fetch (【단일】) items — the four design-direction style names ("ops
console, editorial, kanban, terminal") and the closing sentence ("Every
explainer, brainstorm, interview, and prototype is a cheap way to find out
what you didn't know.") — appear verbatim in the static HTML.

Re-verified 2026-09-06: the index and all 11 demo pages were re-fetched and the
prompts below were extracted from each page's `The prompt` block verbatim.
The index states the reproduction contract: "Each page shows the exact prompt at the
top and the artifact Claude produced below it: paste the prompt, get something like
the page."

The plugin/repo name (unknowns / know-your-unknowns) comes from the title of
source 2 — the methodology's core frame is "The map is not the territory — the
gap between them is your unknowns."

## The 11 "Know your unknowns" examples ↔ plugin mapping

| # | Original example | Phase | Plugin component |
|---|-----------------|-------|------------------|
| 1 | Blindspot Pass | Pre-implementation | `blindspot` skill + `unknowns-scout` agent |
| 2 | Teach Me My Unknowns | Pre-implementation | `teach-me` skill |
| 3 | Four Design Directions | Pre-implementation | `prototypes` skill |
| 4 | Mock before you wire | Pre-implementation | `prototypes` skill (interaction-mockup variant) |
| 5 | Brainstorm the Intervention | Pre-implementation | `brainstorm` skill |
| 6 | The Interview | Pre-implementation | `interview` skill |
| 7 | Point at a Reference | Pre-implementation | `reference` skill |
| 8 | The Tweakable Plan | Pre-implementation | `plan` skill |
| 9 | Implementation Notes | During implementation | `notes` skill + reminder hook |
| 10 | The Buy-In Doc | Post-implementation | `buy-in` skill |
| 11 | Quiz Me Before I Merge | Post-implementation | `quiz` skill |

The `loop` skill is the orchestrator that threads these techniques in order;
the `independent-reviewer` agent is an independent verification step between
#8 and #11 (a plugin extension).

## Per-example source record (prompt + provenance)

One section per example. **Source prompt** is the verbatim text of that demo page's
`The prompt` block (the pages' decorative enclosing quotation marks are dropped; inner
punctuation is unchanged). **Provenance** holds the quotes that used to be narrated in
each SKILL.md body; the skills now point here instead. Six examples have a matching talk
passage; the other five are page-only.

### 1. Blindspot Pass → `blindspot` skill + `unknowns-scout` agent

> I'm adding a new SSO auth provider to Acme but I've never touched the auth module. Do a
> blindspot pass: find my unknown unknowns in this part of the codebase, explain each one,
> and tell me how to prompt you better for the implementation.

Provenance — talk (10:48–11:39): "I'm working on X that I know nothing about. Do a
blind-spot pass to help me figure out my relevant unknown unknowns and help me prompt
better."

### 2. Teach Me My Unknowns → `teach-me` skill

> I don't know what color grading is but I need to grade the Acme launch video. Teach me
> color grading well enough that I understand my unknown unknowns and can prompt you with
> real vocabulary.

Provenance — page only, no talk passage. The demo gives a vocabulary ladder and
before/after comparisons so a user who knew nothing about color grading can turn "make the
video nicer" into precise requests in professional language.

### 3. Four Design Directions → `prototypes` skill

> I want a review-queue dashboard for Acme but I have no visual taste and don't know what's
> possible. Make me one HTML page with 4 wildly different design directions so I can react
> to them.

Provenance — talk (11:39–12:28): "I have no visual taste. Make me an HTML page with four
widely different design decisions so I can react to them."

### 4. Mock before you wire → `prototypes` skill (interaction-mockup variant)

> Before wiring anything up, make a single HTML file mocking Acme's new frame-annotation
> toolbar with fake data. I want to react to the layout before you touch the real app.

Provenance — page only, no talk passage. Page framing: "you'll find out what you actually
want the moment you can click it, not three PRs later."

### 5. Brainstorm the Intervention → `brainstorm` skill

> Here's my rough problem: Acme users churn after onboarding. Search the codebase and
> brainstorm 10 places we could intervene, from cheapest to most ambitious. I'll tell you
> which ones resonate.

Provenance — page only, no talk passage. The demo spreads 10 interventions along one
"Ship this afternoon → Quarter-long bet" axis with S/M/L/XL effort badges, and resonate
checkboxes assemble into a reply.

### 6. The Interview → `interview` skill

> Interview me one question at a time about anything still ambiguous in the
> annotation-export feature. Prioritize questions where my answer would change the
> architecture.

Provenance — talk (12:28–12:58): "prioritize questions that would change the
architecture"; the talk's only count is "ask me 40 questions about the spec. It could
start interviewing me." One-question-at-a-time comes from this page, not the talk.

### 7. Point at a Reference → `reference` skill

> This Rust crate in vendor/rate-limiter implements the exact backoff behavior I want. Read
> it and reimplement the same semantics in our TypeScript API client — but first show me a
> semantics map so I can confirm you understood it.

Provenance — talk (12:58–13:35): "give it another map"; "Here's some code that represents
what I want. It could be in a different system or language. Read this code, understand it,
and use that to start your work."

### 8. The Tweakable Plan → `plan` skill

> Write an implementation plan for annotation export as HTML, but lead with the decisions
> I'm most likely to tweak: data model changes, new type interfaces, and anything
> user-facing. Bury the mechanical refactoring at the bottom — I trust you on that part.

Provenance — page only, no talk passage. The demo sorts by likelihood-of-tweaking rather
than execution order, attaches alternatives to the judgment calls, and folds the mechanical
work into a section marked "safe to skip entirely".

### 9. Implementation Notes → `notes` skill + reminder hook

> Keep an implementation-notes file as you build the export feature. If you hit an edge
> case that forces you to deviate from the plan, pick the conservative option, log it under
> 'Deviations', and keep going.

Provenance — talk (13:35–13:57): "If it runs into an unknown, ask it to log it, so you can
see where the deviations happened and figure out why." The demo's file is
`docs/notes/export-feature-implementation.md`.

### 10. The Buy-In Doc → `buy-in` skill

> Package the prototype, the spec, and the implementation notes into a single doc I can
> drop in Slack to get buy-in on shipping annotation export. Lead with the demo.

Provenance — page only, no talk passage. The demo leads with a working demo, pre-answers
objections with evidence, and names the sign-offs it is asking for.

### 11. Quiz Me Before I Merge → `quiz` skill

> I want to make sure I understand everything that happened in this change before I merge.
> Give me an HTML report on the export-feature diff — context, intuition, what was done —
> with a quiz at the bottom that I must pass.

Provenance — talk (13:57–14:23): "I like to get it to quiz me about what happened, to make
sure I understand what I'm doing and can represent this work when I'm creating a PR or
merging it."

## Shared output format

The shared format of the original examples — **single-file interactive HTML
with a reaction-assembly UI** (steal/skip chips, resonate checkboxes,
copyable prompt fixes, selections auto-assembled into a reply template) — is
the plugin's default deliverable shape. As of 0.4.0 the rules live in one place,
`loop/references/output-routing.md`, and the skills carry only a 3-line pointer.
Two deliberate exceptions: `interview` performs reaction-assembly directly through
AskUserQuestion dialogue, so it needs no separate HTML; and `notes`, as in the
original, produces a markdown file log (`IMPLEMENTATION_NOTES.md`). Rationale: the
parent post's claim — turn documents people skim into documents they actually read,
and export reactions back in a form the agent can read, keeping the loop short.

## Techniques verified directly from the talk (with timestamps)

| Technique | Talk timestamp | Plugin component |
|-----------|---------------|------------------|
| Blind-spot pass ("do a blind spot pass to help me figure out my relevant unknown unknowns and help me prompt better", 11:09) | 10:48–11:39 | `blindspot` skill + `unknowns-scout` agent |
| Four divergent prototypes ("I have no visual taste… four widely different design decisions") | 11:39–12:28 | `prototypes` skill |
| Pre-implementation interview ("prioritize questions that would change the architecture") | 12:28–12:58 | `interview` skill |
| Reference = another map ("give it another map") | 12:58–13:35 | `reference` skill |
| Implementation notes ("runs into an unknown, ask it to log it") | 13:35–13:57 | `notes` skill + reminder hook |
| Post-work quiz ("quiz me… so I can represent this work") | 13:57–14:23 | `quiz` skill |

## Key concepts from the talk (externally fact-checked)

- **Capability overhang** — models get smarter in spikes, and tooling
  (harnesses) unlocks latent capability. The term was popularized by Jack Clark
  (Anthropic co-founder, Import AI #321, 2023).
- **Unhobbling** — coined by Leopold Aschenbrenner in "Situational Awareness"
  (2024-06), presented as one of the three drivers of progress alongside
  compute and algorithms.
- **"Models are grown, not designed"** — phrasing by Chris Olah (Anthropic
  co-founder, head of interpretability). Background of the title "On the
  Biology of a Large Language Model" (Transformer Circuits, 2025-03-27,
  Claude 3.5 Haiku circuit tracing).
- **The Pokémon case** — across all generations (1,025 species, through Gen 9),
  exactly 2 Pokémon have English names ending in "aw": Croconaw (#159) and
  Drednaw (#834). Programmatically verified against canonical PokeAPI data.
- **80% system prompt reduction** — reported by multiple outlets citing the
  talk, e.g. The Decoder (2026-07-02). "Examples constrain the model's
  imagination — give context instead of prohibitions." Official Anthropic
  prompting docs likewise recommend "give context, not constraints" and easing
  over-instruction for recent models.
- **Map–territory** — Alfred Korzybski (1931). The known/unknown matrix —
  Rumsfeld (2002) briefing format + Johari window (1955) lineage.
- **Good/fast/cheap** — a deliberate inversion of the project-management
  triangle (traditionally pick two): "good, fast, cheap. Now it's pick three"
  (17:27); "What if you forced reality to show you the tradeoff" (17:03).
- **Related follow-up material** — Thariq, "HTML is the new markdown"
  (Lenny's Newsletter, 2026-05-18); Anthropic, "Claude Code: Best practices
  for agentic coding".

## Extensions made while building the plugin (not in the sources — design judgment)

Structural extensions:

- Each skill's concrete prompt templates, procedures, and priority lists (the
  sources are example demonstrations)
- The `IMPLEMENTATION_NOTES.md` filename and entry format (the talk only says
  "log it"; the demo writes `docs/notes/export-feature-implementation.md`)
- The `loop` skill's 10-step workflow, scale-down tiers, and `.unknowns/loop.json`
  stage tracker
- The `independent-reviewer` agent (an extension of the talk's "stay in the
  loop" spirit)
- The edit-count-based reminder hook

Devices that read as source-derived but are not (each with the source's counterpart).
Two entries left this list in 0.4.0: blindspot now uses the source's four card kinds,
and quiz now asks the source's six questions with a pass gate.

- **"importance × impact" as a sort axis** (`blindspot`, `unknowns-scout`, README) —
  "importance" occurs zero times across the index, all 11 demos, and the talk transcript.
  Demo 01 *types* its seven cards (Landmine / Convention / Missing concept / History) and
  does not rank them.
- **The interview priority ladder** (architecture → data loss/security → compatibility →
  performance → taste) — demo 06 orders by "blast radius" with four labels only:
  Architecture, Data model, UX, Polish.
- **Brainstorm's impact × effort matrix** — demo 05 has one axis ("Ship this afternoon →
  Quarter-long bet") plus S/M/L/XL effort badges, no matrix.
- **Reference's four analysis categories** — demo 07 reports three: Preserved exactly /
  Deliberately changed / Dropped.
- **Notes' stop-and-ask escalation** (architecture, user-visible behavior, data, or
  security decisions halt the run and ask) — demo 09's prompt says the opposite: "pick the
  conservative option, log it under 'Deviations', and keep going."

Numeric defaults in these extensions are deliberate initial guesses, not
source-derived: the hook threshold of 10 edits; the interview cap of 4
questions per round (the **example page's demo 06**, not the talk, asks one question at
a time — "Interview me one question at a time about anything still ambiguous in the
annotation-export feature"; the talk's only count is "ask me 40 questions about the
spec". 4 per round trades that fidelity for fewer round-trips, and 4 is also
`AskUserQuestion`'s hard cap, so a round is exactly one call); and the medium-tier step
subset (1→2→3→6→7→9: step 1 plus the steps that convert unknowns into decisions, dropping
the exploration and value-review overhead). All are tunable defaults to adjust with use,
not conclusions.

Note: "there are no trade-offs" is not applied literally — it means **don't
compromise too early based on yesterday's cost structure**. Model usage fees,
verification time, security, and technical debt are still real.
