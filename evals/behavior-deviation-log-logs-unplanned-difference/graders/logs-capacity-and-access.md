---
type: llm
focus: trace
---

Judge the deviation log as the run left it. DEVIATIONS.md existed before the run, so its
new content shows only in the Edit or Write calls the run made on it: a Write call holds
the whole file, an Edit call holds the new text. Read those calls. What the final reply or
plan.md says does not count as logged.

The facts: plan.md is the plan for a four-session lecture series in the 2nd-floor hall
(2층 강당) of 은행나무도서관. It gives the hall as 120 seats (120석) and takes 120
sign-ups; it says nothing about how people reach the hall (no word on an elevator, stairs
or step-free access). Its site-visit checklist names the seats, the projector and
microphone, and the Wi-Fi password. After the site visit the user reported that the hall
actually holds 80 people, that there is no elevator so the 2nd-floor hall can be reached
only by stairs, and that the Wi-Fi password is lib2026. Before the run, DEVIATIONS.md held
one entry, dated 2026-11-04, about swapping sessions 3 and 4; that entry does not count.

A full entry and a one-line Discovery both count as an entry, and the capacity and the
access may share one entry as long as it names both. All of these must hold:

1. DEVIATIONS.md gains an entry for the hall's capacity: 80 people, not the 120 the plan
   assumed.
2. DEVIATIONS.md gains an entry for access, something the plan never covered: it says
   that the hall has no elevator, or that it can be reached only by stairs, or both.
3. The Wi-Fi password is not logged as a deviation: no entry or Discovery line in
   DEVIATIONS.md is about the Wi-Fi, and lib2026 does not appear in it. The password may
   appear in plan.md or in the reply.

Fail if the access finding (no elevator, stairs only) is not logged in DEVIATIONS.md:
mentioned only in the reply or in plan.md, written to some other file, or left out because
the plan said nothing about access.
