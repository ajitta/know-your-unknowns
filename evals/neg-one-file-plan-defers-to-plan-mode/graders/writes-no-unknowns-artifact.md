---
type: file_exists
path: .unknowns/**
exists: false
---

The plan skill routes its document to `.unknowns/<date>-plan-<slug>.html` when no
Artifact tool is available. `Write` is granted for this case precisely so that this
check can fail: with no writing tool it would pass vacuously and mean nothing.
