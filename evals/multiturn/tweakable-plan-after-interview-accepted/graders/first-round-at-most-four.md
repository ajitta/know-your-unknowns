---
type: question_count
turn: 2
max: 4
weight: 0.5
---

Counts the numbered question items in the reply right after the user takes the
interview suggestion (reply 2), outside code fences, block quotes and tables. The
interview skill asks "max 4 questions per round"; a fifth numbered question in that
reply fails. A reply 2 that shows the plan again with its numbered unknowns can fail
here too; `asks-after-acceptance` is the check for that.
