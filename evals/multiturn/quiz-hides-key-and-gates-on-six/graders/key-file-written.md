---
type: tool_used
tool: Write
input_match: quiz-[^"]*-key\.md
turn: all
min: 1
weight: 0.5
---

With a writable sandbox, the skill commits the teach-back key to
`.unknowns/<date>-quiz-<slug>-key.md` before asking. This checks the file was written
at all; the judged graders check that its content stayed hidden until the answer.
