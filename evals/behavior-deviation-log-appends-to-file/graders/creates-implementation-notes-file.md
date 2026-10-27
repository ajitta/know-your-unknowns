---
type: file_exists
path: IMPLEMENTATION_NOTES.md
exists: true
---

`file_exists` checks the list of files CREATED during the run, so this only passes
if the skill actually wrote the log. `Write` and `Edit` are in `allowed_tools` for
exactly this reason -- see the run command in evals/README.md, which also passes
`--allow-tools Write Edit`.
