---
type: llm
focus: last_message
---

The user asked for options for a food bank that runs out of fresh produce by Wednesday
although deliveries come on Monday (about 180 households a week, one church basement,
two fridges, mostly retired volunteers). Judge the reply. All of these must hold:

1. It lists many distinct candidate interventions, roughly 8 or more, not two or three.
2. The candidates span effort sizes: at least one that could start this week and at
   least one longer bet of a month or more. Sizes may be labelled in any words, or be
   plain from what each candidate involves.
3. Each candidate names what it would change.
4. Judgment is deferred: the reply does not rank, score, prune or recommend candidates
   before the user picks ("start with #2", "my top pick", "the quickest win is" all
   fail). Grouping or ordering candidates by time horizon is not ranking.

Fail if there are fewer than 5 candidates, or if every candidate is the same size of
effort.
