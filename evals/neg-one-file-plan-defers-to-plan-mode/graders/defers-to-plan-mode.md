---
type: llm
focus: last_message
---

The task is a one-file change with no schema, interface or UX-contract decision --
below the plan skill's own size gate. All of these must hold:

1. The response either says the task is small enough not to need a full
   pre-implementation planning document and points at the built-in plan mode, or
   simply gives a short inline plan of a few steps.
2. It does NOT deliver a document with decision cards sorted by likelihood of being
   tweaked, alternatives-considered blocks, blast-radius notes, rollback methods and
   a weakest-part-of-this-plan section.
3. It does not start editing files.

Fail if the response produces the full tweak-likelihood planning document for this
one-file change.
