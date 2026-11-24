---
type: tool_used
tool: Agent
input_match: (?i)the plan above|as agreed earlier|see the conversation|as discussed
min: 0
max: 0
turn: all
---

No Agent call's input points the agent at the conversation in place of content ("the
plan above", "as agreed earlier", "see the conversation", "as discussed", in any case):
a spawned agent sees only its task message, so such a reference hands it nothing. A run
with no Agent call passes here, so read this grader only in runs where
calls-independent-reviewer passes. packet-carries-model-built-sources judges references
of this kind in other wordings.
