---
name: notes
description: >
  Implementation notes — log significant deviations from the plan while working.
  Use automatically when implementation hits an unknown the plan did not cover, and on
  "implementation notes", "record a deviation", "where did we diverge from the plan?".
---

# Notes — Plan Deviation Log (Implementation Notes)

When work hits a situation the plan/spec does not cover (an unknown), **pick the conservative option, log it, and keep going**. The log is where the user sees where the territory departed from the map, and why.

## Procedure

1. Take the entry from the request: text given with the skill name is the **Situation found**, and the rest of the entry is filled from context. With no text, log the most recent unplanned decision of this session, or say there is none.
2. Append the entry to `IMPLEMENTATION_NOTES.md` at the project root before ending the turn, creating the file with the heading `# Implementation Notes — plan deviation log` if it is missing. buy-in and quiz read that record. Without a tool, do the step in the conversation and say what could not be checked.
3. While working, check for deviations before a commit and before handing work back.

## Entry Format

Deviation entry — two blocks that do **not** carry equal weight. Fill Observed from the artifacts first, and keep it as found when you write Attributed:

```markdown
## [YYYY-MM-DD] <task/feature name>

**Observed** — the record, auditable against the diff
- **Situation found**: what unplanned thing was hit
- **Deviation from plan**: what the plan said (quote it, or "not covered")
- **Response chosen**: what the code now does

**Attributed** — hypothesis, not evidence
- **Reason for choice**: why that approach
- **Alternatives considered**: discarded options and why discarded
- **Risk/follow-up check**: if this decision is wrong, where it shows up
```

**Why the split.** A stated reason is a hypothesis: models and people both produce fluent rationales that omit what actually drove the choice. Observed earns trust only by being checkable against the diff; Attributed is a claim to test later. On conflict, the diff wins.

When context does not say which alternatives were weighed, fill **Alternatives considered** with the plausible options you can name, each with why it loses here, marked *(inferred, not stated)*. If no other option was viable, say why. A bare "none" or "not recorded" leaves the field unfilled. Attributed is hypothesis already, so a marked inference stays honest, and a reviewer can challenge the choice only against named alternatives.

A **Discovery** is the lighter entry, one line in the same file: code or environment differs from what the plan assumed and no decision is needed yet. Log what was assumed / what is true.

## Logging Criteria

- **Log**: decisions affecting design/behavior/compatibility, points where spec interpretation diverges, existing code structure differing from expectation, workarounds, new dependencies.
- **Don't log**: trivial syntax fixes, formatting, variable names, self-evident implementation details.

## Wrap-up

Before ending the session or creating a PR:

1. List first the entries whose decision touches architecture, user-visible behavior (UX/API contract), data or security: the user reviews those calls before anything else.
2. Summarize the remaining entries.
3. Write the **fold back into the plan** block: 3 copyable bullets on what this changes about attempt #2, so the next run does not rediscover today's surprises.
4. Suggest continuing with the **quiz** skill.
5. If the work needs approval, carry this log's unresolved items into the **buy-in** skill doc as "known limitations".
