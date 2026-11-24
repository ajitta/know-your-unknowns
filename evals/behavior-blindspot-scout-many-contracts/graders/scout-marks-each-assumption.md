---
type: llm
focus: trace
---

Judge the report the unknowns-scout agent handed back (shown as a report handed back by a spawned agent), against the packet the assistant sent it (the `prompt` of the Agent tool call that spawned it). If no unknowns-scout agent was spawned, the verdict is FAIL. If the scout was spawned more than once, judge each report against its own packet.

The scout's instruction: "When the packet lists assumptions (the user's, the caller's), check them first and mark each one held or wrong, with its evidence and status (*confirmed* or *inferred*), or still unchecked; a wrong one is also a finding in the table, and one still unchecked, including one the sources do not settle, also goes under **Needs checking** with where to look."

The user's two assumptions were (a) every agreement lets the buyer change the payment terms by giving written notice; (b) every supplier is on 30-day terms today. The packet may list assumptions of the assistant's own as well.

1. Every assumption the packet listed, the user's and the assistant's own, is marked held, wrong or still unchecked in the report, or with a plain equivalent (holds or true; does not hold, partly wrong or false; not checked or unknown). An assumption marked wrong for some agreements and right for the rest counts as marked when the report says which agreements it fails for.
2. Each held or wrong mark carries its evidence (a file path, with or without a line or clause; a document title; or a search over the agreements that the report says it ran) and a status, confirmed or inferred.
3. Each assumption marked wrong is also a finding in the report's finding table, and each one marked still unchecked is also listed under Needs checking with where to look.

Fail if any criterion is not met.
