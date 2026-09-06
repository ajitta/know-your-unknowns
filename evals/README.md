# Evals

Reproducible trigger and behaviour cases for the `unknowns` plugin.

Until now the only evidence that the skills fire was a hand-run n=1 sample covering
3 of the 11 skills ([docs/trigger-eval-v0.3.0.md](../docs/trigger-eval-v0.3.0.md)).
Every description edit since has been unverifiable. This directory replaces that with
case files that two different runners can execute.

Two run paths, because `claude plugin eval` is gated:

| path | command | grades `llm` rubrics? | status |
|---|---|---|---|
| A — first-class runner | `claude plugin eval .` | yes, with a judge model | **early access on this account** |
| B — manual headless | `python3 evals/run-manual.py` | no; prints them for a human | works today |

Both read the *same* case files. Path B exists so the suite is not dead weight while
path A is gated; when the gate lifts, path A is the one to trust.

---

## Layout

```
evals/
  <case-slug>/
    prompt.md            # frontmatter + the user prompt to send
    graders/<name>.md    # one grader per file; `type:` in the frontmatter
  results/               # run output; case discovery always skips this directory
  run-manual.py          # path B
```

`prompt.md` frontmatter keys used here: `description`, `tags`, `runs`, `max_turns`,
`timeout_seconds`, `allowed_tools`. Grader types used here: `tool_used`, `regex`,
`file_exists`, `llm`. The grader's name is its filename; an `llm` or `regex` grader's
body is its rubric or pattern. `claude plugin eval --help` is the authority on the
format — this README does not restate it.

`.claude-plugin/plugin.json` deliberately carries **no** `experimental.evals` key: the
default eval directory is already `evals/`, so the key would only rename it.

---

## Path A — `claude plugin eval`

Run from the plugin root (the directory holding `.claude-plugin/plugin.json`):

```bash
# is the gate still closed?  Prints only "`plugin eval` is currently in early access".
claude plugin eval init --bare smoke

# pilot: one run per case, cheap, local report only
claude plugin eval . --runs 1 --ablation with-without --no-scaffold --no-publish \
  --case 'trigger-*'

# full suite
claude plugin eval . --ablation with-without --judge-model sonnet --no-publish

# the three behaviour cases need file-writing tools granted by the operator
claude plugin eval . --case 'behavior-*' --allow-tools Write Edit \
  --ablation with-without --judge-model sonnet --no-publish
claude plugin eval . --case 'neg-one-file-plan-*' --allow-tools Write \
  --ablation with-without --judge-model sonnet --no-publish
```

Notes that matter:

- **Always `--ablation with-without`.** The headline number is Δ — the with-plugin
  score minus the no-plugin score. A high absolute score means little; a plain model
  already answers most of these prompts helpfully.
- **`--judge-model sonnet`.** The default judge is haiku, which is too small for
  rubrics like "the rewritten prompt is the last substantial block".
- **`--no-scaffold` is the default.** No case here has a `scaffold_script`; every
  prompt is self-contained, because cases run in an empty sandbox cwd.
- **Cost.** 29 cases × 3 runs × 2 arms = 174 agent runs plus judging. Pilot with
  `--runs 1 --case '<glob>'` and read `costUsd` in the aggregate result before
  committing to a full pass. `--max-cost-usd` sets a hard ceiling.

## Path B — manual headless

Same case files, plain `claude -p`, no early-access gate:

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

Each run gets a fresh temporary cwd, loads the plugin with `--plugin-dir` (so the
tree on disk is what is measured, not an installed copy), and applies the case's
`allowed_tools` via `--allowedTools` / `--disallowedTools`. `--arm both` runs the
with- and without-plugin arms, which is the manual equivalent of the ablation.

For the no-plugin arm to be honest the plugin must not *also* be enabled in your own
config. Check with `claude plugin list`; `claude plugin disable unknowns` for the
duration of the run if it is.

The raw one-liner behind it, unchanged from the v0.3.0 procedure:

```bash
claude -p "<prompt body from prompt.md>" --output-format stream-json --verbose \
  --max-turns 6 --plugin-dir . --disallowedTools Edit Write Bash
```

Output lands in `evals/results/manual-<timestamp>/` as `manual-result.json` plus a
`summary.md` that already lists the rubrics still needing a human verdict.

---

## What the suite covers

**22 positive trigger cases** — one per language for each of the 11 skills,
`trigger-{en,ko}-<skill>`. Every prompt embeds a phrase that is quoted verbatim in
that skill's current `description` (see [docs/trigger-matrix.md](../docs/trigger-matrix.md)).
When a description changes, the case that used a dropped phrase must change with it.

**4 negative cases** — the collisions the trigger matrix admits are unresolved:

| case | must not fire | why |
|---|---|---|
| `neg-ui-options-does-not-fire-brainstorm` | `unknowns:brainstorm` | brainstorm advertises "show me options"; prototypes owns UI variants |
| `neg-vocabulary-does-not-fire-blindspot` | `unknowns:blindspot` | blindspot investigates code, teach-me teaches vocabulary |
| `neg-interval-loop-does-not-fire-unknowns-loop` | `unknowns:loop` | a bare "loop … every 5 minutes" is the built-in interval runner |
| `neg-one-file-plan-defers-to-plan-mode` | (behaviour, not trigger) | the plan skill's own size gate: ≤2 files and no schema/interface/UX decision → defer to native plan mode |

**3 behaviour cases** — these grade the deliverable, not the trigger:

| case | checks |
|---|---|
| `behavior-blindspot-ends-with-improved-prompt` | the pass ends with a pasteable rewritten prompt that folds in the risks it found |
| `behavior-interview-max-four-questions` | at most 4 questions reach the user in one round, on a prompt that dangles nine open decisions |
| `behavior-notes-appends-to-file` | `IMPLEMENTATION_NOTES.md` is actually created, with the entry fields filled — not summarised in chat only |

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
2. **The AskUserQuestion call shape is not directly checkable.** The requirement in
   `skills/interview/SKILL.md` is "max 4 questions per round (AskUserQuestion hard cap:
   1-4)". AskUserQuestion cannot be granted to a headless run — there is no user to
   answer — so `behavior-interview-max-four-questions` grades the observable
   equivalent: how many decisions the round puts to the user. The
   `no-fifth-numbered-question` regex only catches numbered or bulleted lists; the
   `llm` grader is the real check.
3. **Negative cases prove absence weakly.** A skill not firing on three runs is
   evidence, not proof. Trigger selection is a contextual judgement, and the without-arm
   result for a negative case is structurally uninformative.
4. **The sandbox has no repository.** Cases run in an empty temporary cwd, so every
   prompt carries its own material inline — the retrospective skills (`quiz`,
   `buy-in`, `reference`) paste the diff or the reference in, and `blindspot` and
   `plan` describe the system they are about. This was not optional: the first draft
   of `trigger-en-quiz` said "you just rewrote our webhook receiver", and the run
   correctly refused ("this session has no prior turns, and the working directory is
   empty"), scoring 0 in both arms for a reason that had nothing to do with the
   plugin. If you add a case, give it its material. What the suite therefore measures
   is what a skill does with a *described* situation, not with real code it can read.
5. **`skills/loop/SKILL.md` step 3 still says "max 5 per round"** while
   `skills/interview/SKILL.md` says 4. `behavior-interview-max-four-questions` grades
   against 4, the interview skill's own number. If the loop's number is the one that is
   right, this case has to change with it.

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

**Not wired as a required gate, on purpose.** `claude plugin eval` is early access on
this account, and a run needs credentials, a judge model and real money — a per-push
gate would be flaky and expensive.

When the command is generally available, the smallest useful wiring is a separate,
manually dispatched job — not a step in the existing `hook-tests` / `plugin-validate`
jobs:

```yaml
  eval:
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - run: npm install -g @anthropic-ai/claude-code
      - run: |
          claude plugin eval ${{ env.PLUGIN_DIR }} \
            --case 'trigger-*' --runs 1 --ablation with-without \
            --judge-model sonnet --no-publish --threshold 0.8
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

`--threshold 0.8` exits 1 when any case scores below 0.8. Add `on: workflow_dispatch`
to the workflow's triggers for the `if:` above to be reachable. Treat a release as the
natural cadence rather than a push.
