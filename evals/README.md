# Evals

Reproducible trigger and behaviour cases for the `unknowns` plugin.

The evidence that the skills fire used to be a hand-run n=1 sample covering 3 of the 11
skills ([docs/trigger-eval-v0.3.0.md](../docs/trigger-eval-v0.3.0.md)), which left every
description edit after it unverifiable. This directory replaced that with case files two
different runners can execute. The current measurement is
[docs/trigger-eval-v0.5.1.md](../docs/trigger-eval-v0.5.1.md): 30 cases, 23 of 23
mechanical graders passing, no timeouts. What it still cannot say is whether a skill did
its job *well* — that needs the `llm` rubrics, and those need path A's judge model.

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
  multiturn/<case>/      # multi-turn cases: case.md + graders/ (see below)
  results/               # run output; case discovery always skips this directory
  run-manual.py          # path B
  run-multiturn.py       # multi-turn runner with a simulated user and a judge
```

`prompt.md` frontmatter keys used here: `description`, `tags`, `runs`, `max_turns`,
`timeout_seconds`, `allowed_tools`, `append_system_prompt`. Grader types used here: `tool_used`, `regex`,
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
its own `description` declares (the `: '<phrase>'` at the end of that line) is still
quoted in that skill's `description` on disk and still present in the prompt. Trim a
phrase out of a `SKILL.md` and `--verify` fails on the case that used it. Run it after
any description edit; it exits non-zero on any problem.

Each run gets a fresh temporary cwd and loads the generated `plugins/unknowns/` directory through an absolute `--plugin-dir` path (so the committed payload is measured, not an installed copy), and applies the case's
`allowed_tools` via `--allowedTools` / `--disallowedTools`. `--arm both` runs the
with- and without-plugin arms, which is the manual equivalent of the ablation.

`--crowd N` also loads a generated plugin of N filler skills (written into the results
directory, so the run can be repeated). Claude Code budgets the skill listing (1% of the
context window by default) and, when it overflows, keeps descriptions for the most-used
skills (usage counts decayed by recency) and lists the rest by name only. A clean eval
environment rarely overflows, so a trigger rate measured there says little about a
machine with sixty skills installed. Usage counts live in the Claude config
(`skillUsage` in `.claude.json`) and headless runs update them too, so each crowd run gets
a fresh, empty `CLAUDE_CONFIG_DIR` (no usage history — synced or managed plugins may still
load) and the filler plugin is loaded first, so ties do not favour this plugin. Each crowd
run writes a `--debug-file`; the report records whether the CLI logged the listing as over
budget and which plugins loaded. **Sign-in:** a fresh config dir usually holds no
credentials, so set `ANTHROPIC_API_KEY` for crowd runs; a run that cannot start is
reported as `FAILED` and left ungraded, not counted as a trigger miss. `--budget-fraction F` sets
`skillListingBudgetFraction` to force an overflow regardless of the context window —
`--crowd 60 --budget-fraction 0.002` drops every unknowns description (the CLI logs
"Skill listing over budget" under `--debug-file`). First result:
[docs/trigger-eval-crowd-2026-09-30.md](../docs/trigger-eval-crowd-2026-09-30.md).

For the no-plugin arm to be honest the plugin must not *also* be enabled in your own
config. Check with `claude plugin list`; `claude plugin disable unknowns` for the
duration of the run if it is.

The raw one-liner behind it, adapted to the generated payload path (run from the repository root):

```bash
claude -p "<prompt body from prompt.md>" --output-format stream-json --verbose \
  --max-turns 6 --plugin-dir ./plugins/unknowns --disallowedTools Edit Write Bash
```

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
  graders/<name>.md    # llm (focus: transcript), regex, question_count, tool_used
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
<session>` in the same cwd. Every prompt is sent on STDIN. The run ends on `STOP`, at
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
recorded as unjudged, not as FAIL.

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
`trigger-{en,ko}-<skill>`. Every prompt embeds a phrase that is quoted verbatim in
that skill's current `description` (see [docs/trigger-matrix.md](../docs/trigger-matrix.md)).
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

**8 Open-cell negatives** — `neg-open-*`: requests both sides already understand. None
may fire an unknowns skill (`input_match: "unknowns:"`, `min: 0`, `max: 0`, `arm: both`).
Five are trivial (a rename, typo fixes, a polite rewrite, an errand "plan", "quiz me" on
trivia) and must be done directly, with no read-back. Three carry weight and must get a
2-3-line read-back of the request, the assumptions and what counts as done, then wait
for confirmation, with no method run. Two of them (`neg-open-weighty-code-en`, a
migration going to production tonight; `neg-open-weighty-text-ko`, a notice to all 80
staff) are tagged `informative`: they measure the gap the plugin leaves without a
`CLAUDE.md` line (the read-back lives in the skill bodies, and no skill loads for a clear
request), so they do not block a release. The third, `neg-open-weighty-memory-line-en`,
runs the migration with the README's `CLAUDE.md` line passed as `append_system_prompt`,
which `run-manual.py` hands to `claude -p --append-system-prompt`; the harness has no
project-memory fixture, so this stands in for the user's `CLAUDE.md`.

**4 negative cases** — the collisions the trigger matrix admits are unresolved:

| case | must not fire | why |
|---|---|---|
| `neg-ui-options-does-not-fire-brainstorm` | `unknowns:brainstorm` | brainstorm advertises "show me options"; prototypes owns UI variants |
| `neg-vocabulary-does-not-fire-blindspot` | `unknowns:blindspot` | blindspot investigates a specific plan or situation, teach-me teaches vocabulary |
| `neg-interval-loop-does-not-fire-unknowns-loop` | `unknowns:unknowns-loop` | a bare "loop … every 5 minutes" is the built-in interval runner |
| `neg-one-file-tweakable-plan-defers-to-plan-mode` | (behaviour, not trigger) | the tweakable-plan skill's own size gate: ≤2 files and no schema/interface/UX decision → defer to native plan mode |

**3 behaviour cases** — these grade the deliverable, not the trigger:

| case | checks |
|---|---|
| `behavior-blindspot-ends-with-improved-prompt` | the pass ends with a pasteable rewritten prompt that folds in the risks it found |
| `behavior-interview-max-four-questions` | at most 4 questions reach the user in one round, on a prompt that dangles nine open decisions |
| `behavior-deviation-log-appends-to-file` | `IMPLEMENTATION_NOTES.md` is actually created, with the entry fields filled — not summarised in chat only |

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

## Known limits — read before quoting a number

1. **`llm` rubrics are unscored on path B.** `run-manual.py` records each one as
   `manual` and writes its rubric to `summary.md` in the results directory; a human
   decides. Only path A scores them automatically.
2. **Interactive question-tool calls are not directly checkable headlessly.** The portable interview still caps a round at four questions, splitting tool calls when needed or using numbered chat replies. With no user to answer during a headless run, `behavior-interview-max-four-questions` grades the observable equivalent: how many decisions the round puts to the user. The
   `no-fifth-numbered-question` regex only catches numbered or bulleted lists; the
   `llm` grader is the real check.
3. **Negative cases prove absence weakly.** A skill not firing on three runs is
   evidence, not proof. Trigger selection is a contextual judgement, and the without-arm
   result for a negative case is structurally uninformative.
4. **The sandbox has no repository.** Cases run in an empty temporary cwd, so every
   prompt carries its own material inline — the retrospective skills (`quiz`,
   `buy-in`, `reference`) paste the diff or the reference in, and `blindspot` and
   `tweakable-plan` describe the system they are about. This was not optional: the first draft
   of `trigger-en-quiz` said "you just rewrote our webhook receiver", and the run
   correctly refused ("this session has no prior turns, and the working directory is
   empty"), scoring 0 in both arms for a reason that had nothing to do with the
   plugin. If you add a case, give it its material. What the suite therefore measures
   is what a skill does with a *described* situation, not with real code it can read.

## Recording results

After a run, record the numbers in `docs/trigger-eval-<version>.md` — replacing
`docs/trigger-eval-v0.3.0.md`, whose "6/6, 0 mis-fires" measured the longer v0.3.0
descriptions and is not a measurement of the current ones. Files under `docs/` are
Korean; this directory and `tests/` are English.

Record, at minimum: the CLI version, which path was used, per-case score, Δ against
the no-plugin arm, and what was *not* measured. `evals/results/*/summary.md` is
already in that shape.

`docs/trigger-matrix.md` is the map from skills to trigger phrases; this suite is the
measurement of it. Changing one without the other is how they drift.

## CI

**Not wired as a required gate, on purpose.** Account access and external-suite support for `claude plugin eval` need a fresh check. A live run needs credentials and real money; automatic LLM grading also needs a judge model.

A future manually dispatched job can invoke `python3 evals/run-manual.py --case 'trigger-*' --runs 1 --arm both` with `ANTHROPIC_API_KEY` supplied by CI. It must leave LLM rubrics marked for human grading and must not claim them as scored. Live runs need credentials and cost money; no such CI job is added by this restructure.
