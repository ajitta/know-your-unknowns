# Skill authoring guide: Anthropic's best practices applied to this plugin

Checked 2026-11-03 against [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) (the `.md` rendering of the page, which keeps the callouts that HTML extractors drop) and the [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). This guide maps each official practice onto this repository. `.claude/rules/skill-writing.md` stays the authority for how skill and agent text reads; this file records which official practices apply here, which are already covered by a rule there, and which are not adopted and why.

## Contents

- Provenance of the "quiet revision" claim
- Supported models and effort
- Practice-by-practice mapping
- Practices not adopted
- Checklist for a skill change

## Provenance of the "quiet revision" claim

The page carries no revision date. A Wayback Machine capture of the same page from 2025-10-16 (the Agent Skills launch week, then at `docs.claude.com`) already contains every item that secondary sources in October 2026 described as new: the table of contents for reference files over 100 lines, one-level references with the `head -100` reason, the three degrees of freedom, the copyable checklist, "Always write in third person", testing with Haiku, Sonnet and Opus, three evaluation scenarios, the 500-line body limit and the explicit install command. Treat these as the original guidance, not as a new rule set.

Claims in secondary sources that the official page does not make:

| Claim | What the page says |
|---|---|
| Claude reads roughly the first 100 lines of any long file to decide whether to load it | Partial reads (`head -100`) are described for files reached through nested references; the table of contents is for reference files over 100 lines. |
| Anthropic now asks to trim instructions for newer reasoning models | Not on this page. The per-model questions ask whether the skill gives Haiku enough guidance and whether it avoids over-explaining for Opus. |
| Document the intended model in the YAML front matter | Not on this page. This repository's frontmatter whitelist (`name`, `description`) does not allow it either. |
| Low freedom for payments and deletions | The page's example is a database migration; payments and deletions are the source's extension. |

## Supported models and effort

Owner policy (2026-11-03): the plugin is developed for and checked on **Claude Opus 5.5** (Claude Code, claude.ai) and **GPT-6.1 Sol** (Codex, ChatGPT), both at **medium effort**. No other model is tested; Sonnet and Haiku are not tuning targets.

This follows the page's principle ("Test your Skill with all the models you plan to use it with"): the set of planned models is ours to name. The page's checklist line "Tested with Haiku, Sonnet, and Opus" is that principle applied to a skill meant for all three, so it is replaced here by the two named models.

How each per-model question maps onto the target:

| Official question | Applies here as |
|---|---|
| Opus: does the skill avoid over-explaining? | Opus 5.5 and GPT-6.1 Sol: every sentence makes the model do the method (`skill-writing.md` rule 17). |
| Haiku: does the skill provide enough guidance? | Medium effort: a step the model skips or reorders with less thinking is a guidance gap. Read failures at medium effort with this question. |
| Sonnet: is the skill clear and efficient? | Covered by the two rows above. |

Measurement rules:

- Eval runs pin the effort: `evals/run-manual.py` and `evals/run-multiturn.py` pass `--effort medium` to the model under test by default (`--effort default` leaves the CLI default) and record it in each result; Codex runs use `-c model_reasoning_effort=medium`. Results recorded before 2026-11-03 ran at the CLI default effort, which was not recorded; do not compare them with medium-effort runs as if the condition were the same.
- Development and iteration run on Opus 5.5 at medium effort. GPT-6.1 Sol at medium effort runs once per release build.
- Users on other models or efforts are not covered by any measurement. The READMEs say which models and effort the plugin was checked on.

Run counts (owner, 2026-11-03: fewer runs; a run sizes a decision, it does not prove completeness). Write the decision rule before the run. Pass the count with `--runs`; the `runs: 3` in each case file is the structural minimum `--verify` checks, not the count to run.

| Check | Runs |
|---|---|
| A fix | 2 runs of each case that failed. 2/2 keeps the fix, 0/2 reverts it, 1/2 gets one more run. |
| Cases next to a fix (same skill or agent, not failing) | 1 run each |
| Routing doubt (a skill did not fire) | 3 runs of that case; 2 or more misses opens the description |
| A watch cell (a 1-in-3 slip) | No run of its own; read it in the next run that includes the case |
| Release, Opus 5.5 | The whole suite once: 1 run per case, single-turn and multi-turn |
| Release, GPT-6.1 Sol | 1 run per `trigger-*` case |
| Text audit (writing-for-models) | One check of the diff, by one reader; no per-file audit |

## Practice-by-practice mapping

Status values: **covered** (an existing rule or check already does it), **adopt** (new here), **n/a** (does not apply to an instruction-only plugin), **watch** (adopt when a failure shows the need).

### Format limits

| Practice | Status | Where |
|---|---|---|
| `name` ≤ 64 characters, lowercase letters, digits and hyphens | covered | `tools/package.py` |
| `name` without the reserved words `anthropic`, `claude` | covered | `tools/package.py` (added 2026-11-03); the name pattern already excludes XML tags |
| `description` 1–1,024 characters | covered | `tools/package.py`. This repository's own limit is 200 characters (`skill-writing.md` rule 18, owner ruling 2026-11-12), checked by `tests/test_portability.py` and `tests/test_skill_descriptions.py`. |
| `description` without XML tags | covered | `tools/package.py` rejects `<` and `>` (added 2026-11-03) |
| `SKILL.md` body under 500 lines | covered | `tools/package.py` (added 2026-11-03); the longest body is 111 lines |
| Claude Code truncates `description` plus `when_to_use` at 1,536 characters | covered | the 1,024 limit is stricter |

### Structure

| Practice | Status | Note |
|---|---|---|
| Progressive disclosure through reference files | not used | Each `SKILL.md` is self-contained by design (AGENTS.md); the audit below found no content worth moving. |
| References one level deep from `SKILL.md` | covered by design | No skill has reference files. If one is ever added, link it from `SKILL.md` only. |
| Table of contents in reference files over 100 lines | n/a | Applies when a reference file exists; this guide follows it. |
| Forward slashes in paths | covered | No backslash paths in skills or agents. |
| Fully qualified tool names (`Server:tool`) | covered | The scout is named `unknowns:unknowns-scout`. |
| Utility scripts, "solve, don't defer", package dependencies | n/a | The plugin ships no executable code. Tool availability is handled by the shared missing-tool line (`skill-writing.md` rule 11). |

### Reference-file audit (2026-11-03)

The page splits content out of `SKILL.md` for two reasons: the body approaches 500 lines, or a part is needed only for some tasks ("Pattern 3: Conditional details"), so the model reads it only then. The bodies total about 9,300 words; the longest (blindspot) is 1,381 words, roughly 1,800 tokens, loaded only when the skill runs. The conditional parts:

| Part | Words | Read when |
|---|---|---|
| prototypes, Variants | 150 | the interaction itself, an internal design or "wild" is asked for |
| deviation-log, Wrap-up | 131 | at the end of a session or a handover |
| blindspot, Scope | 90 | the request could belong to teach-me |
| blindspot, scout packet | 70 | the scope spans many sources |
| brainstorm, scout packet (2b) | 70 | the scout is spawned |
| reference, What Can Be a Reference | 69 | the kind of reference is unusual |
| teach-me, domain comparison table | 49 | step 5 runs |
| interview, step 5 (deep interview) | 26 | the user asks for a deep interview |

Verdict: move none. The largest move saves about 200 tokens per run, and each move costs more than that:

- **The conditional branch is where a link gets skipped.** The page itself lists "missed connections" (the model not following a reference) as a failure to watch. A skipped link fails silently in exactly the branch the content was for, and that failure is likelier at medium effort.
- **Compaction keeps `SKILL.md`, not what was read later.** Claude Code re-attaches an invoked skill's `SKILL.md` (first 5,000 tokens) after compaction; a reference file read through a tool is summarized like any other tool result. deviation-log's Wrap-up runs at the end of a long session, after compaction is most likely.
- **Some runs have no file tool.** The host delivers `SKILL.md` itself, but a reference file needs a tool to read it, and every skill must complete without one (the missing-tool line, rules 3 and 11).
- **The read-back paragraph (118 words, in every skill) stays.** It decides on entry whether the method runs at all, so it is needed on every run, and it is a shared block (rule 11). Owner ruling 2026-11-13, after a run with the paragraph removed from ten bodies: a skill invoked by name with a self-evident request ("sort the import lines") ran its whole method 4 of 4 times in interview and brainstorm, where the shipped text did the request directly 4 of 4.

Revisit when a body passes about 300 lines, or when one conditional part grows past about 500 words.

### Degrees of freedom

Set freedom per step, not per skill. In this plugin:

| Freedom | Steps it fits | Form |
|---|---|---|
| High | Investigating, choosing questions, spreading candidates, judging the outcome | Plain steps with the reason (rule 4). |
| Medium | Deliverables: cards, decision tables, the improved prompt, the deviation log entry | A named structure with fixed fields and labels (kinds, statuses), the content left to the model. |
| Low | none | Low freedom means an exact script; the plugin ships none. A step whose order or count must hold (at most four questions, unchecked items out of the cards) is a medium-freedom rule stated once with its reason and pinned by an eval. |

### Workflows and feedback loops

| Practice | Status | Note |
|---|---|---|
| Clear sequential steps | covered | Rules 1–3. |
| A checklist the model copies into its reply and ticks off | watch | Candidate for `unknowns-loop` only (seven stages). Add it when a medium-effort run skips or merges a stage, then check it by the run-count table. No eval case runs the loop's stages yet, so the medium-effort baseline gave no evidence either way. A checklist in a short skill is read on every run and repeats the steps. |
| Return to an earlier step when a check fails | covered where the check uses outside evidence | blindspot's evidence and status, the independent-reviewer agent. A loop that only re-reads the model's own output adds a pass with no new evidence and is not added. |
| Plan-validate-execute with a script | n/a | No scripts. |

### Descriptions

| Practice | Status | Note |
|---|---|---|
| What the skill does and when to use it, with key terms | covered | Since 0.13.0 every description is the short text of `skill-writing.md` rule 18 (owner ruling 2026-11-12): a label, what the skill is for and a "Use on …" clause with the trigger phrases, in 200 characters or fewer. The method summary moved out; the body states the method. |
| Third person | watch | The short set is not in the third person: it uses imperatives and the second person ("find both sides' unknown unknowns", "ask in rounds of ≤4", "quiz you"). The page's reason is discovery; routing measured 260/260 and 44/44 with the descriptions before 0.13.0, and 22/22 trigger and 22/22 non-coding loads with the short set (1 run each). Rerun the trigger, non-coding and negative cases (1 run each) when a description changes. |
| Specific over vague | covered | Owner ruling 2026-10-28: no "pushier" descriptions. |

### Content

| Practice | Status | Note |
|---|---|---|
| Only what the model does not already know | covered | Rule 17. |
| No time-sensitive information | covered | No dates in skills or agents. |
| One term per concept | covered | Rule 9. |
| One default instead of a menu of options | covered | Scope tables give one action per case. |
| Concrete examples; template strictness matched to the need | covered | Medium-freedom deliverables above. |

### Evaluation

| Practice | Status | Note |
|---|---|---|
| At least three evaluations per skill | covered | `evals/` has single-turn and multi-turn cases for every skill; `independent-reviewer` has two. |
| Baseline without the skill | covered | `--arm` in `evals/run-manual.py`. Distinct from comparing two plugin versions, which the owner does not run. |
| Claude A writes, Claude B uses, observe and refine | covered | Failures read from this build's own runs. |
| Test with real usage | covered | Owner surface checks recorded in the handoff. |

## Practices not adopted

- **Testing on Haiku and Sonnet:** replaced by the supported-model policy above.
- **Stronger wording ("MUST filter") to make a rule prominent:** the page lists it as one possible refinement. Emphasis competes with the method for attention (rule 10); a rule that is missed gets restructured or given its reason instead.
- **Guard prose for fragile steps:** rule 17. A user who needs enforcement builds it into their harness.

## Checklist for a skill change

1. Read `.claude/rules/skill-writing.md` and grep `tests/` for phrases the edit touches (rule 13).
2. Keep the body under 500 lines and self-contained.
3. A new or changed description says what the skill is for and when to use it, stays within 200 characters with no XML tags and no method summary (`skill-writing.md` rule 18), and is changed in `scripts/skill-descriptions.json` too.
4. Give each changed step the freedom it needs (table above) and its reason.
5. Run `python3 tools/package.py`, `python3 tools/package.py --check`, the unit tests and both `claude plugin validate --strict` commands.
6. Run the changed skill's failing cases and its neighbours by the run-count table above; for a description change also the trigger, non-coding and negative cases, 1 run each.
7. At release, run the suite once on Opus 5.5 and the trigger cases once on GPT-6.1 Sol, both at medium effort.
