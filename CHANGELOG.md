# Changelog

## 0.6.0 — 2026-09-06

Skill behaviour changes from a cross-check against the knowledge-elicitation literature
(cognitive task analysis, repertory grid, verbal-protocol research), plus the maintenance
records that had accumulated since 0.5.1. The finding behind the behaviour changes: several
instruments here are artifact-form rediscoveries of established elicitation techniques, so
their *mechanisms* already carry decades of evidence — and two of them diverged from the
technique in ways that cost information.

Release steps per `docs/open-questions.md` A4 (annotated tag → `scripts/build-plugin.sh` →
GitHub Release with the payload attached) are done for this version at tag
`unknowns--v0.6.0` — the first release since 0.4.0 where they happen at release time rather
than retroactively.

### Changed

- **`notes` — the deviation entry now splits into Observed and Attributed.** Self-reports of
  one's own reasoning fail in a specific, measured way: reporting *what happened* is
  non-reactive (Fox, Ericsson & Best 2011, 94 studies, r = −.03) but being asked to *explain*
  changes the behaviour being reported, and models omit the factor that actually drove a choice
  while producing a fluent rationale (Turpin et al. 2023, up to −36 points under a bias never
  mentioned). Observed (situation / what the plan said / what the code now does) is checkable
  against the diff; Attributed (reason, discarded alternatives, risk) is a claim to test later.
  On conflict the diff wins. Field names are unchanged, so
  `evals/behavior-notes-appends-to-file` still grades the same content.
- **`prototypes` — skips now elicit the contrast pole, and the option set gets a saturation
  check.** Kelly's repertory grid (1955) elicits a construct as a *bipolar pair*; steal/skip
  chips captured only one pole, and the contrast pole is the one users volunteer least. Every
  skip now asks what *would* have made it a steal. Kelly's stopping rule — "until no new
  constructs appear" — is added as step 5: a fixed N says nothing about whether the option
  space is covered.
- **`teach-me` — added Limits, and corrected what counts as success.** A vocabulary list hands
  over a request, not fluency; domain fluency is collective tacit knowledge and does not
  transfer as a term list (Collins 2010). The predicted failure point is revision rounds 2–4,
  where terms must be used rather than pasted. Success is convergence across rounds 2–4, not
  the quality of the first rewritten request. Notes that step 6 ("what good looks like") is what
  buys those later rounds — judging criteria transfer better than production vocabulary — and
  should survive size trims.
- **`docs/value-contract.md` — documented a known bias in the value metric.** "Decision-change
  rate" systematically under-credits front-stage skills (`blindspot`, `teach-me`), whose effect
  lands one step later, so the demotion condition would fire on the earliest tools first. Two
  corrections offered. Also narrows B7: `prototypes`/`interview`/`quiz` need only their artifact
  implementation validated, not their mechanism — the untested ground is `plan`, `brainstorm`
  and `buy-in`, which have no counterpart in the elicitation canon.

### Added

- `evals/behavior-prototypes-asks-contrast-on-skip` — grades the two new `prototypes`
  behaviours: a skip must route to "what would have made it a steal", and the fixed option
  count must not be presented as self-evidently sufficient.

### Maintenance records (carried over from Unreleased)

**Release hygiene, applied retroactively.** 0.5.0 and 0.5.1 both shipped without the
release the project's own policy requires (`docs/open-questions.md` A4: annotated tag →
`scripts/build-plugin.sh` → GitHub Release with the payload attached). 0.5.1 now has all
three: tag `unknowns--v0.5.1` at `0a2adf4`, and a Release carrying
`unknowns-v0.5.1.plugin` (86,212 bytes, 42 files — one fewer than 0.4.0, the
`.claude-plugin/marketplace.json` that 0.5.0 deliberately removed). 0.5.0 keeps its tag as
a history pointer but gets no Release: it was superseded 27 minutes later, and it carries
the `README.ko.md` defect 0.5.1 fixed, so there is no reason to publish it as something
downloadable. Note for later: the catalog entry is a git `url` source, so installs follow
the default branch, not a tag — the tag is the audit pointer, not the delivery path.

### Fixed
- `docs/README.md` still stated that skill descriptions are bilingual, which 0.5.1 made
  false, and described `.claude-plugin/marketplace.json` in the present tense after 0.5.0
  deleted it. Neither is reachable by the existing parity tests, which compare README to
  frontmatter and English README to Korean, but never read `docs/**` prose.

**Two open re-verifications closed.**

*B1 — the scout's tools.* Since 2026-07-11 the `unknowns-scout` agent appeared to be
missing Grep and Glob despite declaring them. It was never a defect: both earlier probes
ran from sessions whose own main loop lacked those tools, so "narrowed by the host pool"
and "broken frontmatter" produced the same observation. A probe that separates them now
exists — the parent session first *calls* Grep and Glob successfully, then spawns the
scout with Bash, WebFetch and WebSearch denied so it cannot fall back to a shell `grep` or
answer from memory. The scout called both and returned results matching repository ground
truth exactly. The rule is confirmed in the other direction too: denying three tools at the
parent removed exactly those three from the subagent. `agents/*.md` is unchanged, and the
`grep`/`rg`/`find` entries in the read-only Bash guard stay — nothing became unsafe.

*B5 — trigger firing after the description trims.* All 30 cases now have a measurement
against the shipped 0.5.1 descriptions: 11 Korean, 11 English, 5 negative, 3 behaviour.
No timeouts, and 23 of 23 mechanical graders pass. The conflict pairs separate in
practice — a bare "loop" fires no skill, a UI-options request routes to prototypes rather
than brainstorm, and "I don't know these words" routes to teach-me rather than blindspot.

### Added
- `evals/neg-generic-howto-does-not-fire-teach-me` — `docs/trigger-matrix.md` had listed
  "`teach me` is a two-word generic English phrase" as an overfire risk for two months with
  no case measuring it. There is one now, and the risk does not reproduce: "teach me how to
  center a div" fires no skill and gets answered directly. The risk entry is retired.
- `docs/trigger-eval-v0.5.1.md` — the measurement record behind 0.5.1's English-only
  descriptions: the stripped-description arm fired the right skill 11/11 with no timeouts.
  It also records, rather than papers over, a provenance gap: `evals/results/` is
  git-ignored, and the artifacts still on disk back the stripped arm in full but the
  shipped control arm only 3 of 11. The decision rests on the stripped arm, which is
  complete; the "11/11 in both arms" phrasing in 0.5.1 is more than the repository can
  currently show.
- The same document records one unresolved lead rather than grading it away: on a one-file
  change the `plan` skill's size gate correctly declines to write a document, but the reply
  still reproduces the decision cards, rejected alternatives, verification, rollback and
  weakest-part sections inline. The rubric forbids those components while its wording
  forbids a *document*, so the two readings diverge. It waits for path A's judge model.
- `docs/value-contract.md` now names the dates its own conditions fire on — 2026-09-09 for
  the 60-day "unmeasured" marking, 2026-11-08 for maintenance mode — instead of "at the
  next check", which never arrives if no one checks.

---

## 0.5.1 — 2026-09-06

Descriptions are English-only. The Korean trigger phrases moved out of the skill
and agent `description` fields; they still work, and are now guaranteed by
measurement instead of by being written there.

**Why.** The 13 always-on descriptions cost 1,698 tokens in every session. The
Korean phrases were 221 of 4,001 characters — 5% — but 381 of those tokens, 22%,
because Hangul costs several times more per character than Latin text. Every
installer paid it, including those who never type Korean.

**What was measured.** The eval suite ran the 11 `trigger-ko-*` cases twice: once
against the shipped descriptions, once against a copy identical except that the
Korean was stripped from the frontmatter. Same prompts, same cases, byte-identical
skill bodies, and the stripped copy passed `claude plugin validate --strict`. Korean
prompts fired the right skill in both arms. Measured on the default model; the
supported floor is sonnet-or-better, and haiku is out of scope.

**How the guarantee moved.**
- `tests/test_trigger_containment.py` no longer requires a Korean README phrase to
  appear in a description. It now requires every skill advertising Korean phrases to
  have a `evals/trigger-ko-*` case that actually uses one of them, and it fails if
  Korean reappears in a description.
- `evals/run-manual.py --verify` asserts the inverse for Korean cases: the phrase must
  NOT be in the description, since proving it fires without it is the point.
- `docs/trigger-matrix.md` records the split. `README.ko.md` keeps advertising the
  Korean phrases; they are unchanged and still fire.

**Limit, stated plainly.** One representative phrase per skill is exercised, not all
28 the README advertises, and each arm ran once per case.

### Fixed
- `README.ko.md` still documented the pre-0.5.0 install (`/plugin marketplace add
  ajitta/know-your-unknowns`) and claimed this repository carries its own marketplace
  manifest, which 0.5.0 removed. A Korean reader following it could not install. The
  README parity test caught the drift.
- `evals/run-manual.py` no longer grades a run that timed out. A timeout produced no
  tool calls, which the grader read as "the skill did not fire" — scoring negative
  cases as passes and positive cases as failures. Found when five parallel batches
  pushed every case past the 240s cap: all 11 "failures" sat exactly at it. `--timeout`
  now overrides the per-case cap.

---

## 0.5.0 — 2026-09-06

Distribution only. No skill, agent, hook or test changed.

This repository stopped being its own marketplace. It carried a manifest named
`ajitta`, which meant the marketplace name and the path a user had to type
disagreed: you added `ajitta/know-your-unknowns` to get a marketplace called
`ajitta`, and there was nowhere to list a second plugin without that mismatch
getting worse.

The catalog now lives in [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins),
holds no code, and points back at this repository. Installs and updates still
resolve here, at the version `plugin.json` declares.

```
/plugin marketplace add ajitta/claude-plugins
/plugin install unknowns@ajitta
```

Existing installs keep working until the marketplace is re-added; the plugin id
`unknowns@ajitta` is unchanged, because the marketplace kept its name.

- removed `.claude-plugin/marketplace.json`
- README: install, and the marketplace section, use the catalog

---

## 0.4.0 — 2026-09-06

Two batches ship under this version. The first is the three commits that landed after the
0.3.0 release and were never given a version of their own (`ebf3f1e`, `a4e5304`,
`c0f82c0`) — a marketplace install only re-fetches when the version string changes, so
anyone who installed 0.3.0 at release time has been missing them ever since. The second is
a review pass over every skill, agent, hook, test and packaging file, which is the bulk of
what follows.

Release tag: `unknowns--v0.4.0`, the name `claude plugin tag` generates. No `v0.3.0` tag
was ever created — "0.3.0" means commit `622c32b`.

### Released here for the first time (landed after 0.3.0, never versioned)
- **Hook matcher widened** from `Edit|Write` to `Edit|Write|NotebookEdit`. The matcher is a
  literal tool-name list, not a regex, so notebook edits never counted toward the
  reminder's threshold.
- **Per-user hook state file**: the reminder's session counter moved into a private
  per-user directory instead of a name two accounts on one machine could collide on.
- **Agents' `tools` in the documented comma-string form** (`tools: Read, Grep, Glob, Bash`)
  instead of a JSON array — the array form is the CLI `--agents` flag's shape, not agent
  frontmatter's.
- Trigger-boundary sentences in the `brainstorm`, `teach-me`, `plan` and `loop`
  descriptions; the first `tests/`, `.github/workflows/ci.yml` and
  `scripts/build-plugin.sh`; and the `docs/` verification records.

### Skills
- **Descriptions cut roughly in half**, to 3,248 characters across all 11 (284–314 each,
  from 6,106 / 410–818). Every Korean trigger phrase that has no English twin was kept; the
  near-duplicate English phrases were dropped. Skills load their descriptions into every
  session's context, so this is a per-session cost, not a per-invocation one.
- **One shared output contract**: new `skills/loop/references/output-routing.md` holds the
  page contract, theme/accessibility rules and the reaction-assembly table. The nine skill
  bodies that produce a deliverable now carry a three-line output block naming a three-rung
  ladder — Artifact tool →
  `.unknowns/<YYYY-MM-DD>-<skill>-<slug>.html` → markdown, highest available rung wins —
  and points at that file. Replaces the per-skill copies of the HTML boilerplate and the
  old binary "viewer / no viewer" branch, which the model had been misreading. `interview`
  and `notes` stay text-only, as they have been since 0.2.0 — the first assembles reactions
  through `AskUserQuestion`, the second writes a markdown log.
- **Provenance moved out of the instructions**: each body keeps one
  `Origin: <example title> — see loop/references/talk-source.md` pointer. `talk-source.md`
  gained an 11-section per-example record holding each demo's verbatim source prompt,
  re-fetched from the live pages on 2026-09-06, plus a list of devices that read as
  source-derived but are the plugin's own.
- `blindspot`: findings are typed **Landmine / Convention / Missing concept / History**
  and led by a "what you asked for" vs "what you're actually walking into" comparison; the
  scout is handed an explicit packet (user's prompt verbatim, context sources, target area,
  what to return) instead of a paraphrase.
- `teach-me`: gained the ordered mental-model pipeline, named presets in the live demo, a
  "what good looks like" criteria list, and a ban on external images — comparisons are
  synthetic and inline, a real photo has to come from the user as a `data:` URI.
- `interview`: **max 4 questions per round** — exactly one `AskUserQuestion` call, whose
  hard cap is 1–4 questions. Questions are ordered by blast radius (architecture / data /
  ux / polish), and the exported implementation prompt marks skipped questions and declares
  the architecture and data answers fixed.
- `prototypes`: "mock before you wire" is now a named variant that must state in the page
  that nothing reads from the real app, name the file and flag where real wiring would go,
  and carry an "open questions I'd rather not guess" row per question.
- `brainstorm`: searches the codebase first (or spawns the `unknowns:unknowns-scout` agent)
  before generating, so candidates carry an effort size and a `Found in code — <path>`
  marker — the cheapest ones are usually wiring, not building. Axis renamed to the source's
  ship-this-afternoon → quarter-long bets.
- `reference`: the edge-case table gained a **Match** column (identical / equivalent /
  changed), a numbered sign-off gate now stands between the analysis and any code, and the
  reference's own tests get ported before the implementation.
- `plan`: a size gate up front (≤2 files and no schema, interface or UX-contract decision →
  say so and defer to native plan mode); new or changed public types are rendered as
  annotated code with one numbered note per arguable field; the plan closes by naming its
  own **weakest decision** and offering 2–3 pre-written reply lines.
- `notes`: two non-blocking entry kinds — **Discovery** and **Todo for human** — plus an
  end-of-session "fold back into the plan" block of three copyable bullets for attempt #2.
  `init` now also offers (never silently) to append a deviation-log rule to the project's
  `CLAUDE.md` or `.claude/rules/unknowns.md`. Persistence is explicit: once the file exists
  or `init` has run, appending to it is mandatory and a chat-only summary does not satisfy
  the rule.
- `quiz`: **6 questions, pass = all 6 correct**, delivered as 4 + 2 `AskUserQuestion` calls;
  every wrong or blank answer names the exact `file:line` to re-read and offers a retry; a
  cleared-to-merge checklist is emitted only at 6/6.
- `buy-in`: a "spec at a glance" table of settled decisions, a 90-second target read, and a
  requirement that every objection answer carry a follow-able reference (spec section, a
  dated `IMPLEMENTATION_NOTES.md` entry, a metric, a test run, a `file:line`).
- `loop`: new `status` and `resume` arguments backed by a `.unknowns/loop.json` tracker, so
  a loop survives compaction, `/resume` and a new session. The medium tier is corrected to
  1 → 2 → 3 → 6 → 7 → 9 (step 1 runs in every tier). Step 8 hands the reviewer an explicit
  packet and forbids a fork or `/subtask`, which would inherit the implementer's context —
  the one thing that step exists to exclude.

### Agents
- Both descriptions rewritten without `<example>`/`<commentary>` blocks, an undocumented
  format that appears nowhere in the agent docs: role, "Use proactively …", and a trigger
  list keeping every Korean phrase verbatim.
- `unknowns-scout` gained `WebFetch` and `WebSearch` (still read-only, still no
  `Edit`/`Write`) and a procedure step that checks the *installed* version's official docs
  and changelog for deprecations, breaking changes and known pitfalls.
- `independent-reviewer`: one consistent tool rule replaces the old self-contradicting pair
  — never create or edit files in the repository; Bash for `git diff`/`log`/`show`, the
  project's existing test/lint/build commands, and throwaway inline execution, with scratch
  files only under `$TMPDIR`. It preloads the `unknowns:notes` skill through frontmatter, so
  it judges each logged deviation against the same criteria that produced it. The seven flat
  review items became four the agent alone can do — plan/spec conformance, acceptability of
  recorded deviations, tests-pass-but-reality-fails, and an explicit verified-OK list — with
  general bug and security hunting handed to `/code-review` and `/security-review` and the
  old items kept as a fallback for installs without them.

### Hooks
- **New read-only guard for this plugin's sub-agents**
  (`hooks/scripts/agent_readonly_guard.py`, `PreToolUse(Bash)`). Plugin-shipped agents
  cannot declare `permissionMode` or their own hooks, so "read-only" had been prose. The
  guard returns immediately unless `agent_type` names one of this plugin's agents, then
  denies what would change the user's tree: destructive commands, writing `git`
  subcommands, package installs and publishes, and redirection to anything outside the temp
  dir. The scout is held to an allowlist of read commands; the reviewer keeps test, lint
  and build. Deliberately conservative — unparsable commands and unknown agents are
  allowed. `UNKNOWNS_AGENT_GUARD=0` disables it.
- **The reminder is opt-in per project**: it fires only where the project already uses the
  methodology — an `IMPLEMENTATION_NOTES.md`, or the `.unknowns/` directory the skills write
  into (searched from `CLAUDE_PROJECT_DIR`, then the hook's cwd, walking up). Where the
  project has opted in but the notes file does not exist yet, the reminder carries the
  create-the-file hint. `UNKNOWNS_NOTES_ALWAYS=1` restores firing everywhere.
- **Three new entry points on the same script**: `SessionStart(compact)` re-injects the
  rule after compaction summarized it away and re-arms it, `Stop` says so once if the
  threshold was crossed and the notes file was never touched, and `SessionEnd` deletes the
  session's state file.
- State handling hardened: a private `0700` directory, an ownership and symlink check
  before use, locked atomic writes, and `[unknowns]` stderr diagnostics whenever persistence
  is unavailable or an env var is unparsable.
- `hooks/hooks.json` entries now use the `command` + `args` form rather than one shell
  string, and the description documents every environment variable.

### Tests and evals
- **78 tests, up from 13**: `test_impl_notes_reminder.py` (46),
  `test_agent_readonly_guard.py` (22, new), `test_readme_parity.py` (6, new),
  `test_trigger_containment.py` (4).
- `test_readme_parity.py` guards the two READMEs against structural drift — equal counts of
  headings, code fences and table rows, and identical sets of URLs, `/unknowns:<skill>`
  commands and `UNKNOWNS_*` variable names. Prose is translation and is deliberately not
  asserted.
- **New `evals/`**: 29 cases — one per skill per language (11 English, 11 Korean), four
  negatives that must *not* fire (a bare interval-runner "loop", a UI options request, a
  vocabulary question, a one-file planning request), and three behavior cases (blindspot
  ends with an improved prompt, interview asks at most four, notes actually appends to the
  file). `evals/run-manual.py` runs the same case files through plain `claude -p` for
  accounts without `claude plugin eval`: it grades `tool_used`, `regex` and `file_exists`
  itself, runs each case in a fresh temp directory, and prints the rubric beside the run
  for the graders that need a judge model.

### Packaging, CI, release
- `scripts/build-plugin.sh` builds only a releasable state: it refuses on a dirty tree, on a
  missing `refs/tags/<tag>`, and when the tag's `plugin.json` version differs from the
  working tree's. The zip now comes from `git archive` at the tag — tracked files only, no
  stray local state — and includes `NOTICE`. Output is `unknowns-v<version>.plugin`.
- New `NOTICE`: the MIT line for this plugin, an explicit statement that it is not
  affiliated with, sponsored by, or endorsed by Anthropic PBC, and Apache-2.0 attribution
  for the "Know your unknowns" example collection it is derived from.
- CI: a weekly schedule so the "tested with" claim goes stale loudly, `permissions:
  contents: read`, hook tests as a matrix over `ubuntu-latest` and `windows-latest`, Node
  22 (the CLI's minimum), `--strict` on both validate steps, and a second validation in
  *plugin* form (`plugin.json`) — the marketplace form never opens the plugin's hook, skill
  or agent files. The plugin path lives in one `PLUGIN_DIR` variable.
- `.gitignore` now covers `CLAUDE.local.md`, `.claude/settings.local.json`,
  `.claude/superclaude/` and the `.unknowns/` runtime directory the skills write into.
- Verified, not changed: a GitHub marketplace install from a clean `HOME`
  (`claude plugin marketplace add ajitta/know-your-unknowns` +
  `claude plugin install unknowns@ajitta`) succeeds and reports the plugin enabled at user
  scope. CI has three green runs on `origin/main`, which closes the "confirm after push"
  item that had been sitting open in `IMPLEMENTATION_NOTES.md` since July.

### Documentation
- **Both READMEs restructured**, and kept structurally identical by the new parity test. A
  one-command Quick start and a "Skills at a glance" table now come before the installation
  detail; the lettered "Method A/B/C" list became named install paths (marketplace, run
  straight from a clone, copy individual skills, Cowork/Claude Desktop) with its own
  Updating section; and a new "Attribution and license" section carries what `NOTICE` says.
  Every advertised trigger phrase was brought back in line with the trimmed descriptions.
- **New `docs/README.md`** — an index of everything under `docs/`: purpose, language, what
  produced each file, how to regenerate it, and the decision on the two ~100 KB
  intent-report HTML files that ride into every install (they stay, as dated historical
  evidence, now linked instead of orphaned).
- **The documentation language policy is written down** — in `docs/README.md` — and matches
  the tree for the first time. Skills, agents, hooks, manifests, `README.md`,
  `CHANGELOG.md`, `tests/` and `evals/` are English; `README.ko.md`, every `docs/*.md` and
  `IMPLEMENTATION_NOTES.md` are Korean maintainer records; skill descriptions stay
  bilingual because Korean auto-triggering needs the Korean phrases; and a skill's runtime
  output follows the language the user is writing in. The 0.3.0 note's
  "docs/research-know-your-unknowns.md deliberately remains Korean" had been overtaken by
  five more Korean docs and a Korean deviation log.
- `docs/open-questions.md` rewritten: A1–A5 and B6 are recorded as decided rather than
  pending, the CI item is closed, A4's premise is corrected (there was never a `v0.3.0`
  tag), and a new entry records that agent `memory` stays off in 0.4.0 because enabling it
  auto-enables `Read`/`Write`/`Edit` and would falsify both agents' never-modify-files
  rule. **B1 — whether the scout really loses `Grep`/`Glob` — stays open**, with the reason
  both existing probes are inconclusive and the procedure that would settle it.
- `docs/trigger-matrix.md` regenerated from the current descriptions, with anti-triggers and
  argument hints separated out instead of silently folded into a list called exhaustive.
- `docs/value-contract.md`'s demotion and removal clauses switched from release counts to
  calendar windows — a release counter stalls in exactly the situation the clause exists to
  detect — and `docs/value-scorecard.md` gained column definitions and a self-serve
  recording procedure for installers.
- **The value measurement is now wired, not just specified.** The `loop`'s value review
  and the `quiz` wrap-up ask two questions through one `AskUserQuestion` call — did this
  surface something you did not know, and did it change a decision — and append the answer
  to `.unknowns/scorecard.md`; new `skills/loop/references/scorecard.md` holds the format.
  Neither may answer for the user, and a row where both answers are "no" is still written,
  because the contract's demotion conditions fire only on recorded zeros. Until this, the
  contract promised a metric nothing collected.
- `docs/research-know-your-unknowns.md` re-verified against the live source on 2026-09-06:
  the demo count is 20, not "about 19", and the 2×2 quadrant figure is decorative and
  `aria-hidden`, which closes a hedge that had been standing since July.

### Fixed
- The 0.2.0 entry below pointed at a README section title that does not exist ("Upgrading
  from an older version"). It now cites the heading the README actually carries after this
  release's rewrite, "Upgrading from 0.1.x (field-guide)".

## 0.3.0 — 2026-07-11
- **English translation**: all skills, agents, the hook script, manifests, and the README
  are now English-first (docs/research-know-your-unknowns.md deliberately remains Korean).
  Skills/agents use a terse, token-efficient instruction style; frontmatter
  descriptions keep Korean trigger phrases alongside English ones, so Korean natural-language
  auto-triggering still works.
- **Bilingual README**: `README.md` (English) + `README.ko.md` (한국어), cross-linked.
- **Hook fix**: the deviation-notes reminder is now delivered both to the user
  (`systemMessage`) and into Claude's context (`hookSpecificOutput.additionalContext`) —
  previously the model, which actually records deviations, never saw it. Also hardened
  against non-object JSON on stdin.
- **Output-philosophy fixes**: `prototypes`, `quiz`, and `reference` now explicitly instruct
  the viewer-less markdown fallback promised plugin-wide by the README.
- **Packaging**: marketplace description added (`claude plugin validate` now passes with
  zero warnings); talk-source.md coverage claim corrected (interview/notes are deliberate
  exceptions to the HTML-first output section).

## 0.2.0 — 2026-07-11
- **Renamed**: plugin `field-guide` → `unknowns` (invocation: `/unknowns:<skill>`),
  repo `ajitta/field-guide` → `ajitta/know-your-unknowns`.
  Rationale for the name: the methodology's actual core concept is, verbatim from the
  source material's title, "Know your unknowns".
  Existing installs must remove `field-guide` and reinstall (see README
  "Upgrading from 0.1.x (field-guide)").
- **Skill renames**: `reference-map` → `reference`, `impl-notes` → `notes`.
- **4 new skills** — mapped 1:1 to the 11 examples in the original "Know your unknowns":
  `teach-me` (domain vocabulary primer), `brainstorm` (solution-space map),
  `plan` (tweakable plan ordered by likelihood of change), `buy-in` (reviewer persuasion document).
- **Output format upgrade**: single-file interactive HTML first, with a UI that
  assembles reactions into a structured response; markdown fallback for environments without a viewer.
- Fixed the loop step-count error (said "9 steps" but listed 10 → cleaned up as steps 1–10)
  and wired in the new skills.
- Hook improvements: session ID normalization, `UNKNOWNS_NOTES_THRESHOLD`/`UNKNOWNS_NOTES_REPEAT`
  environment variables (old `FIELD_GUIDE_NOTES_THRESHOLD` still supported).
- Added the "Know your unknowns" page and the 11-example mapping to the source document (talk-source.md).

## 0.1.2 — 2026-07-10
- Published the GitHub repo (`ajitta/field-guide`) and added a marketplace manifest
  (supports `/plugin marketplace add ajitta/field-guide`)
- Added homepage/repository fields to plugin.json

## 0.1.1 — 2026-07-10
- Expanded README usage docs: 3 install methods, per-skill invocation examples,
  auto-triggers, and tips, how to address agents, hook configuration table,
  4 scenarios by project size, FAQ

## 0.1.0 — 2026-07-10
- Initial release: 7 skills (loop, blindspot, interview, prototypes, reference-map,
  impl-notes, quiz), 2 agents (unknowns-scout, independent-reviewer),
  1 hook (deviation-notes reminder)
- Based on: Thariq Shihipar, "Field Guide to Fable" (AI Engineer World's Fair 2026) —
  cross-checked against the original talk and externally fact-verified (`skills/loop/references/talk-source.md`)
