---
type: llm
focus: transcript
---

The deliverable of a blind-spot pass is a better prompt, produced after the user's
answers. Judge the assistant reply that presents the findings (normally the last
substantial reply). All of these must hold:

1. That reply comes after the user has answered the request for what they are sure of,
   what they are assuming, and what they cannot judge.
2. It contains a rewritten version of the user's request, marked as the prompt to use
   next and written as an instruction to a model, not as a summary addressed to the user.
3. The rewritten prompt is the last substantial block of that reply: findings come
   before it; only a short closing offer or next-step suggestion may follow it.
4. The prompt folds in the specific risks found: it names the nightly export job and
   the search indexer, and it reflects at least one thing the user said in the answers
   (for example the indexer assumption about `updated_at`, the cascading foreign keys,
   or the `(workspace_id, slug)` unique constraint).
5. The prompt ends with an explicit stop-and-review checkpoint, such as showing a plan
   before writing any code.

Fail if the conversation ends without such a prompt, for example because the assistant
kept asking questions, declined the task, or only listed risks.
