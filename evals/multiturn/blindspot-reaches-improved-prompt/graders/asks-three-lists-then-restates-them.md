---
type: llm
focus: transcript
---

The pass collects the user's before-picture first and keeps it. All of these must hold:

1. Before presenting any findings, the assistant asks the user, once, for three things:
   what they are already sure of, what they are assuming, and where they do not know how
   to judge. The first reply asks this and does not already present the findings.
2. The reply that presents the findings opens by restating the user's three lists (in
   any wording or language that keeps their content), before the findings.
3. The user's stated assumptions are treated as things to check first: each one (indexer
   reacting to `updated_at`, the export leaving deleted rows out, the unique constraint
   staying as is) is addressed in the findings rather than taken as settled.

Fail if the assistant skips the three-list question, asks it again after it was
answered, or presents findings that ignore the user's answers.
