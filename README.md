# know-your-unknowns

**Language**: English | [한국어](README.ko.md)

> The map is not the territory — the gap is your unknowns.

**The bottleneck of a strong model is not the model — it is your ability to keep the map
(the plan) aligned with the territory (the actual code, domain and constraints).** This
plugin gives you an operating loop for finding and managing that gap before, during and
after implementation: 11 skills, 2 agents and 2 hooks.

What that buys you, concretely:

- You find out what you didn't know **before** you write the prompt, not after the PR.
- Anything you have to look at and react to arrives as a **single-file interactive page
  that assembles your reactions back into a structured answer** — clicking chips beats
  writing paragraphs. It falls back to Markdown where there is no viewer.
- Plan deviations get logged while they are still cheap, and a hook nudges you when a
  session drifts.

It packages the methodology of Thariq Shihipar (Anthropic, Claude Code team). Two sources
are the origin: the talk **"Field Guide to Fable"** (AI Engineer World's Fair 2026
keynote) and the example collection **"Know your unknowns"** (11 interactive examples) —
https://thariqs.github.io/html-effectiveness/unknowns/. The 11 skills cover all 11
original examples (prototypes covers two of them; loop is the orchestrator with no
original counterpart). For fact-checking details, see
`skills/loop/references/talk-source.md`.

---

## Quick start

Install from the marketplace, inside a Claude Code session:

```
/plugin marketplace add ajitta/claude-plugins
/plugin install unknowns@ajitta
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

Other install paths (clone, copy-a-skill, Cowork) are under
[Installation](#installation) below.

---

## Skills at a glance

Covering the original 11 examples — prototypes covers two, loop orchestrates.

| Phase | Skill | What it does | Original example |
|-------|-------|--------------|------------------|
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

## Installation

The plugin name is `unknowns` (invocation: `/unknowns:<skill>`).

### Marketplace (recommended)

The two commands in [Quick start](#quick-start) above. The marketplace is a catalog
repository, [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins), which
lists this plugin and points back here — so `/plugin install unknowns@ajitta` installs
from this repository at the version its `plugin.json` declares. This is the only path
this project actually verifies.

### Run straight from a clone

For trying an unreleased branch, or for hacking on the plugin itself:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns
```

The plugin is loaded for that session only. If `/unknowns:loop` and friends show up
inside the session, it worked. (`--plugin-dir` also accepts a `.zip` archive.)

### Copy individual skills (no plugin)

If you only want specific skills, copy the `skills/<name>` folders into your vault's or
project's `.claude/skills/`, and `agents/*.md` into `.claude/agents/`. Copy
`skills/loop/references/` alongside them — most skills point at
`skills/loop/references/output-routing.md` and `talk-source.md`, and those pointers
resolve relative to the plugin root, so a skill folder copied on its own points at files
you do not have. Invocations then lose the namespace and get short — `/blindspot`,
`/quiz`. The hooks only activate automatically in plugin form; see [Hook behavior and
configuration](#hook-behavior-and-configuration) for the manual setup.

### Cowork / Claude Desktop

If you received an `unknowns` plugin card in chat, its Install button is the fastest
path. Otherwise the documented route is **Customize → Plugins → upload a plugin file**;
plugins added this way are saved locally to your computer. This repo does not publish a
built plugin file — `scripts/build-plugin.sh` produces one from a release tag — and
neither route has been exercised by this project, so treat the desktop path as
unverified. The reminder hook additionally needs `python3` on that environment's PATH,
which is untested there.

### Updating

```
/plugin marketplace update ajitta
/plugin update unknowns@ajitta
/reload-plugins
```

An update only arrives when the plugin's version number changes. Auto-update is off by
default for third-party marketplaces; turn it on for `ajitta` under `/plugin` →
Marketplaces if you would rather not run these by hand.

### Upgrading from 0.1.x (field-guide)

0.1.x shipped under the name `field-guide`. The name changed, so uninstall and reinstall:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace update ajitta
/plugin install unknowns@ajitta
```

The GitHub repo was renamed, so the old URL (`ajitta/field-guide`) redirects
automatically. Skill mapping: `reference-map`→`reference`, `impl-notes`→`notes`; the rest
keep their names. The environment variable `FIELD_GUIDE_NOTES_THRESHOLD` is still
recognized, but `UNKNOWNS_NOTES_THRESHOLD` is recommended.

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
and what is left; `/unknowns:loop resume` picks up where it stopped.

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
large scopes it delegates to the `unknowns:unknowns-scout` agent. It leads with the
contrast — what you asked for versus what you are actually walking into, with a tally —
then one card per finding, sorted by importance × impact and tagged by kind:
**Landmine** (touching this breaks something non-obvious), **Convention** (an unwritten
rule the codebase enforces), **Missing concept** (a mechanism your prompt has no word
for), **History** (an earlier or reverted attempt at this exact task).

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

**How it runs**: **At most 4** questions per round — exactly one AskUserQuestion dialog,
whose hard cap is 1–4 questions with 2–4 options each — in a fixed priority order
(architecture → data loss & security → compatibility → performance & cost → taste).
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
one-line philosophy + pros/cons + when-it-fits conditions. In HTML you switch between
them in one file to compare, and clicking **steal / skip chips** on individual elements
auto-assembles your choices into a draft requirements list.

**How to react**: Say a combination like
`"layout from #2 + colors from #4 + the filter from #1"` and it converts that into an
**explicit requirements list** before starting the real implementation.

**Tip**: Say `"go wild"` to push the philosophies further apart. Works for code
architecture comparisons too: `"event-driven vs polling vs push, side by side as
skeletons"`. If the interaction itself is the contested question (toolbar placement,
etc.), it builds a clickable mockup with A/B choice buttons that states on the page that
everything is fake data and names where real wiring would go.

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
expected impact / effort size / key risks / how to measure. An impact × effort toggle
separates quick wins from big bets, and the items you mark **resonate** get assembled
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
/ parts that are unnecessary or dangerous / parts that can be improved**. For porting
work it also produces a **proof of understanding (semantics map)** — numbered reference
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

**How it runs**: There is a size gate first — a task touching ≤2 files with no schema,
interface or UX-contract decision is handed back to native plan mode instead of getting a
document. Otherwise items are presented **in order of how likely they are to change**,
not execution order: decision items like schemas, interfaces, and UX contracts at the
top, each with the alternatives considered and its blast radius, with every new or
changed public type rendered as annotated code, while mechanical work is folded away at
the bottom. Approve/request-change selections assemble into your reply. It includes
verification method, risks and rollback, flags the weakest part of the plan, and closes
with 2–3 pre-written reply lines you can copy and send.

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
yet) and **Todo for human** (a judgment call that is yours but blocks nothing).

**Persistence**: once the file exists or `init` has been run, appending to the file is
mandatory — a chat-only summary does not satisfy the rule, because the hook, buy-in and
quiz all read the file. With no file a chat summary is allowed, but the final message
must then say there is no notes file.

**Escalation**: decisions touching architecture, user-visible behavior, data, or
security must be recorded and then **work stops and the question goes to you**. At
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
(delivered as 4 + 2, because AskUserQuestion takes at most 4 per call), prioritising
incident response > design rationale > behavior prediction and avoiding rote recall; if
IMPLEMENTATION_NOTES.md exists, at least 1 question covers a recorded deviation →
3. Grading — each wrong or blank answer names the exact change site to re-read, and you
get a retry → 4. At 6/6 a **cleared to merge** checklist (understanding verified, CI
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

An agent's **effective** toolset is its declared list narrowed to what the host session
actually exposes. In an environment without Grep and Glob, for instance, both agents fall
back to Bash `grep`/`find`.

**unknowns-scout** (read-only reconnaissance):
```
Use the unknowns-scout agent — investigate what I'm missing in the migration plan
Scout the auth module with the unknowns-scout agent
```
The blindspot skill also calls this agent automatically for large investigations. It maps
the target area, reads git history for hairy dead ends and reverted commits, checks test
coverage and unwritten conventions, and — for an unfamiliar library — checks the official
docs and changelog for the *installed* version, so it holds WebFetch and WebSearch
alongside the read tools. It returns an investigation table sorted by importance × impact
plus an improved prompt draft. It is instructed never to modify files, its toolset
excludes Edit/Write, and a bundled PreToolUse hook denies mutating Bash commands — but
Bash stays available for read-only inspection, so this is a strong default, not a sandbox
guarantee.

**independent-reviewer** (independent verification):
```
Use the independent-reviewer agent — verify the implementation we just finished before merge
Run an independent verification
```
It treats the implementing session's explanation **as claims only** and verifies directly
by reading code and running tests. Its four checks are deliberately the ones a general
code review does not cover: **plan/spec conformance** (each requirement named met,
partial or missing), **whether each recorded deviation was acceptable to decide alone**,
**tests-pass-but-reality-fails** (mocks hiding real dependencies, tests that merely mirror
the implementation), and a **verified OK list** — because silence is indistinguishable
from not reviewed. General bug and security hunting belongs to `/code-review` and
`/security-review` on the same diff; run those alongside. Where they are unavailable the
agent covers error handling, security, performance and needless complexity itself as a
secondary pass. Stage 8 of the loop skill calls it automatically.

---

## Hook behavior and configuration

The plugin ships two hooks, both pure standard-library Python.

**The notes reminder** counts file edits (Edit / Write / NotebookEdit) in a session and,
when they **reach 10, exactly once**, delivers "if you deviated from the plan, record it
in IMPLEMENTATION_NOTES.md" to both your screen and Claude's context — so that Claude,
the one actually doing the recording, receives it too. It never blocks anything. It is
also restated once after a compaction summarizes it away, and once at Stop if the
threshold was crossed and the notes file was never touched. Editing
IMPLEMENTATION_NOTES.md itself does not count as an edit, and a sub-agent's edits never
spend the reminder, since a sub-agent's context is discarded when it returns.

**It is opt-in per project**: it stays silent unless the project already uses the
methodology — either an `IMPLEMENTATION_NOTES.md`, or the `.unknowns/` directory the
skills write their output into (searched from the project dir, then Claude's cwd, walking
up to the repo root). Where a project has opted in but the notes file does not exist yet,
the reminder carries the hint to run `/unknowns:notes init`. Set
`UNKNOWNS_NOTES_ALWAYS=1` to make it fire everywhere.

**Edits made through Bash do not count.** `sed`, heredocs and `python -c` rewrite files
without a PostToolUse Edit/Write event, so a session that edits that way can finish with
the counter near zero. That is the usual reason the reminder never appears.

**The sub-agent read-only guard** runs on every Bash call, exits immediately unless the
call belongs to `unknowns-scout` or `independent-reviewer`, and denies commands that
would change your tree (`rm`, `mv`, writing `git` subcommands, package installs, …). The
scout is held to an allowlist of read commands; the reviewer keeps tests, lint and build.
Anything it cannot parse is allowed through — it is a guard rail, not a sandbox.

**Configuration**:

| What you want | How |
|---------------|-----|
| Change the threshold (e.g. 20 edits) | `UNKNOWNS_NOTES_THRESHOLD=20` |
| Turn the reminder off | `UNKNOWNS_NOTES_THRESHOLD=0` |
| Repeat the reminder at every multiple of the threshold | `UNKNOWNS_NOTES_REPEAT=1` |
| Fire in every project, not only ones already using the plugin | `UNKNOWNS_NOTES_ALWAYS=1` |
| Turn the sub-agent Bash guard off | `UNKNOWNS_AGENT_GUARD=0` |
| Set any of these per project | `.claude/settings.json` → `{"env": {"UNKNOWNS_NOTES_THRESHOLD": "20"}}`, committed for the team (each teammate must trust the folder first) |
| Set any of these for yourself only | `.claude/settings.local.json`, same `env` block, git-ignored |
| Legacy variable | `FIELD_GUIDE_NOTES_THRESHOLD` is still recognized (the new variable wins) |
| Requirements | `python3` (standard library only, no external dependencies) |
| Tested with | Claude Code 2.1.261, macOS (2026-09-06): `claude plugin validate` passes; the reminder verified through the live PostToolUse pipeline; both scripts covered by `tests/` |
| Platforms | CI runs the script tests on ubuntu-latest and windows-latest and validates the plugin on ubuntu-latest; macOS is covered by local runs only. On Windows the hook command is `python3`, which is usually absent from a default PATH — create a `python3` alias or adjust the command |

**Manual install without the plugin** (for copied-skill users): copy
`hooks/scripts/impl_notes_reminder.py` into your project and add this to
`.claude/settings.json` — merge it into your existing `hooks` object if you already have
one, rather than pasting a second top-level `hooks` key:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3",
            "args": ["<script path>/impl_notes_reminder.py"],
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

The plugin registers the same script on SessionStart(compact), Stop and SessionEnd as
well; add those entries the same way if you want the restatement, the end-of-session
check and the state-file cleanup.

---

## Recommended scenarios

**Scenario A — small fix** (1–2 files, clear spec):
No loop needed. Just implement; only the notes rule applies. The hook is the safety net.

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
session or run `/reload-plugins`.

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

**Q. The hook never fires.**
Work down this list. (1) Does the project have an `IMPLEMENTATION_NOTES.md` or a
`.unknowns/` directory? Without either, the reminder is off by design — run
`/unknowns:notes init`, or set `UNKNOWNS_NOTES_ALWAYS=1`. (2) Were the edits made through Bash (`sed`, heredocs,
`python -c`)? Those never fire a PostToolUse Edit/Write event and never advance the
counter. (3) The default really is once per session at 10 edits — check
`UNKNOWNS_NOTES_THRESHOLD` and `python3 --version`. (4) Run `/hooks` and confirm the
entry appears under PostToolUse. (5) Smoke-test the script directly:

```bash
echo '{"session_id":"x","tool_name":"Edit","cwd":"'$PWD'"}' \
  | UNKNOWNS_NOTES_THRESHOLD=1 UNKNOWNS_NOTES_ALWAYS=1 \
    python3 hooks/scripts/impl_notes_reminder.py
```
It should print a JSON object containing `systemMessage` and exit 0. (6) Run
`claude --debug` and read `~/.claude/debug/<session-id>.txt`; the script writes
`[unknowns] state persist failed` and similar warnings to stderr, which only the debug
log ever shows.

**Q. The counter looks wrong, or the reminder fired twice.**
Per-session state lives in one small JSON file, under `$CLAUDE_PLUGIN_DATA/state/` when
that is set and otherwise in a `0700` per-user directory in your temp dir
(`unknowns-notes-<user>/<session-id>.json`). Delete it to reset the count. Two things
make "exactly once" fire more than once: if the temp dir is cleaned mid-session the count
restarts, and by design SessionStart(compact) re-arms the reminder, so it fires again
after every compaction. SessionEnd removes the file on its own.

**Q. The hook is annoying.**
Set `UNKNOWNS_NOTES_THRESHOLD=0`, or raise the threshold to around 30 — per project via
the `env` block in `.claude/settings.json`, so you don't have to change it globally.

**Q. Where does the plugin differ from the original material?**
`skills/loop/references/talk-source.md` has a table separating "verified directly from
the source" from "extended during authoring".

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
- Verification details and related literature: `skills/loop/references/talk-source.md`
