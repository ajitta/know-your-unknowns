---
name: notes
description: >
  Implementation notes — log significant deviations from the plan while working.
  Use automatically when implementation hits an unknown the plan did not cover, and on
  "implementation notes", "record a deviation", "where did we diverge from the plan?",
  "이탈 기록", "임플 노트", "어디서 계획이랑 달라졌어?".
argument-hint: "[init | show | <content to log>]"
---

# Notes — Plan Deviation Log (Implementation Notes)

When work hits a situation not in plan/spec (unknown), **do not decide arbitrarily and pass silently — log it**. Core device stopping agent from silently drifting off-plan. Origin: Implementation Notes — see skills/loop/references/talk-source.md.

## File Rules

- Location: `IMPLEMENTATION_NOTES.md` at project root (create if missing).
- **Persistence**: once the file exists or `init` has been run, appending to the file is mandatory — a chat-only summary does not satisfy the rule (the reminder hook, buy-in and quiz all read the file). With no file, a chat summary is allowed, but the final message must then say there is no notes file.
- Argument `init`: create the file — heading `# Implementation Notes — plan deviation log`, then a commented-out copy of Entry Format as the template. Then offer (never write silently) to append a 3–5 line deviation-log rule — log criteria, escalation, file path — to the project's `CLAUDE.md` or `.claude/rules/unknowns.md`, so the rule is in context for every later session, not only when this skill is invoked.
- Argument `show`: summarize current notes.
- Any other text: append an entry using that text as **Situation found**, filling remaining fields from context; ask only about what context cannot supply.
- No argument: log the most recent unplanned decision of this session, or state that there is none.

## Entry Format

Deviation entry:

```markdown
## [YYYY-MM-DD] <task/feature name>
- **Situation found**: what unplanned thing was hit
- **Deviation from plan**: what the original plan was
- **Response chosen**: what was done (if conservative choice, why)
- **Reason for choice**: why that approach
- **Alternatives considered**: discarded options and why discarded
- **Risk/follow-up check**: if this decision is wrong, where it shows up
```

Two lighter kinds, same file, one line each:
- **Discovery** — code or environment differs from what the plan assumed, no decision needed yet: what was assumed / what is true.
- **Todo for human** — a judgment call that belongs to the user but blocks neither merge nor QA. Log it and keep working.

## Logging Criteria

- **Log**: decisions affecting design/behavior/compatibility, points where spec interpretation diverges, existing code structure differing from expectation, workarounds, new dependencies.
- **Don't log**: trivial syntax fixes, formatting, variable names, self-evident implementation details.

## Escalation

Not just log — **stop work and ask user** when:
- Decision changes architecture
- Decision changes user-visible behavior (UX/API contract)
- Decision touches data loss/security

## Wrap-up

Before ending session or creating PR: summarize accumulated entries, then write the **fold back into the plan** block — 3 copyable bullets on what this changes about attempt #2, so the next run does not rediscover today's surprises — and list any open **Todo for human** items beside it. Suggest continuing with `/unknowns:quiz` (or `/quiz` for copied installs). If work needs approval, reflect this note's unresolved items into the `/unknowns:buy-in` doc as "known limitations".
