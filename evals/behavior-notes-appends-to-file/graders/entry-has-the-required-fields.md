---
type: llm
focus:
  source: file
  path: IMPLEMENTATION_NOTES.md
---

The file is a plan-deviation log. All of these must hold:

1. It contains an entry for this deviation, with a date and a task or feature name.
2. The entry records the situation that was found, what the plan had said, what was
   chosen instead, and why.
3. The entry records the discarded alternatives and the risk or follow-up check if
   the choice turns out to be wrong.

Fail if the file exists but holds only a one-line note or an unfilled template.
