# Changelog

## [Unreleased]

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
