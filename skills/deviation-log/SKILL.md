---
name: deviation-log
description: >
  Deviation log (implementation notes) — while doing any planned work, log each
  significant departure from the plan, why, and what the user still has to judge, beside
  the deliverable. Use automatically when the work hits an unknown the plan did not
  cover, and on "implementation notes", "record a deviation", "where did we diverge from
  the plan?". Clear to both: no skill or method; if weighty (ships, is sent, hard to
  undo), first read back request, assumptions and what done means in 2–3 lines; a
  mismatch goes to teach-me, interview or blindspot.
---

# Deviation Log

This skill serves what neither the user nor you know yet, and surfaces both sides' unknowns.

When you and the user both seem to understand the request, do it without this method: if its result carries weight (it ships, is sent or is hard to undo), first read back in 2–3 lines the request as you understand it, the assumptions you are making and what outcome counts as done, as the whole reply, and do it once the user confirms; a self-evident request (fix a typo) needs no read-back. When the read-back exposes a mismatch, route by who does not know: the user → the **teach-me** skill; you → the **interview** skill; neither of you → the **blindspot** skill. A misread weighty request costs the work built on it; a read-back costs one exchange.

When work hits a situation the plan or spec does not cover (an unknown neither side saw), **pick the conservative option, log it, and keep going**. The log is where the user sees where the territory departed from the map, and why.

## Procedure

1. Take the entry from the request: text given with the skill name is the **Situation found**, and the rest of the entry is filled from context. With no text, log the most recent unplanned decision of this session, or say there is none.
2. Append the entry to the deviation log before ending the turn, creating the file if it is missing:

   | Work | Log file | Heading when created |
   |---|---|---|
   | Code | `IMPLEMENTATION_NOTES.md` at the project root | `# Implementation Notes — plan deviation log` |
   | Anything else | the file the user names, or `DEVIATIONS.md` beside the deliverable | `# Deviation log — <deliverable>` |

   The **buy-in** and **quiz** skills read that log. Without a tool, do the step in the conversation and say what could not be checked.
3. While working, check for unlogged deviations at each checkpoint (a commit, a shared draft) and before handing the work over, and append each one as in step 2.
4. When a deviation invalidates a decision in the plan document, mark that decision in the plan as superseded by the entry's date, so the plan stays the map the work follows.

## Entry Format

Deviation entry — two blocks that do **not** carry equal weight. Fill Observed from the artifacts first, and keep it as found when you write Attributed:

```markdown
## [YYYY-MM-DD] <task/feature name>

**Observed** — the record, auditable against the work
- **Situation found**: what unplanned thing was hit
- **Deviation from plan**: what the plan said (quote it, or "not covered")
- **Response chosen**: what the work now does

**Attributed** — hypothesis, not evidence
- **Reason for choice**: why that approach
- **Alternatives considered**: discarded options and why discarded
- **Risk/follow-up check**: if this decision is wrong, where it shows up, and what only the user can judge
```

**Why the split.** A stated reason is a hypothesis: models and people both produce fluent rationales that omit what actually drove the choice. Observed earns trust only by being checkable against the work as it stands (the diff, the document, the booking); Attributed is a claim to test later. On conflict, the work as it stands wins.

When context does not say which alternatives were weighed, fill **Alternatives considered** with the plausible options you can name, each with why it loses here, marked *(inferred, not stated)*. If no other option was viable, say why. A bare "none" or "not recorded" leaves the field unfilled. Attributed is hypothesis already, so a marked inference stays honest, and a reviewer can challenge the choice only against named alternatives.

When the choice rests on something only the user can know (their priorities, a person's preference, a local rule), name it in **Risk/follow-up check**: the conservative option was your guess, and the wrap-up puts it to the user.

A **Discovery** is the lighter entry, one line in the same file: the territory differs from what the plan assumed and no decision is needed yet. Log what was assumed / what is true.

## Logging Criteria

- **Log**: decisions affecting design, behavior or compatibility; points where the spec's interpretation diverges; an existing structure (code, a venue, a dataset) differing from expectation; workarounds; new dependencies, suppliers or commitments.
- **Don't log**: trivial wording or syntax fixes, formatting, names, self-evident details.

## Wrap-up

Before ending the session or handing the work over (a PR, a submitted draft, a handoff):

1. List first the entries whose decision touches the structure of the work, what others see or were promised (e.g. a UX/API contract, a published date), data or money, or security and safety: the user reviews those calls before anything else, starting with the ones that rest on something only the user can know.
2. Summarize the remaining entries.
3. Write the **fold back into the plan** block: 3 copyable bullets on what this changes about attempt #2, so the next run does not rediscover today's surprises.
4. Suggest continuing with the **quiz** skill.
5. If the work needs approval, carry this log's unresolved items into the **buy-in** skill doc as "known limitations".
