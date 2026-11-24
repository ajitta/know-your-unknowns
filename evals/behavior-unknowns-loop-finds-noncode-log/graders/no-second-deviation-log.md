---
type: file_exists
path: "**/DEVIATIONS.md"
exists: false
---

fair/DEVIATIONS.md was in the folder before the run, so it is never a file the run
created. This grader fails only when the run creates another `DEVIATIONS.md` (at the
folder root, for example) instead of appending to the one beside the programme.
