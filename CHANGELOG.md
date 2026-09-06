# Changelog

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
