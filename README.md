# know-your-unknowns

**Language**: English | [한국어](README.ko.md)

> The map is not the territory — the gap is your unknowns.

This plugin packages the methodology of Thariq Shihipar (Anthropic, Claude Code team)
into something you can use directly in Claude. Two sources are the origin:

- The talk **"Field Guide to Fable"** (AI Engineer World's Fair 2026 keynote)
- The example collection **"Know your unknowns"** (11 interactive examples) —
  https://thariqs.github.io/html-effectiveness/unknowns/

The core idea: **the bottleneck of a strong model is not the model — it is the user's
ability to keep the map (the plan) aligned with the territory (reality).** This plugin
provides an operating loop for finding and managing that gap (your unknowns) before,
during, and after implementation — 11 skills mapping 1:1 to the original 11 examples,
plus 2 agents and 1 hook. For fact-checking details, see
`skills/loop/references/talk-source.md`.

Deliverable philosophy (half of the original material is about this): any artifact the
user needs to look at and react to is built as a **single-file interactive HTML page that
assembles your reactions into a structured answer**, falling back to Markdown in
environments without a viewer.

---

## Installation

The plugin name is `unknowns` (invocation: `/unknowns:<skill>`).

### Cowork (desktop app)

Click the **Install button** on the `unknowns.plugin` card shared in chat. That's it.

### Claude Code (CLI)

Pick one of three methods.

**Method A — Local test (fastest)**
```bash
unzip unknowns.plugin -d ~/plugins/unknowns
claude --plugin-dir ~/plugins/unknowns
```
If `/unknowns:loop` and friends show up inside the session, it worked.

**Method B — Marketplace install (permanent, recommended)**

This repo includes a marketplace manifest, so it installs directly:
```
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@ajitta
```
To update: `/plugin marketplace update ajitta`, then reinstall.

**Method C — Copy individual skills (no plugin)**
If you only want specific skills, copy the `skills/<name>` folders into your vault's or
project's `.claude/skills/`. Invocations then lose the namespace and get short —
`/blindspot`, `/quiz` — and agents can be copied from `agents/*.md` into
`.claude/agents/`. Note that the hook only activates automatically in plugin form
(for manual setup, see the "Hook" section below).

### Upgrading from the old version (field-guide)

0.1.x shipped under the name `field-guide`. Since the name changed, uninstall and
reinstall:
```
/plugin uninstall field-guide@ajitta
/plugin marketplace update ajitta
/plugin install unknowns@ajitta
```
The GitHub repo was renamed, so the old URL (`ajitta/field-guide`) redirects
automatically. The environment variable `FIELD_GUIDE_NOTES_THRESHOLD` is still
recognized, but `UNKNOWNS_NOTES_THRESHOLD` is recommended.

### Verifying the install

```
/unknowns:blindspot test
```
If the skill loads and responds with the "do not implement yet" principle and an
investigation procedure, everything is working.

---

## Quick start (10-second summary)

- Big or unfamiliar task → `/unknowns:loop <task description>` is all you need. Claude
  guides you through the rest, step by step.
- Only need one specific technique → invoke the individual skill below directly, or just
  say it in natural language and it auto-triggers.
- Works without slashes too: phrases like "do a blind spot pass", "interview me",
  "show me 4 design options", "quiz me" are themselves triggers.

**Skills at a glance** (1:1 with the original 11 examples):

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

## Skill-by-skill usage

### 1. `/unknowns:loop` — the full operating loop

**When**: Large or unfamiliar feature work, tasks with fuzzy specs, or whenever you want
to proceed "properly, by the book".

**Invoke**:
```
/unknowns:loop Add subscription renewal to the billing module
```
Auto-trigger phrases: "run the operating loop", "do the full loop",
"know your unknowns", "운영 루프로 진행해줘", "풀 루프로 해줘"

**How it runs**: Claude drives 10 stages in order —
1. Define value and completion criteria (agreed with you) → 2. blindspot investigation
(+ teach-me if needed) → 3. interview → 4. explore solutions and shape
(brainstorm/prototypes/reference, as needed) → 5. minimally verify the riskiest
assumptions → 6. plan ordered by likelihood-of-change (plan) → 7. implement + record
deviations (notes) → 8. independent verification → 9. quiz + handoff (+ buy-in if
needed) → 10. value review.

**Tip**: Tell it the size of the task and it trims the stages accordingly. Example:
```
/unknowns:loop This is medium-sized. Bug fix, but the root cause is unclear
```
→ shrinks to blindspot → interview → plan → implement → quiz.

---

### 2. `/unknowns:blindspot` — pre-implementation blind-spot investigation

**When**: Before touching a module, library, or domain you don't know well. When you're
in the "I don't know what I don't know" state.

**Invoke**:
```
/unknowns:blindspot Add Kakao OAuth to the auth module. Focus on git history and tests/
```
Auto-triggers: "blind spot pass", "what am I missing", "do a blind-spot investigation",
"사각지대 조사해줘", "내가 놓친 게 뭐지"

**How it runs**: It investigates **without modifying any code**. For large scopes it
delegates to the unknowns-scout agent. The output is one card per finding (HTML) or an
importance × impact table — risky assumptions / unknown unknowns / structural conflicts /
regression risks / questions to answer before implementing / prompt-strengthening info.

**Key deliverable**: an **improved prompt draft** assembled from the cards' "prompt
fixes". Copying that and using it as your actual implementation instruction is the whole
point of this skill.

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
Auto-triggers: "teach me", "make me an explainer", "I don't know the vocabulary of this
field", "가르쳐줘", "설명서 만들어줘", "이 분야 용어를 모르겠어"

**How it runs**: 3–7 decision axes you'll face in this task → a vocabulary ladder per
axis (everyday words → expert terms, with an example request per term) → before/after
comparisons per concept (live sliders when possible) → and finally a **precise request
draft: your original request rewritten in the new vocabulary**.

---

### 4. `/unknowns:interview` — pre-implementation interview

**When**: The spec is incomplete but you don't know what to ask. Right after a blindspot
investigation.

**Invoke**:
```
/unknowns:interview About the OAuth work we just investigated. Architecture questions first
```
Auto-triggers: "interview me", "ask me questions before implementing", "ask me questions
about the spec", "인터뷰해줘", "구현 전에 질문해줘"

**How it runs**: **At most 5** questions per round, in a fixed priority order
(architecture → data loss & security → compatibility → performance & cost → taste).
Each question comes with a one-line "why this matters", and multiple-choice questions
appear as AskUserQuestion dialogs. At the end it presents a **decision table plus a
ready-to-use implementation prompt**.

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
Auto-triggers: "show me 4 design options", "give me different designs",
"design options", "시안 4개 보여줘", "다양한 디자인으로"

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
etc.), it builds clickable mockups with A/B choice buttons.

---

### 6. `/unknowns:brainstorm` — map of the solution space

**When**: You know the problem but not what to do about it. Before jumping on the first
idea.

**Invoke**:
```
/unknowns:brainstorm 40% of new signups churn in the first week. Prefer things usable within 2 weeks
```
Auto-triggers: "brainstorm", "lay out candidate solutions", "show me options",
"브레인스토밍", "해법 후보 펼쳐줘", "옵션 보여줘"

**How it runs**: It lays out roughly 10 candidate interventions along a **time axis from
immediately-applicable to long-term bets**, each annotated with expected impact / effort
/ risk / how to measure. An impact × effort placement separates quick wins from big
bets, and the items you mark **resonate** get assembled into structured next steps.

---

### 7. `/unknowns:reference` — reference analysis

**When**: You have example code, a mockup, a screenshot, or a competitor product, and
you want something "like this".

**Invoke**:
```
/unknowns:reference legacy/billing.py — it's Python, port it to TypeScript in the new service
```
Auto-triggers: "use this code as reference", "use it as a reference", "make it like
this", "이 코드 참고해서", "레퍼런스로 써", "이거랑 비슷하게"

**How it runs**: Instead of copying the reference verbatim, it first presents a 4-way
analysis — **behavior that must be preserved / parts to adapt to the current environment
/ parts that are unnecessary or dangerous / parts that can be improved**. For porting
work it also produces a **proof of understanding (semantics map)** — reference excerpts
matched against the corresponding plan, gotcha notes, and an edge-case table. It
implements only after approval.

**Tip**: The reference doesn't have to be code — an HTML mockup, test code, a
screenshot, a real example of the desired output all serve as the "map".

---

### 8. `/unknowns:plan` — plan ordered by likelihood-of-change

**When**: Investigation and interview are done and you need a plan before implementing.

**Invoke**:
```
/unknowns:plan Using the OAuth spec we just finalized
```
Auto-triggers: "make a plan", "tweakable plan", "plan ordered by likelihood of change",
"계획 세워줘", "수정확률순으로 계획"

**How it runs**: Items are presented **in order of how likely they are to change**, not
execution order — decision items like schemas, interfaces, and UX contracts at the top,
each with the alternatives considered and its blast radius, while mechanical work is
folded away at the bottom. Approve/request-change selections assemble into your reply.
Includes verification method, risks, and rollback.

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
Auto-triggers: during implementation, Claude records deviations automatically when it
detects them itself. "Record a deviation" and "where did we diverge from the plan?"
("이탈 기록해줘", "어디서 계획이랑 달라졌어?") also trigger it.

**What gets recorded**: only decisions that affect design, behavior, or compatibility
(syntax, formatting, and variable naming are excluded). Each entry captures: the
situation encountered / how it differs from the plan / the response chosen / why /
alternatives discarded / risks / what to improve next time.

**Escalation**: decisions touching architecture, user-visible behavior, data, or
security must be recorded and then **work stops and the question goes to you**.

---

### 10. `/unknowns:quiz` — post-work comprehension check

**When**: Right after a big piece of work, just before creating a PR or merging. When
you're wondering "could I actually explain this?".

**Invoke**:
```
/unknowns:quiz Scoped to today's OAuth work
```
Auto-triggers: "quiz me", "give me a quiz", "check whether I understood this",
"퀴즈 내줘", "내가 이해했는지 확인해줘"

**How it runs**: 1. An explanation first (structure of the changes / 3 key design
decisions / where it's most likely to fail / what you should verify yourself) →
2. 5 questions (incident response > design rationale > behavior prediction, avoiding
rote recall; if IMPLEMENTATION_NOTES exists, at least 1 question covers a deviation
point) → 3. Grading — each wrong answer points to the exact change site you should
revisit → 4. A handoff summary (written as if another developer takes over tomorrow).
On request, it converts into a PR body draft.

---

### 11. `/unknowns:buy-in` — reviewer persuasion doc

**When**: Implementation and verification are done and you need **approval** from
reviewers or stakeholders.

**Invoke**:
```
/unknowns:buy-in This billing refactor. Reviewers are the backend lead and the security team
```
Auto-triggers: "buy-in doc", "prep me for review", "prepare for merge approval",
"buy-in 문서", "리뷰 준비해줘", "머지 승인 준비"

**How it runs**: Demo first (at the very top) → preemptive answers to roughly 5
anticipated reviewer objections, backed by evidence (tests, benchmarks, code locations)
→ known limitations and unresolved unknowns (linked with IMPLEMENTATION_NOTES) → the
people/teams whose sign-off is needed and each one's checklist → rollback plan. Where
quiz verifies your own understanding, buy-in prepares other people's trust.

---

## Using the agents

Agents are specialists that run in a separate context. Just name them in natural
language.

**unknowns-scout** (read-only reconnaissance):
```
Use the unknowns-scout agent — investigate what I'm missing in the migration plan
Scout the auth module with the unknowns-scout agent
```
The blindspot skill also calls this agent automatically for large investigations.
It never modifies files, and returns an investigation table plus an improved prompt
draft.

**independent-reviewer** (independent verification):
```
Use the independent-reviewer agent — verify the implementation we just finished before merge
Run an independent verification
```
It treats the implementing session's explanation **as claims only** and verifies
directly by reading code and running tests. It returns findings classified as
Critical/Warning/Info plus a "verified OK" list (distinguishing silence from
not-reviewed). Stage 8 of the loop skill calls it automatically.

---

## Hook behavior and configuration

**What it does**: once file edits (Edit/Write) in a session **reach 10, exactly once**,
it delivers the reminder "if you deviated from the plan, record it in
IMPLEMENTATION_NOTES.md" to both the user's screen and Claude's context (so that Claude,
the one actually doing the recording, receives it too). No blocking, no interference —
one message line is all it is.

**Configuration**:

| What you want | How |
|---------------|-----|
| Change the threshold (e.g. 20 edits) | Environment variable `UNKNOWNS_NOTES_THRESHOLD=20` |
| Turn it off | `UNKNOWNS_NOTES_THRESHOLD=0` |
| Repeat the reminder at every multiple of the threshold | `UNKNOWNS_NOTES_REPEAT=1` |
| Legacy variable | `FIELD_GUIDE_NOTES_THRESHOLD` is still recognized (the new variable wins) |
| Requirements | `python3` (standard library only, no external dependencies) |

**Manual install without the plugin** (Method C users): copy
`hooks/scripts/impl_notes_reminder.py` into your project and add to
`.claude/settings.json` (or your vault's hooks.json):
```json
"PostToolUse": [{
  "matcher": "Edit|Write",
  "hooks": [{ "type": "command",
    "command": "python3 <script path>/impl_notes_reminder.py", "timeout": 5 }]
}]
```

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

**Q. Why `/unknowns:blindspot` and not `/blindspot`?**
Plugin skills are namespaced as `pluginname:skillname` to avoid name collisions. If you
want the short names, install via Method C (copy individual skills).

**Q. I installed this as field-guide before.**
That's the old 0.1.x name. Follow the "Upgrading from the old version" section above:
uninstall, then reinstall. Skill mapping: `reference-map`→`reference`,
`impl-notes`→`notes`; the rest keep their names.

**Q. The hook never fires.**
That's most likely normal — the default is once per session, and only when edits reach
10. Check Python with `python3 --version` and check the `UNKNOWNS_NOTES_THRESHOLD`
value.

**Q. The hook is annoying.**
Set `UNKNOWNS_NOTES_THRESHOLD=0`, or raise the threshold to around 30.

**Q. Where does the plugin differ from the original material?**
`skills/loop/references/talk-source.md` has a table separating "verified directly from
the source" from "extended during authoring".

---

## Sources

- Example collection: https://thariqs.github.io/html-effectiveness/unknowns/ ("Know your unknowns")
- Parent essay: https://thariqs.github.io/html-effectiveness/ ("The unreasonable effectiveness of HTML")
- Talk: https://www.youtube.com/watch?v=9fubhllmsBU (AI Engineer World's Fair 2026)
- Verification details and related literature: `skills/loop/references/talk-source.md`
