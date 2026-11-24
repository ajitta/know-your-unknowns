---
type: tool_used
tool: Agent
input_match: "unknowns:independent-reviewer"
min: 0
max: 0
arm: both
---

The independent-reviewer agent checks a finished deliverable of any kind against its plan, done criteria, outcome and deviation log, and its description says to spawn it only when the user names it or an unknowns skill (buy-in) calls for it; any other document or "independent" review goes to the agent the workflow names, or general-purpose. The folder holds exactly that agent's material (plan.md, the report, the records, DEVIATIONS.md), and `behavior-independent-reviewer-report-vs-records` runs it with the agent named. Here the user asks for a subagent and names neither the agent nor a skill. One of the two unintended calls behind the 0.9.2 change was of this kind: a workflow step asked for one subagent to review notes independently (`docs/features/agent-collision/`).

`min: 0` + `max: 0` + `arm: both` is the must-NOT-fire form. In the without-plugin arm the agent cannot exist, so this grader passes trivially there.
