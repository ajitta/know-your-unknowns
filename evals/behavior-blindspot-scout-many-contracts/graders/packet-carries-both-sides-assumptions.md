---
type: llm
focus: trace
---

Judge the packet: the `prompt` the assistant passed in the Agent tool call that spawned the unknowns-scout agent (`subagent_type` `unknowns:unknowns-scout`), among the run's tool calls. If the run made no such call, the verdict is FAIL. If it made several, every packet must meet the criteria.

The user's message was:

<<<
Can you do a blind spot pass on our plan to pay all our suppliers at 60 days instead of 30 from 1 April 2027? We run twelve garden centres, and the longer terms would carry us through the spring stock build without using the overdraft. Finance would write to every supplier in January. Skip the up-front questions, here are my lists.

Sure of: we have 214 supplier agreements, and all of them are in contracts/.
Assuming: (a) every agreement lets us change the payment terms by giving written notice; (b) every supplier is on 30-day terms today.
Can't judge: how much pushback to expect from the small growers.

Our purchasing policies are in policies/ and the purchasing manager's notes are in notes/.
>>>

The blindspot skill's step 2 says what the packet holds: "the user's original prompt, verbatim"; "② what the user is assuming and ⑤ what you are assuming, to check first"; "the context sources"; "the target area and where to start in it"; and "what to return: each ② and ⑤ assumption marked held or wrong, with its evidence and status (*confirmed* or *inferred*), or still unchecked; a finding table; and an improved prompt draft".

1. The packet carries the user's message verbatim: its sentences appear word for word, quoted or set apart from the assistant's own text. Line breaks, quotation marks and Markdown may differ. A summary or a paraphrase does not meet this criterion.
2. The packet lists the user's two assumptions, (a) every agreement lets the buyer change the payment terms by written notice and (b) every supplier is on 30-day terms today, and at least one assumption of the assistant's own, set apart from the user's (labelled as the assistant's, or under ⑤). It asks for the assumptions to be checked first, before the rest of the investigation.
3. The packet names the sources (contracts/, and policies/ or notes/ or both) and the target area (the payment terms and how they can be changed, or a part of that), and says where to start, for example the agreements' payment clauses (clause 7 in some of them), their clauses on changing the agreement, or the listed assumptions.
4. The packet asks for every listed assumption to come back marked held or wrong, with its evidence and status (confirmed or inferred), or marked still unchecked; and it also asks for a finding table and an improved prompt draft.

Fail if any criterion is not met.
