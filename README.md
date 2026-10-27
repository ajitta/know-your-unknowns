# know-your-unknowns

**Language**: English | [한국어](README.ko.md)

> The map is not the territory — the gap is your unknowns.

**The bottleneck of a strong model is not the model — it is your ability to keep the map
(the plan) aligned with the territory (the actual code, domain and constraints).** This
plugin gives you an operating loop for finding and managing that gap before, during and
after implementation: 11 skills and 2 Claude Code agents.

What that buys you, concretely:

- You find out what you didn't know **before** you write the prompt, not after the PR.
- Reactable deliverables are **Markdown in the conversation**, with numbered items and an assembled reply you can copy. Select the item numbers or describe the changes you want.
- Plan deviations are recorded by the skill instructions at stage boundaries and before the turn ends; no automatic reminder runs.

> **Measurement status: unmeasured.** The value contract
> ([`docs/value-contract.md`](docs/value-contract.md)) holds that this plugin earns its
> place only when it surfaces something you did not already know **and** that changes a
> decision. Its metric needs a 10-row rolling window; the scorecard has 2 rows
> (2026-07-11, 2026-09-20), and the gap between them tripped the contract's own 60-day
> boundary. So the three claims above are design intent, not measured outcomes.

It packages the methodology of Thariq Shihipar (Anthropic, Claude Code team). Two sources
are the origin: the talk **"Field Guide to Fable"** (AI Engineer World's Fair 2026
keynote) and the example collection **"Know your unknowns"** (11 interactive examples) —
https://thariqs.github.io/html-effectiveness/unknowns/. The 11 skills cover all 11
original examples (prototypes covers two of them; loop is the orchestrator with no
original counterpart). For fact-checking details, see
[`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md).

---

## Quick start

Install from the marketplace, inside a Claude Code session:

```
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
```

Then start a new session (or run `/reload-plugins`) and check it loaded:

```
/unknowns:blindspot test
```

If the skill answers with the "do not implement yet" principle and an investigation
procedure, you are set. From there:

- Big or unfamiliar task → `/unknowns:loop <task description>` is all you need; Claude
  drives the rest stage by stage.
- Only need one technique → invoke that skill directly, or just say it in natural
  language and it auto-triggers.
- Works without slashes: phrases like "blind spot pass", "interview me", "design
  options", "quiz me" are themselves triggers.

Other install paths (clone, copy-a-skill, Desktop) are under
[Install](#install) below.

---

## Skills at a glance

Covering the original 11 examples — prototypes covers two, loop orchestrates.

| Phase | Skill | What it does | Original example |
|---|---|---|---|
| Before | `blindspot` | Blind-spot investigation → improved prompt | Blindspot Pass |
| Before | `teach-me` | Domain vocabulary explainer → precise requests | Teach Me My Unknowns |
| Before | `interview` | The model interviews you → decision table | The Interview |
| Before | `prototypes` | N variants with different philosophies → assembled requirements | Four Design Directions / Mock |
| Before | `brainstorm` | Map of the solution space → pick an intervention | Brainstorm the Intervention |
| Before | `reference` | Reference analysis + proof of understanding | Point at a Reference |
| Before | `plan` | Plan ordered by likelihood-of-change | The Tweakable Plan |
| During | `notes` | Record deviations from the plan | Implementation Notes |
| After | `quiz` | Comprehension quiz + handoff | Quiz Me Before I Merge |
| After | `buy-in` | Reviewer persuasion doc | The Buy-In Doc |
| All | `loop` | The operating loop that threads all of the above | — |

---

## Install

The plugin is `unknowns`. Claude Code uses `/unknowns:<skill>`; elsewhere name the skill or use its trigger phrase.

**ChatGPT and Codex behavior: expected; not yet checked by the owner.** The rebuilt package's uploads, mobile loading, and cross-device behavior are also unmeasured.

### claude.ai web and Claude desktop

1. Open Customize › Plugins › Add › Add marketplace and enter `ajitta/know-your-unknowns`.
2. Open Discover, select the `unknowns` plugin, and select Add. Adding the marketplace alone does not install the plugin.
3. Ask for a skill by name or phrase, for example "blind spot pass".

Instead of steps 1 and 2, use Customize › Plugins › Add › Upload plugin with [know-your-unknowns.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns.zip). Use the Plugins upload, not the Skills upload. [Claude's official installation guidance](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) says web/Desktop plugins are saved to your account and follow you across supported surfaces. Mobile/desktop sync for this plugin is not yet checked by the owner.

### Claude mobile

1. Install the plugin on claude.ai web as above.
2. Open the mobile app with the same account and ask for the skill by name or trigger phrase.
3. Check that it follows the skill's procedure. Loading and account sync for this rebuilt package still need an owner check.

### Claude Code

1. Run inside a Claude Code session:

   ```
   /plugin marketplace add ajitta/know-your-unknowns
   /plugin install unknowns@know-your-unknowns
   ```

2. Start a new session or run `/reload-plugins`.
3. Invoke `/unknowns:blindspot test` and check that it investigates before implementation.

### Codex CLI

1. Add the marketplace and plugin:

   ```
   codex plugin marketplace add ajitta/know-your-unknowns
   codex plugin add unknowns@know-your-unknowns
   ```

2. Ask with a scoped skill name, for example `$unknowns:plan`, followed by the task.
3. Check the procedure and tool fallbacks; this route is expected and not yet checked by the owner.

### ChatGPT desktop (with Codex) and mobile

These two routes follow the owner's dia installation procedure; behavior is **not yet checked by the owner for this plugin**.

1. **Upload the zip on the web (web and mobile).** Download [know-your-unknowns-openai.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns-openai.zip) and upload it on chatgpt.com with the plugin zip upload. The plugin is saved to your account for ChatGPT web and mobile. This zip carries the OpenAI manifest, skills, and listing assets. Uploads do not update themselves; upload each new release again.
2. **Add the marketplace in the desktop app.** In the app's Codex plugin interface, add the GitHub marketplace `ajitta/know-your-unknowns` or a local clone, then select and add `unknowns`. This route installs into the desktop app's local Codex folder; it is not saved to your account for web/mobile access. Updates arrive through the marketplace.

### Windows

1. Use the route for your host above with the same package.
2. No Python or shell is required by the installed plugin: it ships instructions and listing assets only.
3. Developers building from source need Python; use `py -3` where the development commands below say `python3`. The rebuilt package has not been exercised locally on Windows; earlier Windows hook checks were CI-only and the hooks are now removed.

### What works where

- All eleven skills deliver Markdown in the conversation, with numbered reactions and an assembled reply. Missing question, file, search, or execution tools have explicit fallbacks.
- The two named agents run only in Claude Code. Elsewhere the assistant performs the scout pass itself; for independent verification it gives you the same packet to paste into a new conversation, whose review stands in for the agent. That stage stays pending until the review returns.
- The installed package has no hooks or scripts on any surface. A runnable prototype requested during a task can still be code written to files when the host supports it.
- Trackers, scorecards, and deviation logs use files when available; otherwise the assistant prints the complete record in Markdown and says what the user should save.

### Run straight from a clone

Use the generated plugin folder:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns/plugins/unknowns
```

The committed generated output is ready to load. After editing source files, regenerate it with the commands in Develop.

### Copy individual skills

Copy complete folders from `plugins/unknowns/skills/<name>/`, including their `references/` and `agents/openai.yaml`. Source folders in `skills/` may still depend on shared loop references that the build vendors.

For a Claude Code `.claude/skills/` copy with bare agent names, run:

```bash
python3 scripts/build-skill-zips.py --target local
```

Copy the desired folders from `dist/local/`; optional agent prompts come from `claude-code/agents/*.md` into `.claude/agents/`. Invocations become `/blindspot` or `/quiz`.

For hosts accepting one skill at a time through Customize › Skills:

```bash
python3 scripts/build-skill-zips.py
```

Upload the desired `dist/<skill>.zip` files. They use the short descriptions in `scripts/skill-descriptions.json`; the trigger-containment tests check those descriptions too.

### Updating

For the self-hosted marketplace:

```
/plugin marketplace update know-your-unknowns
/plugin update unknowns@know-your-unknowns
/reload-plugins
```

Installed updates require a plugin version change. Uploads must be replaced with a newer archive. The catalog [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins) is an alternative marketplace: its install name remains `unknowns@ajitta`.

### Upgrading from 0.1.x (field-guide)

The old plugin was named `field-guide`. Remove that install and add `unknowns`:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
```

The repository's old URL (`ajitta/field-guide`) redirects. Skill mapping: `reference-map` → `reference`, `impl-notes` → `notes`; the other names stay the same.

---

## Skill-by-skill usage

### 1. `/unknowns:loop` — the full operating loop

**When**: Large or unfamiliar feature work, tasks with fuzzy specs, or whenever you want
to proceed "properly, by the book".

**Invoke**:
```
/unknowns:loop Add subscription renewal to the billing module
```
Auto-trigger phrases: "unknowns loop", "run the operating loop", "know your unknowns",
"운영 루프로 진행", "풀 루프로 해줘"

A bare `/loop` is Claude Code's built-in interval runner, not this skill — always type
`/unknowns:loop`. The same goes for a bare "loop" or "루프 돌려줘" in prose.

**How it runs**: Claude drives 10 stages in order —
1. Define value and completion criteria (agreed with you) → 2. blindspot investigation
(+ teach-me if needed) → 3. interview → 4. explore solutions and shape
(brainstorm/prototypes/reference, as needed) → 5. minimally verify the riskiest
assumptions → 6. plan ordered by likelihood-of-change (plan) → 7. implement + record
deviations (notes) → 8. independent verification → 9. quiz + handoff (+ buy-in if
needed) → 10. value review.

**Three tiers**: a small fix (1–2 files, clear spec) needs no loop at all — only the
notes rule from stage 7. Medium work runs stages 1 → 2 → 3 → 6 → 7 → 9. Large or
unfamiliar work runs everything, with stages 4 and 5 only as needed. Stage 1 runs in
every tier. Tell it the size and it picks:
```
/unknowns:loop This is medium-sized. Bug fix, but the root cause is unclear
```

**Staying oriented**: the loop keeps a `.unknowns/loop.json` tracker (task, tier, stage,
decisions, artifacts) and rewrites it at every stage boundary, so it survives compaction,
`/resume` and new sessions. `/unknowns:loop status` reports the tier, the current stage
and what is left; `/unknowns:loop resume` picks up where it stopped. The skill reads the tracker after compaction or on resume; there is no automatic reminder. With no file system it restates the complete tracker in Markdown for you to save and supply in the next conversation.

---

### 2. `/unknowns:blindspot` — pre-implementation blind-spot investigation

**When**: Before touching a module, library, or domain you don't know well. When you're
in the "I don't know what I don't know" state.

**Invoke**:
```
/unknowns:blindspot Add Kakao OAuth to the auth module. Focus on git history and tests/
```
Auto-triggers: "blind spot pass", "what am I missing", "unknown unknowns",
"사각지대 조사해줘", "내가 놓친 게 뭐지"

**How it runs**: It investigates **without modifying any code**. For codebase-wide or
large scopes it uses `unknowns:unknowns-scout` when the host can start that agent; otherwise it performs a labeled scout pass itself. It leads with the
contrast — what you asked for versus what you are actually walking into, with a tally —
then one card per finding, sorted by likelihood × blast radius and tagged by kind:
**Landmine** (touching this breaks something non-obvious), **Convention** (an unwritten
rule the codebase enforces), **Missing concept** (a mechanism your prompt has no word
for), **History** (a past attempt, revert or hairy dead end that explains why the code
looks this way).

**Key deliverable**: an **improved prompt draft** assembled from the cards' "prompt
fixes", naming the execution order and ending with an explicit checkpoint. Copying that
and using it as your actual implementation instruction is the whole point of this skill.

**Tip**: It doesn't have to be code. It applies to new fields too — e.g.
`"I'm doing video color grading for the first time, run a blind spot pass"`. If you need
to learn the vocabulary itself, teach-me below is the better fit.

---

### 3. `/unknowns:teach-me` — domain vocabulary explainer

**When**: When all you can say is "make it better". When you don't know the field's
terminology and your requests come out vague.

**Invoke**:
```
/unknowns:teach-me Video color grading. I'm a complete beginner
```
Auto-triggers: "teach me", "make me an explainer", "가르쳐줘", "설명서 만들어줘",
"이 분야 용어를 모르겠어"

**How it runs**: the domain's mental model as a 3–5 stage pipeline → 3–7 decision axes
you'll face in this task → a vocabulary ladder per axis (everyday words → expert terms,
with an example request per term) → before/after comparisons per concept, plus 2–3 named
presets so a whole look can be felt at once → 4–6 "what good looks like" criteria stated
in the new vocabulary → and finally a **precise request draft: your original request
rewritten in the new vocabulary**.

---

### 4. `/unknowns:interview` — pre-implementation interview

**When**: The spec is incomplete but you don't know what to ask. Right after a blindspot
investigation.

**Invoke**:
```
/unknowns:interview About the OAuth work we just investigated. Architecture questions first
```
Auto-triggers: "interview me", "ask me questions before implementing", "인터뷰해줘",
"스펙 질문"

**How it runs**: **At most 4** questions per round, with 2–4 options each, in a fixed priority order (architecture → data loss & security → compatibility → performance & cost → taste). It uses a question tool when available, splitting calls if the tool accepts fewer questions; otherwise it asks numbered questions in the conversation.
Each question comes with a one-line "why this matters" and each option with its
tradeoff. At the end it presents a **decision table plus a ready-to-use implementation
prompt** that marks skipped questions and declares the architecture and data decisions
fixed.

**Tip**: Want a deep interview? Say `"grill me, 40-question level"` — it repeats rounds
while keeping the priority order.

---

### 5. `/unknowns:prototypes` — divergent prototype fan-out

**When**: When you can't describe what you want in words ("I'll know it when I see it").
Dashboards, UIs, document templates, API designs, and more.

**Invoke**:
```
/unknowns:prototypes Workout tracking dashboard. I have no visual taste, give me 4
```
Auto-triggers: "divergent prototypes", "design options", "know it when I see it",
"시안 4개", "프로토타입 여러 개", "보면 안다"

**How it runs**: It produces 4 variants (count adjustable) that differ in **design
philosophy**, not minor cosmetics. They diverge in information architecture, user flow,
visual density, interaction, and complexity, and each variant carries a name + a
one-line philosophy + pros/cons + when-it-fits conditions. Numbered Markdown comparisons collect **steal / skip** reactions on individual elements and assemble your choices into a draft requirements list. Runnable prototypes are written to files when the host supports it; the comparison stays in the conversation.

**How to react**: Say a combination like
`"layout from #2 + colors from #4 + the filter from #1"` and it converts that into an
**explicit requirements list** before starting the real implementation.

**Tip**: Say `"go wild"` to push the philosophies further apart. Works for code
architecture comparisons too: `"event-driven vs polling vs push, side by side as
skeletons"`. If the interaction itself is the contested question (toolbar placement,
etc.), it builds a clickable mockup with A/B choice buttons when file tools are available, states that everything is fake data, and names where real wiring would go. Without file or execution tools it shows proposed code or mockup states and says what was not run.

---

### 6. `/unknowns:brainstorm` — map of the solution space

**When**: You know the problem but not what to do about it. Before jumping on the first
idea.

**Invoke**:
```
/unknowns:brainstorm 40% of new signups churn in the first week. Prefer things usable within 2 weeks
```
Auto-triggers: "brainstorm interventions", "show me options", "브레인스토밍",
"해법 후보 펼쳐줘", "옵션 보여줘"

**How it runs**: When a codebase is in scope it searches it first — the cheapest
candidates are usually wiring up machinery that already exists, and those carry a
`Found in code — <path>` marker. It then lays out roughly 10 candidate interventions
along a **time axis from ship-this-afternoon to quarter-long bet**, each annotated with
expected impact / effort size / key risks / how to measure. An impact × effort table separates quick wins from big bets, and the item numbers you mark **resonate** get assembled
into structured next steps down to each one's first execution prompt.

---

### 7. `/unknowns:reference` — reference analysis

**When**: You have example code, a mockup, a screenshot, or a competitor product, and
you want something "like this".

**Invoke**:
```
/unknowns:reference legacy/billing.py — it's Python, port it to TypeScript in the new service
```
Auto-triggers: "use this as a reference", "make it like this", "레퍼런스로 써",
"이 코드처럼 만들어줘", "이거 참고해서"

**How it runs**: Instead of copying the reference verbatim, it first presents a 4-way
analysis — **behavior that must be preserved / parts to adapt to the current environment
/ parts that are unnecessary or dangerous / parts that can be improved**. Before implementation, it also produces a **proof of understanding (semantics map)** — numbered reference
excerpts matched against the corresponding plan, gotcha notes, and an edge-case table
with a Match column. Nothing is implemented until you sign off: reply `semantics
confirmed`, or correct any row by its number. On sign-off it ports the reference's
existing tests first, then implements.

**Tip**: The reference doesn't have to be code — an HTML mockup, test code, a
screenshot, a real example of the desired output all serve as the "map".

---

### 8. `/unknowns:plan` — plan ordered by likelihood-of-change

**When**: Investigation and interview are done and you need a plan before implementing.

**Invoke**:
```
/unknowns:plan Using the OAuth spec we just finalized
```
Auto-triggers: "plan this", "make a plan", "tweakable plan", "계획 세워줘", "구현 계획",
"수정확률순으로 계획"

**How it runs**: There is a size gate first: a planned implementation creating or modifying ≤2 files with no schema,
interface or UX-contract decision is handed back to native plan mode instead of getting a
document. Otherwise items are presented **in order of how likely they are to change**,
not execution order. Decision items such as schemas, interfaces and UX contracts go at
the top, each with the alternatives considered and its blast radius, and every new or
changed public type is rendered as annotated code. Mechanical work appears after the decision items, with a summary and details. Approve/request-change selections assemble into your reply. The plan includes
verification method, risks and rollback, flags its own weakest part, and closes with 2–3
pre-written reply lines you can copy and send.

---

### 9. `/unknowns:notes` — recording deviations from the plan

**When**: When implementation hits something the plan or spec didn't cover. In practice
this is close to an **always-on rule**.

**Invoke**:
```
/unknowns:notes init     ← create the IMPLEMENTATION_NOTES.md template in the project
/unknowns:notes show     ← summarize the deviations recorded so far
/unknowns:notes Implemented token refresh by hand instead of the lib — the library doesn't support PKCE
```
Auto-triggers: "implementation notes", "record a deviation", "where did we diverge from
the plan?", "이탈 기록", "임플 노트", "어디서 계획이랑 달라졌어?"

Claude also records deviations on its own when it detects them mid-implementation.
`init` additionally offers — never silently — to append a short deviation-log rule to
the project's `CLAUDE.md` or `.claude/rules/unknowns.md`, so the rule is in context in
every later session rather than only when the skill is invoked.

**What gets recorded**: only decisions that affect design, behavior, or compatibility
(syntax, formatting, and variable naming are excluded). A full entry captures: the
situation found / how it deviates from the plan / the response chosen / the reason /
alternatives discarded / risk and follow-up check. Two lighter one-line kinds share the
same file: **Discovery** (reality differs from what the plan assumed, no decision needed
yet) and **Todo for human** (a judgment call that is yours but blocks nothing and touches
no architecture, user-visible behavior, data or security — anything that does escalates).

**Persistence**: when a file system is available, append to the notes file, creating it if it is missing; buy-in and quiz use that record. With no file system, print the complete updated log as Markdown and say to save it as IMPLEMENTATION_NOTES.md. Before ending a turn, at stage boundaries, and before commits, check for deviations yourself.

**Escalation**: decisions touching architecture, user-visible behavior, data, or security must be recorded and then **work stops and the question goes to you**. At
wrap-up the skill writes a **fold back into the plan** block — three copyable bullets on
what this changes for attempt #2 — beside any open Todo for human items.

---

### 10. `/unknowns:quiz` — post-work comprehension check

**When**: Right after a big piece of work, just before creating a PR or merging. When
you're wondering "could I actually explain this?".

**Invoke**:
```
/unknowns:quiz Scoped to today's OAuth work
```
Auto-triggers: "quiz me", "test my understanding", "퀴즈", "내가 이해했는지 확인해줘"

**How it runs**: 1. An explanation first (structure of the changes / 3 key design
decisions / where it's most likely to fail / what you should verify yourself), each
behavior anchored with a `file:line` → 2. **6 questions, and the pass mark is all 6**
(five multiple choice, delivered as 4 + 1 with smaller tool batches when needed, plus one teach-back the user explains in their own words), prioritising
incident response > design rationale > behavior prediction and avoiding rote recall; if
IMPLEMENTATION_NOTES.md exists, at least 1 question covers a recorded deviation →
3. Grading — each wrong or blank answer names the exact change site to re-read, and you
get a retry. Grading happens in the conversation; the teach-back key stays hidden until the answer, and lack of an advance key file is disclosed → 4. At 6/6 a **cleared to merge** checklist (quiz passed 6/6, CI
green, migration/rollout reviewed, merge style, what to watch after deploy); below 6/6 it
stays "not yet" and lists the sections to re-read. It closes with a handoff summary
written as if another developer takes over tomorrow, convertible into a PR body draft.

---

### 11. `/unknowns:buy-in` — reviewer persuasion doc

**When**: Implementation and verification are done and you need **approval** from
reviewers or stakeholders.

**Invoke**:
```
/unknowns:buy-in This billing refactor. Reviewers are the backend lead and the security team
```
Auto-triggers: "buy-in doc", "prep me for review", "설득 문서 만들어줘", "리뷰 준비"

**How it runs**: Demo first, at the very top, targeting a 90-second read → preemptive
answers to roughly 5 anticipated reviewer objections, each backed by a reference the
reviewer can follow (spec §, IMPLEMENTATION_NOTES.md entry date, metric, test run,
`file:line`) — an answer with no evidence gets moved to limitations instead → a spec-at-a-
glance table → known limitations and unresolved unknowns, pulled from
IMPLEMENTATION_NOTES.md → the people and teams whose sign-off is needed and what each
must check → a rollback plan. Where quiz verifies your own understanding, buy-in prepares
other people's trust.

---

## Using the agents

Agents are specialists that run in a separate context. Name them in natural language, or
address them by their plugin-scoped id — `unknowns:unknowns-scout` and
`unknowns:independent-reviewer` — which is what the Agent tool's `subagent_type` and the
`@agent-unknowns:unknowns-scout` mention form both expect. A bare `unknowns-scout` is
rejected as `subagent_type`.

The named agents run only in Claude Code. An agent's **effective** toolset is its declared list narrowed to what the host session exposes. The scout has Read, Grep, Glob, WebFetch, and WebSearch, with no Bash or write tools. It reads available history records and hands questions needing command execution back to the caller. Other hosts use the labeled scout pass; independent verification hands the packet to you for a new conversation and waits for its review.

**unknowns-scout** (read-only reconnaissance):
```
Use the unknowns-scout agent — investigate what I'm missing in the migration plan
Scout the auth module with the unknowns-scout agent
```
The blindspot skill also calls this agent automatically for large investigations, and the
brainstorm skill may use it to inventory existing code. Otherwise it runs only when you
name it: other workflows asking for an exploring or research subagent get their own
agent, Explore or a general agent. It maps the target area, reads available history records for hairy dead ends and reverted commits, and checks
test coverage and unwritten conventions. For an unfamiliar library it also reads the
official docs and changelog for the *installed* version, which is why it holds WebFetch
and WebSearch alongside the read tools. It returns an investigation table sorted by
likelihood × blast radius plus an improved prompt draft. Its tool list permits only reading and searching; the prompt also forbids file changes and invented findings.

**independent-reviewer** (independent verification):
```
Use the independent-reviewer agent — verify the implementation we just finished before merge
Run the unknowns independent-reviewer on this branch against its plan
```
It treats the implementing session's explanation **as claims only** and verifies directly
by reading code and running tests. Its five checks are deliberately the ones a general
code review does not cover: **plan/spec conformance** (each requirement named met,
partial or missing), **whether each recorded deviation was acceptable to decide alone**,
**tests-pass-but-reality-fails** (mocks hiding real dependencies, tests that merely mirror
the implementation), a **verified OK list** — because silence is indistinguishable
from not reviewed — and **checks by claim type**: a factual claim is checked against its
source, a reasoning claim for its premises and a counterexample. With no done criteria in
its packet it reports conformance as not judgeable instead of guessing, and it ends with
what it could not verify. General bug and security hunting belongs to `/code-review` and
`/security-review` on the same diff; run those alongside. The
agent also always covers error handling, security, performance and needless complexity itself as a secondary pass. It keeps Bash for tests, lint, and builds, with no edits, commits, dependency installs, or writes outside a temporary directory. This read-only contract is prose only: no hook or permission mode enforces it. Stage 8 of the loop skill calls it automatically. Otherwise it runs only
when you name it: an unnamed "independent review" goes to your other review tools or a
general agent instead.

---

## Recommended scenarios

**Scenario A — small fix** (1–2 files, clear spec):
No loop needed. Just implement; apply the notes rule and record significant deviations before ending the turn.

**Scenario B — medium task** (unclear bug cause, half-familiar module):
```
/unknowns:blindspot Cart totals are occasionally wrong. checkout/ module
→ (review the improved prompt from the investigation)
/unknowns:interview
/unknowns:plan
→ implement
/unknowns:quiz
```

**Scenario C — big, unfamiliar task** (new feature, first time using a library):
```
/unknowns:loop Add real-time collaborative editing. First time using CRDTs
```
All 10 stages — Claude walks you through investigation, interview, plan, independent
verification, all the way to buy-in.

**Scenario D — non-coding** (design, documents, new fields):
```
/unknowns:teach-me YouTube thumbnail design. Start with the vocabulary
/unknowns:prototypes 4 channel-art variants, different philosophies
/unknowns:brainstorm Channel growth has stalled. Things to try this month
```

---

## Troubleshooting (FAQ)

**Q. Skills don't trigger automatically.**
Auto-triggering is a contextual judgment call and is conservative. To be certain, invoke
directly with a slash: `/unknowns:blindspot`. Right after installing, start a new
session or run `/reload-plugins`. With many skills installed there is a second cause:
Claude Code gives the skill listing a budget (1% of the context window by default) and,
when it overflows, keeps descriptions only for the skills you use most (recency-weighted)
and lists the rest by name alone. Whichever unknowns skills you rarely use are the ones at
risk, and it matters most for notes, which is meant to fire on its own. In one measured
run with every unknowns description dropped, 9 of 11 English trigger cases still fired;
notes and blindspot did not. The CLI logged the overflow; that all eleven lost their
descriptions is a probe run's self-report
([docs/trigger-eval-crowd-2026-09-30.md](docs/trigger-eval-crowd-2026-09-30.md)).
`/doctor` shows the listing's cost; raise the budget with the
`skillListingBudgetFraction` setting (e.g. `0.02`), or set other rarely used skills to
`"name-only"` in `skillOverrides` (which does not apply to plugin skills, so it frees room
rather than protecting these). The eval suite's `--crowd N` option measures this case.

**Q. Can I type `/blindspot` instead of `/unknowns:blindspot`?**
Yes for most of them. A plugin skill is reachable both by its scoped name and by its bare
name, as long as no other command already uses that name — so `/blindspot` and `/quiz`
work out of the box. The exception is `loop`: Claude Code ships its own `loop` skill (the
recurring-interval runner), so a bare `/loop` goes there and this plugin's loop always
needs `/unknowns:loop`. The scoped form is never ambiguous, which is why this README uses
it throughout.

**Q. I installed this as field-guide before.**
That's the old 0.1.x name. Follow "Upgrading from 0.1.x" above: uninstall, then
reinstall.

**Q. Where are the interactive pages?**
Deliverables are now Markdown in the conversation. Reply by item number or describe the changes; the assistant assembles the next prompt or requirements list. Runnable task prototypes can still be written to files, but there is no generated presentation page.

**Q. Where does the plugin differ from the original material?**
[`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md) has a table separating "verified directly from
the source" from "extended during authoring".

---

## Repository layout

```
skills/<name>/                 source: SKILL.md, references/, agents/openai.yaml
skills/loop/references/         shared references, vendored transitively by the build
claude-code/agents/             source: Claude Code agent prompts
plugin-manifest.json           source manifest, currently 0.10.0
packaging/                     shipped README, OpenAI interface and SVG listing assets
.claude-plugin/marketplace.json marketplace -> ./plugins/unknowns
plugins/unknowns/               generated Claude plugin; the installed payload
releases/know-your-unknowns.zip generated Claude archive, top folder unknowns/
releases/know-your-unknowns-openai.zip
                               generated OpenAI archive, skills and listing assets only
plugin-release.json            generated version and content digest
tools/package.py               validate, regenerate, or check the committed output
scripts/build-skill-zips.py     optional individual skill uploads/local copies
tests/                         developer checks
evals/                         model eval cases and manual runner
docs/                          historical measurements and methodology records
```

## Develop

Edit source files, then regenerate; never hand-edit `plugins/unknowns/` or the archives:

```bash
python3 tools/package.py
python3 tools/package.py --check
python3 -m unittest discover -s tests -v
claude plugin validate --strict plugins/unknowns
claude plugin validate --strict .
python3 evals/run-manual.py --verify
```

A non-empty `## [Unreleased]` entry in CHANGELOG.md permits changed shipped content to be rebuilt at the same version and updates `plugin-release.json`. Without that entry, changed content requires a version bump. `--check` always rejects stale generated files, archives, or the digest record; rebuild first.

Release: bump `plugin-manifest.json`, move the Unreleased entry under the new version, rebuild, and merge with green CI. An annotated `unknowns--vX.Y.Z` tag then triggers the release workflow, which validates and attaches both committed zips; no release is created by a local build.

Text uses UTF-8 and LF. Release archives use ZIP_STORED with fixed timestamps and modes for byte reproducibility. The packager is standard-library-only and supports Python 3.7+; the optional individual-skill helper uses Python 3.9+.

The developer tooling test matrix targets Ubuntu and Windows; strict plugin validation runs on Ubuntu. The new Windows CI job has not been observed running yet. Earlier Windows evidence covered the removed hooks through CI only; the rebuilt package's Windows behavior is not measured. Historical routing results in `docs/` refer to the versions they name. Structural checks do not measure the updated skills' behavior, loading, or uploads.

---

## Attribution and license

This plugin is an independent, third-party work. It is **not affiliated with, sponsored
by, or endorsed by Anthropic PBC.**

The methodology, example titles and quoted prompt lines it builds on come from the "Know
your unknowns" example collection, Copyright 2026 Anthropic PBC, licensed under the
Apache License, Version 2.0 — https://www.apache.org/licenses/LICENSE-2.0. Short
quotations from the "Field Guide to Fable" talk are used as brief attributed quotations.
The plugin's own code and prose are MIT-licensed; `LICENSE` carries the full MIT text, and
`NOTICE` carries the Apache-2.0 attribution notice with a link to that license's text.

---

## Sources

- Example collection: https://thariqs.github.io/html-effectiveness/unknowns/ ("Know your unknowns")
- Source repository: https://github.com/ThariqS/html-effectiveness
- Parent essay: https://thariqs.github.io/html-effectiveness/ ("The unreasonable effectiveness of HTML")
- Talk: https://www.youtube.com/watch?v=9fubhllmsBU (AI Engineer World's Fair 2026)
- This plugin: https://github.com/ajitta/know-your-unknowns
- Verification details and related literature: [`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md)
