---
type: file_exists
path: .unknowns/**
exists: false
---

The tweakable-plan skill keeps its plan in the conversation as Markdown, so any file
under `.unknowns/` would mean the small case produced a document anyway. `Write` is
granted for this case precisely so that this check can fail: with no writing tool it
would pass vacuously and mean nothing.
