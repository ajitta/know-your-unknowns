# Changelog

## [Unreleased]

Owner decisions on the open items left after 0.13.3, in two rounds (owner approvals 2026-11-24; choices and the run rules written before the runs in the two newest `IMPLEMENTATION_NOTES.md` entries, 2026-11-24).

### Changed

- unknowns-loop, step 3 stage a: the Run cell gives the order for a user who can describe the task but lacks the field's vocabulary: "the **blindspot** skill; the **teach-me** skill first when the user cannot yet describe the task, and after the **blindspot** skill when the user can describe the task but lacks the field's vocabulary". The cell had named only the first case, and runs that knew no terms put a vocabulary lesson before the investigation of the user's own situation (`behavior-unknowns-loop-terms-only`: 0 of 6 in the 0.13.3 round; 1 of 8 saved replies passes the clarified grader).
- buy-in, step 4b: a report the user gave of where the work stands goes to the independent-reviewer agent as claims: "Even when the user produced the work, hand it each statement in any report the user gave of where the work stands (e.g. what is done, figures so far, what is still pending) among the claims, as a claim whose original source is the record it reports on." The shared field sentence now ends at "the claims the work rests on.", as the reviewer's copy does, and "Leave out the producer's own summary, …" is its own sentence. Step 4b had named no form for such a report: in 3 of 4 runs of `behavior-buy-in-reviewer-packet-from-conversation` the user's status went in as material to check against, and the reviewer called its figures verified.

### Changed (developer-only)

- blindspot and brainstorm scout cases (`behavior-blindspot-scout-many-contracts`, `behavior-brainstorm-scout-inventory-monorepo`): the spawn grader and the three scout-path graders of each case are indicators (`weight: 0`; the scout-path graders pass when no scout ran). Owner ruling: "more sources than you can read in full" is the model's own judgment of what it can read; a direct investigation that reaches the result conforms, a spawn conforms too, and no case asserts a spawn from the size of the material. No skill text changes.
- tweakable-plan: `behavior-tweakable-plan-autoloaded-reads-back` is renamed `behavior-tweakable-plan-autoloaded-weighty-plan` and graded by `plans-through-the-size-gate`, written from the size gate's first row. Owner ruling: a request for the skill's own plan goes through the size gate however weighty the work it plans; the read-back paragraph covers requests to do the work. No skill text changes.
- `behavior-unknowns-loop-terms-only`: `blindspot-before-teach-me` gives one reading for a stage that holds both the investigation and a vocabulary explainer (the investigation is named first).
- buy-in outcome graders (`noncode-en-buy-in`, `noncode-ko-buy-in`, `trigger-en-buy-in`, `trigger-ko-buy-in`): one identical sentence counts an item with no evidence yet as answered when it is listed under the limitations with the evidence it needs, as step 4c asks. The trigger graders had failed that move.
- New case `behavior-buy-in-reviewer-packet-from-conversation`: buy-in whose plan, criteria, outcome, deviation log and status exist only in the user's message, with the Agent tool allowed; it grades what the independent-reviewer's packet carries and what its report says it could not check.
- `evals/run-multiturn.py`: `MAX_USER_TURNS` 8 → 10, and `unknowns-loop-every-stage-to-outcome-check` uses 10, so a run that spends a turn on the probe reaches the outcome question.
- `.github/workflows/release.yml`: the annotated-tag check prints an `::error::` when it fails. The release procedure no longer checks the release body by hand: run logs show `actions/checkout` overwriting the annotated tag with a lightweight ref and the workflow's re-fetch restoring it.

- `evals/run-manual.py --crowd`: the results directory is absolute, so the filler plugin loads when `--out` is relative; a crowd run whose CLI log does not show the filler plugin is void (reported `FAILED`, never scored); each crowd run records the CLI's listing lines and the session's `plugin_errors`.
- New multi-turn case `unknowns-loop-blindspot-then-teach-me`: a user who can describe the task but knows no audio terms picks prompt fixes from the blind-spot pass and terms from the vocabulary explainer; `hands-on-both-picks` judges whether the reply that opens the next stage builds on a request carrying both sets of picks or says which are still to apply. A gate of the 0.13.4 release check.
- `behavior-buy-in-reviewer-packet-from-conversation`: `doc-carries-what-the-review-found` criterion 1 judges every status figure in the doc, whatever the reviewer concluded: given as the user's figure with a record the user mentioned or the doc asks for, or listed as unconfirmed; a record the user never mentioned does not count. Two graders quote step 4b in words that fit both its old and its new wording.
- `behavior-buy-in-autoloaded-reads-back` is informative: buy-in loaded in 0 of 3 runs, and a request clear to both sides gives buy-in nothing to surface. Its regex `whole-reply-fits-a-read-back` is `weight: 0`.
- `behavior-reference-asks-for-the-reference` names the skill ("Use the reference skill."): without the name, reference loaded in 1 of 3 runs. It stays scored.
- README (both languages), "What works where" and the agents section: the agents run in Claude Code and, by Anthropic's documentation, in Cowork (not checked with this plugin); chat skips them; a general subagent that a host starts in the reviewer's place, as Codex did in recorded runs, is not buy-in's independent check.
- `docs/protocol-alignment.md` (frozen): line 3 names its source as the owner's notes outside the repository in place of a personal notes location, with a dated line in its banner. The rest is unchanged; git history keeps the earlier text.
- The teach-back citation of the frozen `docs/value-contract.md` is identified (Kidd 1987, pp. 91–108); what it supports is recorded in `IMPLEMENTATION_NOTES.md`, and the record is unchanged.
- `evals/run-multiturn.py`: an `llm` grader may set `focus: packets`; its judge also sees, after the conversation, the `prompt` of each Agent or Task call the assistant made itself, marked with the reply it was sent in. The transcript judge prompt is unchanged byte for byte (a test pins it), and text written inside a spawned agent no longer joins the reply that the simulated user, the stop test and the judges read. New case `buy-in-reviewer-packet-after-plan`: a plan the assistant wrote and the user approved, a change reported later, then a buy-in doc; it grades the reviewer's packet.
- `evals/README.md`: the case counts (105 single-turn, 104 having missed `behavior-buy-in-reviewer-packet-from-conversation`; 19 multi-turn), `focus: packets`, and the notes on the changed cases.
- README (both languages): the recorded automated runs include the Codex CLI and the empty-config installs on 0.13.3.

### Checked (developer-only)

Claude Code 2.1.331, Opus 5.5 (`ANTHROPIC_MODEL=claude-opus-5-5`), `--effort medium`, isolated config, 2026-11-24, under keep/revert rules committed before the runs (`IMPLEMENTATION_NOTES.md`, 2026-11-24). Shipped candidates ran on a copy of the build with only those sentences changed. Single-turn `llm` graders were judged in this session, one judge per item and an independent second judge on every fail (no verdict was disputed); multi-turn ones by `run-multiturn.py --judge`. Results are in `evals/results/round-2026-11-24b/` (git-ignored).

- Before the runs, one reader who did not write the candidates found phrases with two readings in both shipped candidates; the first wordings were revised and never run.
- unknowns-loop stage a (kept): a second reader, after the runs, found the kept cell's "lacks only the field's words" open to two readings and a second name for vocabulary; the revised wording ran again (terms-only 2 of 2; the six single-turn neighbours and `unknowns-loop-criteria-unanswered` passed every grader) and ships byte-identical to the text those runs used. The first wording's runs: `behavior-unknowns-loop-terms-only` passed 2 of 2 on the candidate; the clarified grader passes 1 of 8 saved replies of the current text (the 0.13.2 release run), second judges agreeing on the seven fails. Neighbours, one run each: `behavior-unknowns-loop-cannot-describe` (teach-me still first), `-finds-noncode-log`, `-keeps-investigation`, `-probe-fails`, `noncode-en-unknowns-loop` and `noncode-ko-unknowns-loop` passed every grader; multi-turn `unknowns-loop-criteria-unanswered` passed. `unknowns-loop-every-stage-to-outcome-check` passed `stages-run-in-order` (the stage-d probe asked of the user), `deviation-logged` and `outcome-check-ends-the-loop`, which the 0.13.3 round had missed, and missed `done-criteria-carry-to-verification` (the step-5 check gave no status for what must not break or for the cost, and marked the email criterion met), which the 0.13.3 run had passed; 2 more runs passed it both times (a watch cell), with `stages-run-in-order` 2 of 3 and `deviation-logged` 3 of 3 over the three runs.
- teach-me 7b (reverted): the candidate "Put in the draft only the terms, presets and details the user gave or picked …" passed `draft-with-assumptions` in 1 of 3 runs of `teach-me-stops-at-draft` (the drafts kept their concrete settings; nothing was built in 3 of 3). With 1 of 7 on the current sentence and 0 of 2 on the widened one, the item is closed as a known miss and the grader stays scored.
- buy-in 4b (reverted): `behavior-buy-in-reviewer-packet-from-conversation`, two baseline runs and two with a sentence asking for conversation-only items "copied rather than retold and marked with where it came from". The reviewer was called in 4 of 4, and every source that existed only in the user's message reached the packet as content in 4 of 4, with no reference in its place. The user's status report was given as a claim to check in 1 of 4 (baseline 1 of 2, with the sentence 0 of 2) and the reviewer treated it as verified or as fact in the same 3 runs; the doc carried what the review found in 4 of 4 and no packet held the producer's own summary. The sentence reverted under the rule, and the status-as-claim question went to the open-items table.
- Corrected graders: the four buy-in outcome graders pass 16 of 16 saved Korean replies and 2 of 2 English ones (the prediction written before was that the `st-g3` `trigger-ko-buy-in` replies would stay failed; they passed, listing the missing evidence as open questions), and one new run of each of the four cases passed. The Korean buy-in body finding is closed.
- `behavior-tweakable-plan-autoloaded-weighty-plan`: loaded tweakable-plan and passed `plans-through-the-size-gate` (1 run, steps one line each).
- buy-in step 4b (kept), second round of 2026-11-24, under the rule committed before the runs (`6e6fe96`). Two readers who did not write it checked the wording before any run. The first found three phrases with two readings in the first candidate. The second found that the first reader's revision, "check against its original source", could make the user's own message the source. The shipped wording is the second reader's. The corrected doc grader judged the four saved docs of the first round 2 of 4, as predicted before the judging (both baseline docs pass, and the two docs from the reverted sentence fail on "18 of 20 let" with no record and "Evidence: plot list"). On a copy of the build with only step 4b changed, the case passed every grader in 2 of 2 runs (reviewer called, packet criteria 1–5, report, doc, producer-summary indicator). Both packets listed the user's status under a heading such as "STATUS CLAIMS TO CHECK (source would be the organiser's records; none attached)", and both reports marked the three done criteria and gave an outcome line. Neighbours, one run each on that copy: `behavior-buy-in-relays-reviewer`, `behavior-independent-reviewer-report-vs-records` and `behavior-buy-in-finds-noncode-log` passed every grader. The multi-turn `buy-in-partial-picks` (no Agent tool, so step 4b does not run) missed `final-doc-keeps-unpicked-limits`: an open question from the draft ("anyone else who has to agree, such as a landowner or a ward councillor?") was dropped from the final doc without a word. It missed in 2 of 3 runs of the 0.13.3 round too; it goes to the open-items table.
- `behavior-reference-asks-for-the-reference`, now naming the skill: loaded reference and passed `asks-one-question-for-the-reference` (1 run; one question with ways to supply the reference, and a note that the reading comes before any drafting). It stays scored.
- Crowd runner check (not a measurement): one probe run with `--crowd 60 --budget-fraction 0.002` on the fixed runner logged "Skill listing over budget: 88 skills, 19014 chars > 6000 budget — descriptions will be truncated" with `evalcrowd` and `unknowns` loaded. The model, asked to copy its listing, gave all eleven unknowns skills by name only and 15 of Claude Code's own skills with descriptions (a self-report).
- Correction to 0.13.3 **Checked**: its crowded-listing figures (blindspot 0 of 6, the other ten skills 60 of 60) come from a listing of this plugin and Claude Code's own skills, 28 skills over a forced 6,000-character budget, not from 60 filler skills. `--out` was relative, the runner passed the filler path under it to runs that start in a temporary directory, and every run logged 28 skills with only this plugin loaded. Which descriptions that listing kept was not recorded. The released 0.13.3 section is left as it was.

### Not measured

- On Codex, whether a buy-in doc's "independent review" wording matches a subagent that ran: the 0.13.3 Korean Sol run's doc states a review result, and its exec stream shows no wait.

- How the buy-in reviewer handles material built over earlier turns (a plan or a deviation log made by the model in the conversation): the multi-turn runner cannot grade an Agent call's packet.
- Whether buy-in waits for the reviewer in an interactive session, where Claude Code cannot wait for a background subagent while fork mode is on; every eval runs `claude -p`.
- The neighbours of the reverted candidates (teach-me's single-turn cases, the buy-in reviewer cases) were not run.

## 0.13.3 — 2026-11-24

Prepared 2026-11-24 for the owner's merge and tag. Text that had gone out of date across releases, from an audit of the repository at 0.13.2 (owner approval 2026-11-24). Then a description round and the recommendations of the open-items table (owner approval 2026-11-24): six skill descriptions and the code row of the deviation-log skill's log-file table changed, and 20 eval cases were added.

### Changed

- Plugin and marketplace descriptions (`plugin-manifest.json`, `.claude-plugin/marketplace.json`): the list after "Eleven skills" names the unknowns loop ("buy-in docs, quizzes and the unknowns loop"). The list never named the loop; both descriptions named it only as "an operating loop" at their start, which 0.12.0 removed. The plugin description is now 498 characters, under the 500 the Claude apps upload form allows; the marketplace one is 396.
- OpenAI listing (`packaging/openai/interface.json`): the three default prompts call the skills as `$unknowns:blindspot`, `$unknowns:interview` and `$unknowns:quiz`, the form of every skill's `agents/openai.yaml` and of the README's Codex instructions; they read `unknowns:blindspot` and so on, without the `$` (owner decision 2026-11-24). `tools/package.py` fails a default prompt that does not start with `Use $unknowns:<skill> to ` for an existing skill, with a test.
- unknowns-scout: the **brainstorm** and **blindspot** skills are named in the "the **name** skill" form of writing rule 9 (wording only), the change 0.13.2 made in tweakable-plan, brainstorm and deviation-log.
- Descriptions, one point of view: in a description's own words "you" is the model and the user is "the user"; names and quoted trigger phrases keep their wording (writing rule 18, new paragraph). Each quoted trigger phrase is kept.
  - quiz: "quiz the user so they can defend it at handover" (was "quiz you so you can defend it"). The round also removed the closing "or before merging", the only unquoted condition in any "Use on" clause, and the run rules put it back: without it the source talk's own merge-time request (`behavior-quiz-before-merge-understanding`) loaded quiz in 0 of 3 runs, with it in 3 of 3. 188 → 194 characters.
  - interview: "what you cannot know or judge in the user's situation" (was "what the AI cannot know or judge about your situation"). 198 characters.
  - teach-me: the border names the sibling as its description names itself, with the subject that separates the two, "Not a blind-spot pass on a plan." (was "Not a plan investigation."; blindspot's description never says investigation, and both bodies give a field's blind spots to teach-me). 181 → 188.
  - blindspot: "turn them into an improved prompt", the name its body and the scout use (was "a better prompt"). 182 → 185.
  - brainstorm: the border names prototypes' own trigger phrase, "NOT for design options." (was "NOT for design variants."). 192 → 191.
  - deviation-log: "log where and why the work departed from the plan" (was "log departures from the plan as work hits unknowns", which read like the automatic start condition 0.12.4 removed). 171 → 173.
- deviation-log, step 2 log-file table: for code work the log is the file the user names, or `IMPLEMENTATION_NOTES.md` at the project root, as the shared deviation-log sentence in buy-in, quiz and unknowns-loop already says. Both READMEs say the same.

### Changed (developer-only)

- Repository documents, comments and checks were brought up to date with 0.13.2 (the two READMEs, `AGENTS.md`, the writing rules, `docs/`, the header of `IMPLEMENTATION_NOTES.md`, `evals/`, `tools/`, `tests/`, the workflows and the `_comment` of `scripts/skill-descriptions.json`). Dated records (released sections of this file, `IMPLEMENTATION_NOTES.md` entries, the frozen records in `docs/`) kept their content; the frozen records got a banner or a dated status line. No shipped file changed by it.
- Writing rule 18 gains the description point-of-view paragraph; `docs/skill-authoring-guide.md` records it against the best-practices page's third person; `docs/trigger-matrix.md` carries the changed lengths and borders.
- 20 eval cases (single-turn 16, multi-turn 4), none run before this round's check: the README's sentence to paste (`neg-open-weighty-pasted-sentence-en`, whose `append_system_prompt` `tests/test_portability.py` now reads instead of a constant), three agent negatives (`neg-unnamed-review-does-not-spawn-reviewer`, `neg-unnamed-report-check-does-not-spawn-reviewer`, `neg-unnamed-investigation-does-not-spawn-scout`), two cases where a skill should spawn the scout (`behavior-blindspot-scout-many-contracts`, `behavior-brainstorm-scout-inventory-monorepo`), no-input quiz and reference (`behavior-quiz-asks-for-the-work`, `behavior-reference-asks-for-the-reference`), the log of non-code work found by quiz and unknowns-loop (`behavior-quiz-finds-noncode-log`, `behavior-unknowns-loop-finds-noncode-log`), versions asked for without naming what of (`behavior-prototypes-asks-target-first`), the read-back of an auto-loaded skill (`behavior-tweakable-plan-autoloaded-reads-back`, `behavior-buy-in-autoloaded-reads-back`), a log file the user names for code work (`behavior-deviation-log-code-user-named-file`), a plain "show me options" on a problem that is not a design request (`behavior-brainstorm-show-me-options`), the source talk's merge-time request with no "quiz" in it, which the dropped "or before merging" used to cover (`behavior-quiz-before-merge-understanding`), and the multi-turn `tweakable-plan-after-interview-accepted`, `prototypes-two-options-contrast`, `quiz-partial-retry-score` and `unknowns-loop-every-stage-to-outcome-check`.
- `evals/run-multiturn.py`: a reply that asks with a Korean polite request and no question mark ("…알려 주세요.") now counts as waiting for the user. The runner had ended such conversations before the simulated user answered (`stop: assistant-ended`), which voided both runs of `reference-free-text-correction` and one of `unknowns-loop-criteria-unanswered` in this round, and all three 0.13.2 runs of the former (the two reruns, recorded as passes, had no correction to judge). The pattern is ASCII-escaped and pinned by a test.
- Case corrections after their first runs (the run rules: a grader or case that asks more or less than the body says is corrected and run once more): `behavior-unknowns-loop-finds-noncode-log` accepts deviation-log as the work stage's route (unknowns-loop step 4 hands the stage to it; it loaded in 3 of 3 runs on this build and 3 of 3 on the 0.13.2 descriptions); `prototypes-two-options-contrast`'s simulated user answers a reply's other questions before it stops on a requirements list; `plan-rebuilt-from-answers` lets a decision the user settled in the interview stand as a fixed part of the spec (not run again); `behavior-blindspot-scout-many-contracts` builds its 214 agreements from four layouts with varied clause wording and placement, because the first version collapsed to two documents under `sort | uniq -c`.
- `behavior-quiz-on-submit` is informative: quiz loaded in 0 of 8 runs from 2026-11-09 to 2026-11-22, on the long and the short description, and the plugin does not claim that load.
- `evals/run-multiturn.py`: the judge prompt asks for a one-line verdict per numbered criterion that quotes what in the conversation decides it, in place of "one line of reasoning per numbered criterion", the sentence Opus 5.5's safeguards refused twice in the 0.13.2 release check (`reasoning_extraction`, in the single-turn judge helper). The grader `deeper-not-padded` asks for each round's questions, with a quote of the earlier answer or open item each one follows from, in the verdict lines in place of "in your reasoning"; `every-round-at-most-four` asks for its per-reply counts there. The judge helper kept outside the repository still asks for "one line of reasoning per numbered criterion"; changing it is an open item in `docs/handoff.md` (owner decision 2026-11-24).

### Checked (developer-only)

Claude Code 2.1.331, Opus 5.5 (`ANTHROPIC_MODEL=claude-opus-5-5`), `--effort medium`, isolated config, no connector listed in any session, 2026-11-24, on the build of this release. The keep/revert rules were written and committed before the runs (`IMPLEMENTATION_NOTES.md`, 2026-11-24). Single-turn `llm` graders were judged in this session, one judge per batch and an independent second judge on every fail (no verdict was disputed), not by the judge helper kept outside the repository; multi-turn ones by `run-multiturn.py --judge` on Opus 5.5. Results are in `evals/results/round-2026-11-24/` (git-ignored).

- Routing, the whole single-turn suite once (104 cases): every trigger (22) and non-coding (22) case loaded its skill and every unknown-cell case (4) an unknowns skill; no negative case (17) loaded an unknowns skill its case rules out (three loaded the sibling their case allows: tweakable-plan, prototypes, teach-me), and the three agent negatives spawned a general-purpose or Explore agent, never independent-reviewer or unknowns-scout. Known misses were read: `behavior-deviation-log-auto-on-mismatch` and `behavior-quiz-on-submit` (both informative) and `behavior-prototypes-interaction-mockup` did not load their skills, as before.
- quiz's "or before merging": the case built for it loaded quiz in 0 of 3 runs without the clause, so the rule reverted the removal; with the clause it loaded 3 of 3 and its outcome grader passed 3 of 3. On the final build `trigger-en-quiz`, `trigger-ko-quiz`, `noncode-en-quiz` and `noncode-ko-quiz` loaded quiz, and `neg-open-quiz-en` and `neg-unnamed-review-does-not-spawn-reviewer` ("before I merge it") loaded nothing. The point-of-view edit stayed.
- deviation-log step 2: `behavior-deviation-log-code-user-named-file` wrote the named file with the entry and created no `IMPLEMENTATION_NOTES.md`; `behavior-deviation-log-appends-to-file` still creates `IMPLEMENTATION_NOTES.md`; `behavior-quiz-finds-noncode-log` and `behavior-unknowns-loop-finds-noncode-log` used the existing `DEVIATIONS.md`.
- Scored graders, single-turn: mechanical 47 of 50 and judged 105 of 124 (one not applicable). Every mechanical miss and eight judged misses are in new cases (below); five judged misses are the known ones above and the two informative read-back negatives. Six graders that passed in 0.13.2 missed and got 2 more runs: `finds-the-unused-module` and `noncode-en-reference` passed both (watch cells); `at-most-four-questions-this-round` passed 1 of 2, and `blindspot-before-teach-me` (`behavior-unknowns-loop-terms-only`), `noncode-ko-buy-in` and `trigger-ko-buy-in` 0 of 2, which the rules send to the open-items table. The 0.13.2 runs of these four, judged again by this round's judges, pass (`evals/results/round-2026-11-24/rejudge-0.13.2-single-turn.json`), so the judges are not the difference; on a build with the 0.13.2 descriptions `behavior-unknowns-loop-terms-only` missed 3 of 3 and `noncode-ko-buy-in` 2 of 2, and three more runs of `trigger-ko-buy-in` passed 3 of 3 on this build and 0 of 3 on the old one: run-to-run variation, not this release's edits.
- Multi-turn, 17 cases once: 32 of 42 judged graders (one run voided by the runner fault, one grader unjudged after two refused judge calls and judged by reading as a fail). After 2 more runs each: `interview-then-work` and `unknowns-loop-criteria-unanswered` passed both (watch cells); `findings-labelled-by-evidence-status` (`blindspot-reaches-improved-prompt`) and `final-doc-keeps-unpicked-limits` (`buy-in-partial-picks`) passed 1 of 2 (open-items table). The 0.13.2 runs of these four, judged again by this round's judge, pass, so the judge is not the difference. `reference-free-text-correction` passed once the runner let the simulated user answer. `assumption-verdicts-carry-status` and `draft-with-assumptions` missed as in their watch cells.
- New cases, first runs: passed `neg-open-weighty-pasted-sentence-en` (the README sentence's read-back), the three agent negatives with their outcome graders, `behavior-quiz-asks-for-the-work`, `behavior-quiz-finds-noncode-log`, `behavior-brainstorm-show-me-options`, `behavior-deviation-log-code-user-named-file`, `quiz-partial-retry-score`, and `prototypes-two-options-contrast` after its persona fix. `behavior-brainstorm-scout-inventory-monorepo` is the first recorded run in which a skill spawned the scout: the packet asked for the inventory and the candidates built on its rows, but two of the scout's open items did not reach the reply. Misses that the rules send to the open-items table as body findings: blindspot investigated 214 agreements itself with scripts instead of spawning the scout (twice, the second time on the varied material, with correct verdicts both times); tweakable-plan, auto-loaded by "make a plan" for a clear one-line change, gave its short-plan reply instead of a read-back; prototypes with no target asked for the count and tastes beside the target; `tweakable-plan-after-interview-accepted` and `unknowns-loop-every-stage-to-outcome-check` (stage d's probe folded into the plan; the deviation entry in its own fields). Not reached: `behavior-buy-in-autoloaded-reads-back` loaded nothing in 3 runs; `behavior-reference-asks-for-the-reference` loaded reference in 1 of 3, and that run asked the one question.
- teach-me step 7b: the six saved conversations of `teach-me-stops-at-draft`, judged again, pass `draft-with-assumptions` in 1 of 6; two runs on a copy with the proposed sentence pass it in 0 of 2, each leaving two or three details unmarked. The sentence was not adopted.
- GPT-6.1 Sol, medium effort, the 22 trigger cases once on commit 31249e4 (Codex CLI 0.164.0 in WSL, isolated HOME and `CODEX_HOME`, the read-only cache folder that keeps the account-synced plugin copy out): 22 of 22 read the intended skill's `SKILL.md`, every one from the 0.13.3 build; no session mentioned the account copy, and the copied login did not refresh on its own.
- Crowded listing (informative; `--crowd 60 --budget-fraction 0.002`, the listing over its budget): the 22 trigger cases 3 times each loaded their skills in 60 of 66 runs; blindspot loaded in 0 of 6, English and Korean, as in the first crowded measurement (2026-09-30).

### Not measured

- The routing of the changed descriptions on claude.ai and ChatGPT.
- One to three runs per cell: they show that a behaviour happens, not how often.
- The OpenAI listing's default prompts and the plugin description it carries changed, so `know-your-unknowns-openai.zip` needs uploading again; how ChatGPT shows the `$unknowns:` prompts has not been seen.

## 0.13.2 — 2026-11-22

Released 2026-11-22. Body fixes to ten skills and the unknowns-scout agent, from a prompt audit of the eleven skill bodies and two independent reviews that were not given its conclusions: one repeated the audit, one read each body as the model that runs it, and both read recorded runs. The owner approved four groups of changes, then asked for the remaining findings to be handled and for the release. No description changed. The OpenAI listing's long description changed by one sentence.

### Changed

- deviation-log: **Don't log** no longer gives "a value such as a password does not belong in a shared log" as a reason for leaving out an item that came back as planned. In the site-visit case the clause also kept the Wi-Fi password out of the user's plan: the plan held it in 7 of 7 recorded runs before the clause (2026-11-09) and in 0 of 5 after it, with replies giving "a shared document" as the reason, where the case's grader allows the password in the plan.
- quiz: a correct teach-back mentions all of the 2–3 points in the key (owner decision 2026-11-22). The sentence did not say whether all were needed: two recorded keys read "at least 2 of these 3", and one run required all three and failed a user who gave two.
- quiz: grading and explanations start once all six questions are answered (owner decision 2026-11-22). In one recorded run the explanation of a multiple-choice answer stated a point of the teach-back key before the teach-back was answered.
- blindspot, brainstorm: the scout is for a task (blindspot) or material (brainstorm) that spans more sources than the model can read in full. blindspot said "many sources" and brainstorm gave the choice no condition. Neither skill spawned the scout in any recorded run of its scout case (0 of 5 each; one of the blindspot runs on Claude Fable 5.2, the rest on Opus 5.5): the model read the 22 documents or the small codebase itself.
- OpenAI listing (`packaging/openai/interface.json`): the long description said other hosts use "labeled passes performed by the assistant", a fallback removed in 0.11.0. It now states the missing-tool rule.

The remaining findings of the two reviews, which the owner asked to have handled the same day. Where a finding left a choice open, the text now states what recorded runs already did and their graders already accept; those choices are listed in `IMPLEMENTATION_NOTES.md`, entry 2026-11-22, for the owner to confirm or overturn.

- blindspot, unknowns-scout: the scout packet asks for each ② and ⑤ assumption marked held or wrong, with its evidence and status, or still unchecked, the words of step 4a, and the scout marks every listed assumption that way; a wrong one is also a finding, and one still unchecked goes under **Needs checking**. The scout reported only assumptions it found "wrong or unsupported", so a held assumption came back with no row for step 4a to cite.
- blindspot: the first improved prompt draft applies every prompt fix; a pick still narrows it to the picked ones. The step did not say which fixes the draft held before a pick.
- tweakable-plan: with big gaps in the spec, the reply suggests the interview skill and gives the plan, with each gap under **Your own unknowns**. The step said "suggest … before planning; if the user declines, plan anyway" and did not say whether the reply waits; the recorded run gave the suggestion and the whole plan in one reply.
- unknowns-loop: step 1 is labelled "A request clear to both of you skips the loop" in place of "Read back first", which three recorded first replies took three ways ("Skipped", "Done", an actual read-back). The outcome check no longer ends with "nothing is scored", a remainder of the scorecard removed in 0.11.0.
- prototypes: with only two options, a question on what most sets them apart stands in for the triad, which needs three.
- quiz, reference: each says where the work or the reference comes from and asks one question when neither the request nor the conversation has one. reference: the Output line follows step 5 (approve all with `semantics confirmed` or name the rows to change) in place of an approve / request-change choice on every row, which a recorded run did not render.
- buy-in, quiz, unknowns-loop: the shared deviation-log sentence names the non-code file too ("otherwise the file the user names or `DEVIATIONS.md` beside the deliverable"), as deviation-log's table and the interview prompt already did. `.claude/rules/skill-writing.md` rule 11 quotes the new sentence.
- teach-me: "Keep this step however short the explainer is" in place of "in a short explainer too" (wording only). tweakable-plan, brainstorm, deviation-log: other skills are named in the "the **name** skill" form of writing rule 9 (wording only).

### Changed (developer-only)

- `README.md`, `README.ko.md`: the scout condition in the blindspot section and the agent section follows the bodies, and the loop's quiz carries its condition (when Claude largely produced the work), as `unknowns-loop` step 5b does.
- `behavior-blindspot-scout-assumption-verdicts`: the half-weight grader `spawns-unknowns-scout` required a spawn for 22 policy documents. It is now an indicator (`min: 0`, `weight: 0`), and the case description says so; `evals/README.md` names the form. No case in the suite makes a skill spawn the scout.
- `docs/skill-authoring-guide.md`: the scout-packet row of the reference-file audit uses the new condition.

### Checked (developer-only)

Claude Code 2.1.330, Opus 5.5 (`ANTHROPIC_MODEL=claude-opus-5-5`), `--effort medium`, isolated config, no connector listed in any session. `llm` graders were judged by a separate isolated `claude -p` on Opus 5.5 (multi-turn with `--judge`, single-turn with the judge helper kept outside the repository). Each decision rule below was written before its runs. Results are in `evals/results/audit-2026-11-22/` (git-ignored).

- deviation-log. Rule: keep the removal when 2 of 2 runs of `behavior-deviation-log-logs-unplanned-difference` write the password into the plan and leave it out of the log; revert when 2 of 2 put it in the log. Result: `lib2026` went into `plan.md` in 2 of 2 and into the log in 0 of 2, and `logs-capacity-and-access` passed 2 of 2. Cases next to it, 1 run each (five `behavior-*`, two `noncode-*`): 12 of 13 graders. The miss is `logs-and-continues` of `behavior-deviation-log-auto-on-mismatch`, a run in which the skill did not load, as in the 0.13.1 release check.
- quiz. Rules: keep the grading sentence when 2 of 2 runs of `quiz-hides-key-and-gates-on-six` grade and explain nothing before the teach-back is answered and both judged graders pass; keep the all-points wording when 2 of 2 keys require every point. Result over 3 runs (the third by the 1-of-2 rule): grading began after all six answers in 3 of 3, the key and the retry key required every point in 3 of 3, `grades-after-answers-six-of-six-gate` passed 3 of 3 and `key-hidden-until-answered` 2 of 3. The miss is that grader's first item: in three questions the correct option was longer and more detailed than the others, the slip the length rule of step 1a covers and these changes do not touch; its items on the teach-back points and on waiting for the answers passed.
- quiz, single-turn, 1 run each: `noncode-en-quiz`, `noncode-ko-quiz`, `trigger-en-quiz` and `trigger-ko-quiz` asked all six questions in the first reply and said grading follows the six answers; the two that wrote a key file required all three points; 5 of 5 graders. `behavior-quiz-on-submit` did not load the skill (0 of 1, as in 0.13.0 and 0.13.1).
- Scout condition. Rule: keep when the scored grader of each scout case passes 1 of 1. `assumption-verdicts-with-evidence` of `behavior-blindspot-scout-assumption-verdicts` and `finds-the-unused-module` of `behavior-brainstorm-scout-finds-unused` passed 1 of 1 each; neither run spawned the scout. Cases next to them, 1 run each: blindspot single-turn 8 of 8 graders, brainstorm `noncode-*` 2 of 2, `blindspot-partial-pick` 2 of 2 and `blindspot-reaches-improved-prompt` 4 of 5. The miss is `assumption-verdicts-carry-status`: one of the model's own assumptions was marked true on the strength of an assumption the user had listed (step 4a, a cell already under watch).
- One reader who did not write the change compared old against new without the writer's explanation. Three of the five changed sentences were reworded after that reading and before their runs: the header of the blindspot scope table and the "e.g." in its two rows, the word order of quiz step 1c, and the grading sentence of quiz step 2 (now the last sentence of the step, counting a blank or a skip as a reply). The same reading corrected the README sentence on brainstorm's condition, the listing sentence and the grader's note. The deviation-log runs came before the reader's report, which asked for no change to that sentence.
- `tools/package.py` and `tools/package.py --check`, 100 unit tests, `evals/run-manual.py --verify` (88 cases), `evals/run-multiturn.py --verify` (13 cases), `scripts/build-skill-zips.py`, and `claude plugin validate --strict` for the plugin and the marketplace.

- A second reading by one reader who did not write the change, of the remaining-findings batch, before its runs. Three sentences were reworded after it: reference step 1a ("names or contains a reference", where "holds" could mean either and one reading would ask for a reference the user had named), the scout's sentence on assumptions (an assumption still unchecked, one the sources do not settle included, also goes under **Needs checking**), and prototypes step 5a (the two-option sentence moved to the end of the step, so "Run it whether reactions stall" still points at the triad).

### Checked — release runs (developer-only)

The whole suite once on the final text, 2026-11-22: Claude Code 2.1.330, Opus 5.5, `--effort medium`, isolated config, no connector listed and no void run. The rule written before the run: a scored grader that passed in the 0.13.1 release check and misses now gets 2 more runs of its case (2 of 2 keeps the text, 0 of 2 reverts the sentence that touches that step, 1 of 2 gets one more run); misses already in a watch cell are read, not run again. Results are in `evals/results/release-0.13.2/` (git-ignored).

- Single-turn, 88 cases: 125 of 134 scored graders, the count of the 0.13.1 release check, and 30 of 30 mechanical ones. Multi-turn, 13 cases: 3 graders missed.
- Passed in 0.13.1 and missed now, each run 2 more times:
  - `behavior-deviation-log-logs-public-rename` / `logs-the-public-rename`: the reply said it "added two entries" without saying what they record. 2 of 2 on the rerun.
  - `reference-free-text-correction` / `free-text-corrections-applied`: the simulated user never replied (0 user turns), so there was no correction to apply; the judge called the transcript truncated. 2 of 2 on the rerun.
  - `behavior-tweakable-plan-opens-with-done-criteria` / `alternatives-are-lettered`: not judged. The judge call was refused twice by Opus 5.5's safeguards (`reasoning_extraction`; the helper's prompt asks for "one line of reasoning per numbered criterion"). Counted by script instead: all seven decision items of the reply list lettered alternatives, each with why it was rejected.
- `behavior-deviation-log-logs-unplanned-difference`, missed in 0.13.1 as well, missed in a new way: the password went into the plan, and the log ended with an HTML comment that said the Wi-Fi item was no deviation and held `lib2026`. A rule was written before two more runs (both keep the value out of the log: keep the removal and watch the cell; either puts it in: replace the sentence with two separate **Don't log** items and run those). Both kept the value out of the log and wrote it into the plan, and `logs-capacity-and-access` passed 2 of 2. Since the password clause was removed the value has reached the log in 1 of 5 runs and the plan in 5 of 5. The cell is under watch.
- Missed as in 0.13.1, read and not run again: `assumption-verdicts-carry-status` in `blindspot-partial-pick` (one of the model's own assumptions got no verdict) and in `blindspot-reaches-improved-prompt` (a "held" verdict credited to the user's prompt for a fact the prompt did not state), both step 4a; three cases in which the skill did not load (`behavior-deviation-log-auto-on-mismatch`, `behavior-prototypes-interaction-mockup`, `behavior-quiz-on-submit`); the two informative open-cell cases `neg-open-weighty-code-en` and `neg-open-weighty-text-ko`, where no skill loads and the reply does the work without a read-back; and `key-locations-from-the-material` of `noncode-en-quiz`.
- Missed in 0.13.1 and passed now, 1 run each: `finds-the-unused-module` of `behavior-brainstorm-scout-finds-unused`, `does-it-directly` of `neg-open-text-en`, `draft-with-assumptions` of `teach-me-stops-at-draft`.
- `tools/package.py` and `tools/package.py --check`, 100 unit tests, both `--verify` commands, `scripts/build-skill-zips.py`, and `claude plugin validate --strict` for the plugin and the marketplace, on the 0.13.2 build.
- GPT-6.1 Sol, `model_reasoning_effort = "medium"`, Codex CLI 0.164.0, the 22 `trigger-*` cases once, run after the release on the tag `unknowns--v0.13.2` (commit `dfb0bb9`): the intended skill loaded in 22/22, all 22 runs read this build's 0.13.2 `SKILL.md` files, and no session listed the account-synced copy (isolated HOME and `CODEX_HOME` in WSL, with the read-only cache folder of the 0.13.0 check in place). The tag message says the check was not run; it had not been at the release.
- After the release, an install into an empty Claude Code config from this repository's marketplace and from `ajitta/claude-plugins`: 0.13.2 with 11 skill folders and 2 agents on both.

### Not measured

- The scout side of the condition and of the new verdict packet: no case gives a skill a task too large to read in full, so no run shows blindspot or brainstorm spawning the scout or the scout returning a verdict for each assumption.
- The OpenAI listing text changed, so `know-your-unknowns-openai.zip` needs uploading again.
- Claude Fable 5.2 was not run on these changes.
- Sentences with no case that reaches them: tweakable-plan step 1b when the user takes the interview suggestion, the two-option question of prototypes step 5a, the empty-input sentences of quiz and reference, and the non-code half of the shared deviation-log sentence in quiz and unknowns-loop.

## 0.13.1 — 2026-11-17

Released 2026-11-17. Body fixes to interview, buy-in, unknowns-loop and tweakable-plan, from three passes of one day: a reading of the bodies by the model that runs them, a third rule-based review, and a writing rule that numbers and letters mark execution order only. No description changed. Eval runs now stay out of the signed-in account. The sections below keep the order in which the day's records were written.

A reading of the eleven skill bodies by Claude Fable 5.2, followed by two runs on that model (medium effort, 1 run each). Fable 5.2 is not a supported model; the three sentences below are checked on Claude Opus 5.5 as well.

### Changed

- interview: the skill ends at the decision table and the ready-to-use prompt, and the work starts from the user's next message. In the run on Fable 5.2, the reply that delivered the two also wrote the requested script, which rested on seven choices the user had not made, one of them a question the user had left unanswered.
- interview: from round 2 on, what the model knows goes into each option's consequence note and the options come without a recommendation. A saved Opus 5.5 run (0.12.3 text) marked three options "I don't recommend this".
- buy-in: unless the user names another place for it, the doc is Markdown in the conversation, and where it goes from there is the user's choice. The body did not say where the doc lives.
- interview: when the user asks which option the model would pick, it gives its pick with its reason; a recommendation the user did not ask for is still left out.
- interview: the sentence on where the interview ends now says what starts the work (the user sends the prompt or says to go ahead) and what a changed decision does (the table and the prompt are revised and shown again). It said "the user's next message", which a correction or a question also is.
- buy-in: the sentence on where the doc lives carries its reason.
- unknowns-loop: stage c of step 3 has one row per skill, each with its own condition (wording only). The three skills and their three conditions shared one row, matched by the position of a slash.
- interview: the rule that round 1 opens with the question about what the user is sure of and what they are assuming moved, word for word and with the sentence after it, from step 1 into the round-1 paragraph of step 2. Step 1 is one paragraph now and has no letters. In the earlier place the rule sat one step away from "in priority order within every round", and the replies that missed it opened with a structure question.
- tweakable-plan: step 3, the size gate, is a table of two cases. The small case says its reply holds nothing from steps 4–7, and the other case, which also takes work whose size is unclear, is the document. The prose form did not say that the later steps stop for small work, and replies had added the document's weakest-part section.

### Changed (developer-only)

- New multi-turn case `interview-then-work`: an interview before a small script that can be written in the run's folder, with Write and Edit granted. Its graders check that the last reply holds the decision table and the ready-to-use prompt and writes or edits no file.
- `evals/run-manual.py` and `evals/run-multiturn.py` now start every `claude` call in a fresh, empty `CLAUDE_CONFIG_DIR` with the account's connectors off (`ENABLE_CLAUDEAI_MCP_SERVERS=false`), and pass the sign-in as a token in the environment without copying the credentials file. A run loads this plugin and nothing else of the user's. `--own-config` restores the earlier behaviour. Each result records the connectors the session listed. Reason: `--disallowedTools` names tools and does not cover account connectors, and one run in the owner's own config wrote a document into the signed-in account (see **Not measured**). Results recorded before this change ran in the owner's own config, with other plugins and `CLAUDE.md` loaded.
- Writing rule 1 (`.claude/rules/skill-writing.md`) is rewritten (owner decision 2026-11-17): a number or a letter marks execution order and nothing else; parallel items, cases and states are table rows; several constraints on one action stay in its paragraph; a rule sits in the step whose action it governs; converting a step or moving a rule is a change of its own, one step at a time. It replaces "One step, one action". A reading of the eleven bodies found the same markers carrying five meanings, and of the 22 lettered sets 8 a sequence, 10 a classification and 4 mixed. Only interview step 1 was converted.
- New secondary grader `round-one-opens-with-sure-and-assumed` in `interview-then-work` (regex on the first question of the first reply).
- The `deeper-not-padded` grader of `interview-deep-grill` no longer counts as filler a first question that asks the user to check or confirm an assumption they said they had not checked; the interview skill asks for that question. A second question about the same assumption is still filler.
- The `defers-to-plan-mode` grader of `neg-one-file-tweakable-plan-defers-to-plan-mode` names the two things the size gate tells a small reply to hold (the line with the outcome, done criteria, what must not break and the allowed cost and scope; the questions, the model's own unknowns among them) as allowed, and says a weakest-part section is not.
- The `deeper-not-padded` grader also accepts a question that names two of the user's decisions, or a decision and a stated constraint, that cannot both hold and asks which gives way. This was written with a sentence for interview step 4b, before its runs; the sentence did not ship (see the release check below) and the grader line stays.
- Both runners create a run's folder outside any `.claude` folder. Claude Code treats a path under one as a sensitive location and refuses file writes there unless the user's own settings allow them, and a shell can point its temp folder into `~/.claude`; in the isolated condition every case that must create a file then failed for that reason alone.

### Checked (developer-only)

Claude Code 2.1.326, `--effort medium`; `llm` graders judged by a separate `claude -p` (Opus 5.5); the simulated user is Opus 5.5.

- On the 0.13.0 text, `claude-fable-5-2`, 1 run each: `interview-then-work` wrote `report.py` in the reply that delivered the decision table and the prompt. `behavior-blindspot-scout-assumption-verdicts` did not spawn the scout (`spawns-unknowns-scout` 0/1, a miss already recorded on Opus 5.5); it read the 22 policy files itself and gave both assumptions a verdict with evidence (its `llm` grader was not judged). The scout row in blindspot is unchanged and under watch.
- The end-point sentence, by the rule written before the run (2 of 2 keeps it, 0 of 2 reverts it): `interview-then-work` on `claude-fable-5-2` passed 2 of 2 on its three graders, and 1 of 1 on Opus 5.5.
- Cases next to the change, Opus 5.5, 1 run each. Single-turn, 10/10 scored graders: `behavior-interview-max-four-questions`, `noncode-en-interview`, `noncode-ko-interview`, `behavior-buy-in-relays-reviewer`, `behavior-buy-in-finds-noncode-log`, `noncode-en-buy-in`, `noncode-ko-buy-in`. No buy-in run wrote a file; the doc was in the reply. Multi-turn: `interview-undecided-item` 1/1, `buy-in-partial-picks` 1/1, `interview-rounds-stay-at-four` 3 of 4 graders.
- The miss in `interview-rounds-stay-at-four` is the half-weight grader `questions-carry-reasons-in-priority-order`. Read from the transcript (the judge's reasons were not saved): round 1 did not open with the question about what the user is sure of and is assuming. Step 1b asked for that question at that point (the rule moved into step 2 later the same day, below), and that change did not touch it.
- In the five conversations where the interview skill loaded, no option question carried a recommendation.
- One reader who did not write the change checked the diff against the writing rules; the option sentence, the reason after the end-point sentence and the buy-in sentence were reworded after it, before the runs.
- The isolated runners, live (Opus 5.5, 1 run each): `trigger-en-interview` loaded the interview skill and `buy-in-partial-picks` passed its grader over two replies of one resumed session; both sessions listed no connector. A check of the session start on Claude Code 2.1.326: 14 connectors and 98 skills in the owner's config, no connector and 34 skills (the CLI's own and this plugin's 11) in the isolated one. Every run above this line ran in the owner's own config.
- `interview-deep-grill`, isolated, Opus 5.5, 3 runs (the count for a routing doubt): the interview skill loaded in 3 of 3, `four-per-round` passed 3 of 3 (every reply of every run asked four questions), and `deeper-not-padded` passed 2 of 3 (one run asked again, in round 6, about two decisions the user had already made).
- `tools/package.py` and `tools/package.py --check`, 98 unit tests, `evals/run-manual.py --verify` (88 cases), `evals/run-multiturn.py --verify` (13 cases), `scripts/build-skill-zips.py`, and `claude plugin validate --strict` for the plugin and the marketplace.

Third rule-based review, 2026-11-17 (the same four rules, and two items their text gained since the second review: one labelled sub-item per case, and a reading shown beside the person's own words on two labelled lines). Scope: those two items on the eleven bodies and both agents, and all rules on the eleven descriptions, the prompts in the published documents and the text added since 0.12.4. Two readers who wrote none of the text reported 24 findings and the maintainer's own reading of the added text 4 more; every quote was found in its file. Five findings were acted on, one of them as a trial. All runs below are isolated, Claude Code 2.1.326, `--effort medium`, Opus 5.5 unless named.

- Tried and removed: the outcome on two labelled lines ("Outcome, as stated", "Outcome, as read") in step 2 of unknowns-loop and of tweakable-plan. The rule written before the run kept it only if the lines appeared and the cases' scored graders passed. The lines appeared in 5 of 5 runs, but `first-reply-covers-step-2` of `noncode-en-unknowns-loop` missed its outcome item in 2 of 3 runs: the reply quoted the request as the stated outcome and did not reach what the user is ultimately after. On the final text that item passed 2 of 2 (the grader missed once on its done-criteria item, so the case reads 1 of 2). Both skills carry no such lines.
- The read-back paragraph breaks the two-labelled-lines item in every body and is unchanged (owner decision 2026-11-17, after the 2026-11-13 ruling).
- interview, on the final text: `interview-then-work` 3 of 3 graders on Opus 5.5 and on `claude-fable-5-2`; `interview-rounds-stay-at-four` 4 of 4; `interview-undecided-item` 1 of 1; `behavior-interview-max-four-questions` 2 of 2; `noncode-en-interview` 1 of 1; `noncode-ko-interview` 0 of 1 (round 1 reasons ran two or three sentences where step 2d asks for one line; step 2d is unchanged); `interview-deep-grill` `four-per-round` 1 of 1 and `deeper-not-padded` 0 of 1 (round 7 asked again about a decision already made; 2 of 4 over this day's runs).
- buy-in, on the final text: `buy-in-partial-picks` 1 of 1, `behavior-buy-in-relays-reviewer` 3 of 3 graders, `behavior-buy-in-finds-noncode-log`, `noncode-en-buy-in` and `noncode-ko-buy-in` 1 of 1 each.
- unknowns-loop, on the final text: `behavior-unknowns-loop-cannot-describe`, `-keeps-investigation`, `-probe-fails` and `-terms-only` 1 of 1 each, `noncode-ko-unknowns-loop` 2 of 2 graders, `unknowns-loop-criteria-unanswered` 1 of 1. `behavior-unknowns-loop-terms-only` had missed in all 6 runs recorded under 0.13.0, which ran in the owner's own config; this is its first isolated run.
- tweakable-plan is byte-for-byte the 0.13.0 text again. With the trial text, `neg-one-file-tweakable-plan-defers-to-plan-mode` passed `defers-to-plan-mode` in 2 of 3 runs (the miss added a weakest-part section) and `alternatives-are-lettered` passed 1 of 2, the slip already under watch.
- One reader who did not write the change checked old against new; four of its six findings were about the trial text or the stage c rows and were fixed before the runs, and the fixes were checked by the writer.

The interview move, 2026-11-17 (isolated, Opus 5.5, `--effort medium`). Read from the first reply of every saved interview run of the day: before the move round 1 opened with the sure-or-assuming question in 10 of 11 isolated runs and 4 of 6 runs in the owner's own config, and `interview-then-work` missed it in both of its Opus runs (one in each condition); `claude-fable-5-2` opened with it in 4 of 4. The rule written before the run kept the move at 2 of 2 on that case.

- After the move: `interview-then-work` 2 of 2 on the new grader and on its three others; round 1 opened with the question in 8 of 8 first replies across the skill's cases.
- Cases next to it, 1 run each: `interview-rounds-stay-at-four` 4 of 4 graders, `interview-undecided-item` 1 of 1, `behavior-interview-max-four-questions` 2 of 2, `noncode-en-interview` and `noncode-ko-interview` 1 of 1 each, `interview-deep-grill` `four-per-round` 1 of 1 and `deeper-not-padded` 0 of 1.
- That `deeper-not-padded` miss: the judge counted as asking again a round-2 question about an assumption the user had stated as unchecked. The skill asks for that question ("stated assumptions become questions of their own"), the same question was asked in 3 of the 4 isolated runs before the move, and the judge passed two of those. The grader reads 2 of 5 over the day.
- One reader who did not write the change checked the move and the new rule 1. Its main finding on the move: "Settled items are not asked again, and stated assumptions become questions of their own" now sits in the round-1 paragraph and may be read as covering round 1 only. In the saved conversations round 2 took up the user's stated assumptions as it did before the move (in `interview-deep-grill` both times, in `interview-rounds-stay-at-four` neither time); the sentence stays where the runs measured it and is under watch. Its findings on rule 1 were applied and checked by the writer.

After the grader change, 2026-11-17: the day's five saved `interview-deep-grill` conversations were judged again, with no new run. `deeper-not-padded` reads 2 of 5. Each of the three misses asked again, in round 6 or 7, about a decision the user had already made; none is failed for the assumption question now. For one of the three the first judging had named the assumption question and the second names a repeated decision, so the two judgings of that conversation disagree on the reason and agree on the verdict.

Tried and removed, 2026-11-17: tweakable-plan step 3 (the size gate) as two cases in a table, the small case saying that its reply holds nothing from steps 4–7. Before it, `defers-to-plan-mode` of `neg-one-file-tweakable-plan-defers-to-plan-mode` passed 2 of 3 isolated runs on the current text, the miss adding the document's weakest-part section. The rule written before the run kept the table only at 4 of 4. With the table the grader passed 3 of 4 and the table came out; tweakable-plan is the 0.13.0 text. No reply of the four carried a weakest-part section. The one miss was failed for the done-criteria line and the list of the model's own unknowns, both of which the size gate tells the reply to hold, and which a passing run of the same batch also held; the grader's text does not say those parts are allowed. The skill's other cases passed with the table (6 of 6 graders, 1 run each).

The table went back in, 2026-11-17 (owner decision: correct the grader, then judge the saved replies again; no new run). The rule written before the re-judging put the table back at 4 of 4 under the corrected grader. The seven saved replies read: 2 of 3 before the table, the miss still the weakest-part section, and 4 of 4 with it. tweakable-plan step 3 is the table; the runs behind it are those four and the three of the skill's other cases.

Tried, merged and then removed before the release: the decided-stays-decided sentence in interview step 4b, 2026-11-17 (isolated, Opus 5.5, `--effort medium`). It said a decided item stays decided, that a why follow-up asks for the reason, and that two decisions which cannot both hold are asked again with both named. Before it, `deeper-not-padded` of `interview-deep-grill` read 2 of 5, each miss a decision asked again in round 6 or 7. The rule written before the run: 3 of 3 keeps the sentence, 2 of 3 gets one more run and 3 of 4 keeps it.

- `interview-deep-grill`: 2 of 3, then the fourth run passed, 3 of 4, and the sentence stays. The miss asked about on-call pay after the user had put it out of scope and asked one decision again. Two of the passing runs asked a question that named two colliding decisions, which the sentence allows.
- Cases next to it, 1 run each: `interview-rounds-stay-at-four` 4 of 4 graders, `interview-undecided-item` 1 of 1, `behavior-interview-max-four-questions` 2 of 2, `noncode-en-interview` and `noncode-ko-interview` 1 of 1 each, `interview-then-work` 3 of 4 graders.
- The `interview-then-work` miss is `ends-at-the-two-deliverables`, on its first item: the ready-to-use prompt held two requirements the user had not chosen (the week's date range in the output; the skipped-rows line only when rows were skipped) without marking them as the model's. The reply started no work and ended as the skill says. The miss is in the final deliverables, which this change does not touch.
- One reader who did not write the change checked the first, one-sentence wording and found that it forbade the why follow-up of step 4c and that two colliding decisions, both decided, would open no further round. The wording that ran fixes both; the writer checked the fix.

### Checked — release runs (developer-only)

Claude Code 2.1.326, Claude Opus 5.5, `--effort medium`, the isolated condition, 1 run per case unless a count is given; `llm` graders judged by a separate `claude -p`.

- The whole suite once. Combined over the three passes below: 88 single-turn cases, graders 194/206 (scored 125/134); 13 multi-turn cases, scored graders 28/32. For the form of the figures only, the 0.13.0 record reads 195/206 (scored 126/134) and 24/28, in the owner's own config; the two are not a comparison of versions.
- First pass, all 101 cases: no run failed to start or timed out. Every run that had to create a file could not: the session's temp folder sat under `.claude` and the fresh config refused writes there. Those runs are void, not failures. The runners were corrected (above), and the 13 single-turn and 4 multi-turn cases that grant Write or Edit ran again; every one that writes created its file.
- The step 4b sentence came out because of this check. `interview-then-work`'s grader `ends-at-the-two-deliverables` failed its first item (the ready-to-use prompt shows only the user's decisions as decided) in 3 of 5 runs with the sentence: twice the prompt listed a requirement the model had added as fixed, once it showed an unanswered question as confirmed. Before the sentence the item passed 3 of 3. The rule written after the second failure and before the last three runs stopped the release at 3 of 5. With the sentence out, interview is the text of the commit before it and the item passed 3 of 3; the skill's other eight cases then ran once each on that text.
- Single-turn misses, all known from earlier releases: the two informative `neg-open-weighty-*` cases; prototypes and quiz not loading in `behavior-prototypes-interaction-mockup` and `behavior-quiz-on-submit`; the scout not spawned in `behavior-blindspot-scout-assumption-verdicts`; deviation-log not loading unasked in `behavior-deviation-log-auto-on-mismatch`; a check item that came back as planned logged as a Discovery in `behavior-deviation-log-logs-unplanned-difference`; a candidate titled as an instruction in `behavior-brainstorm-scout-finds-unused`; a long list of changes after a proofread in `neg-open-text-en`.
- Multi-turn misses, all under watch: blindspot's `assumption-verdicts-carry-status` in both blindspot cases; teach-me's `draft-with-assumptions`; interview's half-weight `questions-carry-reasons-in-priority-order` (round 3 put its why follow-ups after another question).
- `behavior-unknowns-loop-terms-only`, which missed in every run recorded under 0.13.0, passed; those runs were in the owner's own config.
- GPT-6.1 Sol, `model_reasoning_effort = "medium"`, Codex CLI 0.167.2, the 22 trigger cases once, on the final commit of the release branch: the intended skill loaded in 22/22, all 22 runs read this build's 0.13.1 `SKILL.md` files, and no session listed the account-synced copy (the read-only cache folder of the 0.13.0 check was in place). An earlier run of the same day on the first release commit, which still held the interview sentence that came out, also read 22/22.

### Not measured

- The one `interview-deep-grill` run in the owner's own config is void: with the owner's other plugins loaded, the interview skill did not load for "Grill me … 40-question level", and the model wrote the requirements into a document through a connector of the signed-in account. In the isolated condition the skill loaded in 3 of 3 runs (see **Checked**); how the short descriptions route in a config crowded with other plugins' skills is not measured here. The runners' deny list names tools; it does not cover account connectors or other plugins' skills. The runners are isolated from the account since (see **Changed (developer-only)**).
- The buy-in sentence in a session that has a page or document tool: the runners deny `Artifact`, so no case reaches it.
- The option sentence has no grader of its own.
- No trigger case was run (no description changed), and GPT-6.1 Sol was not run.
- Each cell is 1 or 2 runs: they show that a behaviour happens, not how often.
- The third rule-based review's changes were checked by runs of each skill's cases, not by an old-against-new comparison (owner rule). Findings held without a change: prototypes' requirements list and the README's sentence to paste (each a meaning change to measured text), and four description findings (quiz "or before merging", teach-me "Not a plan investigation", blindspot "a better prompt", brainstorm "NOT for design variants"), which wait for one description round with its trigger, non-coding and negative cases.
- The interview move was not run on `claude-fable-5-2`. Rule 1 was applied to one step; the other lettered sets that are a classification or mixed (14 of 22) are unchanged.
- Late rounds of the deep interview still ask again about decisions the user has made (`deeper-not-padded` 2 of 5 before the removed sentence); the sentence that reduced it is not in this release.
- ChatGPT and claude.ai were not run. The release check is one run per case.

## 0.13.0 — 2026-11-13

Owner rulings of 2026-11-12 and 2026-11-13. The eleven skill descriptions are now the short set (200 characters or fewer each), three sentences that only repeated another sentence of the same file leave one skill body (blindspot) and one agent, and both READMEs gain a sentence to paste when the read-back is wanted in one conversation only. The read-back paragraph, the cell sentence and the routing sentence stay in every body. Apart from their descriptions, the other ten skills are the 0.12.4 text. No skill was added; skill names are unchanged.

### Changed

- Descriptions (owner ruling 2026-11-12): each `SKILL.md` description is now the text `scripts/skill-descriptions.json` already held for the single-skill upload zips, character for character: a label, what the skill is for, its trigger phrases and, in three skills, a border. The method summaries and the closing sentence "Clear to both sides: no skill or method." are gone from all eleven. Loaded in every conversation: 949 → 475 tokens (cl100k), 4,318 → 1,997 characters. The plugin, both release zips and the upload zips now carry one description per skill.
  - Every trigger phrase the READMEs advertise is still in its description; blindspot's "unknown unknowns" is there as plain words, no longer as a quoted phrase.
  - Among the text that left: blindspot's "run it even when you could answer directly", tweakable-plan's "Not native plan mode" sentence (the size gate stays in its body), unknowns-loop's stage list, and the situation clauses ("or when …", "or before …") of blindspot, brainstorm, buy-in, interview, reference and teach-me. quiz and reference keep a short "runs even when …" clause, quiz keeps "or before merging", brainstorm keeps "NOT for design variants", teach-me's border is "Not a plan investigation." and unknowns-loop's is "A bare "loop" is NOT this."
  - The OpenAI zip carries the same skill files, so its listing text changed: upload `know-your-unknowns-openai.zip` to ChatGPT again after the release. `skills/*/agents/openai.yaml` and `packaging/openai/interface.json` quote no description and are unchanged.
- Kept in every body (owner ruling 2026-11-13): the read-back paragraph ("When you and the user both seem to understand the request, do it without this method: …"), the routing sentence inside it and the cell sentence ("This skill serves …"). The reason is the read-back paragraph run under **Checked** below.
- Sentences removed because another sentence of the same file gives the same instruction with the same scope (owner ruling 2026-11-13, made after a read-only review of every sentence, not published). Three are removed; each row names the sentence that still says it:

  | File | Removed | Still said by |
  |---|---|---|
  | blindspot, Output | "Reaction: a numbered, copyable **prompt fix** per finding card; the user's selected numbers assemble into the improved prompt draft; a missing pick is undecided." (the section held only this line) | Step 4b: "the recommended action as a numbered, copyable **prompt fix**". Step 5: "when the user picks prompt-fix numbers, revise the draft so it applies only the picked fixes and lists the unpicked ones as undecided below it", which now carries the shared ending "; a missing pick is undecided." |
  | blindspot, Scope | "Not limited to code: a funding call, a policy, an event, a study, infrastructure and vendor integrations all have landmines and unwritten conventions." | The opening paragraph: "the **territory** (the actual situation: its documents, rules, people, data, or codebase)"; the kind table: "a rule with penalties", "(a codebase, an organisation, a funder, a community)" |
  | independent-reviewer, review item 3 | "— confirm by checking, not by reading the producer's explanations" | The opening line: "Treat the producer's explanations … as **claims only** — verify them directly against the work itself". The item's table column "Confirm by" |

  Six more sentences were removed in an earlier commit of this branch and went back before the release, so the bodies of brainstorm, teach-me, tweakable-plan and deviation-log are the 0.12.4 text byte for byte:
  - Four name a skill's goal or a step's reason: brainstorm's "The user picks; you draw the space.", teach-me's "This skill fills the **vocabulary gap**.", tweakable-plan's "A plan's purpose is to **pull the points where the user would intervene forward**, not to list steps in execution order." (the reason sentence that follows it is back in its old place) and deviation-log step 2's "The **buy-in** and **quiz** skills read that log." An earlier finding of this repository says such sentences stay even when they look like duplicates (`docs/features/concise-plugin-text/06-results.md`, 2026-10-09: after a clause naming blindspot's deliverable was deleted as a duplicate, a grader went from 3/6 to 0/6; the cause was inferred, not isolated). For deviation-log the scope was also not the same: the sentence is unconditional and is step 2's reason for appending to a file, while the wrap-up sentences that seemed to repeat it apply only when the model largely produced the work (Wrap-up 4) or when the work needs approval (Wrap-up 5).
  - Two are Iron Rules: brainstorm's Iron Rule 2 ("Spread candidates **across time horizons and approaches**, not 10 near-duplicates.") and tweakable-plan's Iron Rule 2 ("Every decision carries **considered alternatives** — a decision without alternatives cannot be reviewed."). Without its Iron Rule 2, tweakable-plan's grader `alternatives-are-lettered` passed 2 of 4 runs, against 2 of 2 on the 0.12.4 text the same day (**Checked** below). brainstorm's Iron Rule 2 went back with it; no run showed a miss from its removal.

  Nine more candidate sentences were left from the start because their copies differ in scope, the review that listed them was unsure, or a later sentence depends on them; `IMPLEMENTATION_NOTES.md` (2026-11-13) lists each with its reason.
- READMEs (both languages), next to the existing `CLAUDE.md` tip in Scenario A: a sentence to paste as a message when the read-back is wanted in one conversation only. It also asks, when that work is finished, for each done criterion with its evidence and whether the result achieved the outcome. A short paragraph says when to use which. The Korean README prints the English sentence, a Korean version of it, and says the measurement used the English one.
- No session-wide "mode" skill (owner ruling 2026-11-13). The reason is the "Why no skill" item under **Checked** below.

### Changed (developer-only)

- `.claude/rules/skill-writing.md`: rule 11 no longer lists a closing sentence for the descriptions and records the ruling that the read-back paragraph, the routing sentence and the cell sentence stay; new rule 18 says what a description holds (200 characters or fewer, no method summary, no sentence about clear requests, the same text as `scripts/skill-descriptions.json`) and what it may hold (one border clause, a "runs even when …" clause).
- Tests: `tests/test_portability.py` no longer requires the closing sentence in each description; it checks that each description is 200 characters or fewer and has a "Use on …" clause, still checks the read-back paragraph, the routing sentence and the cell sentence in every body, and checks that both READMEs print the pasted sentence word for word. `tests/test_skill_descriptions.py` checks that each `SKILL.md` description equals its entry in `scripts/skill-descriptions.json`. 94 tests (91 before).
- `scripts/skill-descriptions.json`: the `_comment` says the `SKILL.md` descriptions are now the same texts; `scripts/build-skill-zips.py` still reads the file for the upload zips.
- `docs/skill-authoring-guide.md`, `docs/trigger-matrix.md`, `AGENTS.md` and `docs/handoff.md` follow the new description rule; the trigger matrix lists the new lengths and the clauses that left.

### Checked (developer-only)

- Before the commit: `tools/package.py` and `tools/package.py --check`, 94 unit tests, `evals/run-manual.py --verify` (88 cases, 206 graders, 0 problems; structure only), `scripts/build-skill-zips.py` for both targets, and `claude plugin validate --strict` for the plugin and the marketplace (Claude Code 2.1.322).
- Earlier record for the short descriptions (0.12.2 below, 2026-10-28): 259/260 against 260/260 for the longer descriptions on 26 routing cases × 10 runs.
- Short descriptions, on a build with the short set as the `SKILL.md` descriptions and the 0.12.4 bodies (Claude Code 2.1.322, Claude Opus, `--effort medium`, `evals/run-manual.py`, 1 run per case, mechanical graders only): the intended skill loaded in 22/22 trigger cases and 22/22 non-coding cases, and a skill loaded in the 4 unknown-cell cases. The 13 negative cases were read by each case's own graders, 13 of 13, not by "no skill loads at all": three of them load the sibling skill their case allows (tweakable-plan, prototypes, teach-me), and the interval case loads the built-in `loop`, as intended. Judge-graded items were not scored in that run; the release check below scored them.
- Read-back paragraph (same engine, the 0.12.4 descriptions): a skill invoked by name with a self-evident request ("sort the import lines"), 6 runs on the shipped bodies and 6 with the paragraph removed from ten bodies (interview, brainstorm and blindspot, 2 runs each). The bar written before the run: the shipped text does the request without the method in at least 5 of 6, and the text without the paragraph runs the method in at least 2 of 6. Result: the shipped text did the request directly in 4 of 6; the text without the paragraph ran its method in 6 of 6. The first half of the bar was missed because of blindspot, which ran its method with and without the paragraph (2 of 2 each): a new observation, under watch in `docs/handoff.md`, not fixed. In interview and brainstorm the shipped text did the request directly in 4 of 4, the text without the paragraph in 0 of 4 (it ran its method; the interview runs asked round 1 and stopped).
- Pasted sentence (same engine, an editable example project, 4 sessions per condition, a blind judge per turn). No edit before confirmation on a weighty request: nothing 0/4, the pasted sentence 4/4, the `CLAUDE.md` line 4/4. Outcome question after the work: nothing 0/4, the pasted sentence 4/4, the `CLAUDE.md` line 0/4. With the pasted sentence the read-backs were about 600 characters long and passed the repository's read-back grader 3 of 4 (one invited corrections without asking for confirmation), and the replies to a trivial request passed the trivial-request grader 3 of 4 (one offered other sort orders); the `CLAUDE.md` line passed both 4 of 4. After a context compaction the pasted sentence's read-back still held 2/2; the outcome question was not tested after compaction. Setup: these runs used the 0.12.4 descriptions, with the draft skill of the next item present in the skill listing, and loaded the `CLAUDE.md` line as an appended system prompt, not from a `CLAUDE.md` file.
- Why no skill: a draft session-wide skill of about 800 tokens gave the same two behaviours (4/4 and 4/4) with read-backs about 1,100 characters long, which failed the repository's own read-back grader 0 of 4 (trivial-request grader 4 of 4).
- Release check, Claude: the whole suite once (Claude Code 2.1.322, Claude Opus, `--effort medium`, 1 run per case) on this branch at commit 63e0360, which had the short descriptions and all nine removals of that time: 88 single-turn cases, graders 195/206 (scored 126/134); multi-turn 24/28. For the form of the figures only, the 0.12.4 record reads 190/204 (scored 122/132) and 26/28; each is one run, and the two are not a comparison of versions.
  - Single-turn misses known from earlier releases: the two informative `neg-open-weighty-*` cases (expected without the `CLAUDE.md` line; `neg-open-weighty-memory-line-en` passed); prototypes and quiz not loading in `behavior-prototypes-interaction-mockup` and `behavior-quiz-on-submit`; the scout not spawned in `behavior-blindspot-scout-assumption-verdicts`; deviation-log not loading unasked in `behavior-deviation-log-auto-on-mismatch`.
  - Single-turn misses new in this run: `noncode-en-brainstorm` (the reply recommended one candidate before the user picked) and `behavior-unknowns-loop-terms-only` (the plan put the plain-language explainer before the blind-spot check).
  - Multi-turn misses: blindspot's `assumption-verdicts-carry-status` in `blindspot-partial-pick` and `blindspot-reaches-improved-prompt` (under watch since 0.12.4); quiz's `key-hidden-until-answered` (the correct option of one question was about twice as long as the others); teach-me's `draft-with-assumptions` (under watch since 0.12.4).
  - The judge graders of the negative and unknown-cell cases were scored for the first time on the short descriptions: all passed except the two informative weighty cases. tweakable-plan's description has no border to native plan mode; in the one-file case its body's size gate handled the request, and the judge grader `defers-to-plan-mode` passed 1/1.
- Re-runs, same engine, after the four goal and reason sentences went back and before the two Iron Rules did: `noncode-en-brainstorm` 2/2; `neg-open-quiz-en` 3/3 on both graders (three runs, because quiz's description lost its scope clause and the closing sentence); `trigger-en-brainstorm` 1/1; `behavior-brainstorm-scout-finds-unused` 1/1.
  - `behavior-unknowns-loop-terms-only` 0/2, and 0/3 on the 0.12.4 text run the same day, so this miss does not come from this release. The 0.12.4 record reads "the loop's teach-me order 3/3"; the cell is under watch.
  - tweakable-plan's `alternatives-are-lettered` passed 2 of 4 runs without Iron Rule 2 (the suite's run and three more; in each of the two misses one decision item, of six in one run and of seven in the other, gave its alternatives without letters) and 2 of 2 on the 0.12.4 text the same day. The rule went back.
- What the suite ran and what it did not: it ran the short descriptions with nine removals. Six of those sentences went back afterwards, and the suite was not run again on the final text. The released bodies of brainstorm, teach-me, tweakable-plan and deviation-log equal 0.12.4's, the bodies the short-description run above used. blindspot and the independent-reviewer agent carry the three removals the suite ran with: both reviewer cases passed, and blindspot's cases passed except the two misses named above (the scout not spawned, the multi-turn verdict grader).
- Release check, GPT-6.1 Sol at medium effort (Codex CLI), on commit 02484af, whose descriptions are the release's: the 22 trigger cases 22/22, each run reading the 0.13.0 `SKILL.md`. Three earlier attempts are void: the Codex app had synced the owner's own uploaded copy of the plugin (0.12.4) into the isolated home, and 7 or 8 of 22 sessions listed it beside the build and read its `SKILL.md`. The counted run created that cache folder (`plugins/cache/created-by-me-remote`) read-only beforehand, and 0 of 22 sessions listed it. The GPT-6.1 Sol checks of earlier releases did not guard against this.
- Not measured: the final text as a whole (above); the three remaining removals have one run per case; ChatGPT and claude.ai were not run with the short descriptions, and Codex only on the 22 trigger cases; the pasted sentence has no eval case in the repository; every cell above is 1 to 6 runs.

## 0.12.4 — 2026-11-10

Released 2026-11-10. A second rule-based review of the eleven skill bodies and both agents, the owner's decisions on its findings, a buy-in fix for limitations the user did not pick, deviation-log described as starting by name, by a trigger phrase or inside the loop rather than on its own, and 25 measuring eval cases (developer-only). Skill names unchanged.

### Fixed

- Second rule-based review of the eleven skill bodies (four rules: a condition stays with what it gates, scope words, fewer instructions with reasons, one name per thing), repeated until a round confirmed no new defect. Each round, two independent reviewers per skill (three for a skill the previous round changed, one of them comparing the old and the new text) read the file without the reasons for any edit; an adjudicator per skill checked each finding's quote in the file and against `.claude/rules/skill-writing.md`, and each skill's edits are one commit per round. Rounds applied 37, 11, 2 and 0 edits: 50 in all, 24 of them meaning changes.
  - Missing default branches: blindspot's scope table ("Otherwise", including a task with nothing beyond the conversation), and its investigation order now stated for direct investigation; prototypes asks one question for the target when nothing names one; teach-me's comparison table has an "Any other domain" row; brainstorm puts your own unknowns above the candidates when there is no ask-back; deviation-log with no text skips deviations already logged; quiz scores a partial retry one point per retry question answered correctly; reference's application plan says so when the reference has no checks of its own.
  - Reasons added: buy-in step 1b (a missing input rebuilt from the work would measure the work against the producer's own reading of it) and reference Iron Rule 1.
  - Names and scope: deviation-log hands buy-in "recorded deviations and unresolved risks", buy-in's own phrase; tweakable-plan sorts by "tweak likelihood × blast radius" in its title and Iron Rule 1 as step 5a does, and says "outcome" and "opening line" where it said "purpose" and "done criteria"; unknowns-loop's verify step checks what must not break and the allowed cost and change scope as well as the done criteria; reference numbers mapping and edge-case rows in one sequence and gives gotcha notes approve / request-change; quiz commits to each teach-back point with its change site and retries one question per wrong or blank answer in the same format; interview asks the next round by step 2 instead of proposing one; brainstorm suggests the next skill after step 5 and puts the scout's open lists above the candidates.
  - Not edited: findings on shared sentences, descriptions, names across files and method decisions (93 after duplicates were removed). They are Todo for human in `IMPLEMENTATION_NOTES.md`.
- Owner decisions on those findings, applied as separate commits: the loop's first reply states or asks for all four step 2 items (outcome, done criteria, what must not break, allowed cost and change scope); blindspot marks each ② and ⑤ assumption held or wrong with its evidence and status, or still unchecked, and lists unpicked prompt fixes as undecided under the revised draft; quiz asks its five multiple-choice questions in one batch, split only when the question tool takes fewer; teach-me says above the ladder which sources it opened and which it cites from memory, says so when it can name no source, and marks *unverified* only terms whose usage it doubts; deviation-log suggests the quiz, and the loop runs its quiz stage, only for work the AI largely produced; the loop runs teach-me first only when the user cannot yet describe the task, as blindspot and teach-me already do; the blindspot / teach-me order sentence names both skills as skills. Both READMEs follow the quiz and loop changes.
- buy-in: the final doc keeps the limitations the user did not pick, as drafted, beside kept and revised entries, and the reply names the entries with no pick. Both runs of a new multi-turn case had dropped them.
- deviation-log description: the "Use automatically when the work hits an unknown the plan did not cover" clause is gone, because in 5 measured runs where the work met an unplanned difference and nobody named the log the skill never loaded. The trigger phrases are unchanged and the method clause is in the third person. Both READMEs say the skill starts by name, by a trigger phrase or inside the loop. Routing before and after, 1 run each: trigger and collision cases 26/26 and 26/26.
- deviation-log: **Don't log** names an item the plan said to check that came back as planned. A site-visit case had logged the venue's Wi-Fi password as a Discovery in 2 of 2 runs; 1 of 3 after the change.
- independent-reviewer: "the producer's explanations" names one thing in review item 5 and output item 2, and the output refers to "review item" N. Second rule-based review of both agents: the reviewer took three rounds of wording fixes, the scout none.

### Changed (developer-only)

- `behavior-deviation-log-auto-on-mismatch`'s member list uses placeholder phone numbers (`010-0000-…`, `031-000-…`) in place of realistic ones; the case reads only which column is present.
- 25 eval cases (18 single-turn, 7 multi-turn) and graders on six existing cases, written to measure the open decisions before changing text; each case was checked by a second agent. The multi-turn discovery test expects 12 cases. The decision rule, each case's result and decision, and the cases corrected after their first runs are in `IMPLEMENTATION_NOTES.md` (2026-11-10).

### Checked (developer-only)

- Before each commit: `tools/package.py --check`, 91 unit tests (3 skipped), and `claude plugin validate --strict` for the plugin and the marketplace.
- Model runs on the final text, Claude Code 2.1.319, claude-opus-5-5, `--effort medium`, 1 run per case: single-turn graders 157/161 (scored graders 102/106; the skill loaded or stayed unloaded as each case expects 70/70), multi-turn 16/16. A first attempt failed at sign-in for every run (the headless CLI was signed out) and was re-run in full.
- Misses: the two informative `neg-open-weighty-*` cases (expected without the `CLAUDE.md` line, as in 0.12.3); `trigger-en-tweakable-plan`, where one decision had no check (the ordering held), and `neg-interval-loop-does-not-fire-unknowns-loop`, where the skill stayed unloaded but the model asked what counts as done. Each passed 2 of 2 on re-run and is under watch.
- Not measured: the meaning changes no case reaches (brainstorm's scout lists, prototypes' question when nothing names a target, quiz's score after a partial retry).
- Owner decisions, on the changed text (Opus 5.5, medium, 1–3 runs per case): the loop's four items 5/5; blindspot assumption verdicts 2 of 3 runs against 1 of 5 on the earlier text, by the same grader; unpicked prompt fixes undecided 2/2; quiz in one batch 2/2; teach-me's sources line 5 of 6; deviation-log suggested the quiz 0 of 5; the loop's teach-me order 3/3; buy-in kept unpicked limitations 2/2 after its fix (0/2 before). The measure-first cases that passed on the current text left it unchanged; prototypes (single mockup) and quiz (before submitting) did not load, so their bodies were not reached.
- Whole suite once on the final text (Claude Code 2.1.319, claude-opus-5-5, `--effort medium`): the original 70 single-turn cases 158/161 graders (scored 103/106, against 102/106 on the first run of this review), all 87 cases 190/204 (scored 122/132); multi-turn 26/28, the original five cases 16/16. Misses beyond the known ones (the informative `neg-open-weighty-*` pair; prototypes and quiz not loading; the scout not spawned; the Wi-Fi Discovery): brainstorm titled a candidate "Fix the metric first" (2 of 4 runs so far), teach-me framed wine vocabulary around buying without saying so (2 of 3 pass), the English loop reply left change scope out (8 of 9 pass), Korean quiz's explanation worked through Q2's own numbers, blindspot's partial-pick verdicts (2 of 4 pass) and teach-me's draft marking only some assumed details. Each is a single-run slip under watch.
- After the whole-suite run: the deviation-log cases 16/16 graders with the **Don't log** change; `behavior-scout-checks-pinned-version` 2/2, so unknowns-scout step 5 keeps its wording. deviation-log loaded on its own in 0 of 5 runs where the work met an unplanned difference and the prompt did not name the log; the owner chose to drop the automatic claim (above). `behavior-deviation-log-auto-on-mismatch` now requires a written log and is tagged informative; it failed its 1 run after the change, as expected.

## 0.12.3 — 2026-11-04

Released 2026-11-04. Text fixes from the first medium-effort runs and from a rule-based review of every skill and agent, the reference and quiz descriptions, an eval-runner fix for agents that hand their report back through a SubagentHandback call, and developer-only changes below. Skill names unchanged.

### Fixed

- reference and quiz descriptions: each adds one sentence that the skill runs even when the work looks simple ("Runs even when the adaptation looks simple, …", "Runs even when a quiz could be written directly, …"), and each body says why such a request is never clear to both sides by itself (reference Iron Rule 3; a sentence after quiz's opening). At medium effort the Korean non-code reference case loaded the skill 0 of 3 times and the quiz case 1 of 3; after the change 2 of 2 each, with the 22 trigger cases 22/22 and the 4 collision cases 4/4 (1 run each).
- Rule-based review of all skills and both agents (four rules: a condition stays with what it gates, scope words, fewer instructions with reasons, one name per thing), by three independent reviewers, then an independent review of the resulting diff; each finding's quote was checked in the file before it was applied. Wording: interview's priority heading, "Harm" tier and "blast radius" column; reference "new environment" and "the reference"; teach-me numbers each term and says "vocabulary"; buy-in "No such text" and "picks"; quiz's deviation question is one of the six; unknowns-loop's stage table carries its skip condition. Missing branches: blindspot step 6 ends with "Otherwise, suggest no next skill"; buy-in step 5 always lists the unanswered step 2b questions, the answers moved in step 4c and missing inputs, with deviation-log items only when a log exists, and step 1b names a missing input instead of reconstructing it; tweakable-plan says what happens when the user declines the interview and on change requests; brainstorm's scout packet carries the problem, constraints, where to search and a done-when; the scout has a done-when; unknowns-loop says a request whose read-back exposed a mismatch goes on to step 2 and the routed skill runs at its stage; independent-reviewer's outcome line also names what the done criteria missed. Rejected: two blindspot sentences that repeat a rule on purpose (fixes for measured slips in 0.12.1 and 0.12.2) and quiz's "key" naming (quoted by eval graders). Deferred: findings on cells under watch (prototypes saturation, interview skipped questions) and on shared blocks. Checked by one run of each neighbouring case (16 runs, 25 of 26 scored graders; the miss, buy-in using an unbacked figure as evidence, passed 2 of 2 on re-run and is under watch); the review's call for a 12-run A/B per meaning change was not run (owner: fewer runs).
- independent-reviewer: review item 1b names the outcome values (likely, unlikely, likely except a named gap, not judgeable and what would settle it) and says that met or missed done criteria do not answer it; the output opens with one `Outcome: …` line and its reason. One medium-effort run of three judged only the done criteria and left the outcome to the user.
- quiz: step 2 asks for answers by question and option number with no sample answer line. One medium-effort run gave "like `2 1 1 1`" as the reply format, which was the answer key.
- `evals/run-manual.py`: since Claude Code 2.1.31x a spawned agent can hand its report back through a SubagentHandback call, and the caller's tool result is then only a pointer. The runner now reads the report from the agent's transcript, so `focus: trace` graders judge the agent's own report again. The first medium-effort pass judged the independent-reviewer cases on the caller's relay alone and reported 0/3 for the outcome judgement; re-judged on the recovered reports it is 2/3.

### Checked — release runs (developer-only)

- Claude Code 2.1.317, claude-opus-5-5, `--effort medium`, 1 run per case: single-turn scored graders 156/161 and multi-turn 16/16, after re-running the 17 single-turn and 3 multi-turn runs that an Anthropic API 500 error broke. Misses: the two informative `neg-open-weighty-*` cases (expected without the `CLAUDE.md` line), `neg-open-text-en` (a proofread answered directly but followed by an eight-item change list), and `trigger-ko-blindspot` answered directly without the skill once, then 3/3 on the routing re-check.
- Codex CLI 0.166.0, gpt-6.1-sol, `model_reasoning_effort = "medium"`, the 22 `trigger-*` cases once each from a clean `CODEX_HOME` with the plugin added from this build's marketplace: the right skill loaded 22/22.

### Checked — medium-effort baseline (developer-only)

Claude Code 2.1.317, claude-opus-5-5, `--effort medium`, on the 0.12.2 bodies; `llm` graders judged by a separate `claude -p` (Opus 5.5).

- Single-turn, 70 cases × 3: mechanical graders 75/75, all scored graders 303/318, skill fired 161/165. Below 3/3: `noncode-ko-reference` 1/3 and `noncode-ko-quiz` 1/3 (the skill did not load in 2 and 1 runs), the informative `neg-open-weighty-*` cases 0/3 each (as before without the `CLAUDE.md` line), and 2/3 each for independent-reviewer outcome judgement, tweakable-plan lettered alternatives and plan-mode deferral, teach-me Korean, and trigger-en-quiz.
- Multi-turn, 5 cases × 3: 12 of 16 graders 3/3; 2/3 for blindspot evidence status (two *inferred* cards without their basis), interview question order, prototypes contrast question on a bare skip, and quiz key hidden (the correct option longer than the rest).
- Fix checks (owner: fewer runs; 2 runs of each failing case): independent-reviewer code case 2/2 with the report-vs-records case 1/1; trigger-en-quiz 2/2.
- Korean routing re-check, 3 runs each: `noncode-ko-reference` fired 0/3 and `noncode-ko-quiz` 1/3. Fixed by the description change above.

### Changed (developer-only; the shipped payload is unchanged)

- Supported models: Claude Opus 5.5 and GPT-6.1 Sol at medium effort (both READMEs). Other models and effort levels are not tested.
- `evals/run-manual.py` and `evals/run-multiturn.py` pass `--effort medium` to the model under test by default and record the effort in each result; earlier results ran at the CLI default effort.
- `tools/package.py` also rejects the reserved words `anthropic` and `claude` in a skill name, `<` or `>` in a description, and a `SKILL.md` body over 500 lines, per Anthropic's skill authoring best practices.
- `scripts/skill-descriptions.json`: the claude.ai upload descriptions of reference and quiz carry the same "runs even when" clause (188 and 194 characters).
- `docs/skill-authoring-guide.md`: the official best practices mapped onto this repository, with an audit of which `SKILL.md` content could move to reference files (none), and the run counts for fixes, routing checks, releases and text audits.

## 0.12.2 — 2026-10-28

Released 2026-10-28. Two body fixes from this build's own runs (interview counts a question inside a reason line toward the four; blindspot puts an unchecked finding under Needs checking instead of a card); descriptions, skill names and always-on tokens unchanged. Also: a buy-in eval case that lets buy-in spawn the independent-reviewer, and the proxy measurement of the claude.ai upload descriptions.

### Checked — the claude.ai upload descriptions (developer-only; shipped payload unchanged)

- Claude Code proxy measurement of the short upload descriptions (`scripts/skill-descriptions.json`, 200 characters or fewer) against the plugin's own descriptions, 2026-10-28, Claude Code 2.1.309, claude-opus-5-5. Two arms run side by side on the 0.12.1 bodies, which are byte-identical in both arms; only the `description` lines differ. 26 cases × 10 runs × 2 arms: the 22 `trigger-{en,ko}-*` cases and 4 must-not-fire collision cases. Measured by the routing graders (`tool_used` Skill).
- Plugin descriptions 260/260, upload descriptions 259/260 (Fisher p = 1.0; 95% Wilson lower bound 97.9%). English triggers 110/110 in both arms, Korean 110/110 vs 109/110, collision cases 40/40 in both arms. The one miss: in one Korean blindspot run no skill loaded and the model answered the risk directly.
- A first pass hit the account's session limit in 156 runs across 9 cases, in both arms. Those 9 cases were re-run in both arms and the void runs were dropped; none are counted.
- Not shown by this: claude.ai's own routing and the upload screen. The outcome graders were not judged, because the bodies are identical and the arms can differ only in which skill loads.

### Changed — fixes from this build's own runs

- interview: step 2a also counts a question mark inside a question's reason line toward the four. One multi-turn run had asked a fifth decision inside a "why it matters" line ("should a dropped recipient ever be told?"); earlier runs had tucked a fact request or a second question into an item.
- interview, tried and taken out: a sub-step that sorts each round's questions by the Question Priority before writing them, for the round-order slips (an empty-result question asked before a retry question). In step 4 it kept rounds 2 and 3 in order in 3 of 3 runs, but round 1 dropped its sure-of/assuming question in 2 of 3. Moved to the start of step 2 and naming that question, it kept round 1 in 3 of 3 but put a why follow-up under a harm question in 1 of 3. The order wording is back to 0.12.1's, which passed the order grader in 6 of 6 runs this round.
- blindspot: step 4 says where an unchecked finding goes when the cards are written (a card's status is *confirmed* or *inferred*; an *unchecked* finding goes under **Needs checking**), and the tally counts the cards. The rule was already in step 3b; one multi-turn run kept an unchecked card in the cards and the tally (1 of 3, the same slip as 1 of 9 last round).

### Evals (developer-only; not in the shipped payload)

- `behavior-buy-in-relays-reviewer`: the pilot-report material from the independent-reviewer case, a buy-in request for a second year of funding, and the Agent tool allowed, so buy-in's step 4b spawns the independent-reviewer. Graders: the agent is spawned; the buy-in doc uses the records' figures and keeps the unbacked claims out of the evidence; the doc carries the reviewer's outcome judgement. The four earlier buy-in cases allow no Agent tool, so they could not show this.
- Suite: 70 single-turn cases (161 graders), 5 multi-turn cases (21 graders).

### Checked — interview, blindspot and buy-in on this build's own runs

Claude Code 2.1.309, claude-opus-5-5, no comparison arm (owner decision); `llm` graders judged by a separate `claude -p`, which also sees spawned agents' reports and the files a run wrote.

- interview, the two sort iterations: multi-turn 10/12 and 10/12 (order 1/3, then 2/3; four-per-reply 3/3, then 2/3); single-turn five cases 18/18 on the first. Final wording, multi-turn 6 runs: 24/24 (order 6/6, four-per-reply 6/6); single-turn five cases 3 runs: 18/18, and round 1 opened with the sure-of/assuming question in 15/15.
- blindspot multi-turn on the 0.12.1 body: 11/12 (evidence status 2/3). After the fix, 6 runs: 24/24 (status 6/6); the six single-turn blindspot cases, 3 runs: 30/30.
- buy-in, 3 runs each: the four earlier cases 12/12; the new reviewer case 9/9. The independent-reviewer was spawned in 3/3 runs, and in 3/3 the written buy-in doc carried its outcome judgement (nothing in the material measures whether residents bought fewer tools), the recomputed members and loans, the unbacked rota and thank-you claims as limitations, and the dropped deposit. The short chat reply that pointed to the doc named the outcome in 1 of 3; the doc is the deliverable, so no body change.
- The intended skill loaded in every run: 63/63 single-turn and 21/21 multi-turn.
- Writing-for-models, Claude only: per-file checks of interview and blindspot and a diff check of the round's fixes; 19 findings, all quotes verified, 0 confirmed (19 rejected: two repeat what the sort iterations tried, the rest restate the owner's read-back ruling, guard prose, shared blocks, or wording points with no failing run).
- Tokens (cl100k): always-on frontmatter unchanged at 1,404; the 11 bodies 13,653 → 13,683; all shipped text 17,430 → 17,460.

### Not measured

- The interview order cell across runs: 2/3 per batch for two rounds, 6/6 this round on the same wording; 3–6 runs per batch cannot separate a fix from run-to-run variance.
- The four-per-reply and blindspot evidence-status fixes were each seen at about 1 in 3 to 1 in 9 runs before; 6 clean runs each do not show the slips are gone.
- The independent-reviewer called by name outside buy-in (the caller's retelling dropped the outcome judgement in round 4): not re-run; the bodies are unchanged for it.

## 0.12.1 — 2026-10-28

Released 2026-10-28. Body fixes from this build's own runs (blindspot, brainstorm, interview, quiz); descriptions, skill names and always-on tokens unchanged. Eval coverage for the independent-reviewer agent and reference's correction rule, the thin cells re-measured on this build, a Codex run, and fixes from the build's own runs.

### Changed — fixes from this build's own runs

- blindspot: a risk the AI already sees is a finding, not one of its own assumptions, and waits for the user's answer or skip like every other finding. Korean trigger runs had put the core risk ("a 502 does not mean the processor did nothing") into the AI's ⑤ list in the opening reply. "Context sources" and "kinds" each keep one name.
- brainstorm: step 4 gives the reason the picks come first: they show the user's priorities, which the AI does not know yet, so a recommendation added after the list makes the pick for them. The Output layout says "candidates" ("cards" are the scout's blindspot cards), and step 5 starts once the user names the picks.
- interview: a further round is proposed only for unsettled items (neither decided nor deliberately left undecided by the user), and the why follow-ups make up a round of their own when none remain. A tag naming each question's radius was tried for the order slips and taken out again: in two iterations it did not fix the order and dropped the reasons from option questions.
- quiz: the teach-back is graded against "the 2–3 points in the key file from step 1c".
- brainstorm, interview, quiz: "the model" becomes "you" in three body sentences, as everywhere else in the bodies (from the skill-creator check).

### Evals (developer-only; not in the shipped payload)

- Input files through the CLI's own scaffold form: a case may carry `files/`, a `place-files.sh` and a `case.yaml` naming it under `context: scaffold_script:`; `run-manual.py` runs the script with bash in the run's fresh cwd before the run, as `claude plugin eval --scaffold` does, and `--verify` checks `case.yaml` and the script. A `fixture:` key in `prompt.md` was tried first and dropped: the CLI fails to load a case with a key it does not know.
- `run-manual.py` keeps the report each spawned agent hands back as `agent_reports`, so a grader with `focus: trace` judges the agent's report, not the caller's retelling of it.
- Two independent-reviewer cases call the agent by name: `behavior-independent-reviewer-code-change` (a git repository whose last commit silently misses one of five done criteria: an empty month prints no header) and `behavior-independent-reviewer-report-vs-records` (a pilot report whose members, loans and loss rate contradict the records beside it, with an undisclosed deviation). Graders: the agent is spawned; each done criterion judged met, partial or missing; the planted miss found; an outcome judgement; a claim-checks part.
- Multi-turn `reference-correction-revises-plan`: the user corrects one semantics-map row by its number in turn 2 and says nothing about what else it changes; the grader checks that the reply revises the plan items built on that row.
- Suite: 69 single-turn cases (157 graders), 5 multi-turn cases (21 graders).

### Checked

Claude Code 2.1.309, claude-opus-5-5, this build on its own runs (no comparison arm, by owner decision); `llm` graders judged by a separate `claude -p`, which for the reviewer cases also sees the agent's report.

- independent-reviewer, 3 runs per case: the agent was spawned in 6/6 runs; 30/30 graders on the final case form. In the first form, the caller's retelling dropped the reviewer's outcome judgement in 3/3 code runs, although the agent's own report had it; the graders now judge the report.
- reference multi-turn, 3 runs: 6/6 graders; every reply revised the corrected row and the rows and plan items built on it (form fields, documents, payment).
- Thin cells, 3 runs each on the 0.12.0 bodies: prototypes single-turn 18/18 graders and multi-turn 9/9; blindspot evidence status 9/9 single-turn and multi-turn 12/12; brainstorm noncode-en 1/3 (a recommendation after the closing question), noncode-ko 3/3; multi-turn interview 11/12 (order 2/3). Korean blindspot trigger ×10: `unknowns:blindspot` loaded 10/10, method grader 6/10 (the ⑤ leak above).
- After the fixes, failing cells and every changed skill's cases 3× (two iterations, then the final interview): Korean blindspot trigger 10/10 and 10/10; brainstorm's five cases 18/18 and noncode-en 3/3 again on the final wording; blindspot behaviour, trigger and non-coding cases 27/27 in each iteration; single-turn interview cases 17/18, 18/18 and 17/18 (each miss one non-coding run: reasons of two or three sentences, once with extra questions inside a reason); quiz 5/6 (one response cut off mid-stream), then 3/3. Multi-turn: blindspot 12/12 and 11/12; interview 10/12, 10/12 and, on the final wording, 11/12.
- The intended skill loaded in every run: 153/153 single-turn and 30/30 multi-turn.
- Codex (codex-cli 0.164.0, isolated HOME and CODEX_HOME, a `git archive` copy of this branch): the three renamed skills by `$unknowns:` name and by English and Korean trigger phrase, 2 runs each, 18/18 to the intended skill. Behaviour, 1 run each, judged by Claude: tweakable-plan 3/4 graders (it wrote "completion criteria", which the regex grader does not accept; the method held), interview 1/2 (round 1 asked four open questions with reasons but did not say more rounds follow). Both pass on Claude; the bodies are unchanged for them.
- skill-creator check of the 11 skills and 2 agents: `quick_validate.py` 11/11 valid; 16 criteria adjudicated against the repository's rules (3 form fixes applied, the rest kept by rule or owner decision).
- Writing-for-models, Claude only: per-file checks of the four changed skills before and after the fixes and four diff checks (65 findings; 14 confirmed, 11 edits, one later reverted with the radius tag; 51 rejected as guard prose, shared blocks, measured wording, the owner's read-back ruling, or form points with no failing run).
- Tokens (cl100k): always-on frontmatter unchanged at 1,404; the 11 bodies 13,559 → 13,653; all shipped text 17,336 → 17,430.

### Not measured

- No comparison with 0.12.0 (owner decision); every figure above is from this build's own runs at 1–10 runs per cell, so small differences are within noise.
- Cells still to watch: the multi-turn interview's order (2/3 in every batch this round, with or without the tried tag) and its four-per-reply count (one fact request tucked into an item in 1 of 3 runs in two batches); blindspot's multi-turn evidence status (an unchecked item kept in the cards in 1 of 9 runs).
- The claude.ai upload descriptions (`scripts/skill-descriptions.json`): a 520-run Claude Code proxy measurement was approved and runs after this release; its result goes into the next entry.
- claude.ai, ChatGPT and mobile behaviour; Codex beyond the three renamed skills and two behaviour cases; real Windows use (the scaffold tests that run bash are skipped on Windows).

## 0.12.0 — 2026-10-28

Released 2026-10-28. The plugin is rescoped to three cells of what the user and the AI know, in any domain, judged by the outcome.

**Breaking:** three skills are renamed. `loop` is now `unknowns-loop` (Claude Code's built-in `loop` owns the bare name; `/unknowns-loop` now works without the plugin prefix), `notes` is now `deviation-log` (the name says what it logs), and `plan` is now `tweakable-plan` (a bare `plan` collides with native plan mode and other plugins' plan skills). Use `/unknowns:unknowns-loop`, `/unknowns:deviation-log` and `/unknowns:tweakable-plan` (Codex: `$unknowns:unknowns-loop`, `$unknowns:deviation-log`, `$unknowns:tweakable-plan`); re-upload the skill zips on claude.ai and desktop. The trigger phrases stay: "unknowns loop", "run the operating loop", "implementation notes", "record a deviation", "plan this", "make a plan", "tweakable plan", and the Korean "운영 루프로 진행", "이탈 기록", "임플 노트", "계획 세워줘". Every skill and agent description is rewritten: domain-neutral, compacted, and each skill description ends with "Clear to both sides: no skill or method." instead of "Self-evident requests are done directly."

### Changed — purpose

- `.claude/rules/skill-writing.md` opens with rule 0, the plugin's purpose: of the four cells of what the user and the AI know about a task (the Johari window's panes, adapted), the plugin serves Blind (the user does not know, the AI does), Hidden (the user knows, the AI does not) and Unknown (neither knows, the widest cell), in any domain. Open (both know; the request is self-evident) is out of scope and done directly. Work is judged by the outcome (the achievement that matches the user's intent), not only by the output (the artifact). Rule 9 adds the vocabulary (output/outcome, 산출물/성과, the cell names) and one form per skill name per file; rule 17 lists both sides' unknowns and the outcome check among the method's moves.

### Changed — each skill serves its cell, in any domain

Every skill body opens by naming the cell it serves and with the read-back rule for requests both sides understand (see "Changed — follow-up rulings"); every description ends with "Clear to both sides: no skill or method."

- **Blind** (the user's or approvers' gaps):
  - teach-me: unchanged method; examples and the comparison table name text, code or process; the blindspot boundary is "a specific plan, system or situation".
  - quiz: explains and quizzes any delegated work (a report, an analysis, a lease review, a code change) before it is handed over, presented, submitted or merged. Each explained part is anchored to its location (`file:line` for code; section, page or row otherwise); the top question type is "what to do when it goes wrong"; misses name the exact change site.
  - buy-in: rewritten from a reviewer persuasion doc to the **approvers' unknowns doc**. Step 2 maps, per approver, what they do not know that their decision depends on and what they will object to, asks the user what they know about each approver (priorities, past objections, unwritten politics), and lists what neither knows as questions to find out. The result is shown first (a demo, sample, pilot result or budget table; when none, a limitation), each point is answered with followable evidence checked by independent-reviewer, unsupported answers become limitations, and the doc names who signs off.
- **Hidden** (what the AI does not know or cannot judge):
  - interview: before deciding, it asks in rounds of at most four what it cannot know or judge about the user's situation. The fixed order is by what a wrong decision breaks, in any domain: structure → irreversible harm → compatibility → cost → taste (architecture → data/security → APIs/existing code → performance → UI in code). The final prompt is "a ready-to-use prompt for the work", declares the structure and harm decisions fixed, closes with "start with a short plan, then do the work", and logs deviations in the deviation log (IMPLEMENTATION_NOTES.md for code work).
  - reference: any example (another organisation's policy, a past proposal, a contract template, code, a mockup). Semantics-map rows that rest on a guess about the user's context are marked *assumed* for correction first; the application plan first carries over how the reference checks itself (tests, checklists or acceptance criteria).
- **Unknown** (both sides):
  - blindspot: the opening reply puts the AI's own three lists (④ what it does not know about the user's situation, ⑤ what it is assuming, ⑥ what it cannot check) next to the user's three; ⑤ is checked with ②, ④ becomes questions and ⑥ Needs checking. Kinds, evidence and scope are domain-neutral (a funding call, a policy, an event, a codebase); the scout is used when the task spans many sources.
  - brainstorm, prototypes, tweakable-plan, unknowns-loop: a shared **Your own unknowns** sentence states what the AI does not know about the user's situation, what it assumes and what it cannot check, for the user to fill or correct.
  - brainstorm: grounded in what already exists (in code, disconnected machinery; elsewhere resources, programmes, people), marked `Already exists — <where>`; success is the sign the problem moved.
  - prototypes: axes fit the subject (a screen; a document, event, role or campaign; complexity for any); "versions to react to" is a trigger phrase.
  - tweakable-plan: the size gate is domain-neutral (work with no decision the user might want to change; for code ≤2 files and no schema, interface or UX-contract decision, which suits native plan mode); decision and mechanical items and the annotated artifact have code and non-code examples.
  - deviation-log: logs beside any deliverable — `IMPLEMENTATION_NOTES.md` for code, otherwise the file the user names or `DEVIATIONS.md` beside the deliverable. Observed is auditable against the work as it stands; a choice resting on something only the user can know is named in Risk/follow-up and put to the user first at wrap-up.
  - unknowns-loop: the purpose is the outcome the user is after; the probe is the cheapest test of the riskiest assumption (a spike, a call, a pilot); after verify and quiz/buy-in, a short **outcome check** with the user asks whether the result achieved the outcome, not only whether it met the done criteria (no score or stored record).
- independent-reviewer: checks any deliverable (a report, plan, event programme, proposal, analysis or code change) against its plan, done criteria and outcome, treating the producer's account as claims. Its packet adds the outcome and names the deliverable (for code, the diff range and how to run the tests); item 1 adds an outcome judgement ("outcome not judgeable — no outcome stated" when missing); "passes on paper, fails in reality" covers figures, sources and ownerless steps as well as mocks and mirrored tests; findings carry a `file:line`, section, page or row. Its scoping sentences are unchanged.
- unknowns-scout: investigates whatever sources the task has (documents, data, the web, a codebase, history); each step names its code and non-code form.
- Descriptions, short descriptions, `agents/openai.yaml`, the plugin and marketplace descriptions and the OpenAI listing are domain-neutral with code as one example. Every trigger phrase is kept; new English phrases: interview "ask me before you decide", buy-in "get sign-off", prototypes "versions to react to". Skill descriptions grow from 3,057 to 4,179 characters.

### Changed — follow-up rulings

- Plain words for the cells: shipped text (skills, agents, descriptions, the plugin README) says "what the user does not know and you do", "what you do not know and the user does" and "what neither the user nor you know yet"; the Johari pane names stay in developer documents and appear once per README, where the source is credited. The READMEs' cell tables drop the pane column. A test fails if a pane name or "Johari" returns to the shipped plugin.
- Read-back for requests both sides understand (replaces "done directly"): when the result carries weight, the AI first reads back in 2–3 lines the request, its assumptions and what outcome counts as done, and does it on the user's confirmation without a method; a truly self-evident request needs no read-back. A mismatch routes by who does not know: the user → teach-me, the AI → interview, neither → blindspot. The rule is a paragraph under every skill's cell line, the unknowns-loop skill's new step 1 (later steps renumbered), and, until round 3, a compact line at the end of every description (see below).
- interview: round 1 asks open questions, without options, about what the AI cannot know or judge about the user's situation; option questions for the decisions come from round 2 on. Four per round, sure-of/assuming first and unanswered-stays-unanswered are unchanged.
- brainstorm: candidates are generated before any judging (Osborn: defer judgment, go for quantity), each with only a name, one line and the Already-exists marker; impact, effort, risks and the success measure are attached to the picks.
- prototypes: the description says prototypes in the design-thinking sense, several versions of anything for the user to react to; the trigger phrases are unchanged.
- Descriptions compacted: the example-domain lists and repeated wording are cut from every skill and agent description; every declared trigger phrase and the agents' scoping sentences stay. Always-on frontmatter (cl100k): skill descriptions without their closing line 1,143 → 884 tokens; the read-back line costs 51 tokens per description against 9 for the old line, so skills total 1,341 → 1,571; agents 357 → 311.
- Read-back wording, from the own-run check: "no skill or method" and what makes a request weighty (it ships, is sent or is hard to undo); the read-back is the whole reply.

### Changed — round 3 rulings

- Descriptions drop the read-back line: it showed no effect on weighty requests (0/21 runs) and cost about 460 always-on tokens. Each ends with "Clear to both sides: no skill or method." (10 tokens); the read-back stays in the bodies and as the unknowns-loop skill's step 1. Always-on frontmatter falls from 1,882 to 1,404 cl100k tokens (0.11.0: 1,094). Descriptions stay English-only.
- README.md and README.ko.md: Scenario A gives one line to put in your own `CLAUDE.md` for a read-back on every weighty request: "Before doing a request whose result carries weight (it ships, is sent or is hard to undo), reply with only a 2-3-line read-back (the request, your assumptions, what counts as done) and wait for my confirmation; just do self-evident requests."
- interview: each question asks one thing in one sentence; every question in the reply counts toward the four (a second question mark in an item, one in an option, a fact request, a request to check something elsewhere); every question carries its reason; the deliverables come when every item is decided or left undecided and no why follow-up is pending, or the user ends the interview.
- brainstorm: ranking, pruning, sizing and any recommendation wait for the picks, and the reply ends on asking which numbers resonate; horizons are this afternoon / up to a month / 1–3 months / longer.
- tweakable-plan: the description says work with no decision the user might change gets plain steps; alternatives are lettered; the size-gate reply keeps the own-unknowns questions.
- teach-me: the reply ends by asking which terms, comparisons and presets to include; the precise-request draft is written from the answers.
- Fixes from the deferred writing-for-models findings of rounds 1 and 2 (113 re-checked: 52 confirmed, 56 rejected, 5 gone): blindspot cards carry a numbered prompt fix and the picks leave only the picked fixes in the draft; quiz assembles its block after the gate with the final score and names change sites; reference revises plan items that rest on a corrected entry; deviation-log's steps name the one-line Discovery and the Logging Criteria; buy-in's missing-tool line sits at the reviewer step; the loop's skip rule covers stages marked always and stage d tests the approach; the scout keeps Questions to answer and Information still needed in any return shape and reports checked assumptions; the reviewer's output carries the worth-logging judgement, the list-first order, item 3's findings and every claim it met.

### Changed — fixes from the new build's own runs and checks

- teach-me: the precise-request draft marks every detail the user did not give (their taste, numbers, situation) as an assumption to confirm.
- buy-in: collects the done criteria and the outcome its reviewer packet needs; an answer whose evidence the independent-reviewer agent could not confirm becomes a limitation; one title, "The Buy-In Doc".
- reference: the semantics map comes before building anything on the reference, a port or adaptation included (an "and" had narrowed it to ports).
- brainstorm: its own unknowns go in the same round as its one ask-back.
- interview: the non-code deviation log is the file the user names or `DEVIATIONS.md` beside the deliverable.
- unknowns-loop step 1 fixes "the outcome"; deviation-log is titled "Deviation Log" and the other skills "read that log"; independent-reviewer says "the producer's explanations" throughout and points missing done criteria or outcome at item 1; the scout's territory includes the web.
- Evals: three graders that judged form the cases do not test (an errand answer's length, a second rewrite variant, an unmarked example list) now judge the method.

### Renamed

- Skill folders, `name:`, `agents/openai.yaml`, `scripts/skill-descriptions.json`, sibling references, both READMEs, the trigger matrix and the eval cases (`trigger-{en,ko}-unknowns-loop`, `trigger-{en,ko}-deviation-log`, `trigger-{en,ko}-tweakable-plan`, `behavior-deviation-log-appends-to-file`, `behavior-tweakable-plan-opens-with-done-criteria`) follow the new names. `tests/test_renamed_skills.py` fails if an old name returns outside CHANGELOG, IMPLEMENTATION_NOTES.md and dated docs.

### Docs

- README.md and README.ko.md: a Purpose section (the three cells, output vs outcome), a pitch for any domain, a Cell column in "Skills at a glance", non-coding examples for every skill with code kept as one example among several, the agents described for any deliverable, scenarios from a self-evident request to a new field, and a note on the renames under Updating.

### Checked

Claude Code 2.1.309, claude-opus-5-5, the new build on its own runs (no comparison arm, by owner decision); `llm` graders judged by a separate `claude -p`.

- Whole single-turn suite once, new cases 3× each: existing triggers 22/22 runs, behaviour 6/6, negatives 5/5; non-coding 62/66; Unknown cell 11/12; Open-cell negatives 9/15 (no skill fired in 15/15; the graders failed verbose direct answers). After the fixes above, the seven failing cells at 3 runs each: 21/21.
- Multi-turn cases once: 14/14 graders.
- Routing, 2 runs each: every skill named in English and Korean 44/44 to the named skill; the old names `loop` and `notes` (informative) 8/8 to the renamed skills; a bare "loop … every 5 minutes" 2/2 to the built-in. The intended skill loaded in 66/66 non-coding runs.
- Per-file writing-for-models checks by Claude (71 findings) and Codex (16) on every changed skill and agent and the plugin README, adjudicated against the owner's rules, and Codex diff checks of the fixes.

- Follow-up rulings, on the new build only: tweakable-plan named in English and Korean 4/4 runs to the skill, the old name `plan` 1/1 to tweakable-plan; every non-coding, Unknown-cell and Open-cell case once (non-coding 17/22 runs fully passing, intended skill loaded 22/22; Unknown cell 4/4; trivial Open cell 4/5); interview, brainstorm, prototypes, tweakable-plan and blindspot behaviour cases 3× each, 21/24; multi-turn interview and prototypes 3× each. After two fix iterations the failing cells pass except: the weighty Open-cell cases (0/9: with no skill loaded the model does a clear request directly instead of reading it back, under three description wordings), the multi-turn interview's four-per-round and reason checks (1/3 and 2/3 in iteration 2), and brainstorm's deferral of judgment in 1 of 3 runs.
- Agents, one run each on non-code material: buy-in called independent-reviewer on a pilot report, which found the report's three figures contradicted by the records and an undisclosed deviation; blindspot called unknowns-scout over 20 documents, which found the planted landmines (a standing board ban, an 18+ insurance limit, a grant clause).
- Per-file writing-for-models checks by Claude on every changed skill and agent (83 findings, 8 confirmed and fixed) and a diff check of the fixes (1 more fixed).
- Round 3, new build only: the `CLAUDE.md` line gave a read-back that waited for confirmation on 9/9 weighty runs (6 as a real project `CLAUDE.md`, 3 as appended system prompt) and left 4/4 trivial requests done directly. The three left failures, two iterations each: the one-file "plan this" 3/3, the interview's four-per-reply count 3/3 (multi-turn and single-turn), reasons and order 3/3 then 2/3, brainstorm's deferral 2/3 in both iterations. After the deferred-finding fixes, every behaviour-changed skill's cases 3×: 182/189 graders, then teach-me 12/12 after its fix; multi-turn blindspot, interview and quiz 3/3 on every grader; buy-in called independent-reviewer and blindspot called unknowns-scout on non-code material. Full run on the final build: 67 single-turn cases once and trigger-ko-tweakable-plan 3×, 93/95 scored graders (the two failures are the informative weighty cases), every routing indicator to the intended skill; multi-turn 13/14 (blindspot's evidence-status grader failed, then 2/3 on a re-run: status-labelling slips in text this round did not change).
- Writing-for-models, Claude only: the 113 deferred findings re-checked (52 confirmed, 56 rejected, 5 gone); fresh per-file checks of every changed skill and agent and two diff checks of the fixes (94 findings, 9 edits).

### Not measured

- No comparison with 0.11.0 (owner decision); every figure above is from this build's own runs, most at 1 or 3 runs per cell, so small differences are within noise.
- prototypes' wording-only changes ran once, not 3×; its multi-turn case passed 3/3 graders.
- independent-reviewer has no eval case of its own (one informative run through buy-in); reference's rule that a correction also revises the plan items built on it has no multi-turn case.
- Cells to watch: blindspot's evidence-status labelling (3/4 on the final build) and brainstorm's deferral of judgment (1 of 3 runs in one cell).
- claude.ai, ChatGPT and mobile behaviour; Codex runs of this build; real Windows use.

### Evals (developer-only; not in the shipped payload)

- 22 non-coding cases, `noncode-{en,ko}-<skill>`, each with a routing indicator and an outcome grader (`moves-toward-the-outcome`) that fails a reply forcing software concepts onto non-software work.
- 4 Unknown-cell cases, `unknown-*` (a county permit, an organisation's unwritten politics, a three-month-old scheme, a personal job trade-off), graded on surfacing both sides' unknowns.
- 8 Open-cell negatives, `neg-open-*`, which must fire no unknowns skill: five trivial ones (a rename, typo fixes, a polite rewrite, an errand "plan", "quiz me" on trivia) must be done directly with no read-back; two weighty ones (`neg-open-weighty-code-en`, a production migration; `neg-open-weighty-text-ko`, an all-staff notice) must get a 2–3-line read-back that waits for confirmation and runs no method; since round 3 they are tagged `informative` (the gap without a `CLAUDE.md` line), and `neg-open-weighty-memory-line-en` runs the migration with the README's line as `append_system_prompt`, which `run-manual.py` now passes to `claude -p`.
- The interview graders check that round 1 asks open questions; the brainstorm graders check that the first reply does not rank, score or prune.
- Updated graders: blindspot's opening question may carry the AI's own unknowns (not findings) and the multi-turn case checks them; buy-in grades the approvers' unknowns; the loop's first reply establishes the outcome; the interview prompt fixes structure and harm decisions.

## 0.11.0 — 2026-10-27

**Breaking:** the plugin is compacted to its method. The loop tracker (`.unknowns/loop.json`, `status`/`resume`, tiers), the scorecard (`.unknowns/scorecard.md` and its end-of-session questions), notes `init`/`show`, the reviewer stage of loop, and the per-host fallback branches are gone. Skills and agents carry no guard prose, tool allow-lists or identity lines; both agents inherit every tool. Installed text is about a third of 0.10.0's.

### Changed — compacted to the method

Every skill and agent now keeps only the text that makes the model surface or resolve the user's unknowns. Skill and agent source text is 43% smaller than in 0.10.0 (19,054 → 10,796 cl100k tokens), and the installed payload's text 65% smaller now that no references are vendored. Skill descriptions are unchanged; two agent descriptions change, as noted below.

- All skills: the shared reference files (host surfaces, output routing, scorecard) are gone, and each skill folder is self-contained. The repeated Markdown-delivery sentence, question-tool fallbacks, no-file-system branches and read-only contracts are removed. A skill that needs a tool says once: "Without a tool, do the step in the conversation and say what could not be checked." Reaction lines end with "a missing pick is undecided."
- loop: a short sequence card. Done criteria in one exchange; before the build blindspot (teach-me first when the terms are missing), interview, brainstorm/prototypes/reference as needed, a minimal probe of the riskiest assumption, and plan; during the build notes; after it a check of the result against each done criterion with evidence, then quiz, plus buy-in when others must approve. The interview stage runs whenever the requirements leave decisions open, not only architecture decisions. The first reply still names the stages and states the done criteria. Tiers, the `.unknowns/loop.json` tracker, `status`/`resume`, stage checkpoints, the value review, the scorecard and the reviewer stage are removed.
- blindspot: marks each finding that none of the user's three lists mentioned as "new to you". The lists are restated in the reply, or the reply says the user skipped them; the loop baseline and scorecard lines are removed. The pass ends at the improved prompt, without a closing offer.
- teach-me: the Limits section and closing offer are removed, and so is a leftover "without inventing an image" clause; the hand-off to interview when revisions stop converging stays in Related.
- interview: the Iron Rules (covered by the steps) and the closing offer are removed. The implementation prompt declares the architecture and data decisions fixed and says that where the plan leaves a choice open or the code conflicts with a fixed decision, the implementer picks the conservative option and logs the deviation in IMPLEMENTATION_NOTES.md, instead of flagging conflicts before writing code.
- prototypes: ends at the confirmed requirements list; the implementation step and deviation clause are removed. The method's history is cut and its reasons kept.
- brainstorm: the impact × effort table and the execution prompts are removed; it ends at the assembled selection.
- reference: ends at sign-off; the application plan ports the reference's existing tests first. The implementation step is removed.
- plan: done criteria are one line at the top, with "not set" for any part the context does not give, asked for in the same reply. Each decision item carries its verification and what breaks if it is wrong; mechanical items carry their verification. The size gate is one sentence: it says the change suits native plan mode and replies with the done-criteria line, its questions, and the steps in execution order. The implementation step and the reviewer-packet sentence are removed.
- notes: picks the conservative option, logs it and keeps going; the check before a commit or hand-back appends what it finds, and a plan decision a deviation invalidates is marked superseded in the plan; at wrap-up, entries touching architecture, user-visible behavior, data or security are listed first. The entry format, inferred alternatives, the Discovery line, the logging criteria and the fold-back block stay. The location table, `init`/`show`, the CLAUDE.md rule offer, Todo-for-human entries, the plan-revision escalation and stop-and-ask are removed.
- quiz: ends at the score. 6/6 passes and suggests buy-in when reviewers must approve; below 6/6 stays "not yet" with sections to re-read and a retry. The cleared-to-merge checklist, the handoff summary and PR body, and the scorecard are removed.
- buy-in: leads with the working demo (when none exists, it says so and lists that as a limitation), answers objections with followable evidence checked by independent-reviewer, moves answers without evidence, or whose evidence the reviewer could not confirm, to limitations, pulls limitations from the log, and names who signs off and what each will check. The quiz prerequisite, spec table, rollback paragraph and sign-off checklist are removed.
- unknowns-scout: no tool list, bans or identity line; it reads git history itself. Its description drops "Read-only".
- independent-reviewer: no tool list, identity line, read-only contract or general bug and security pass. Deviations are judged by whether the conservative option was chosen, and the reviewer lists risky ones first for the user. Its description names buy-in as its only calling skill.

### Changed — fixes from the compacted plugin's own runs

- blindspot: the scout is chosen by the task's scope, not the repo's size: a task that spans the codebase or many modules uses the `unknowns:unknowns-scout` agent even in a small repo. The improved prompt draft is presented as the prompt to paste next; the user's prompt-fix picks edit it. The opening reply is the three-list question alone; every finding, the most urgent included, follows the answer or a skip. The two Iron Rules are merged into one.
- plan: every decision item, the last as fully as the first, carries the five labeled lines (chosen option, alternatives and why rejected, scope affected, verification, what breaks if wrong), and each annotated-code note names the alternative it beat.
- interview: the "why" follow-up is asked open, with its why-it-matters line and no options, so the reason is the user's own. A request for a fact (a repo path, the stack) counts toward the round's four questions.
- prototypes: the user scores every option on the triad's construct; the model does not pre-fill scores for the user to confirm. The model asks the user to confirm the assembled requirements list.
- quiz: when the correct option carries a cause, a consequence or a remedy, each distractor carries one too. The Output table is folded into step 1a.
- Sentences the method does not need are cut: buy-in's quiz contrast line, reference's slogan line, interview's purpose line after the prompt, and the reviewer's pointer to `/code-review` and `/security-review`. The cuts (−192 tokens) roughly pay for the fixes (+202): skill and agent source text is 10,806 cl100k tokens, from 10,796. Skill and agent descriptions are unchanged.
- Evals: the interview grader checks that conflicts with fixed decisions are logged as deviations (the current contract), not flagged before code; the single-turn blindspot trigger graders accept the opening three-list question with no finding beside it, which the multi-turn case requires.

The entries below were made earlier in this cycle, before the compaction. Those about the loop tracker, tiers and stage checkpoints, the scorecard, notes `init`, brainstorm's impact × effort table, blindspot's loop baseline, buy-in's demo read target, the quiz wrap-up, and the reviewer's temporary directory, read tools and permission note describe text that no longer ships.

### Changed

- plan: below the size gate, the reply is the one-line done criteria plus the implementation steps in execution order; the Iron Rules, steps 4–8 and the Output section of the full document no longer apply there.
- prototypes: the first reply says the option set can grow, and how (step 5c), instead of presenting the fixed number of options as sufficient.
- loop: the first reply lists the tier's steps by their headings in run order and marks the current one, so "skip ahead" at a stage checkpoint is visible.
- notes: when the context does not name the alternatives weighed, the entry names plausible ones, marked as inferred, instead of "not recorded".
- Wording fixes from a per-file writing-for-models review (one name per concept, condition before action, pointer fixes); no step or rule changes.
- interview: a further decision tucked under a question or into one of its options counts toward the round's four questions; when the user has not said what they are sure of and assuming, a list of what is still open no longer stands in for asking it first; a question asked but not answered is marked unanswered and its options and reasons stay out of the fixed decisions; when nothing else is undecided, the "why" follow-ups make up the next round on their own.
- quiz: options are formatted alike with no mark on the correct one, and every option of a question has similar length and detail; a retry is a new question on each missed part, graded the same way, and a retry that gets every missed part right brings the score to 6/6; the wrap-up runs in the reply that closes the quiz (at 6/6, or when the user declines the retry), not after a grading reply that leaves a retry open.
- prototypes: the triad is no longer read as stall-only: it runs before the saturation call even when reactions keep coming, and earlier if they stall.
- notes: `init` creates the log only when it is missing; an existing log is left unchanged.
- brainstorm: when the problem statement is still vague after the one follow-up, or the user skips it, the candidates are generated anyway with the assumed metric and constraints stated above them; the cards keep time-axis order and the impact × effort comparison is a table after them.
- blindspot: the pre-investigation lists are recorded as the loop baseline only when blindspot runs as a loop stage, and only then is the user without a file system told to save them as that baseline; otherwise the lists are restated in the reply.
- buy-in: the 90-second read target applies to the demo section.
- teach-me: before/after comparisons are made per decision axis (the same subject at two contrasting settings), and the user picks from numbered terms.
- loop (scorecard): the offer to add `.unknowns/` to `.gitignore` is made only when it is not already listed.
- unknowns-scout: a caller-requested return shape keeps the **Needs checking** list.
- independent-reviewer: marks each done criterion met, partial or missing, and its report opens with a conformance-and-deviations section (each criterion, or "conformance not judgeable", a verdict per recorded deviation, and unplanned decisions no log entry records), followed by a claim-checks section for the packet's claims. The task message is defined as the caller's packet, and a missing packet field is listed as not verified. Files are read with Read, Grep and Glob; "temporary directory" means `$TMPDIR`, or `/tmp` when it is unset; "a passing test does not confirm a claim" replaces an ambiguous sentence. Not measured with a model (no eval case); two hand-run sessions on a planted missed criterion, before the claim-checks and packet edits, caught it both times and left the repository unchanged.
- loop and the shared reviewer reference: say that the reviewer agent can run tests only when the calling session allows those commands, otherwise it reviews by reading and lists the runs as not verified.
- buy-in: names the reviewer's "verified OK" list by the agent's own name.

### Added

- Claude plugin listing icon: `packaging/icon.png` (512 px square PNG rendered from the OpenAI listing SVG) ships as `.claude-plugin/icon.png` in the Claude plugin and zip only; `tools/package.py` checks it is a square PNG of 512 to 2,048 px under 2 MB. Clears the `ICON_MISSING` warning from `claude plugin validate --strict plugins/unknowns`.

### Evals (developer-only; not in the shipped payload)

- Multi-turn eval cases for blindspot, interview, quiz, and prototypes, run by `evals/run-multiturn.py`: a simulated user answers the questions each skill asks, and a separate judge grades the whole conversation.
- The two single-turn blindspot cases now tell the skill to skip its up-front questions, so they grade the full pass; the asking path is graded by the multi-turn blindspot case. The exact-wording `labels-the-prompt-draft` regex was removed (the llm grader already checks the draft) and a finding-card marker regex added.
- Method-marker regex graders for notes (Observed/Attributed blocks) and plan (weakest part / allowed cost), so a skill that loads and then declines no longer passes those cases on the load alone.
- The one-file plan grader names the document parts it forbids (likelihood-ordered decisions, rollback or blast-radius notes, a weakest-part section) and allows a short list of choices and approval lines.

### Checked

Claude Code 2.1.309, claude-opus-5-5, `evals/run-manual.py` and `evals/run-multiturn.py`, `llm` graders judged by a separate `claude -p`.

- Before the compaction, against 0.10.0 at 10 runs per case per arm, same day, in parallel (Fisher exact): plan size gate 0/10 → 9/10 (p < 0.001); prototypes first reply says the set can grow 3/10 → 10/10 (p = 0.003); loop first reply names its stages 1/10 → 10/10 (en, p < 0.001) and 2/10 → 10/10 (ko, p = 0.001); notes entry fields 0/10 → 10/10 (p < 0.001). A second pair (review fixes vs wording-only build, 10 runs, multi-turn): quiz key hidden 0/10 → 6/10 (p = 0.01); interview four questions per round 4/10 → 9/10 (p = 0.06) and reasons in priority order 1/10 → 5/10 (p = 0.14), not significant.
- The compacted build on its own runs (no comparison arm, by owner decision): the full single-turn suite and the four multi-turn cases at 3 runs each, the failing cells fixed and re-run at 3 runs, then the whole suite once (single-turn 45/49, multi-turn 12/14 before the last fixes).
- Agent routing with the changed descriptions, 36 runs: named calls 12/12, buy-in → independent-reviewer 3/3, generic review and explore requests (English and Korean) 0/18 to an unknowns agent.
- Per-file writing-for-models checks by Claude and Codex on the compacted text, adjudicated against the owner's rules, and Codex diff checks of every edit round.
- `tools/package.py --check`, unit tests, both eval `--verify` runs, and strict plugin and marketplace validation; CI on Ubuntu and Windows.

### Not measured

- The compacted build was not compared with 0.10.0 or with the pre-compaction build; the improvements above were measured on the earlier text and are carried over in substance, re-checked only at 3 runs.
- claude.ai, ChatGPT and mobile behaviour; Codex runs of this build; real Windows use.
- independent-reviewer has no eval case (two hand-run sessions before the compaction).
- The claude.ai upload short descriptions in `scripts/skill-descriptions.json` have never been measured for triggering.
- Known weak cells at release: the Korean blindspot trigger sometimes answers without the skill (3 of 10 runs); interview sometimes asks a no-reason taste question before a higher-radius one, and once let a declined option into the fixed decisions.

## 0.10.0 — 2026-10-27

**Breaking:** deliverables are Markdown in the conversation (no HTML pages), and the plugin ships no hooks. Installed payload: 49 files, about 157 KB (0.9.2 installed the whole repository, 2.0 MB).

### Changed

- Split source from generated output: edit `skills/`, `claude-code/agents/`, `plugin-manifest.json`, and `packaging/`; only `plugins/unknowns/` is installed. The self-hosted marketplace points to that folder.
- Vendor shared loop reference instructions transitively into every skill that uses them; tests compare the copies byte for byte. Every skill also has `agents/openai.yaml` for its OpenAI interface.
- Commit two reproducible ZIP_STORED archives under `releases/`: `know-your-unknowns.zip` for the Claude plugin and `know-your-unknowns-openai.zip` for the OpenAI manifest, skills, and listing SVGs. Both have top folder `unknowns/` and carry the manifest version. The tag workflow checks and attaches them; this branch has not been tagged or released.
- **Breaking: deliverables are Markdown in the conversation.** Removed the shared HTML presentation assets and renderer. Numbered reactions still assemble into a prompt, requirements list, decision summary, or review comment. Task-specific runnable prototypes may still be code written to files.
- Removed both hooks, their launchers and tests, and their environment-variable settings. No executable code ships in either plugin archive. The Ubuntu/Windows hook matrix was replaced by a plain test job; package and strict manifest validation remain.
- The scout has only Read, Grep, Glob, WebFetch, and WebSearch; it returns history questions needing command execution to its caller. The reviewer keeps Bash for tests, lint, and builds under a **prose-only read-only contract**: no edits, commits, dependency installs, or writes outside a temporary directory.
- Replaced Claude-only argument substitution and question-tool names with request prose and conditional tool use. Missing scout sub-agents become labeled passes performed by the assistant; missing independent reviewers use the same packet pasted by the user into a new conversation, and the stage waits for that review. Missing file systems use complete Markdown records that the user can save.
- Updated English and Korean install instructions, repository layout, development commands, and the eval runner's default `plugins/unknowns/` path. Existing invocation and scenario examples remain.
- Replaced the transitional record-deletion workaround: `tools/package.py` may update `plugin-release.json` at an unchanged version only while a non-empty `## [Unreleased]` entry exists. Without one it requires a version bump; `--check` still fails on stale output or a stale digest.

### Skill body changes

| Skill | Portable behavior |
|---|---|
| blindspot | Plain request input, numbered prompt fixes, conditional scout with a read-only inline pass, baseline records without files, and question-tool fallback; seven procedure steps retained. |
| teach-me | Markdown before/after descriptions and named presets replace live presentation controls; unverified sources stay labeled; request draft and closing checkpoint remain. |
| interview | At most four questions per round across smaller tool calls or numbered chat replies; implementation prompt includes deviation logging; priority order and decision table remain. |
| prototypes | Numbered steal/skip reactions, runnable code when files are available, and mockup-state fallbacks; contrast-pole, triad, saturation, and confirmation rules remain. |
| brainstorm | Conditional read-only scout inventory, numbered candidates and impact/effort table, plus logging in implementation prompts; existing-code search and time horizons remain. |
| reference | Supplied-source fallback, conversational sign-off, tests before implementation, and file/execution fallbacks; semantics map and correction gate remain. |
| plan | Question and native-plan-mode fallbacks, Markdown alternatives, and explicit deviation logging; existing approval/change-request permission and decision ordering remain. |
| notes | Skill-driven checks at stage boundaries and before turn end replace reminders; complete Markdown logs replace unavailable files; entry format, escalation, and fold-back remain. |
| quiz | Conversation grading replaces page self-grading; six questions, 6/6 gate, private teach-back key, retry, and scorecard remain; deviation-question condition now precedes question composition. |
| buy-in | Numbered sign-off replies, supplied-evidence fallback, and a labeled read-only review pass without a sub-agent; evidence, limitations, and rollback remain. |
| loop | Ten stages and tracker fields remain; explicit logging and tracker reads replace automatic reminders; missing tools use labeled passes and complete Markdown records. |

### Writing-for-models audit

- Audited **29 source files** using separate read-only, ephemeral Codex checker processes. Four findings were reported and all four quoted passages verified; **three were confirmed and fixed**, and one was rejected after context review because it would have tightened the existing approval policy.
- Fixes moved the quiz's deviation-question condition into question composition, made the scorecard's question heading unconditional while retaining conditional baseline comparison, and bound the no-file-system code/reporting fallback in reference, loop, and plan. The rule-required meaning clarifications are **unmeasured**; a supporting retry-step move was form-only.
- The final independent diff checker returned no findings. The detailed report, per-file scope, adjudications, and inputs/outputs are in the owner's local `kyu-review/wfm/report.md` audit record, outside this repository.
- Trigger phrases, skill descriptions, shared closing offers, and procedure step numbering were retained. This audit is a text review, not a behavior measurement.

The Phase W2 per-file re-audit covers the same 16 instruction sources individually. The brief says 32 findings, but the 16 supplied JSON outputs contain **30 findings**, all verified against frozen commit `e1652fa`; Phase C changed no skill or agent bodies. All supplied findings were adjudicated. None repeats an already-fixed Phase W finding.

| Audit | Found | Confirmed | Fixed | Rejected |
|---|---:|---:|---:|---:|
| Phase W | 4 | 3 | 3 | 1 |
| Phase W2 supplied checker findings | 30 | 27 | 27 | 3 |
| Phase W2 owner-added escalation wording (reversed in R) | 1 | 0 | 0 | 1 |
| Phase W2 diff review, unique findings | 3 | 2 | 2 | 1 |
| **W + W2 after the R ruling** | **38** | **32** | **32** | **6** |

- W2 binds investigation constraints, interview option notes, review execution limits, scout output overrides, quiz preparation/grading conditions, scorecard eligibility/answer rules, and judging criteria to their actions. It numbers the existing brainstorm selection, buy-in prerequisites/review, and mockup procedures. Shared reply instructions consistently say Markdown in the conversation.
- W2 clarifies that small fixes have no tracker/checkpoints, the plan size gate counts files created or modified, verification/risk/rollback applies to plan items, final implementation of prototypes requires the combined-option confirmation, and read-only records use complete Markdown updates. Reference keeps its semantics map for port/transform work and also requires it before any reference-based implementation, matching its Iron Rule.
- W2 initially narrowed the escalation scope to data loss. Phase R reverses that item under the owner's final ruling: all escalation instructions now use **architecture, user-visible behavior, data, or security**, preserving main loop's broader permission boundary. The rejected column above includes this one owner-reversed W2 item; the remaining five rejections retain their original adjudications.
- The retained scope and execution-order clarifications in W2 are **meaning-changing and unmeasured**; the escalation decision has been reversed. The report classifies every fix; naming, duplicate removal and mockup numbering are form-only. Existing explicit approval rules and stage-specific question/logging reminders were preserved when three initial checker suggestions would have changed them without a rule requiring it.
- The fresh diff review against `0ac7d82` found two confirmed regressions, both fixed. The second and final round reported only a repeat of the rejected prototype-permission objection; no confirmed finding remains. This repeat is not double-counted in the totals. Per-file findings, quote verification, adjudications, and classifications are recorded in the owner's local `kyu-review/wfm2/report.md` audit record, outside this repository.

### Independent review fixes — Phase R

Reproduced and fixed the review's seven findings plus the owner's Windows CI ruling. The W2 escalation item is reversed rather than counted as a retained audit fix.

| Audit scope | Found | Confirmed | Fixed | Rejected |
|---|---:|---:|---:|---:|
| W + W2 after reversal | 38 | 32 | 32 | 6 |
| R review findings and CI ruling | 8 | 8 | 8 | 0 |
| R writing-for-models diff review | 1 | 0 | 0 | 1 |
| **Combined** | **47** | **40** | **40** | **7** |

- Restore the no-sub-agent independent review substitute: hand the same packet to the user for a new conversation and keep the stage pending until that review returns. Scout fallbacks still run a labeled pass locally.
- Restore escalation for architecture, user-visible behavior, **data**, or security in every implementation prompt, notes Todo/exclusion/escalation rule, reviewer contract and README summary. This owner-authorized reversal restores main's broader scope; it is meaning-changing and unmeasured.
- Replace both unshipped value-contract pointers in the scorecard with the required value signal, provisional thresholds and baseline/ratio interpretation. Validate file paths in every generated skill Markdown file, with an explicit allow-list for user-project records; negative tests cover missing vendored-reference paths.
- Include the entire canonical plugin manifest in the content digest except `version`. A manifest-only mutation without Unreleased notes is rejected; version/JSON-format-only changes keep the same digest.
- Cite official Claude guidance for account-based installation while keeping this plugin's mobile/desktop sync unverified. Document the ChatGPT zip/account/local-desktop routes, labeled not yet owner-checked for this plugin; uploads need to be replaced for updates.
- Move missing-tool fallbacks after the affected instructions and reasons after the fallbacks in blindspot, plan and reference; inspect all eleven skill bodies for the same ordering pattern.
- Add Ubuntu/Windows developer-tooling CI coverage: package build/check, unit tests, and both individual-skill helper targets. The new Windows job is configured, not observed passing.
- The independent review, reproduction evidence and findings-to-fix table are in the owner's local `kyu-review/review/` records outside the repository. The fresh writing-for-models diff check uses `4bb7d86` as its base; prompt scope/order changes remain unmeasured. It returned one quote-verified suggestion to narrow data; rejected because it contradicts the owner's explicit broader-data ruling. No confirmed finding remains.

### Writing-for-models Claude-checked round — Phase WC

The model-read files were last written by Codex, so this round used Claude as the checker: one `claude -p --tools ''` process per file on frozen `d07db74`, 17 files. They reported 118 findings. One had a wrong quote and was dropped; the other 117 were adjudicated in context. The diff check went back to Codex.

| Audit scope | Found | Confirmed | Fixed | Rejected |
|---|---:|---:|---:|---:|
| Combined through Phase R | 47 | 40 | 40 | 7 |
| WC Claude per-file findings (quote ok) | 117 | 35 | 34 | 82 |
| WC Codex diff review, two rounds | 0 | 0 | 0 | 0 |
| **Combined** | **164** | **75** | **74** | **89** |

- Of the 35 confirmed, 25 came from this branch and 10 were already on `main`. Nine of the branch findings are one defect: the shared output sentence still said "with the same structure" after Phase B removed the HTML page it pointed at. It is fixed once in all nine copies and in its test guard.
- One confirmed finding is not fixed. The reviewer cannot see whether `/code-review` and `/security-review` are available, so the condition on its secondary pass cannot be checked with its tools. It is logged as a Todo for human because any fix decides when that pass runs.
- Owner ruling (a) resolves that finding: the reviewer always runs its own secondary pass (error handling, security, performance, needless complexity), with no condition on `/code-review` or `/security-review` and no new packet field. Meaning-changing and unmeasured.
- 25 fixes are form only (names, antecedents, list names in the scout output). Nine change meaning and are **unmeasured**: blindspot opens its output with the three lists before the contrast; interview investigates before it lists gaps and uses step 5's radius names; loop writes the tracker once the tier is known and records the tier there; notes always appends (creating the file if missing) and drops the chat-summary permission when there is no file system; buy-in hands the reviewer the surfaces packet; quiz runs the wrap-up in the same reply.
- 82 findings were rejected because the text was already right in context, the fix would change a method step, number, shared block or owner ruling, or it only restyled. Owner rulings, frontmatter, trigger phrases, step numbering and shared blocks are unchanged. Per-item adjudications are in the owner's local `kyu-review/wfm-claude/report.md`.

### Checked

- **Claude Code** 2.1.309, claude-opus-5-5, isolated config with the account's synced plugins disabled; cases from `evals/` run with `evals/run-manual.py`, `llm` graders judged by a separate arm-blind `claude -p`. 3–6 runs per cell, so these rule out large regressions only; no improvement is claimed.
  - Triggers: all 22 cases fired the intended skill (a single-run Korean blindspot miss fired 6/6 on 0.9.2 and on this build when rerun).
  - Negatives: the how-to, interval-loop, UI-options and vocabulary cases fired no wrong unknowns skill and passed their outcome graders (12/12). The one-file plan case loads `unknowns:plan`; it defers to plan mode 1/3 (0.9.2: 0/3).
  - Behaviour, 0.9.2 vs this build run side by side: prototypes contrast pole 6/6 vs 6/6, saturation offer 1/6 vs 1/6; blindspot status labels 2/3 vs 3/3, nothing-confirmed-unseen 1/3 vs 2/3; notes required fields 1/3 vs 1/3; loop stages 0/3 vs 0/3 (en), 0/3 vs 1/3 (ko). An earlier batch on the pre-WC build: plan done criteria first 2/3 vs 3/3, interview at most four questions 2/3 vs 3/3.
- **Codex CLI** 0.164.0, isolated HOME: all 11 skills listed; 22/22 trigger cases loaded the intended skill (each run stopped at the first skill read); the plan behaviour case delivered its done criteria in the chat where 0.9.2 linked an HTML file.
- **CI** on the release branch: unit tests on ubuntu-latest and windows-latest, strict plugin and marketplace validation.

### Not measured

- Routing and behaviour on Claude web/desktop/mobile and ChatGPT web/mobile/desktop; multi-turn behaviour on any surface (the eval cases are single-turn); the reviewer's always-on secondary pass.
- Uploads of the rebuilt Claude archive to claude.ai or the rebuilt OpenAI archive to ChatGPT.
- Mobile skill loading and cross-device/account synchronization.
- Live A/B measurements of the Phase W and W2 writing-for-models fixes; prior trigger and behavior results describe older snapshots. W2 scope and execution-order clarifications, and the nine WC meaning changes, are not measured improvements. An optional W2 behavior smoke was stopped after repeated 60-second timeouts; its no-plugin arm also loaded an installed unknowns skill, so it supplies no valid baseline.

## 0.9.2 — 2026-10-22

Both agents, `independent-reviewer` and `unknowns-scout`, now run only when you name them
or an unknowns skill calls them. Other review or research workflows no longer pick them
up, and an unnamed "independent review" or "investigate first" request no longer reaches
them either. Release steps per `docs/open-questions.md` A4 are done the same day as the
merge, at tag `unknowns--v0.9.2`.

### Fixed

- **`agents/independent-reviewer.md` description**: a workflow asking for an
  "independent" review or an isolated reviewer subagent could pick this agent. It
  happened in 2 of 32 review-type dispatches in the owner's session history: SuperClaude's
  `/sc:review`, whose own flow names its `self-review` agent, and a vault skill asking a
  subagent to compare note claims. The description dropped "Use proactively before
  merging…" and `Triggers: "independent review before merge"`. It now says to spawn the
  agent only when the user names it or an unknowns skill (loop, buy-in) calls for it, and
  that any other review request, or another workflow's reviewer or subagent, goes to the
  agent that workflow names, or general-purpose. The agent body is unchanged.
- **`agents/unknowns-scout.md` description**: the same pattern ("Use proactively BEFORE
  implementation…", `Triggers: "blind-spot pass", "what am I missing"`) is replaced by the
  same rule: by name, or from blindspot or brainstorm; other exploring or research
  subagent requests go to the workflow's own agent, Explore, or general-purpose. The
  trigger phrases stay with the blindspot skill. No unintended scout call was found in the
  session history; this closes the same risk before it shows. The agent body is unchanged.
- README (both languages): the agent example "Run an independent verification" /
  "독립 검증 돌려줘" no longer reaches the reviewer, so it names the agent; both agent
  sections say when each agent runs.

### Added

- `tests/test_agent_descriptions.py`: both agent descriptions must not say "proactively"
  or carry `Triggers:`, and must keep the by-name rule.

### Checked

Opus 5.5 (`claude-opus-5-5`), base `main` and this change run side by side from frozen
worktrees with the owner's install set (dia, design, SuperClaude at user level; the small
test repository also carries a project-level SuperClaude install). Agent calls were
recorded and denied by a probe hook so no subagent ran. A run passes a "not unknowns" cell
when no unknowns skill or agent appears anywhere in it. The `independent-reviewer` runs
used Claude Code 2.1.307.
Details and harness: `docs/features/agent-collision/`.

- `independent-reviewer`, review requests that do not name it (three cells, 10 runs
  each): picked in 21 of 30 base runs and 0 of 30 with this change (English "independent
  review before I merge" 10/10 → 0/10, p = 1.1e-5; Korean 9/10 → 0/10, p = 1.2e-4; "spawn
  one subagent to check the README" 2/10 → 0/10, p = 0.47). Seven of the 30 change-arm
  runs went through `/sc:review` and hit the turn limit before choosing a reviewer. The
  independent review re-ran the two main cells at a 20-turn limit, 5 runs per arm:
  20/20 → 0/20; with this change, runs that chose a reviewer after `/sc:review` took
  `self-review` or general-purpose, never the unknowns agent. Without SuperClaude the same
  requests went to general-purpose (English) or a direct answer (Korean).
- `independent-reviewer` by name: 10/10 → 10/10 in Korean and in English. Loop stage 8
  from `/unknowns:loop resume`: 8/10 → 10/10 (the two base misses stopped on permission
  prompts before stage 8). With permissions granted, `/unknowns:loop resume` at stage 8
  5/5 → 5/5 and `/unknowns:buy-in` 5/5 → 5/5.
- `unknowns-scout`, re-run on Opus 5.5 with `--model` pinned (Claude Code 2.1.308, the
  access token passed as an environment variable, 10 runs per cell). English "have a
  subagent investigate the codebase for risks first" picked the scout in 10/10 base runs
  and 0/10 with this change, both in the small test repository and in a shallow clone of
  `pallets/click` that has no project-level SuperClaude (20/20 → 0/20, p = 1.1e-5 per
  cell); the change sent them to general-purpose. Korean "investigate the codebase with a
  subagent" and "explore the repository structure" requests went to Explore (with one or
  two general-purpose runs), and a library-research request to SuperClaude's
  `deep-researcher` (one change-arm run: general-purpose), in both arms. By name: 20/20 →
  20/20. `/unknowns:blindspot` on the whole click repository: 20/20 → 20/20. A first
  scout batch ran on Sonnet 5.5 by mistake (the token path defaulted to it); it pointed
  the same way (unnamed English requests 20/20 → 0/20, by name 20/20 → 20/20, blindspot
  17/20 → 16/20, the misses read the files without the scout).
- `python3 -m unittest discover -s tests`, both `claude plugin validate --strict` forms,
  `evals/run-manual.py --verify`; two independent review passes, both "ship with fixes"
  (the second covered the scout change), with every fix in this entry.

Single-turn screens before the change (base only, 3 runs per cell: brainstorm, review,
plan, quiz, interview, notes and reference wording with dia, design or SuperClaude next to
unknowns) found no unintended unknowns skill call. Generic brainstorm requests went to
`dia:dia-brainstorm` or a direct answer, and `/sc:brainstorm` typed as a command ran
without any unknowns skill. No skill description changed.

### Not verified

- claude.ai, the desktop app and mobile, where skill names show without the plugin
  prefix. The brainstorm collision the owner reported was not reproduced in Claude Code
  and is not covered by this measurement.
- The brainstorm skill's optional scout call: it searched the code itself in every run of
  both arms, so whether it still reaches the scout after this change was not observed.
- Routing in the middle of a long multi-turn workflow. Both real cases were
  mid-workflow; the probes are single requests, and the base arm never reproduced the
  choice made inside `/sc:review` (base picked the agent at the top level instead).

## 0.9.1 — 2026-10-18

The hooks now run on Windows without a `python3` alias. Release steps per
`docs/open-questions.md` A4 are done the same day as the merge, at tag
`unknowns--v0.9.1`.

### Changed

- **`hooks/hooks.json`**: every handler is one shell string instead of exec form
  (`"command": "python3"` + `args`). Exec form has to name one interpreter, and Windows
  usually has no `python3`, or has the Microsoft Store stub that exits 9009. Claude Code
  runs a shell string with `sh -c` on Linux and macOS, Git Bash on Windows, and PowerShell
  on Windows without Git Bash, so the string is a sh/PowerShell polyglot: each shell runs
  its own half and reads the other half as a comment.
  - Linux and macOS: `exec python3 "<script>" <args>`, the same process, argv,
    stdout/stderr and script exit codes as before.
  - Windows (Git Bash or PowerShell): the first of `python3`, `python` and `py -3` that
    passes a one-line Python 3 check runs the script, so a Python 2 `python` is skipped.
  - Exit codes the PreToolUse guard relies on are unchanged: a deny is JSON on exit 0 and
    a missing script exits 2 and blocks the call (A7). No interpreter is still a
    non-blocking error (an exit code other than 2): on Windows the hook prints
    `[unknowns] no working Python 3 found`; on Linux and macOS the shell reports
    `exec: python3: not found` (exit 127), where exec form reported
    `Executable not found in $PATH`.
  - The PreToolUse guard sets `"onFailure": "continue"` (Claude Code 2.1.295+). The hooks
    reference says a failing shell-form PreToolUse hook on Windows without Git Bash can
    block the call when `onFailure` is unset; with it, a failure or timeout lets the call
    through as exec form did, and exit 2 still blocks.
- README "Platforms" and "Requirements" rows (both languages) drop the alias advice.
- CI's hook-tests job installs the Claude Code CLI on both systems.

### Fixed

- `hooks/scripts/agent_readonly_guard.py`: the `"\;"` literal (a `SyntaxWarning` on every
  guard run under Python 3.12+) is now `"\\;"`, the same string.

### Added

- **`tests/test_hook_launcher.py`**: pins every handler to the one launcher, then runs
  each handler's string through every shell on the machine (sh/bash/dash, Git Bash,
  Windows PowerShell, pwsh): SessionStart marker, guard deny with stdin passed through, a
  plugin path with a space and `$`, exit 2 on a missing script, a non-blocking exit with
  no Python, fallback past a `python3` that fails and (POSIX shells) past a Python 2
  `python`. It also runs the real `claude --init-only`, which fires SessionStart from
  hooks.json without logging in, in the default shell and pinned to PowerShell, from a
  plugin path holding a space and a literal `$HOME`.

### Checked

- Locally (Linux arm64, Claude Code 2.1.301, pwsh 7.6.7): the full suite, both
  `claude plugin validate --strict` forms, `evals/run-manual.py --verify`; a live
  `claude -p --plugin-dir .` session fired SessionStart (marker in context), PreToolUse
  (the scout's `rm` denied) and Stop through the new strings. After the review fixes
  (Python 3 probe, `onFailure`), a second live session ran SessionStart, PreToolUse (the
  scout's `touch` outside a temp dir denied by the guard's JSON, file not created) and
  Stop through the final strings.
- Independent review (separate reviewer run, read-only on the repo): one blocker (the
  no-interpreter message was claimed for Linux and macOS too) and one should-fix
  (`onFailure`), both fixed here, plus nits N1–N3 fixed; N4 (zsh word splitting, never
  used by Claude Code) and N5 (CI installs Claude Code unpinned) left as they are. A second
  pass on the fixes gave `VERDICT: ship`; its three nits (the default-shell Claude Code
  test now runs from the `plug in $HOME` copy too, two wording fixes) are in.

### Not verified

- An interactive Claude Code session on Windows: on windows-latest the hooks run through
  `claude --init-only` (SessionStart only) and the shells directly; PreToolUse, PostToolUse
  and Stop never fire inside Claude Code there. macOS was not run.
- Through Claude Code on Windows: Windows PowerShell 5.1 (the pinned-PowerShell test gets
  pwsh 7 on windows-latest), the PowerShell default without Git Bash (where `onFailure`
  matters), and the real Microsoft Store stub (CI's fallback test uses a stand-in, and
  windows-latest has a working `python3`).
- `onFailure` on Claude Code older than 2.1.295.

## 0.9.0 — 2026-10-18

Pages are now built from a shared template, so the model writes only their content. On
Opus 5.5, a page-producing run used 30% fewer output tokens on average (median −16% to
−34% per case, each p < 0.03) and cost 26% less in total (−10% to −33% per case,
significant in two of three). Measured on 3 skills × 6 runs, this release and main run
side by side with the same harness:
`docs/features/html-page-template/README.md`.

Release steps per `docs/open-questions.md` A4 are done the same day as the last merge, at
tag `unknowns--v0.9.0`.

### Added

- **Page template**: `skills/loop/assets/page.css` (light/dark tokens, focus, reduced
  motion for CSS, layout classes) and `skills/loop/assets/page.js` (reply assembly from
  `data-reply` controls: checkboxes, chip rows, self-graded questions with a score, and
  text, slider and select inputs once they differ from their opening value; copy button).
- **`skills/loop/scripts/render-page.py`**: wraps a fragment in place with the template
  inlined (`--artifact` for the Artifact tool form, no document wrapper). It refuses the
  common external-resource forms, a missing `<title>`, and a missing, empty, nested or
  duplicated reply section. Python 3.7+, standard library only.
- `tests/test_render_page.py`.

### Changed

- **`output-routing.md` §3–§4** describe the fragment + script workflow and the full
  control vocabulary, and say the template sources need not be read. The template is found
  relative to the reference file itself, because `${CLAUDE_PLUGIN_ROOT}` is not substituted
  in reference files and is not set in the shell. With no shell or no Python, the model
  inlines the two asset files itself, with `page.js` after the content.
- Page rules: the theme, focus, CSS reduced-motion and JS-off reply rules now live in the
  template. The rest is restated: a new **Self-contained** block (inline all CSS and JS,
  no separate files), the language rule now covers the reply labels and `--lang`, custom
  colors keep the per-theme rule, and custom JS animation must respect reduced motion.
  The look rules are unchanged.
- The nine skills that produce pages point at the template with one shared sentence in
  place of their `Details:` line (listed in `.claude/rules/skill-writing.md` rule 11).
- `scripts/build-skill-zips.py` bundles the template into every standalone skill that uses
  `output-routing.md`.

### Windows

- The render command quotes both paths and falls back to `py -3` or `python` when there
  is no `python3`. The script survives a cp1252/cp949 console, reads a BOM, and writes LF
  on every OS. Covered by unit tests that CI runs on windows-latest; not run inside Claude
  Code on Windows.

### Checked

- Two independent reviews (a separate agent profile) of the branch; every blocker and
  should-fix finding was fixed. Headless-Chromium checks of the template's controls, theme
  and JS-off reply.
- `behavior-*` evals, 3 runs, mechanical graders: main 33/33, this
  release 31/33. Both misses are blindspot asking its intake questions before writing the
  prompt draft; a side-by-side 10-run rerun of that grader gave 8/10 on main and 8/10 here.

### Not measured

- The other six page-producing skills, the Artifact tool rung (headless runs have no
  Artifact tool), standalone skill zips on Desktop/web, and the `llm` graders of the
  `behavior-*` cases.

## 0.8.4 — 2026-10-14

Skill and agent text was rewritten under new writing rules, and the inconsistencies that
pass found were decided and applied, so some skill behavior changes (PR #12, and the loop
alignment in the release PR). Checked with unit tests, `run-manual.py --verify`,
`claude plugin validate` and an independent review against the previous text. **Model-run
evals were not run for this release.**

Release steps per `docs/open-questions.md` A4 are done the same day as the last merge, at
tag `unknowns--v0.8.4`.

### Added

- **`.claude/rules/skill-writing.md`**: 16 rules for writing skill and agent text, loaded
  when `skills/**` or `agents/**` is edited. Development only; not part of the payload.

### Changed

- **Skill and agent bodies rewritten** to follow those rules: one action per step, tables
  for parallel cases, shared names and shared sentences copied word for word. Frontmatter
  is byte-identical, so triggers are unchanged.
- **Finding kinds and statuses unified.** The scout follows blindspot's definitions; History
  is "a past attempt, revert or hairy dead end that explains why the code looks this way"
  in both; *inferred* may rest on how such systems usually work, saying which. The scout's
  column is "Why it bites". Both READMEs updated.
- **blindspot / teach-me order.** teach-me first when the user cannot yet describe the task;
  otherwise blindspot first, with its "cannot judge" list handed to teach-me. The same
  sentence is in blindspot, teach-me and loop step 2. blindspot checks the user's
  assumptions first, in the given sources first, and passes them to the scout.
- **One output ladder in nine skills**, including the rule to end every rung with the
  assembled reply in chat (previously in three skill bodies and `output-routing.md`).
- **Smaller alignments:** the fresh-thread review packet in `surfaces.md` gains the claims
  list; quiz says so when loop already captured the scorecard row; loop's closing-offer
  table lists reference's real options; `independent-reviewer` reports unplanned decisions
  whether or not `IMPLEMENTATION_NOTES.md` exists.

## 0.8.3 — 2026-10-10

A text-only release: no skill, agent or hook behavior changes. The plugin's own text was
tightened into complete, shorter sentences and checked against the eval suite on Sonnet
5.5 before and after (PR #9). The author fix from PR #8 ships with it.

Release steps per `docs/open-questions.md` A4 are done the same day as the last merge, at
tag `unknowns--v0.8.3`.

### Changed

- **Plugin text tightened without changing behavior or triggers.** Agent bodies (2), skill
  bodies (11 including loop), the three loop references, the brainstorm description and
  five README.md passages now use complete, shorter sentences. Table separator rows in
  the agents, scorecard template and both READMEs use `---` per cell. Hook messages and
  manifest descriptions were already concise and are unchanged. On Sonnet 5.5, the
  `behavior-*` evals match the baseline grader for grader (no regression), and brainstorm's
  trigger cases fire 3/3 (en, ko) with its neg case 0/3. Results:
  `docs/features/concise-plugin-text/06-results.md`.
- **`plugin.json` names the author `ajitta`** (was `chosh`, same email), matching the
  owner in `marketplace.json` and the copyright line in LICENSE and NOTICE.

## 0.8.2 — 2026-10-02

From a blind-spot review of 0.8.1 that checked the plugin's assumptions against the
current Claude Code docs and the literature the skills cite, then had its own draft
re-checked by a separate agent (which retracted several claims before any code changed).
A second pass then removed text from the skill bodies that the model does not act on.

Release steps per `docs/open-questions.md` A4 are done the same day as the last merge, at
tag `unknowns--v0.8.2`.

### Fixed

- **Cross-skill paths did not resolve from the user's project.** SKILL.md bodies pointed at
  `skills/loop/references/*.md`, a path relative to the plugin root, while the model works
  in the user's project directory. They now write `${CLAUDE_PLUGIN_ROOT}/skills/loop/...`,
  which Claude Code substitutes in plugin skill content. Reference files, which are read
  with the Read tool and get no substitution, name their siblings as "in this folder".
  `build-skill-zips.py` strips the prefix for standalone zips; a test fails if a SKILL.md
  body uses the bare path or a zip keeps the prefix.
- **"No reminder hook in this session" was undetectable.** The notes skill told the model
  to self-check when hooks do not run, and named the surfaces where they do — against
  `surfaces.md`'s own rule of keying on what the session has, not on its name. A model
  cannot see whether hooks run. SessionStart now fires on every source: on
  startup/resume/clear/fork it emits `[unknowns] hooks active`, only while a reminder is
  still to come (opted-in project, threshold > 0, state persists, the once-per-session
  reminder not yet spent — a resumed session whose reminder fired gets no marker); after
  compaction it restates the rule, re-arms, and carries the marker. The notes skill and `surfaces.md` key on that line.
- **Double stops inside the loop.** Each stage skill's closing offer (proceed / edit /
  stop, or approve / revise) was followed by the loop's stage checkpoint — a dozen or more
  user stops in one medium-tier run, counted from the skill texts. The loop now folds the skill's options into its single
  checkpoint, and each such skill says so, so the rule survives if compaction drops the
  loop's own text.

- **Stale description-length note.** `scripts/skill-descriptions.json`, `build-skill-zips.py`
  and `tests/test_skill_descriptions.py` said the SKILL.md descriptions run 248-283
  characters; blindspot's has been 383 since 0.7.1. `docs/trigger-matrix.md`'s length column
  and total are re-measured.

### Changed

- **Three skills now carry the mechanism `docs/value-contract.md` credits them with.**
  The contract argued that prototypes, interview and quiz rest on established elicitation
  methods and only need to preserve them; a text comparison found each only partly did.
  - `prototypes`: adds a **triad** step (which two of three are alike, and how the third
    differs), then places every option on the construct it yields — Kelly's elicitation,
    where steal/skip only harvests constructs the user can already name.
  - `quiz`: one of the six questions is now a **teach-back** in plain text (5 multiple
    choice as 4 + 1, plus one "explain it in your own words"), graded against points fixed
    before reading the answer. The checklist says "quiz passed", marked self-graded when
    the page graded it, instead of "understanding verified".
  - `interview`: an architecture or data answer given without a reason gets one "why"
    follow-up next round (laddering); follow-ups count toward the 4 per round.
  The contract records the check; B7 (efficacy) stays open.
- **The loop tracker says whether it is finished.** `.unknowns/loop.json` gains `status`
  (`active` / `done` / `stopped`). After a compaction the hook puts one line pointing back
  at an `active` loop into Claude's context: compaction re-attaches invoked skills
  most-recent-first within a fixed budget, so the loop skill — invoked first — is the one
  most likely dropped, along with its own "re-invoke me after compaction" line. The hint
  does not depend on the notes reminder (it still appears with the threshold at 0), and a
  file without `status` gets none, since it may be a finished loop. The loop writes the
  tracker as `active` before its first exchange, `resume` sets it back to `active`, and a
  bare `/unknowns:loop` offers to resume only an `active` tracker, confirming first since an
  abandoned loop stays `active` until someone says stop.
- **`independent-reviewer` no longer preloads the notes skill.** The `skills:` field
  injects the whole body, including instructions this read-only agent cannot follow
  (append to the file, stop and ask the user — sub-agents have no AskUserQuestion). The
  criteria it judges deviations by are now written into its own item 2.
- **Small-fix tier states its done criteria.** The scale-down list said "notes only, no
  loop" for a small fix and "step 1 runs in every tier" two lines later; a small fix now
  states the done criteria in one line, as `plan`'s size gate already did.
- **Scorecard rows can be anchored.** blindspot keeps the user's pre-investigation lists
  (sure of / assuming / cannot judge) verbatim, and the scorecard shows findings against
  them before asking "did you learn something?", recording `compared` or `none` in a new
  last column, **Baseline** — a recollection of what one already knew drifts once the
  answer has been seen. Columns are only ever appended, so an existing scorecard migrates
  by extending its header; `docs/value-contract.md` now reports `compared` rows separately.
- **The teach-back key predates the answer.** quiz writes the grading points to
  `.unknowns/<date>-quiz-<slug>-key.md` before asking and quotes the file when grading.
- **notes' "Why the split" cites what the studies measured.** Fox, Ericsson & Best (2011)
  measured whether people speaking during a task change the task, not whether an
  after-the-fact log is accurate; the paragraph now leans on Turpin et al. (2023) and
  Nisbett & Wilson (1977) for "a stated reason is a hypothesis", and keeps Fox as a caution.
- **Standalone skill builds.** References are bundled transitively, so the six zips whose
  `output-routing.md` points at `surfaces.md` now contain it. `--target local` builds plain
  folders for a Claude Code `.claude/skills/` copy that keep the full description,
  `argument-hint` and `$ARGUMENTS`, and drop the plugin namespace from agent names
  (`unknowns:unknowns-scout` → `unknowns-scout`) to match agents copied into
  `.claude/agents/`; the README's copy-a-skill section now uses it. Siblings a reference
  names by full plugin path are bundled too, not only bare names.
- **blindspot cards sort by likelihood × blast radius** — how likely this task is to hit a
  finding, times how much breaks if it does. "Importance × impact" named one quantity
  twice and was, per `talk-source.md`, never in the source.
- **brainstorm asks the scout for an inventory**, not its default blindspot cards and
  prompt draft: one row per existing mechanism, with what is missing to wire it in. The
  scout now follows a return shape the packet asks for.
- **"Todo for human" vs stop-and-ask.** A Todo is now only a call that changes no
  architecture, user-visible behavior, data or security; anything touching those
  escalates, and when unsure, escalate.
- **The Stop check sees notes written outside Edit/Write.** An append through Bash
  (`cat >> IMPLEMENTATION_NOTES.md`) fired no Edit/Write event, so Stop said the notes were
  never updated. The hook now records the notes file as it stood at the session's first
  counted edit (absent, or its modification time) and at Stop counts it as touched if it
  has since appeared or its modification time changed. It compares the file with itself,
  never with the hook's clock, so a file stamped in the future (network share, `cp -p` from
  a fast clock) is not mistaken for one written now.
- **Crowded skill listings.** `evals/run-manual.py --crowd N` loads a generated plugin of
  N filler skills first, in a fresh, empty `CLAUDE_CONFIG_DIR` per run (usage counts,
  which decide whose descriptions survive, live in the config and headless runs update
  them; synced or managed plugins may still load); `--budget-fraction F` forces an
  overflow. Each crowd run records what the CLI logged about the listing, and a run that
  cannot start is reported as FAILED rather than scored as a miss. Forced overflow (logged
  by the CLI; that every unknowns description was dropped is a probe run's self-report):
  9 of 11 English trigger cases still fired, notes and blindspot did not (one run per
  case; `docs/trigger-eval-crowd-2026-09-30.md`). The README's "skills don't
  trigger" answer explains the budget and `skillListingBudgetFraction`.
- **Skill bodies carry instructions, not their justification.** An invoked body stays in
  context for the rest of the session, so rationale written for maintainers is paid for on
  every later request. notes' "Why the split" and teach-me's "Limits" keep every rule and
  drop the citations (Turpin, Nisbett & Wilson, Fox, Collins), which move to
  `docs/value-contract.md`. `output-routing.md` drops the reaction-control table — each of
  the nine skill bodies already states its own control. prototypes keeps its Kelly text:
  with it trimmed, the saturation check (offer more options) appeared in 3 of 6
  `behavior-prototypes-asks-contrast-on-skip` runs against 5 of 5 on the previous text.
  `hooks.json`'s description is one sentence pointing at the README instead of a third copy
  of the hook variables. Measured on the files: about 430 fewer tokens across the six bodies
  a medium loop invokes (more once `${CLAUDE_PLUGIN_ROOT}` expands), about 200 fewer when
  `output-routing.md` is read.

### Removed

- **`Origin:` lines in the eleven skill bodies.** They pointed at a provenance file the model
  had no reason to read. The mapping stays in `talk-source.md` and the README's "Skills at a
  glance" table.
- **loop's "Operating principles (compressed)"**, a third summary of the ten steps above it.
- **`talk-source.md` moved from `skills/loop/references/` to `docs/`.** It is provenance, not
  procedure, and nothing in `skills/` names it any more; the plugin payload is 16 KB smaller.
  `build-skill-zips.py` loses its talk-source special case (and the standalone zips their
  GitHub link to it).

## 0.8.1 — 2026-09-28

Fixes from an outside review of 0.8.0, then a second pass after the plugin's own
`independent-reviewer` checked the first draft of this release. Each defect below was
reproduced before it was fixed; the guard ones by piping the command into the hook exactly
as Claude Code does.

Release steps per `docs/open-questions.md` A4 are done the same day as the merge, at tag
`unknowns--v0.8.1`.

### Fixed

- **The sub-agent read-only guard let writes through.** Two probes of 0.8.0 (15 commands,
  then 10 more) found 21 writes allowed; `python3 -c` was also allowed, by design. The
  independent review of the first fix then found neighbouring forms of the same classes
  (parenthesised awk `print`, sed address shapes, clustered `sort -uo`, `cp -t`, `xargs -i`,
  `env -S`, `/tmp/../`), and those are fixed here too.
  - `unknowns-scout`: commands on its read allowlist still wrote through their options or
    program text — `awk '{print > "f"}'`, `sed 'w f'`, `sort -o`, `yq -i`, `find -fprint`,
    `tree -o`, `uniq in out`, `git diff --output=`. `git fetch` and `git notes add` changed
    `.git`. All are now denied; the read forms (`awk '{print $1}'`, `sed -n '1,40p'`,
    `sort -u`, `git notes list`) stay allowed. awk programs are read by a small lexer that
    blanks string and regex literals, and sed scripts by a scanner rather than a regex —
    the regex in the first draft took 5 s on a 1,000-character argument, which is the
    hook's timeout.
  - `independent-reviewer`: the guard was a deny list, so a wrapper or an unlisted command
    got past it — `xargs rm`, `bash -c 'rm -rf src'`, `env rm`, `cp /dev/null src/x`,
    `touch src/x`. Wrappers (`xargs`, `env` including `-S`, `command`, `timeout`, `nice`,
    `time`, `sh -c`, `eval`, `find -exec`) are now unwrapped and the inner command checked;
    nesting deeper than six levels is denied rather than trusted. `cp`, `touch`, `mkdir`,
    `ln`, `chmod` and friends are denied unless every target — including a `-t` /
    `--target-directory` value — is under a temp directory, so the scratch files
    `agents/independent-reviewer.md` prescribes still work. A variable set from
    `$(mktemp)` in the same command counts as temp; a path with a `..` segment never does.
    `patch` needs `--dry-run`; `git format-patch` needs `--stdout` or a temp output
    directory.
  - Both agents: `git -c alias.x='!cmd'` (and other `-c` keys that run a program, such as
    `core.fsmonitor` or `*.textconv`) could run any command; it is now denied. `git remote
    update`, `archive -o`, `read-tree`, `checkout-index`, `clone`, `merge-file`, `hash-object
    -w`, `symbolic-ref <name> <ref>`, `sparse-checkout set`, `reflog expire`, `bundle
    create`, `replace`, `update-index` and the state-changing `bisect` verbs join the write
    lists. `git -c core.pager=cat`, `bisect log` and `reflog` stay allowed.
  - Still not inspected, and now said so in the README: scripts the agent runs
    (`python3 -c`, a test file, `bash script.sh`). The guard remains a guard rail, not a
    sandbox.
- **`output-routing.md` pointed at an Artifact action that does not exist.** Rung 1 told
  the model to collect comments with `action: comments`; the Artifact tool has no such
  action. Comments go through the separate `ArtifactComments` tool, and the text now says so.
- **`surfaces.md` read like a detection rule.** A Claude app task running in a cloud
  workspace starts from web or desktop yet carries the Agent tool and this plugin's agents,
  which the "Desktop / web chat: no sub-agents" column contradicts. The table is now marked
  as defaults, with the tool list as the deciding signal — which is what every substitute
  was already keyed to.
- Text left over from earlier edits: `reference` still named `/notes` for copied installs
  (0.7.0 removed slash commands from skill bodies); "the the **buy-in**" in `notes`; "a the
  **loop**" in `quiz`.

### Added

- Guard tests for every bypass above, each paired with the read forms that must stay
  allowed, and one for a long sed argument (`tests/test_agent_readonly_guard.py`, 24 → 41
  tests).

## 0.8.0 — 2026-09-25

The six gaps `docs/protocol-alignment.md` found against the human-AI collaboration protocol
(G1–G6), now in the skill bodies. The plugin still asks "do you understand the result?" and
now also asks "is the result right?". The decisions come from that document's decision
table. What changed from its plan is in its new "집행 기록" section.

Release steps per `docs/open-questions.md` A4 are done the same day as the merge, at tag
`unknowns--v0.8.0`.

### Added

- **Done criteria are part of `plan` (G1).** Every plan opens with purpose / done criteria /
  must-never-break / allowed cost & scope. A task under the size gate still states them
  in one line. If the user skips the questions, the plan says the criteria are not set.
  The independent reviewer's packet no longer asks for input that only `loop` used to
  produce, and with no criteria the reviewer reports "conformance not judgeable" instead
  of reconstructing them from the diff.
- **Evidence and status on factual findings (G2).** In `blindspot` and `unknowns-scout`,
  each finding carries evidence (`file:line` / commit / URL) and a status: confirmed,
  inferred or unchecked. Unchecked findings leave the table and the tally for a **Needs
  checking** list. `reference` rows cite the source location. `teach-me` gives each term a
  source and marks uncertain ones *unverified*.
- **Known knowns are declared up front (G3).** `blindspot` asks once what the user is sure
  of, what they are assuming and where they cannot judge. Assumptions are checked first,
  not skipped. `interview` opens round 1 the same way.
- **The reviewer checks claims by type (G4).** New fifth check: a factual claim against its
  source, a reasoning claim for premises and a counterexample. `loop` step 8 hands over the
  list of claims the work rests on.
- **A recheck date, and a reader for it (G5).** `loop`'s value review asks how the result
  will be checked in reality and when. The scorecard gains **Recheck on** and **Reality
  check** columns. `loop` reads the scorecard on every start and asks about overdue
  rechecks before the new task. That start-of-loop read is the answer to the document's
  weakest part ("who reads this column?"). No hook was added: hooks only run in Claude Code
  and Cowork.
- **Plans are revised, not just logged against (G6).** A deviation that invalidates a
  plan's decision item (schema, interface, UX contract) now changes that item in the plan,
  marked *revised — needs re-approval*.
- Two eval cases: `behavior-plan-opens-with-done-criteria` (G1) and
  `behavior-blindspot-labels-evidence-status` (G2).

### Measured on Claude Opus 5.5

- G1: the plan fired 3/3 and opened with the done-criteria section every time. Unknown
  targets were marked *(assumed)* rather than presented as agreed.
- G2: blindspot fired 3/3 and used status labels in every run. No codebase finding was
  marked confirmed about a repository the model was told it could not see.
- No regressions: `trigger-en-plan` 3/3, and `neg-one-file-plan-defers-to-plan-mode` still
  writes no plan document (3/3).
- G3–G6 are wording only. Their effects need multi-turn or sub-agent runs that a headless
  single-prompt eval cannot drive, so they are unmeasured.

## 0.7.1 — 2026-09-25

A check against Claude Opus 5.5 (`claude-opus-5-5`, Claude Code 2.1.281). The suite had last
been run on the model before it. Record: [docs/trigger-eval-v0.7.1-opus-5-5.md](docs/trigger-eval-v0.7.1-opus-5-5.md).

Release steps per `docs/open-questions.md` A4 are done the same day as the merge, at tag
`unknowns--v0.7.1`.

### Fixed

- **`blindspot` fired 3 times in 8 on Opus 5.5.** "What am I missing?" (and "내가 놓친 게 뭐지?")
  was answered directly in the other 5 runs. The answers were good, but they had no card
  kinds and no improved prompt, and those are the point of the skill. The model had decided
  it could answer without the skill. The description now says to run the skill even then,
  because the deliverable is the prompt, not the answer. After the change it fired 6 of 6,
  and the `neg-vocabulary-does-not-fire-blindspot` negative case stayed at 3 of 3.
- **`evals/run-manual.py` crashed partway through the suite** with
  `AttributeError: 'str' object has no attribute 'get'`. Claude Code 2.1.281's stream-json
  output has some events whose `message` is a plain string. The parser now skips any
  `message` that is not an object.

### Changed

- **`loop` step 7 names the stops it does not want.** On a long run, Opus 5.5 sometimes ends a
  turn by reporting progress: it names the next step without taking it, or offers to
  continue. Anthropic's prompting guide for the model says it follows instructions that
  name those stops. Inside the implement stage the rule is now to keep going and put status
  in the same message as the next action. The stage-boundary checkpoint stays where the
  user steers. The escalation rule (architecture, user-visible behavior, data, security) is
  unchanged.
- **`output-routing.md` names the design defaults to leave out.** With no design direction,
  the model falls back on a few default styles, and a general "avoid a generic look" only
  swaps one default for another. The page contract now lists the specific patterns instead:
  cream backgrounds, italic heading accents, "01/02/03" labels, monospace labels, pill
  buttons.
- **`independent-reviewer` ends with a "not verified" list**: each area it could not check,
  why, and where it looked. This pairs with the existing verified-OK list.

### Checked, no change needed

- No "think hard" or "step by step" instructions in any skill or agent. Opus 5.5 always
  thinks, and these lines only slow it down.
- No request to reproduce the model's reasoning in the reply. On Opus 5.5 that can be
  refused as `reasoning_extraction`. The notes skill's **Attributed** block asks for a
  decision's reason in a few lines, which is not the same thing.
- No `model:` pins or `effort:` frontmatter. Both agents use `model: inherit`, which avoids
  the Claude Code bug where `effort:` next to `model:` silently drops the model override.

## 0.7.0 — 2026-09-15

Claude Desktop, Claude web and Cowork as install targets. The skills already loaded there;
what they did not do was notice when a step's tool was missing. A skill that spawns a
sub-agent, writes `IMPLEMENTATION_NOTES.md` and relies on a reminder hook silently loses
all three in the Chat tab, and the failure mode was a step reported as done when nothing
ran it.

Release steps per `docs/open-questions.md` A4 (annotated tag → `scripts/build-plugin.sh` →
GitHub Release with the payload attached) are done for this version at tag
`unknowns--v0.7.0`, cut 2026-09-16 — a day after the merge, during which the catalog was
already serving 0.7.0 from `main` HEAD. The tag is the immutable record of what that
version was, not the install path.

### Added

- **`skills/loop/references/surfaces.md`** — the one place that says what each surface has
  and what to do instead when it does not. Sub-agent absent → a review packet the user
  pastes into a fresh conversation, never a same-thread review called independent. Hooks
  absent → the notes discipline becomes the skill's own. No durable files → the log lives
  in the session workspace, or is restated in full in the conversation, with the user told
  which. Referenced from `loop`, `notes`, `blindspot`, `brainstorm`, `buy-in` and
  `output-routing.md`.
- **`scripts/build-skill-zips.py`** — one uploadable zip per skill for Customize → Skills,
  the route for a free plan or an organization with plugin installs turned off. It ports
  each skill for standalone upload and lists every difference in its header.
- **`scripts/skill-descriptions.json`** — short descriptions for those zips. The upload form
  documents a 200-character maximum and the SKILL.md descriptions run 248–283, so they are
  shortened here rather than in `SKILL.md`: the descriptions the 0.5.1 eval A/B measured
  stay untouched, and the new surface carries the new risk.
- **`tests/test_skill_descriptions.py`** — fails if a skill has no short description, if one
  is over the limit, if a port drops a trigger phrase the README advertises, or if a built
  zip still holds a plugin-root path or `$ARGUMENTS`.

### Changed

- **Cross-skill pointers no longer name a slash command.** `/unknowns:quiz` (or `/quiz` for
  copied installs) became "the **quiz** skill" in every skill body — the namespace exists in
  Claude Code and nowhere else, and the parenthetical was a third of the sentence. The
  README keeps the slash form, which is where it is true.
- **`scripts/build-plugin.sh` accepts `HEAD`** for building an untagged file to test an
  install with. Tag checks still apply to everything else.
- **README / README.ko** — "Cowork / Claude Desktop", which this project had flagged as
  unverified, is replaced by the two install routes, a what-works-where table, and a plain
  statement that Anthropic's documentation does not name the phone apps as a skills surface.
- **`plugin.json` description cut from 579 to 477 characters.** The Customize → Plugins
  upload rejects anything over 500 — a limit `claude plugin validate --strict` does not
  check and CI therefore never caught. Found by the first real upload of this plugin to
  Claude Desktop, which is the point of this release. `tests/test_manifest_limits.py` now
  holds the number.

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
