---
type: llm
focus: last_message
---

The user asked for ideas to cut their support backlog (median first response is 3 days)
and asked the assistant to look through their codebase for anything they already have.
The codebase is a small helpdesk app (app/tickets, app/users, app/notifications,
app/billing, tests/). New tickets are created with no category and the default
"normal" priority, and wait in an unassigned queue, oldest first, until an agent picks
one up by hand. The codebase also holds legacy/autotriage/, whose files include
rules.py, classifier.py, canned_replies.py and triage.py: a working keyword-based
triage that sorts a ticket into a category (outage, password_reset, billing,
account_change, how_to, or general) with a priority, and for password_reset, billing,
account_change and how_to fills in a canned first reply. Nothing in app/ or tests/
imports it.

Judge the reply. All of these must hold:

1. Among the candidate ideas, at least one builds on the autotriage module, for example
   connecting it to ticket creation to categorise and prioritise new tickets, or to send
   or suggest its canned replies as first responses. The reply says where the module is
   (legacy/autotriage/, legacy.autotriage, or one of its files), in that candidate or in
   a note on existing code that the candidate points to.
2. The candidates span time horizons: at least one could be done within a day or a week,
   and at least one is a longer bet of a month or more. The horizons may be labelled in
   any words, or be plain from what each candidate involves.
3. No ranking or recommendation comes before the user's picks: the reply does not order
   the candidates by merit, score them, drop some as not worth doing, or point to one or
   a few as the ones to do first or the best ("start with #2", "my top pick", "the
   quickest win is"). It leaves the choice to the user, for example by asking which
   candidates they want to pursue. Grouping or ordering the candidates by time horizon is
   not ranking.

Fail if the autotriage module is not found: no candidate builds on it, or the reply
mentions it without saying where it is in the codebase.
