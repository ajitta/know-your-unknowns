# Surfaces — use the tools the current session exposes

The skills deliver Markdown in the conversation on Claude Code, claude.ai web/desktop/mobile, ChatGPT web/mobile, and Codex CLI. Named Claude agents are available only in Claude Code; other hosts use the separate-pass substitute below. ChatGPT and Codex behavior is expected; not yet checked by the owner.

A tool list determines what can run. Never infer tool availability from the app's name or claim a check ran without its result.

## Questions

Keep the skill's question count, priority, and approval gate. If a question tool accepts fewer questions than the skill's round, split the round across calls without increasing its total.

Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

## Scout and reviewer passes

Use `unknowns:unknowns-scout` or `unknowns:independent-reviewer` when the host can start a sub-agent of that name.

Keep the scout pass read-only: never create or modify files, run implementation commands, or invent findings. Read available history records; hand history questions that require unavailable tools back to the caller. Return evidence and status for each finding, and list what could not be checked.

The reviewer receives this packet:

- done criteria (step 1 / the plan's done-criteria section)
- the approved plan (step 6)
- the `IMPLEMENTATION_NOTES.md` path
- the diff range / touched files
- how to run the tests
- a list of the **claims** the work rests on (facts about APIs, data or the domain, and reasoning the design depends on), for the reviewer's claim-type check

Never give the reviewer the implementer's own summary. With no file system, supply the conversation's saved plan, deviation record, and code excerpts in place of file paths.

Keep the review read-only: never edit or commit repository files or write outside a temporary directory. Check plan/spec conformance, recorded deviations, tests-pass-but-reality-fails cases, verified OK areas, and factual and reasoning claims against their evidence. Run available tests, lint and builds only when they can obey that read-only contract; report checks you cannot run.

No scout sub-agent → do the scout pass yourself as a separate step and label it "Scout pass performed by the assistant". Use the packet the calling skill would hand the scout and the scout read-only contract above.

For independent verification:

No sub-agent → hand the user the same packet to paste into a new conversation, and say that review stands in for the agent. The independent verification stage stays pending until that review returns. Use the same read-only contract.

No file access, search, or execution tools → check only the supplied material, ask for missing evidence, and report unverified areas. Never invent files, history, command output, or test results.

## Records

Use `IMPLEMENTATION_NOTES.md`, `.unknowns/loop.json`, and `.unknowns/scorecard.md` in the current project when a file system is available. Treat a connected folder as the project root.

With a writable session workspace but no project root, keep the same named files there, say they are session-local, and give them to the user at every wrap-up.

Read-only project records → read them in place and print updates in the conversation as complete Markdown records, saying which named files the user should save them as. Keep quiz keys hidden until the user answers, as below.

No file system → print the record in the chat as Markdown and say which named file the user should save it as. Restate the whole updated record whenever it changes, so the newest message holds the full log or tracker. On resume in another conversation, ask for that saved record instead of inventing its contents.

Keep a quiz key hidden until the user answers. Without a file system, choose the key before asking, disclose at grading that it was not committed to a file in advance, and print it only with the grading result.

## Deviation discipline

At each stage boundary, before a commit, and before handing work back, check whether work departed from the plan. Append design, behavior, or compatibility deviations to `IMPLEMENTATION_NOTES.md` before ending the turn. Apply the notes skill's entry format and escalation rules; stop and ask before changing architecture, user-visible behavior, data, or security.

No file system → print the record in the chat as Markdown and say to save it as IMPLEMENTATION_NOTES.md.

## Prototypes and verification

Write requested prototype code to files when the host can write files. Keep the comparison, reactions, and requirements in Markdown in the conversation.

No file system → present proposed code or mockup states in Markdown for the user to save. No execution tool → give run instructions, ask for execution evidence, and mark the result unverified until it arrives.
