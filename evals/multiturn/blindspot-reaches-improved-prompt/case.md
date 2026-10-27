---
description: "Blind-spot pass carried past its opening question: after the user answers the three lists, the pass must end with an improved prompt to paste back"
tags: [multiturn, behavior, en, blindspot]
runs: 3
max_turns_per_reply: 12
user_turns: 3
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Do a blind spot pass on this before I start. I am adding soft delete to our documents
table: a deleted_at timestamp, and every existing query gets WHERE deleted_at IS NULL.
There are about 30 queries across the API, a nightly export job, and a search indexer
that reads the table directly.

## Persona

You are a backend developer on a Postgres + Python service. The code is not available
in this conversation: if the assistant asks for paths or files, say it has no access and
should work from your description.

What you are sure of (checked last week):
- All 30 API queries go through one `DocumentRepository` class.
- Comments and attachments reference `documents.id` with foreign keys that use
  `ON DELETE CASCADE`.

What you are assuming but have not checked:
- The search indexer will drop a document once `deleted_at` is set, because it re-reads
  rows whose `updated_at` changed.
- The nightly export job should simply leave deleted documents out.
- The unique constraint on `(workspace_id, slug)` can stay as it is.

What you do not know how to judge:
- Whether soft-deleted documents still count as stored personal data for the
  retention policy (you have heard "GDPR" mentioned but never dealt with it).

How you behave:
- When asked for the three lists, give them in a short reply in the shape the assistant
  asked for. Answer any extra question it asked in the same reply (for example where the
  code lives: it is not available here).
- If the assistant asks you to confirm before it investigates, say "go ahead".
- If it asks a follow-up you have no fact for, say you do not know.
- Stop (output STOP) once the assistant has given its findings and a rewritten prompt,
  or offers to proceed / edit / stop. Do not ask it to implement anything.
