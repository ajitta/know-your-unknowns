---
type: tool_used
tool: Skill
input_match: unknowns:unknowns-loop
min: 0
max: 0
arm: both
---

The Claude Code build sets `disable-model-invocation: true` on unknowns-loop
(claude-code/skill-frontmatter.json, owner decision 2026-11-26), so Claude Code
blocks a Skill call to it unless the user's message names it. This must-NOT-fire
check keeps that build setting honest. The upload zips keep the trigger phrase; the
`trigger-*-unknowns-loop` cases (tag `upload-build-only`) measure it there.
