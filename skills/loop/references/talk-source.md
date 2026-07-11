# Sources and verification — Know your unknowns

This plugin is based on two sources by Thariq Shihipar (Anthropic, Claude Code team):

1. **Talk** — AI Engineer World's Fair 2026 keynote "Field Guide to Fable"
   (2026-06-29 to 07-02, San Francisco). Video: https://www.youtube.com/watch?v=9fubhllmsBU
2. **Example collection** — "Know your unknowns" (companion page to the blog post
   "The unreasonable effectiveness of HTML", 11 interactive examples):
   https://thariqs.github.io/html-effectiveness/unknowns/
   Parent page: https://thariqs.github.io/html-effectiveness/

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

The shared format of the original examples — **single-file interactive HTML
with a reaction-assembly UI** (steal/skip chips, resonate checkboxes,
copyable prompt fixes, selections auto-assembled into a reply template) — is
reflected, as of 0.2.0, in the "Output Format (HTML first)" sections of the
skills that produce document deliverables (`quiz` has an "HTML Option" section
instead). Two deliberate exceptions: `interview` performs reaction-assembly
directly through AskUserQuestion dialogue, so it needs no separate HTML; and
`notes`, as in the original, produces a markdown file log
(`IMPLEMENTATION_NOTES.md`). Rationale: the parent post's claim — turn
documents people skim into documents they actually read, and export reactions
back in a form the agent can read, keeping the loop short.

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

- Each skill's concrete prompt templates, procedures, and priority lists (the
  sources are example demonstrations)
- The `IMPLEMENTATION_NOTES.md` filename and entry format (the talk only says
  "log it")
- The `loop` skill's 10-step workflow and scale-based trimming criteria
- The `independent-reviewer` agent (an extension of the talk's "stay in the
  loop" spirit)
- The edit-count-based reminder hook

Note: "there are no trade-offs" is not applied literally — it means **don't
compromise too early based on yesterday's cost structure**. Model usage fees,
verification time, security, and technical debt are still real.
