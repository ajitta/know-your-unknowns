# Surfaces — where these skills run, and what is missing where

The skills are written for Claude Code, where there is a project directory, sub-agents and hooks. They also load in Claude Desktop, Claude web and Cowork, where some of that is absent. This file is the one place that says what to do instead. When a step calls for a tool the current session does not have, read this file — never silently skip the step.

## What each surface has

| | Claude Code | Cowork | Desktop / web chat | Mobile |
|---|---|---|---|---|
| Skills | yes | yes | yes | not documented |
| Sub-agents (Agent tool) | yes | yes | no | no |
| Hooks | yes | yes | no | no |
| Project files that persist | yes (the repo) | yes (connected folder) | session only | no |
| Artifact publishing | yes | yes | yes | view only |
| Slash invocation | `/unknowns:<skill>` | by name | by name | by name |

The columns are defaults, not a detection rule: a session's own tool list decides. Every substitute below is keyed to a tool being absent (for hooks, to a marker line being absent), never to the surface's name. For example, a Claude app task that runs in a cloud workspace is started from web or desktop, yet it can carry the Agent tool and this plugin's agents.

"By name" means the skill is model-invoked: say the trigger phrase, or name the skill ("run the blindspot skill on this"). There is no namespace prefix outside Claude Code.

## Substitutes

**No sub-agent (Agent tool absent).** Two steps want a reader who has not seen the work: blindspot's scout and the loop's independent verification. A fresh thread is the substitute, never a fork or a summary of the work written by whoever did the work.

- Hand the user a self-contained review packet to paste into a **new conversation**: done criteria, the approved plan, the deviation log, the diff or the files touched, how to run the tests, and a list of the **claims** the work rests on (facts about APIs, data or the domain, and reasoning the design depends on).
- Say plainly that this packet stands in for the sub-agent and that a same-thread review would not be independent.
- For blindspot's scout, investigate directly instead and say the scope was narrowed to what one pass can read.

**No hooks.** The plugin's SessionStart hook announces `[unknowns] hooks active` wherever a notes reminder is still to come (and restates it after compaction), because a tool list shows whether a tool exists but nothing shows whether hooks run.

When no `[unknowns] hooks active` line is in context, or the one reminder was already delivered, nothing more will fire, so the discipline is the skill's own: re-read the logging criteria at every natural break — before a commit, before handing work back, after roughly ten file edits.

**No persistent project files.** `IMPLEMENTATION_NOTES.md`, `.unknowns/loop.json` and `.unknowns/scorecard.md` have nowhere durable to live. In order:

1. **Code execution available** (Desktop, web, Cowork) →

   a. Keep the real file in the session workspace, exactly as named.

   b. Give the user the file itself at every wrap-up, so a closed conversation does not lose it.

   c. Say once that the file lives in the session, not in their repo.

2. **Nothing writable** (mobile, tool-free chat) →

   a. Keep the log in the conversation and **restate it in full** each time it grows, so the newest message always holds the whole log.

   b. Tell the user once that the log will not survive the conversation, and that the wrap-up block is the thing to paste into their repo.

Either way the content rules do not relax: the same entry format, the same escalation rule, the same wrap-up. What changes is only where the bytes sit.

**Connected-folder sessions (Cowork, or Desktop with a folder attached).** Treat the connected folder as the project root: the notes file and `.unknowns/` belong beside the code, not in a scratch directory.

## What not to do

- Do not claim a step ran when its tool was missing. Name the substitute you used.
- Do not review your own implementation in the thread that produced it and call it independent verification.
- Do not drop the deviation log because there is no file to write. A log restated in chat still beats a decision nobody recorded.
