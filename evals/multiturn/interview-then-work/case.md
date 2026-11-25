---
description: "Interview before a small script that can be written in the run's folder: the last reply delivers the decision table and the ready-to-use prompt and leaves the work to the user's next message"
tags: [multiturn, behavior, en, interview]
runs: 3
max_turns_per_reply: 12
user_turns: 4
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

## Opening message

Use unknowns to ask me questions before implementing. I want a small Python script in this folder,
report.py, that reads our weekly sign-ups export and prints a summary for the Monday
meeting. The export is not in this folder yet; its columns are email, signed_up_at (a UTC
timestamp), plan and referrer. Nothing is settled -- not which numbers the summary shows,
not how duplicate sign-ups are handled, not what counts as a week, and not what happens
when the file is empty.

## Persona

You are the operations lead who runs the Monday meeting. The folder holds no files yet.
The export is a CSV named signups.csv with the columns email, signed_up_at (UTC, ISO
8601), plan (free or pro) and referrer (may be blank).

What you are sure of: the summary is read aloud in the meeting, so it must fit on one
screen of plain text; the script must use only the Python standard library.

What you are assuming but have not checked: every row has a valid timestamp; the export
never holds more than a few thousand rows.

Your answers when asked (use only the ones the assistant actually asks about):
- Numbers shown: total sign-ups for the week, the split by plan, and the top three
  referrers.
- Duplicates: the same email twice in one week counts once; keep the earliest row.
- Week: Monday 00:00 UTC to Sunday 23:59 UTC, and the script reports the last full week.
- Empty file or no rows in the week: print "No sign-ups last week." and exit normally.
- Blank referrer: count it as "direct".
- A row with a bad timestamp: skip it and print how many rows were skipped.
- Input path: signups.csv in the same folder by default, with an optional path argument.
- Output: printed to the terminal only; no file is written.

How you behave:
- Answer every question the assistant asked, by its numbers or option letters, in one
  short reply. Give a reason only when the assistant asks why.
- If it asks what you are sure of and what you are assuming, give the two lists above.
- After you have answered two rounds of questions, if it asks a third round, reply only
  "That's enough questions."
- Stop (output STOP) once the assistant has delivered a decision table and a ready-to-use
  prompt, whether or not it has also started the work, or once it asks whether to
  proceed. Do not ask it to implement, do not tell it to wait, and do not tell it to
  stop.
