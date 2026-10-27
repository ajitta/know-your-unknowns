---
name: notes
description: >
  Implementation notes — log significant deviations from the plan while working.
  Use automatically when implementation hits an unknown the plan did not cover, and on
  "implementation notes", "record a deviation", "where did we diverge from the plan?".
---

# Notes — Plan Deviation Log (Implementation Notes)

When work hits a situation the plan/spec does not cover (an unknown), **do not decide arbitrarily and move on silently: log it**. This log is what keeps the agent from drifting off-plan unnoticed.

## File Rules

- **Location**: `IMPLEMENTATION_NOTES.md` at the project root; append to it, creating it if missing. buy-in and quiz read that record. Without a tool, do the step in the conversation and say what could not be checked.

- **Record deviations while working**: re-read the logging criteria at each stage boundary, before a commit, and before handing work back. When work departs from the plan, append the deviation to IMPLEMENTATION_NOTES.md before ending the turn.

- **Arguments**:

  | Argument | What to do |
  |---|---|
  | `init` | Run the `init` steps below. |
  | `show` | Summarize current notes. |
  | Any other text | Append an entry using that text as **Situation found**, filling remaining fields from context; ask only about what context cannot supply. |
  | No argument | Log the most recent unplanned decision of this session, or state that there is none. |

  `init` steps:

  a. When the file is missing, create it: heading `# Implementation Notes — plan deviation log`, then a commented-out copy of Entry Format as the template. When it exists, leave its entries unchanged and say so.

  b. Offer (never write silently) to append a 3–5 line deviation-log rule — log criteria, escalation, file path — to the project's `CLAUDE.md` or `.claude/rules/unknowns.md`, so the rule is in context for every later session, not only when this skill is invoked.

## Entry Format

Deviation entry — two blocks that do **not** carry equal weight. Fill Observed from the artifacts first, and never revise it to fit Attributed:

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

Two lighter kinds, same file, one line each:

| Entry | When | What to do |
|---|---|---|
| **Discovery** | Code or environment differs from what the plan assumed, no decision needed yet. | Log one line: what was assumed / what is true. |
| **Todo for human** | A judgment call that belongs to the user but blocks neither merge nor QA, and falls outside every stop-and-ask case below (it changes no architecture, no user-visible behavior, no data or security). | Log it and keep working. |

If a judgment call touches any of those (architecture, user-visible behavior, data, or security), it is not a Todo — escalate. When unsure whether it is a Todo, escalate: a question costs one round trip, a silent contract change costs a revert.

## Logging Criteria

- **Log**: decisions affecting design/behavior/compatibility, points where spec interpretation diverges, existing code structure differing from expectation, workarounds, new dependencies.
- **Don't log**: trivial syntax fixes, formatting, variable names, self-evident implementation details.

## Escalation

When a deviation invalidates a **decision item** of the approved plan (schema, public interface, UX contract), the log entry does not close it:

1. Revise that item in the plan document itself.
2. Mark it *revised — needs re-approval*.
3. Get the user's approval before building on it.

Deviations from mechanical items need only the log entry, not a plan revision; the stop-and-ask cases below still apply.

When a decision does any of the following, do more than log — **stop work and ask the user**:
- Decision changes architecture
- Decision changes user-visible behavior (UX/API contract)
- Decision touches data or security

## Wrap-up

Before ending the session or creating a PR:

1. Summarize the accumulated entries.
2. Write the **fold back into the plan** block: 3 copyable bullets on what this changes about attempt #2, so the next run does not rediscover today's surprises.
3. List any open **Todo for human** items beside the fold back into the plan block.
4. Suggest continuing with the **quiz** skill.
5. If the work needs approval, carry this log's unresolved items into the **buy-in** skill doc as "known limitations".
