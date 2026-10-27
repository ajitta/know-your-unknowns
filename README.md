# know-your-unknowns

**Language**: English | [한국어](README.ko.md)

> The map is not the territory — the gap is your unknowns.

**The bottleneck of a strong model is not the model — it is keeping the map (the plan)
aligned with the territory (the actual situation: its rules, people, material and
constraints).** Some of that gap is what you don't know, some is what the AI doesn't know
about your situation, and the widest part is what neither of you knows yet. This plugin
gives you an operating loop for finding and managing that gap before, during and after
the work, in any domain — a grant, a policy, an event, a study, a hire, a codebase: 11
skills and 2 Claude Code agents.

What that buys you, concretely:

- You and the AI find out what you didn't know **before** the work starts, not after it is handed over.
- The work is judged by the outcome you were after, not only by the artifact: the loop ends by asking you whether the result achieved it.
- Self-evident requests stay self-evident: the skills do them directly, without the method.
- Reactable deliverables are **Markdown in the conversation**, with numbered items and an assembled reply you can copy. Select the item numbers or describe the changes you want.
- Plan deviations are recorded by the skill instructions at stage boundaries and before the turn ends; no automatic reminder runs.

> **Measurement status: unmeasured.** The value contract
> ([`docs/value-contract.md`](docs/value-contract.md)) holds that this plugin earns its
> place only when it surfaces something you did not already know **and** that changes a
> decision. The plugin ships no in-session measurement of that, so the claims above
> are design intent, not measured outcomes.

It packages the methodology of Thariq Shihipar (Anthropic, Claude Code team). Two sources
are the origin: the talk **"Field Guide to Fable"** (AI Engineer World's Fair 2026
keynote) and the example collection **"Know your unknowns"** (11 interactive examples) —
https://thariqs.github.io/html-effectiveness/unknowns/. The 11 skills cover all 11
original examples (prototypes covers two of them; unknowns-loop is the orchestrator with no
original counterpart). For fact-checking details, see
[`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md).

---

## Purpose: three cells of what you and the AI know

Every task has two knowers: you and the AI. The plugin borrows the four panes of the Johari window (Open, Blind, Hidden, Unknown), adapted: "self" is you, "others" is the AI, and the knowledge is about the task. It serves three of the four cells, in any domain: research, policy, events, hiring, a personal decision, or code.

| You : AI | Without the plugin | What the skills do | Skills |
|---|---|---|---|
| known : known — both of you know | The request is self-evident; the AI just does it well. | Nothing: such requests are done directly, without the method. | — |
| unknown : known — you don't know, the AI does | The AI may get it right, but you (or the people who approve it) cannot judge it. | Surface your gaps or your approvers' gaps. | teach-me, quiz, buy-in |
| known : unknown — the AI doesn't know, you do | You keep correcting the AI until the result comes out. | Ask or read back what the AI does not know or cannot judge, before deciding. | interview, reference |
| unknown : unknown — neither of you knows yet | Output appears, but it is unlikely to be what you were after. The widest cell. | Surface both sides' unknowns: yours and the AI's own. | blindspot, brainstorm, prototypes, deviation-log, tweakable-plan, unknowns-loop |

**Output** is what the AI produces; the **outcome** is the achievement you were actually after. A result can meet every done criterion and still miss the outcome, so the loop ends by asking you whether it achieved the outcome.

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

If the skill answers with an investigation procedure that ends at an improved prompt,
you are set. From there:

- Big or unfamiliar task, in any domain → `/unknowns:unknowns-loop <task description>` is all
  you need; Claude drives the rest stage by stage.
- Only need one technique → invoke that skill directly, or just say it in natural
  language and it auto-triggers.
- Works without slashes: phrases like "blind spot pass", "interview me", "design
  options", "quiz me" are themselves triggers.

Other install paths (clone, copy-a-skill, Desktop) are under
[Install](#install) below.

---

## Skills at a glance

Covering the original 11 examples — prototypes covers two, unknowns-loop orchestrates.

| Phase | Skill | Cell | What it does | Original example |
|---|---|---|---|---|
| Before | `blindspot` | neither knows | Blind-spot investigation → improved prompt | Blindspot Pass |
| Before | `teach-me` | you don't know | Domain vocabulary explainer → precise requests | Teach Me My Unknowns |
| Before | `interview` | AI doesn't know | The model asks what it cannot know → decision table | The Interview |
| Before | `prototypes` | neither knows | N variants with different philosophies → assembled requirements | Four Design Directions / Mock |
| Before | `brainstorm` | neither knows | Map of the solution space → pick an intervention | Brainstorm the Intervention |
| Before | `reference` | AI doesn't know | Reference analysis + proof of understanding | Point at a Reference |
| Before | `tweakable-plan` | neither knows | Plan ordered by likelihood-of-change | The Tweakable Plan |
| During | `deviation-log` | neither knows | Record deviations from the plan | Implementation Notes |
| After | `quiz` | you don't know | Comprehension quiz | Quiz Me Before I Merge |
| After | `buy-in` | you don't know | What approvers don't know, answered with evidence | The Buy-In Doc |
| All | `unknowns-loop` | neither knows | The operating loop that threads all of the above | — |

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
3. Invoke `/unknowns:blindspot test` and check that it asks before it investigates.

### Codex CLI

1. Add the marketplace and plugin:

   ```
   codex plugin marketplace add ajitta/know-your-unknowns
   codex plugin add unknowns@know-your-unknowns
   ```

2. Ask with a scoped skill name, for example `$unknowns:tweakable-plan`, followed by the task.
3. Check the procedure; this route is expected and not yet checked by the owner.

### ChatGPT desktop (with Codex) and mobile

Behavior on these two routes is **not yet checked by the owner for this plugin**.

1. **Upload the zip on the web (web and mobile).** Download [know-your-unknowns-openai.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns-openai.zip) and upload it on chatgpt.com with the plugin zip upload. The plugin is saved to your account for ChatGPT web and mobile. This zip carries the OpenAI manifest, skills, and listing assets. Uploads do not update themselves; upload each new release again.
2. **Add the marketplace in the desktop app.** In the app's Codex plugin interface, add the GitHub marketplace `ajitta/know-your-unknowns` or a local clone, then select and add `unknowns`. This route installs into the desktop app's local Codex folder; it is not saved to your account for web/mobile access. Updates arrive through the marketplace.

### Windows

1. Use the route for your host above with the same package.
2. No Python or shell is required by the installed plugin: it ships instructions and listing assets only.
3. Developers building from source need Python; use `py -3` where the development commands below say `python3`. The rebuilt package has not been exercised locally on Windows; earlier Windows hook checks were CI-only and the hooks are now removed.

### What works where

- All eleven skills deliver Markdown in the conversation, with numbered reactions and an assembled reply. Where a step needs a tool the host lacks, the skill does the step in the conversation and says what could not be checked.
- The two named agents run only in Claude Code. Elsewhere the steps that call them follow the missing-tool rule above, and buy-in's independent evidence check is not available.
- The installed package has no hooks or scripts on any surface. A runnable prototype requested during a task can still be code written to files when the host supports it.
- The deviation log is a file when files are available (`IMPLEMENTATION_NOTES.md` for code work, otherwise `DEVIATIONS.md` beside the deliverable); otherwise the record stays in the conversation.

### Run straight from a clone

Use the generated plugin folder:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns/plugins/unknowns
```

The committed generated output is ready to load. After editing source files, regenerate it with the commands in Develop.

### Copy individual skills

Copy complete folders from `plugins/unknowns/skills/<name>/`, including their `agents/openai.yaml`. Each skill folder is self-contained.

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

Two skills are renamed in 0.12.0: `loop` is now `unknowns-loop` and `notes` is now `deviation-log`. Type `/unknowns:unknowns-loop` and `/unknowns:deviation-log` (Codex: `$unknowns:unknowns-loop`, `$unknowns:deviation-log`), and replace uploaded skill zips; the trigger phrases are unchanged.

### Upgrading from 0.1.x (field-guide)

The old plugin was named `field-guide`. Remove that install and add `unknowns`:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
```

The repository's old URL (`ajitta/field-guide`) redirects. Skill mapping: `reference-map` → `reference`, `impl-notes` → `notes` (renamed again in 0.12.0, see below); the other names stay the same.

---

## Skill-by-skill usage

### 1. `/unknowns:unknowns-loop` — the full operating loop

**When**: Large or unfamiliar work with a fuzzy goal: launching a programme, planning an
event, a study, a product feature. Or whenever you want to proceed "properly, by the book".

**Invoke**:
```
/unknowns:unknowns-loop Start a tool library for our apartment complex, run by volunteers
```
Auto-trigger phrases: "unknowns loop", "run the operating loop", "know your unknowns",
"운영 루프로 진행", "풀 루프로 해줘"

A bare `/loop` is Claude Code's built-in interval runner, not this skill; `/unknowns-loop`
or `/unknowns:unknowns-loop` reaches this one. The same goes for a bare "loop" or
"루프 돌려줘" in prose.

**How it runs**: Claude agrees the outcome you are after and the done criteria with you
in one exchange, says what it does not know about your situation, and names the stages up
front. Before the work: blindspot (teach-me first if the field's terms are new) →
interview → brainstorm/prototypes/reference as needed → the cheapest probe of the riskiest
assumption (a phone call, a pilot, a spike) → a plan ordered by likelihood-of-change
(plan). During the work, deviation-log records deviations. After it, the result is
checked against each done criterion with evidence, then quiz, plus buy-in when reviewers
or stakeholders must approve, and finally an **outcome check**: Claude asks you whether
the result achieved what you were after, not only whether it meets the criteria. A stage
whose question is already answered is skipped, and the loop says so. For a self-evident
task you need no loop.

---

### 2. `/unknowns:blindspot` — blind-spot investigation before the work

**When**: Before starting work whose territory you have not checked: a funding call, a
new policy, an unfamiliar module or library. When you're in the "I don't know what I
don't know" state.

**Invoke**:
```
/unknowns:blindspot Our first city arts grant: a mural programme at three library branches
```
Auto-triggers: "blind spot pass", "what am I missing", "unknown unknowns",
"사각지대 조사해줘", "내가 놓친 게 뭐지"

**How it runs**: It first asks what you are sure of, what you are assuming and where you
cannot judge, and puts its own three lists beside yours: what it does not know about
your situation, what it is assuming, and what it cannot check from here. Then it
investigates, checking both sides' assumptions first; it does not start the work. When
the task spans many sources (a whole codebase, a large body of documents) it uses the
`unknowns:unknowns-scout` agent in Claude Code. It marks each finding none of your three
lists mentioned as **new to you**, and leads with the contrast — what you asked for
versus what you are actually walking into, with a tally — then one card per finding,
sorted by likelihood × blast radius and tagged by kind: **Landmine** (touching this
breaks something non-obvious), **Convention** (an unwritten rule the territory enforces),
**Missing concept** (a mechanism your prompt has no word for), **History** (a past
attempt or dead end that explains why things are the way they are). What it could not
settle is listed as questions for you and things to check.

**Key deliverable**: an **improved prompt draft** assembled from the cards' "prompt
fixes", naming the execution order and ending with an explicit checkpoint. Copying that
and using it as your actual instruction is the whole point of this skill.

**Tip**: It works the same on code — e.g. `"Add Kakao OAuth to the auth module, blind
spot pass first, focus on git history and tests/"`. If you need to learn a field's
vocabulary itself, teach-me below is the better fit.

---

### 3. `/unknowns:teach-me` — domain vocabulary explainer

**When**: When all you can say is "make it better". When you don't know the field's
terminology and your requests come out vague, or you cannot judge the result.

**Invoke**:
```
/unknowns:teach-me Video color grading. I'm a complete beginner
```
Auto-triggers: "teach me", "make me an explainer", "가르쳐줘", "설명서 만들어줘",
"이 분야 용어를 모르겠어"

**How it runs**: the domain's mental model as a 3–5 stage pipeline → 3–7 decision axes
you'll face in this task → a vocabulary ladder per axis (everyday words → expert terms,
with an example request per term, and terms it could not check marked *unverified*) →
before/after comparisons per axis, plus 2–3 named presets so a whole look can be felt at
once → 4–6 "what good looks like" criteria stated in the new vocabulary → and finally a
**precise request draft: your original request rewritten in the new vocabulary**. The
same works for a lease, a research method or a coffee roaster's jargon.

---

### 4. `/unknowns:interview` — interview before deciding

**When**: The work is underdetermined and the answers sit with you: your constraints,
the people involved, local rules, your priorities. Right after a blindspot investigation.

**Invoke**:
```
/unknowns:interview A two-day reunion for 40 relatives from four countries. Nothing is decided
```
Auto-triggers: "interview me", "ask me questions before implementing", "ask me before you
decide", "인터뷰해줘", "스펙 질문"

**How it runs**: Before deciding anything, it asks what it cannot know or judge about your
situation, **at most 4** questions per round: round 1 asks open questions about your
situation, and from round 2 on each decision gets 2–4 options. Questions follow a fixed
order of what a wrong decision breaks (structure → irreversible harm → compatibility with what
exists → cost → taste). A question tool that takes fewer questions gets the round split
across calls. Each question comes with a one-line "why this matters" and each option with
its tradeoff. At the end it presents a **decision table plus a ready-to-use prompt for the
work** that marks skipped questions, declares the structure and harm decisions fixed, and
asks for deviations to be logged in the deviation log (IMPLEMENTATION_NOTES.md for code).

**Tip**: Want a deep interview? Say `"grill me, 40-question level"` — it repeats rounds
while keeping the priority order. For a feature: `"interview me about the OAuth work,
architecture questions first"`.

---

### 5. `/unknowns:prototypes` — divergent prototype fan-out

**When**: When you can't describe what you want in words ("I'll know it when I see it"):
a job description, an event format, a campaign, a report layout, a dashboard, an API.

**Invoke**:
```
/unknowns:prototypes Our first head of operations. I can't write the job description, give me 4
```
Auto-triggers: "divergent prototypes", "design options", "versions to react to", "know it
when I see it", "시안 4개", "프로토타입 여러 개", "보면 안다"

**How it runs**: It produces 4 versions (count adjustable) that differ in **design
philosophy**, not minor cosmetics, along axes that fit the subject (for a screen:
information structure, flow, density, interaction; for a document, role or event:
structure, scope, tone, audience, format), and each carries a name + a one-line
philosophy + pros/cons + when-it-fits conditions. It says what it does not know about
your situation. Numbered Markdown comparisons collect **steal / skip** reactions on
individual elements and assemble your choices into a draft requirements list. Runnable
prototypes or full drafts are written to files when the host supports it; the comparison
stays in the conversation.

**How to react**: Say a combination like
`"scope from #2 + tone from #4 + the reporting line from #1"` and it converts that into an
**explicit requirements list**. The skill ends there; the work starts from that list.

**Tip**: Say `"go wild"` to push the philosophies further apart. Works for code
architecture comparisons too: `"event-driven vs polling vs push, side by side as
skeletons"`. If the interaction itself is the contested question (toolbar placement,
etc.), it builds a clickable mockup with A/B choice buttons, states that everything is fake data, and names where real wiring would go.

---

### 6. `/unknowns:brainstorm` — map of the solution space

**When**: You know the problem but not what to do about it. Before jumping on the first
idea.

**Invoke**:
```
/unknowns:brainstorm Our choir fell from 60 to 35 regular members in two years. Things to try this season
```
Auto-triggers: "brainstorm interventions", "show me options", "브레인스토밍",
"해법 후보 펼쳐줘", "옵션 보여줘"

**How it runs**: It first says what it does not know about your situation, then looks
for what already exists but is not used for the problem — resources, programmes and
people in reach, or, in a codebase, machinery that sits disconnected — since the cheapest
candidates are usually connecting what exists; those carry an `Already exists — <where>`
marker. It then lays out roughly 10 candidate interventions along a **time axis from
this afternoon to a quarter-long bet**, each annotated with expected impact / effort
size / key risks / how to see that it moved the problem. The item numbers you mark
**resonate** are assembled into a copyable "proceed with these, in this order", where it stops.

---

### 7. `/unknowns:reference` — reference analysis

**When**: You have an example to build from: another organisation's policy, a past
proposal, a contract template, a competitor's product, example code, a mockup.

**Invoke**:
```
/unknowns:reference The neighbouring town's library volunteer policy. Write ours, we're much smaller
```
Auto-triggers: "use this as a reference", "make it like this", "레퍼런스로 써",
"이 코드처럼 만들어줘", "이거 참고해서"

**How it runs**: Instead of copying the reference verbatim, it first presents a 4-way
analysis — **behavior that must be preserved / parts to adapt to your context / parts
that are unnecessary or dangerous / parts that can be improved**. Before building on it,
it produces a **proof of understanding (semantics map)** — numbered reference excerpts
matched against their counterparts in your work, gotcha notes, and an edge-case table
with a Match column, with the rows that rest on guesses about your situation marked
*assumed*. It stops for your sign-off: reply `semantics confirmed`, or correct any row by
its number. Its application plan first carries over how the reference checks itself (its
tests, checklists or acceptance criteria); the work starts from the signed-off map.

**Tip**: Porting code works the same way — e.g. `legacy/billing.py, port it to TypeScript
in the new service`. A screenshot or a real example of the desired output also serves as
the "map".

---

### 8. `/unknowns:tweakable-plan` — plan ordered by likelihood-of-change

**When**: Investigation and interview are done and you need a plan before the work.

**Invoke**:
```
/unknowns:tweakable-plan Launch the community garden on the city lot: 20 beds, a shed, water, 50 households waiting
```
Auto-triggers: "plan this", "make a plan", "tweakable plan", "계획 세워줘", "구현 계획",
"수정확률순으로 계획"

**How it runs**: The plan opens with the purpose and done criteria in one line, saying
"not set" where you gave none, and says what it does not know about your situation. There
is a size gate: work that holds no decision you might want to change (for code, ≤2 files
with no schema, interface or UX-contract decision, which suits native plan mode) gets
that line, any questions for missing done criteria, and its steps in execution order
instead of a document. Otherwise items are presented **in order of how likely they are to
change**, not execution order. Decision items — what other parts build on, such as plot
allocation or the city agreement, or schemas and interfaces in code — go at the top,
each with the alternatives considered, its blast radius, how it will be verified and
what breaks if it is wrong, and the central artifact (a budget table, a run sheet, or a
public type as annotated code) is annotated with the alternatives each choice beat.
Mechanical work appears after the decision items, each with a summary and its
verification. Approve/request-change selections assemble into your reply. The plan flags
its own weakest part and closes with 2–3 pre-written reply lines you can copy and send.

---

### 9. `/unknowns:deviation-log` — recording deviations from the plan

**When**: When the work hits something the plan or spec didn't cover. In practice this
is close to an **always-on rule**.

**Invoke**:
```
/unknowns:deviation-log The renovation closed the community hall, so the year-end event moves to the school gym (no elevator)
```
Auto-triggers: "implementation notes", "record a deviation", "where did we diverge from
the plan?", "이탈 기록", "임플 노트", "어디서 계획이랑 달라졌어?"

Claude also records deviations on its own when it detects them mid-work.

**What gets recorded**: only decisions that affect design, behavior, or compatibility
(wording, formatting, and naming are excluded). A full entry captures: the situation
found / how it deviates from the plan / the response chosen / the reason / alternatives
discarded / risk and follow-up check, including what only you can judge. A lighter
one-line **Discovery** shares the same file: reality differs from what the plan assumed,
and no decision is needed yet.

**Persistence**: entries are appended to a deviation log, created if it is missing:
IMPLEMENTATION_NOTES.md at the project root for code work, otherwise DEVIATIONS.md beside
the deliverable or a file you name; buy-in and quiz use that record.

**Keep going, review at wrap-up**: where the plan is silent, Claude picks the conservative
option, logs it and keeps going; a plan decision the deviation invalidates is marked superseded in the plan. At wrap-up, entries touching the work's structure, what others
see or were promised, data or money, or safety are listed first for you to review,
starting with the calls that rest on something only you know, followed by a **fold back
into the plan** block — three copyable bullets on what this changes for attempt #2.

---

### 10. `/unknowns:quiz` — post-work comprehension check

**When**: Right after a big piece of delegated work, just before presenting, submitting,
signing or merging it. When you're wondering "could I actually explain this?".

**Invoke**:
```
/unknowns:quiz The market analysis you wrote. I present it to the board tomorrow
```
Auto-triggers: "quiz me", "test my understanding", "퀴즈", "내가 이해했는지 확인해줘"

**How it runs**: 1. An explanation first (structure of the work / 3 key decisions / where
it's most likely to fail / what you should verify yourself), each part anchored to its
location (`file:line` for code; section or page otherwise) → 2. **6 questions, and the pass
mark is all 6** (five multiple choice, delivered as 4 + 1 with smaller tool batches when needed, plus one teach-back the user explains in their own words), prioritising
what to do when something goes wrong > decision rationale > predicting outcomes and
avoiding rote recall; if a deviation log exists, at least 1 question covers a recorded
deviation → 3. Grading — each wrong or blank answer names the exact place to re-read,
and you get a retry. Grading happens in the conversation; the teach-back key stays hidden
until the answer → 4. 6/6 passes, and buy-in is suggested when reviewers must approve;
below 6/6 it stays "not yet" and lists the sections to re-read.

---

### 11. `/unknowns:buy-in` — approvers' unknowns doc

**When**: The work is done and you need **approval** from someone who has not seen it: a
director, a funder, a client, a committee, code reviewers.

**Invoke**:
```
/unknowns:buy-in The hybrid-work policy. My director signs; the COO rejected a similar one last spring
```
Auto-triggers: "buy-in doc", "prep me for review", "get sign-off", "설득 문서 만들어줘",
"리뷰 준비"

**How it runs**: For each approver, what they do not know that their decision depends on
and what they will object to; Claude asks you what you know about them (priorities, past
objections, the politics) and lists what neither of you knows as questions to find out →
the result shown first (a demo, a sample, a pilot result; when there is none, the doc
says so and lists it as a limitation) → an answer to each point, backed by a reference
the approver can follow (spec §, deviation log entry date, metric, source document, test
run, `file:line`) and checked by the independent-reviewer agent in Claude Code — an
answer with no evidence moves to limitations → known limitations and unresolved unknowns,
pulled from the deviation log → the people whose sign-off is needed and what each will
check. Where quiz closes your own gaps, buy-in closes the approvers'.

---

## Using the agents

Agents are specialists that run in a separate context. Name them in natural language, or
address them by their plugin-scoped id — `unknowns:unknowns-scout` and
`unknowns:independent-reviewer` — which is what the Agent tool's `subagent_type` and the
`@agent-unknowns:unknowns-scout` mention form both expect. A bare `unknowns-scout` is
rejected as `subagent_type`.

The named agents run only in Claude Code. Both declare no tool list, so they inherit every tool your session allows, and their prompts carry no read-only rules. If you want them confined, use your own permission settings or sandbox.

**unknowns-scout** (reconnaissance):
```
Use the unknowns-scout agent — investigate what I'm missing in the funding call and our draft
Scout the auth module with the unknowns-scout agent
```
The blindspot skill also calls this agent automatically for large investigations, and the
brainstorm skill may use it to inventory what already exists. Otherwise it runs only when
you name it: other workflows asking for an exploring or research subagent get their own
agent, Explore or a general agent. It investigates whatever sources the task has —
documents, data, the web, a codebase and its history: what exists and what governs it,
past attempts and reversals, where checks exist and where they don't, and unwritten
conventions. For an unfamiliar library, field or rule set it reads the official source
for the version in force. It returns an investigation table sorted by likelihood × blast
radius plus an improved prompt draft, reports only what it found, and lists what still
needs checking.

**independent-reviewer** (independent verification):
```
Use the independent-reviewer agent — check the gala plan against the board's four goals
Run the unknowns independent-reviewer on this branch against its plan
```
It treats the producer's explanation **as claims only** and verifies directly against
the work: the document, the figures and sources, and for code by reading it and running
the tests. Its five checks are deliberately the ones a general review does not cover:
**plan and outcome conformance** (each done criterion named met, partial or missing, and
whether the deliverable is likely to achieve the stated outcome), **whether each recorded
deviation was acceptable to decide alone**, **passes on paper but fails in reality**
(figures that do not add up, sources that do not say what they are cited for; for code,
mocks hiding real dependencies and tests that merely mirror the implementation), a
**verified OK list** — because silence is indistinguishable from not reviewed — and
**checks by claim type**: a factual claim is checked against its source, a reasoning
claim for its premises and a counterexample. With no done criteria or outcome in its
packet it reports them as not judgeable instead of guessing, and it ends with what it
could not verify. General bug and security hunting on code belongs to `/code-review` and
`/security-review`; run those alongside. The buy-in skill calls it to check the evidence
behind its answers. Otherwise it runs only when you name it: an unnamed "independent
review" goes to your other review tools or a general agent instead.

---

## Recommended scenarios

**Scenario A — self-evident request** (fix the typos, rename a variable, a clear one-step
task): no skill and no loop. Claude does it directly; record a significant deviation if
one comes up.

**Scenario B — medium code task** (unclear bug cause, half-familiar module):
```
/unknowns:blindspot Cart totals are occasionally wrong. checkout/ module
→ (review the improved prompt from the investigation)
/unknowns:interview
/unknowns:tweakable-plan
→ implement
/unknowns:quiz
```

**Scenario C — big, unfamiliar work** (a new programme, an event, a first-time process):
```
/unknowns:unknowns-loop Start an in-house mentoring programme for 80 people. I'm the only HR person
```
Claude walks you through investigation, interview, a probe of the riskiest assumption,
plan, deviation notes, the quiz, buy-in when approval is needed, and the outcome check.

**Scenario D — a new field** (design, research, a decision you cannot yet frame):
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
risk, and it matters most for deviation-log, which is meant to fire on its own. In one measured
run with every unknowns description dropped, 9 of 11 English trigger cases still fired;
notes (now deviation-log) and blindspot did not. The CLI logged the overflow; that all eleven lost their
descriptions is a probe run's self-report
([docs/trigger-eval-crowd-2026-09-30.md](docs/trigger-eval-crowd-2026-09-30.md)).
`/doctor` shows the listing's cost; raise the budget with the
`skillListingBudgetFraction` setting (e.g. `0.02`), or set other rarely used skills to
`"name-only"` in `skillOverrides` (which does not apply to plugin skills, so it frees room
rather than protecting these). The eval suite's `--crowd N` option measures this case.

**Q. Can I type `/blindspot` instead of `/unknowns:blindspot`?**
Yes for most of them. A plugin skill is reachable both by its scoped name and by its bare
name, as long as no other command already uses that name — so `/blindspot` and `/quiz`
work out of the box. Claude Code ships its own `loop` skill (the recurring-interval runner), so a bare `/loop`
goes there; this plugin's loop is `unknowns-loop`, so `/unknowns-loop` reaches it. The scoped form is never ambiguous, which is why this README uses
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
skills/<name>/                 source: SKILL.md, agents/openai.yaml
claude-code/agents/             source: Claude Code agent prompts
plugin-manifest.json           source manifest, currently 0.11.0
packaging/                     shipped README, listing icon, OpenAI interface and SVGs
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
