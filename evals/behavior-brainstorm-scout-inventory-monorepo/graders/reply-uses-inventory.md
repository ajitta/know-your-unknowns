---
type: llm
focus: trace
---

Judge the assistant's final reply against the report the unknowns-scout agent handed back (every report, if the scout was spawned more than once). If no unknowns-scout agent was spawned, the verdict is FAIL.

The brainstorm skill's step 2c says: "When the scout returns, put its **Questions to answer**, **Information still needed** and **Needs checking** lists above the candidates in step 3, for the user to answer or check." In step 3 a candidate carries "`Already exists — <where>`, when the candidate builds on something step 2 found".

1. At least two candidates build on mechanisms in the scout's inventory and carry an "Already exists — <where>" line (the same label in close wording counts), whose where is the place the inventory gives for that mechanism.
2. Each item of the scout's Questions to answer, Information still needed and Needs checking lists appears in the reply above the candidates; merged or reworded items count. A list the scout returned empty or left out needs nothing.

Fail if fewer than two candidates carry the where of an inventory row, or if any item of the scout's three lists appears only below the candidates or not at all.
