---
name: notes
description: >
  Implementation notes — log every significant deviation from the plan while working.
  This skill should be used automatically whenever implementation encounters a
  situation not covered by the plan or spec (an "unknown") and a non-trivial decision
  is made, and when the user says "implementation notes", "impl notes", "이탈 기록",
  "임플 노트", "log deviations", "record a deviation", "where did we diverge from
  the plan?", "어디서 계획이랑 달라졌어?", or asks where/why the work diverged from
  the plan.
argument-hint: "[init | show | <content to log>]"
---

# Notes — Plan Deviation Log (Implementation Notes)

When work hits a situation not in plan/spec (unknown), **do not decide arbitrarily and pass silently — log it**. Origin: Thariq Shihipar — "If it runs into an unknown, ask it to log it, so you can see where the deviations happened and figure out why." Core device stopping agent from silently drifting off-plan.

## File Rules

- Location: `IMPLEMENTATION_NOTES.md` at project root (create if missing).
- Argument `init`: create file with empty template. Argument `show`: summarize current notes.

## Entry Format (per entry)

```markdown
## [YYYY-MM-DD] <task/feature name>
- **Situation found**: what unplanned thing was hit
- **Deviation from plan**: what the original plan was
- **Response chosen**: what was done (if conservative choice, why)
- **Reason for choice**: why that approach
- **Alternatives considered**: discarded options and why discarded
- **Risk/follow-up check**: if this decision is wrong, where it shows up
- **Improvements for next attempt**: what to do differently on same task next time (1–3)
```

## Logging Criteria

- **Log**: decisions affecting design/behavior/compatibility, points where spec interpretation diverges, existing code structure differing from expectation, workarounds, new dependencies.
- **Don't log**: trivial syntax fixes, formatting, variable names, self-evident implementation details.

## Escalation

Not just log — **stop work and ask user** when:
- Decision changes architecture
- Decision changes user-visible behavior (UX/API contract)
- Decision touches data loss/security

## Wrap-up

Before ending session or creating PR, summarize accumulated note entries to user and suggest continuing with `/unknowns:quiz`. If work needs approval, reflect this note's unresolved items into the `/unknowns:buy-in` doc as "known limitations".
