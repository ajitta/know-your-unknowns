---
type: llm
focus: last_message
---

The user asked to be taught a domain's vocabulary. All of these must hold:

1. The response defines each term the user quoted, in plain language.
2. It relates the terms to each other -- where each one sits in the payment lifecycle.
3. It does NOT investigate a codebase for landmines, unwritten conventions or earlier
   attempts, and does not deliver a "here is what you are actually walking into"
   risk inventory about this repository.

Fail if the response is a risk investigation of code rather than an explanation of
the domain.
