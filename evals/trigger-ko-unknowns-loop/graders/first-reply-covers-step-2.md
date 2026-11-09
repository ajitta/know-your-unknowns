---
type: llm
focus: last_message
---

The user wrote in Korean; the reply may be in Korean. The user asked for
per-organisation rate limiting on the public API. The shape is not settled, and the
change touches the gateway, the pricing plan table and the public docs. The reply must
cover four things. An item counts when the reply asks the user for it, or states it as
a draft or an assumption; naming it only as something to settle later does not count.
All of these must hold:

1. The outcome the user is ultimately after: what the rate limiting is for (for
   example protecting the API from a few heavy organisations, enforcing plan tiers),
   not only the feature itself.
2. The done criteria: what must be true for the work to count as finished (for example
   limits enforced per organisation and per plan, a clear response when a limit is
   hit, the public docs describing the limits).
3. What already works and must not break (for example existing clients whose traffic
   stays under the limits, the gateway's current behaviour, the plans already sold).
4. The allowed cost and change scope: what the work may cost (time, money, added
   latency or infrastructure) and how far the change may reach (for example whether
   the pricing plan table's schema may change).

Fail if any of the four is neither asked for nor stated as a draft or assumption.
