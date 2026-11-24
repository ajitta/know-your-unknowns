# Evals

Reproducible trigger and behaviour cases for the `unknowns` plugin.

The evidence that the skills fire used to be a hand-run n=1 sample covering 3 of the 11
skills ([docs/trigger-eval-v0.3.0.md](../docs/trigger-eval-v0.3.0.md)), which left every
description edit after it unverifiable. This directory replaced that with case files two
different runners can execute. The suite holds the single-turn cases that
`run-manual.py` runs and the multi-turn cases under `multiturn/` that `run-multiturn.py`
runs; `--verify` on each prints the current count (105 and 19 after the cases added on
2026-11-24; 88 and 13 at 0.13.2). Release checks
from 0.9.0 on record their figures in that version's **Checked** section of
`CHANGELOG.md`, most with what they did not measure under **Not measured**; run output
stays in the git-ignored `evals/results/`. `docs/trigger-eval-*.md` are frozen records of
the versions or dates they name. The runners score the mechanical graders; `llm` rubrics
need a judge model: `run-multiturn.py --judge` runs one for the multi-turn cases, and
`run-manual.py` writes the single-turn rubrics out for a judge or a human.

Two run paths, because `claude plugin eval` is gated:

| path | command | grades `llm` rubrics? | status |
|---|---|---|---|
| A — first-class runner | `claude plugin eval --help` (see below) | yes, with a judge model | account access and external-suite layout not rechecked |
| B — manual headless | `python3 evals/run-manual.py` | no; prints them for a human | works today |

Path B reads the case files in this repository and loads the generated plugin from `plugins/unknowns/`. The suite remains developer-only; it is not copied into the installed payload. Historical model results below describe their recorded versions, not the rewritten portable bodies.

---

## Layout

```
evals/
  <case-slug>/
    prompt.md            # frontmatter + the user prompt to send
    graders/<name>.md    # one grader per file; `type:` in the frontmatter
    case.yaml            # optional: `context: scaffold_script:` names the script below
    place-files.sh       # optional: lays files/ (input material) into the run's cwd
    files/               # optional: the material the scaffold script copies
    templates/           # optional: templates the scaffold script generates material from
  multiturn/<case>/      # multi-turn cases: case.md + graders/ (see below)
  results/               # run output; case discovery always skips this directory
  run-manual.py          # path B
  run-multiturn.py       # multi-turn runner with a simulated user and a judge
```

`prompt.md` frontmatter keys used here: `description`, `tags`, `runs`, `max_turns`,
`timeout_seconds`, `allowed_tools`, `append_system_prompt`; an unknown key makes the CLI fail to load the case. Grader types used here: `tool_used`, `regex`,
`file_exists`, `llm`. The grader's name is its filename; an `llm` or `regex` grader's
body is its rubric or pattern. `claude plugin eval --help` is the authority on the
format — this README does not restate it.

`plugins/unknowns/.claude-plugin/plugin.json` carries no developer eval configuration. The cases stay in repository `evals/`, alongside rather than inside the generated payload.

---

## Path A — `claude plugin eval`

The plugin target is `plugins/unknowns/` and the case directory is repository `evals/`. Current CLI help exposes `--eval-dir`, but calls it a directory below the plugin; this repository's split keeps the cases outside that folder. External-suite resolution and account access have not been verified for this layout, so no working first-class invocation is claimed here.

```bash
claude plugin eval --help
```

Use path B below for the current layout. Before a future first-class run, check the installed CLI's external-suite support, use a no-plugin baseline arm, grant writing tools only for cases that need them, and keep results unpublished unless explicitly requested. Do not add eval files to the generated plugin just to make discovery work.

## Path B — manual headless

Same case files, plain `claude -p`, with the generated plugin path as the default:

```bash
python3 evals/run-manual.py --verify                     # structural check, calls no model
python3 evals/run-manual.py --list                       # what would run
python3 evals/run-manual.py --case 'trigger-*' --runs 1  # trigger sweep, with-plugin arm
python3 evals/run-manual.py --case 'behavior-*' --arm both
```

`--verify` is the one command here that is free and instant. It checks every case
against the CLI's own schema (legal frontmatter keys, known grader types, compilable
patterns, `runs >= 3`, at least one scored grader per case, the `min:0 max:0 arm:both`
form on every must-NOT-fire guard) **and**, for every `trigger-*` case, that the phrase
its own `description` declares (the `: '<phrase>'` at the end of that line) is still in
the prompt. For a `trigger-en-*` case the phrase must also still be quoted in that
skill's `description` on disk; for a `trigger-ko-*` case the description must hold no
Korean, since descriptions are English-only and the case shows the Korean phrase still
routes. Trim a phrase out of a `SKILL.md` and `--verify` fails on the English case
that used it. Run it after any description edit; it exits non-zero on any problem.

Each run gets a fresh temporary cwd and loads the generated `plugins/unknowns/` directory through an absolute `--plugin-dir` path (so the committed payload is measured, not an installed copy), and applies the case's
`allowed_tools` via `--allowedTools` / `--disallowedTools`. `--arm both` runs the
with- and without-plugin arms, which is the manual equivalent of the ablation.
Both runners also pass `--effort medium` to the model under test unless `--effort` names another level (`--effort default` leaves the CLI's own default); the release records in `CHANGELOG.md` from 0.12.3 on use medium.

**Runs stay out of your account.** Both runners start every `claude` call in a fresh,
empty `CLAUDE_CONFIG_DIR` with `ENABLE_CLAUDEAI_MCP_SERVERS=false`, so a run loads this
plugin and nothing else of yours: no installed plugins or their skills, no `CLAUDE.md`,
no account connector. `--disallowedTools` names tools and does not cover connectors: on
2026-11-17 a run in the owner's own config, with no unknowns skill loaded, wrote a
document into the signed-in account through a document connector. A check on Claude
Code 2.1.326 listed 14 connectors (mail, calendar, drive and documents among them) and
98 skills in the owner's config, and no connector and 34 skills (the CLI's own and this
plugin's 11) in the isolated one. The sign-in is passed as `CLAUDE_CODE_OAUTH_TOKEN`,
taken from the current login unless that variable or `ANTHROPIC_API_KEY` is already
set; the credentials file is never copied, because a copy refreshes on its own and can
end the main login. An isolated run cannot refresh the token, so the runner stops
before the first run when less than 30 minutes are left. Each result records the
connectors the session listed (`mcp_servers`, empty when isolated). `--own-config`
runs in your own config instead; results recorded before 2026-11-17 ran that way, with
the owner's other plugins and `CLAUDE.md` loaded, so do not compare them with isolated
runs as if the condition were the same.

`--crowd N` also loads a generated plugin of N filler skills (written into the results
directory, so the run can be repeated). Claude Code budgets the skill listing (1% of the
context window by default) and, when it overflows, keeps descriptions for the most-used
skills (usage counts decayed by recency) and lists the rest by name only. A clean eval
environment rarely overflows, so a trigger rate measured there says little about a
machine with sixty skills installed. Usage counts live in the Claude config
(`skillUsage` in `.claude.json`) and headless runs update them too, so the fresh, empty
`CLAUDE_CONFIG_DIR` every run gets also means no usage history, and the filler plugin is
loaded first, so ties do not favour this plugin. Each crowd run writes a `--debug-file`;
the report records whether the CLI logged the listing as over budget, the CLI's whole
listing lines, which plugins loaded and any `plugin_errors` from the session's init event.
A run that cannot start is reported as `FAILED` and left ungraded, not counted
as a trigger miss, and so is a crowd run whose CLI log does not show the filler plugin
loaded: the results directory is made absolute so the filler path resolves from each
run's temporary cwd (on 2026-11-24 a relative `--out` left it unresolved, and every run
listed 28 skills: this plugin and the CLI's own). `--budget-fraction F` sets
`skillListingBudgetFraction` to force an overflow regardless of the context window —
`--crowd 60 --budget-fraction 0.002` drops every unknowns description (the CLI logs
"Skill listing over budget" under `--debug-file`). First result:
[docs/trigger-eval-crowd-2026-09-30.md](../docs/trigger-eval-crowd-2026-09-30.md).

With `--own-config`, the no-plugin arm is honest only when the plugin is not *also*
enabled in your own config. Check with `claude plugin list`; `claude plugin disable
unknowns` for the duration of the run if it is. An isolated run needs neither.

The raw one-liner behind it, adapted to the generated payload path (run from the repository root):

```bash
claude -p "<prompt body from prompt.md>" --output-format stream-json --verbose \
  --max-turns 6 --effort medium --plugin-dir ./plugins/unknowns --disallowedTools Edit Write Bash
```

**Input material.** A case that needs real files (a repository to review, a report and its records) carries them in `files/` and a `place-files.sh` named in `case.yaml` under `context: scaffold_script:`, the CLI's own form (`claude plugin eval --scaffold` runs it). `run-manual.py` runs that script with bash in the run's fresh cwd before the run; the script may build a git history (the independent-reviewer code case commits the change under review as `HEAD~1..HEAD`). Each agent the run spawns has its report kept as `agent_reports` beside `last_message`, so a grader with `focus: trace` can judge what the agent found, not the caller's retelling of it.

Output lands in `evals/results/manual-<timestamp>/` as `manual-result.json` plus a
`summary.md` that already lists the rubrics still needing a human verdict.

## Multi-turn cases — `run-multiturn.py`

Every case above is single-turn, so a skill whose method is to ask and stop (blindspot's
three lists, interview rounds, the quiz gate, prototype reactions) is graded on its
question, never on what it does with the answer. The multi-turn cases play the rest of
the conversation against a simulated user.

```bash
python3 evals/run-multiturn.py --verify                      # structural check, calls no model
python3 evals/run-multiturn.py --list
python3 evals/run-multiturn.py --case 'quiz-*' --runs 3 --judge --jobs 3
python3 evals/run-multiturn.py --judge-dir evals/results/multiturn-<ts>   # judge later
python3 evals/run-multiturn.py --tally evals/results/multiturn-<ts>
```

Layout (`run-manual.py` only discovers directories holding a `prompt.md`, so it never
sees these):

```
evals/multiturn/<case>/
  case.md              # frontmatter + "## Opening message" + "## Persona"
  graders/<name>.md    # llm (focus: transcript or packets), regex, question_count, tool_used
```

`case.md` frontmatter: `description`, `tags`, `runs`, `max_turns_per_reply` (agent
turns per assistant reply), `user_turns` (most simulated replies after the opening),
`timeout_seconds` (per reply), `allowed_tools`, optional `model`. The persona holds the
facts the user knows, how they answer and concede, and when they stop ("stop once the
assistant has delivered the decision table").

How a run works: the opening message goes to `claude -p --output-format stream-json
--verbose --plugin-dir <abs plugin>` in a fresh temporary cwd, with the same tool flags
as `run-manual.py`. After each reply a separate `claude -p --tools ""` is given only the
persona and the conversation so far and writes the user's next message, answering what
the last reply actually asked, or `STOP`. That message goes back with `claude -p --resume
<session>` in the same cwd. Every prompt is sent on STDIN. All three kinds of call
(assistant, simulated user, judge) are isolated as described under path B; a
conversation keeps one config dir across its replies, because `--resume` reads the
session from it. The run ends on `STOP`, at
`user_turns`, or when a reply asks nothing of the user. Each run writes
`<case>/<arm>-run-<n>/transcript.json` (every turn: text, tool calls with inputs, skills
loaded, files written, cost) and `result.json` (grader verdicts, stop reason). A run
that times out or cannot start is recorded as not graded, never as a FAIL.

Graders: `regex` and `question_count` read the assistant replies chosen by `turn:`
(`first`, `last`, `final_substantive` = the last reply of 800+ characters, `all`, `any`,
or a reply number); `question_count` counts numbered question items per reply, outside
code fences, quotes and tables. `tool_used` counts tool calls in the chosen replies; a
`tool: Skill` grader without `arm:` is display-only, as in `run-manual.py`. `llm`
graders are judged with `--judge` or `--judge-dir` by a separate `claude -p --tools ""`
(prompt on STDIN) that sees the criteria and the conversation text only: user messages
and every assistant reply, numbered. It does not see tool calls, file contents, skill or
plugin names, or the arm. A verdict without an `OVERALL:` line is retried once and then
recorded as unjudged, not as FAIL. An `llm` grader may set `focus: packets` (the case must
allow `Agent` or `Task`): its judge also sees, after the conversation, the `prompt` of each
Agent or Task call the assistant made itself, each marked with the reply it was sent in. It
does not see calls made inside a spawned agent, any other tool call, or other inputs such as
the agent type, though a packet's own text may name a skill or plugin. A `packets` grader
judges what single-turn `focus: trace` packet graders judge, whether the task message
carries its sources as content, when those sources come from any turn: a plan the assistant
wrote itself, or a change the user reported later. Text written inside a spawned agent never
joins a reply, so the simulated user and the stop test do not read it.

Limits: the simulated user is a model. A result measures the skill's behaviour against
that persona, played by that model, not against real users; a persona that drifts or
answers a question nobody asked is a measurement error, so read the transcripts before
quoting a number. Each run costs several model calls: in the first smoke runs a
blindspot, interview or quiz conversation cost about $0.4-1.1 and a prototypes
conversation, which writes runnable prototypes, $3-5. One run per case is a smoke check, not
a measurement: compare arms run side by side on the same day, with enough runs per case
for an exact test, before claiming a difference.

---

## What the suite covers

**22 positive trigger cases** — one per language for each of the 11 skills,
`trigger-{en,ko}-<skill>`. Every `trigger-en-*` prompt embeds a phrase quoted verbatim in
that skill's current `description`; every `trigger-ko-*` prompt embeds a Korean phrase
that the English-only description does not carry (see [docs/trigger-matrix.md](../docs/trigger-matrix.md)).
When a description changes, the case that used a dropped phrase must change with it.

**22 non-coding cases** — one per language for each of the 11 skills,
`noncode-{en,ko}-<skill>`: a grant, a choir, a family reunion, a lease, a hiring
decision, a parents' association. Each carries a display-only routing indicator and
one `llm` grader, `moves-toward-the-outcome`, that asks whether the reply moves toward
what the user is actually after (surfacing both sides' unknowns, clarifying intent)
rather than only producing an artifact, and fails a reply that forces software
concepts onto work that has none.

**4 Unknown-cell cases** — `unknown-*`: a county permit nobody in the conversation
knows, an organisation's unwritten politics, a three-month-old scheme with almost no
sources, a personal job trade-off. Neither the user nor the model can know the answer;
the `surfaces-both-sides-unknowns` grader passes a reply that labels what it cannot
know, asks for what only the user knows, and gives no confident answer it cannot
back. The routing indicator accepts any unknowns skill.

**9 Open-cell negatives** — `neg-open-*`: requests both sides already understand. None
may fire an unknowns skill (`input_match: "unknowns:"`, `min: 0`, `max: 0`, `arm: both`).
Five are trivial (a rename, typo fixes, a polite rewrite, an errand "plan", "quiz me" on
trivia) and must be done directly, with no read-back. Four carry weight and must get a
2-3-line read-back of the request, the assumptions and what counts as done, then wait
for confirmation, with no method run. Two of them (`neg-open-weighty-code-en`, a
migration going to production tonight; `neg-open-weighty-text-ko`, a notice to all 80
staff) are tagged `informative`: they measure the gap the plugin leaves without a
`CLAUDE.md` line (the read-back lives in the skill bodies, and no skill loads for a clear
request), so they do not block a release. The third, `neg-open-weighty-memory-line-en`,
runs the migration with the README's `CLAUDE.md` line passed as `append_system_prompt`,
which `run-manual.py` hands to `claude -p --append-system-prompt`; the harness has no
project-memory fixture, so this stands in for the user's `CLAUDE.md`. The fourth,
`neg-open-weighty-pasted-sentence-en` (added 2026-11-24), runs the same migration with
the README's sentence to paste for one conversation passed the same way, which stands in
for pasting it as a message and may weigh more than a pasted message would. Its rubric is
the memory-line case's, word for word, so the two read side by side. One turn reaches
only the read-back half of that sentence; the end-of-work half (each done criterion with
its evidence, the outcome question) is not judged. `tests/test_portability.py` checks that
both READMEs print the line and the sentence these two cases run with.

**5 negative cases** — the collisions and the overfire direction the trigger matrix lists:

| case | must not fire | why |
|---|---|---|
| `neg-ui-options-does-not-fire-brainstorm` | `unknowns:brainstorm` | brainstorm advertises "show me options"; prototypes owns UI variants |
| `neg-vocabulary-does-not-fire-blindspot` | `unknowns:blindspot` | blindspot investigates a specific plan or situation, teach-me teaches vocabulary |
| `neg-interval-loop-does-not-fire-unknowns-loop` | `unknowns:unknowns-loop` | a bare "loop … every 5 minutes" is the built-in interval runner |
| `neg-one-file-tweakable-plan-defers-to-plan-mode` | (behaviour, not trigger) | the tweakable-plan skill's own size gate: ≤2 files and no schema/interface/UX decision → defer to native plan mode |
| `neg-generic-howto-does-not-fire-teach-me` | `unknowns:teach-me` | "teach me" is a generic phrase; a how-to with a known answer and a named output is no vocabulary gap |

**3 agent-collision negatives** (added 2026-11-24) — review and investigation requests
that name neither agent, which the two agents intercepted before 0.9.2
(`docs/features/agent-collision/`, a frozen 0.9.2 record) and which no case measured
after the 0.12.0 description change. Each must spawn neither agent (`tool: Agent`,
`input_match` on the agent's name, `min: 0`, `max: 0`, `arm: both`) and load no unknowns
skill, and its outcome grader checks that the request was served, on material the
scaffold script lays into the run. A `spawns-a-subagent` indicator shows whether the run
spawned any subagent: a run that spawned none passes the guards without exercising the
routing.

| case | must not spawn | repeats | outcome grader |
|---|---|---|---|
| `neg-unnamed-review-does-not-spawn-reviewer` | `unknowns:independent-reviewer`, `unknowns:unknowns-scout` | 0.9.2 cell `f-rv-indep-en`: an independent review of a branch before merge, in a git repository that holds the branch's plan | the review names the inverted `--overdue` comparison |
| `neg-unnamed-investigation-does-not-spawn-scout` | `unknowns:unknowns-scout`, `unknowns:independent-reviewer` | 0.9.2 cell `s-pre-en`, with a named search target ("everything that reads or writes todo.json") in place of "for risks", which is close to the **blindspot** skill's own purpose | the reply finds `export.py`'s direct read beside `todo.py`'s `load()` and `save()` |
| `neg-unnamed-report-check-does-not-spawn-reviewer` | `unknowns:independent-reviewer`, `unknowns:unknowns-scout` | the material of `behavior-independent-reviewer-report-vs-records` without the agent's name (non-code) | the reply recomputes at least two of the report's figures and confirms neither unbacked figure |

**2 independent-reviewer cases** — the agent called by name on real material laid into the run by the case's scaffold script: `behavior-independent-reviewer-code-change` (a git repository whose last commit silently misses one of five done criteria) and `behavior-independent-reviewer-report-vs-records` (a pilot report whose figures contradict the records beside it). Graders: the agent is spawned; each done criterion judged met, partial or missing; the planted miss found; an outcome judgement (or "outcome not judgeable"); a claim-checks part.

**7 behaviour cases** — these grade the deliverable, not the trigger:

| case | checks |
|---|---|
| `behavior-blindspot-ends-with-improved-prompt` | the pass ends with a pasteable rewritten prompt that folds in the risks it found |
| `behavior-interview-max-four-questions` | at most 4 questions reach the user in one round, on a prompt that dangles nine open decisions |
| `behavior-deviation-log-appends-to-file` | `IMPLEMENTATION_NOTES.md` is actually created, with the entry fields filled — not summarised in chat only |
| `behavior-blindspot-labels-evidence-status` | findings carry a confirmed / inferred / unchecked status, and nothing about an unseen repository is marked confirmed |
| `behavior-prototypes-asks-contrast-on-skip` | a skip asks what would have made it a steal, and the option set can grow |
| `behavior-tweakable-plan-opens-with-done-criteria` | the plan opens with its done criteria, "not set" where the user gave none, and letters each decision's alternatives |
| `behavior-buy-in-relays-reviewer` | the independent-reviewer's findings and outcome judgement reach the buy-in doc |

**Measuring cases from the second rule-based review** (2026-11-10): 18 single-turn `behavior-*` cases and 7 multi-turn cases, each written to settle one open decision before the text changes. A case runs on the current text; when it fails, a fix decided before the run goes in and the case runs again (the rule, the results and the decision for each are in `IMPLEMENTATION_NOTES.md`, entry 2026-11-10). They cover, among others: a loop whose probe fails, a loop the user wants to skip investigating, a deviation report and a wrap-up, a public rename and a difference the plan never mentioned, blindspot's verdict on each assumption, brainstorm finding an unused module, quiz on a submission, reference corrected in free text, a deep interview and an item the user left undecided, buy-in finding a non-code deviation log, and the scout checking a pinned library version.

**Cases for sentences no run had reached** (added 2026-11-24): 12 single-turn `behavior-*` cases and 4 multi-turn cases, each written for a step or sentence that no recorded run reached. Single-turn: blindspot and brainstorm on large material (`behavior-blindspot-scout-many-contracts`, 214 supplier agreements; `behavior-brainstorm-scout-inventory-monorepo`, a 41-service monorepo), whose spawn and scout-path graders became indicators on 2026-11-24, when the owner ruled that whether material is more than the model can read in full is the model's own judgment: when the scout is spawned, the packet carries both sides' assumptions or asks for an inventory of existing mechanisms, and the scout's marks or rows reach the reply; quiz, reference and prototypes with nothing to work on, each asking one question for the work, the reference or the target (`behavior-quiz-asks-for-the-work`, `behavior-reference-asks-for-the-reference`, `behavior-prototypes-asks-target-first`; the reference case names the skill since it loaded reference in 1 of 3 runs without its name); quiz and unknowns-loop finding the `DEVIATIONS.md` beside non-code work that the prompt never names (`behavior-quiz-finds-noncode-log`, `behavior-unknowns-loop-finds-noncode-log`); the read-back paragraph in a skill that loaded through its trigger phrase rather than by name (`behavior-buy-in-autoloaded-reads-back`, informative since it loaded buy-in in 0 of 3 runs: a request clear to both sides gives buy-in nothing to surface, so the plugin does not claim the load), and a request for tweakable-plan's own plan about weighty work, which goes through the size gate (`behavior-tweakable-plan-autoloaded-weighty-plan`, renamed on 2026-11-24 from `behavior-tweakable-plan-autoloaded-reads-back` with the owner's ruling on the read-back paragraph), which expect a skill to load, so they are `behavior-*` cases rather than must-NOT-fire negatives and are read only in runs where the skill loaded. Three more come from the description round of the same day: a log file the user names for code work (`behavior-deviation-log-code-user-named-file`: the entry goes to that file and no `IMPLEMENTATION_NOTES.md` is created) and a plain "Show me options." on a problem that is not a design request (`behavior-brainstorm-show-me-options`, the positive side of brainstorm's border "NOT for design options."), and the source talk's merge-time request with no "quiz" in it, which quiz's "or before merging" covers (restored on 2026-11-24 after this case loaded quiz in 0 of 3 runs without it; `behavior-quiz-before-merge-understanding`). Three graders of the two scout cases (`packet-carries-both-sides-assumptions`, `scout-marks-each-assumption`, `packet-asks-for-inventory`) judge the packet, the `prompt` input of the Agent call that spawned the scout, which `manual-result.json` keeps under `tool_calls`; a judge given only `last_message` and `agent_reports` cannot see it. `behavior-buy-in-reviewer-packet-from-conversation` (added 2026-11-24) gives buy-in a plan, done criteria, outcome, deviation log and status that exist only in the user's message, with the Agent tool allowed, and grades what the independent-reviewer's packet carries and what its report says it could not check. The four multi-turn cases are listed below.

**19 multi-turn cases** — `evals/multiturn/`: the seven measuring cases above; `interview-then-work` (the interview ends at its decision table and ready-to-use prompt in a folder where the script could be written); `blindspot-reaches-improved-prompt`, `interview-rounds-stay-at-four`, `prototypes-saturation-after-reactions`, `quiz-hides-key-and-gates-on-six` and `reference-correction-revises-plan`, which play blindspot's three lists, interview rounds, prototype reactions, the quiz gate and a numbered semantics-map correction to the end; and the four added on 2026-11-24: `tweakable-plan-after-interview-accepted` (the user takes step 1b's interview suggestion, and the plan shown again is built on the answers), `prototypes-two-options-contrast` (with only two options, step 5a's question on what most sets them apart in place of the triad), `quiz-partial-retry-score` (a retry asks only the missed questions, and the score reaches 6/6 only once every missed part is answered right) and `unknowns-loop-every-stage-to-outcome-check` (the loop played through every stage to the outcome check on a non-code task); and `unknowns-loop-blindspot-then-teach-me` (added later on 2026-11-24: a user who can describe the task but knows no audio terms picks prompt fixes from the blind-spot pass and terms from the vocabulary explainer, and the reply that opens the next stage builds on a request carrying both sets of picks or says which are still to apply); and `buy-in-reviewer-packet-after-plan` (added the same day: a plan the assistant wrote and the user approved, a change reported in a later message, then a buy-in doc, with the Agent tool allowed; `focus: packets` judges whether the independent-reviewer's packet carries the plan's done criteria, outcome and figures and the later change as content).

## How the graders are meant to be read

- `type: tool_used`, `tool: Skill`, no `arm:` — a **display-only** trigger indicator.
  The runner reports it and excludes it from the score in both arms, so it can never
  move Δ by itself. Every case therefore also carries an outcome grader; that is the
  scored one.
- `min: 0` + `max: 0` + `arm: both` — the must-NOT-fire form. In the no-plugin arm the
  skill cannot exist, so it passes trivially there; the outcome grader beside it is
  what carries the delta for a negative case.
- `weight: 0.5` marks a secondary check written against wording in `SKILL.md` (a
  heading, a numbering convention). It never stands alone — an outcome grader is
  always the primary.
- `min: 0` + `weight: 0` on a `tool_used` grader for a tool other than Skill — an
  indicator that is reported and adds nothing to the score (the runner's display-only
  form covers `tool: Skill` only). `spawns-unknowns-scout` in
  `behavior-blindspot-scout-assumption-verdicts`, `behavior-blindspot-scout-many-contracts`
  and `behavior-brainstorm-scout-inventory-monorepo`, `reads-the-log` in
  `behavior-quiz-finds-noncode-log` and `spawns-a-subagent` in the agent-collision
  negatives use it.
- `weight: 0` on an `llm` grader — an indicator that is judged and reported and adds
  nothing to the score. The scout-path graders of the two scout cases above use it and
  pass when no scout ran; `packet-leaves-out-producer-summary` in
  `behavior-buy-in-reviewer-packet-from-conversation` uses it for a clause whose miss is
  recorded on its own.

## Known limits — read before quoting a number

1. **`llm` rubrics are unscored by `run-manual.py`.** It records each one as `manual`
   and writes its rubric to `summary.md` in the results directory, for a judge run
   outside this script or a human. `run-multiturn.py --judge` (or `--judge-dir`) judges
   the multi-turn rubrics with a separate `claude -p`.
2. **Interactive question-tool calls are not directly checkable headlessly.** The portable interview still caps a round at four questions, splitting tool calls when needed or using numbered chat replies. With no user to answer during a headless run, `behavior-interview-max-four-questions` grades the observable equivalent: how many questions the round puts to the user, counted as the interview skill counts them. The
   `no-fifth-numbered-question` regex only catches numbered or bulleted lists; the
   `llm` grader is the real check.
3. **Negative cases prove absence weakly.** A skill not firing on three runs is
   evidence, not proof. Trigger selection is a contextual judgement, and the without-arm
   result for a negative case is structurally uninformative.
4. **The sandbox has no repository** unless the case scaffolds one. Cases run in an empty temporary cwd, so every
   prompt without a scaffold script carries its own material inline — the retrospective skills (`quiz`,
   `buy-in`, `reference`) paste the diff or the reference in, and `blindspot` and
   `tweakable-plan` describe the system they are about. This was not optional: the first draft
   of `trigger-en-quiz` said "you just rewrote our webhook receiver", and the run
   correctly refused ("this session has no prior turns, and the working directory is
   empty"), scoring 0 in both arms for a reason that had nothing to do with the
   plugin. If you add a case, give it its material. Cases without a scaffold script
   therefore measure what a skill does with a *described* situation; scaffolded cases
   hand it real files, and some of them (`behavior-independent-reviewer-code-change`,
   `behavior-brainstorm-scout-finds-unused`, `behavior-scout-checks-pinned-version`,
   `behavior-brainstorm-scout-inventory-monorepo`, `neg-unnamed-review-does-not-spawn-reviewer`,
   `neg-unnamed-investigation-does-not-spawn-scout`) real code it can read.

## Recording results

After a release check, record the figures in that version's **Checked** section of
`CHANGELOG.md`, as releases from 0.9.0 on do, and what was not measured under
**Not measured**; run output stays in the git-ignored `evals/results/`.
`docs/trigger-eval-*.md` are frozen records of the versions or dates they name; v0.3.0's
"6/6, 0 mis-fires" measured the longer v0.3.0 descriptions. Write new files and new
`IMPLEMENTATION_NOTES.md` entries in English; existing Korean records stay as written, an
edit inside one (a freeze banner included) follows its language, and `docs/handoff.md`,
which the owner keeps, stays in Korean.

Record, at minimum: the CLI version, which path was used, per-case score, Δ against
the no-plugin arm, and what was *not* measured. `evals/results/*/summary.md` gives the
method, arms, config and each run's mechanical score; add the CLI version and the Δ by
hand.

`docs/trigger-matrix.md` is the map from skills to trigger phrases; this suite is the
measurement of it. Changing one without the other is how they drift.

## CI

**Not wired as a required gate, on purpose.** Account access and external-suite support for `claude plugin eval` need a fresh check. A live run needs credentials and real money; automatic LLM grading also needs a judge model.

A future manually dispatched job can invoke `python3 evals/run-manual.py --case 'trigger-*' --runs 1 --arm both` with `ANTHROPIC_API_KEY` supplied by CI. It must leave LLM rubrics marked for human grading and must not claim them as scored. Live runs need credentials and cost money; no such CI job is added by this restructure.
