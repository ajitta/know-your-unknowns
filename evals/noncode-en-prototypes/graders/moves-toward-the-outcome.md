---
type: llm
focus: last_message
---

The reply shows contrasting versions to react to, aiming at the outcome (a role the
user actually wants) rather than one finished job description. All of these must hold:
1. It offers several versions (about 3-5) that differ in philosophy (e.g. scope,
   seniority, focus, structure), not small wording variations, each with a one-line
   philosophy and when it fits.
2. It asks the user to react: what to keep or drop from each, and for a skipped
   element what would have made it a keeper.
3. It says it will turn the reactions into a list of requirements for the role, or
   says the set can grow if reactions keep coming.
4. It does not settle on one version for the user.
Fail if the reply forces software concepts onto the task (code, repositories, tests, pull requests, implementation) where the user's work has none.
