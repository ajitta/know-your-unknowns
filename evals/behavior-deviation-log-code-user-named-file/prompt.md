---
description: "deviation-log on code work with a log file the user names: the entry goes to docs/notes/importer-deviations.md, and no IMPLEMENTATION_NOTES.md is created"
tags: [behavior, en, deviation-log]
runs: 3
max_turns: 12
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

Record a deviation. This project keeps its deviation log in
docs/notes/importer-deviations.md, which does not exist yet. The plan said the importer
would stream the vendor CSV row by row, but their endpoint only serves a whole ZIP, so
src/importer.py now downloads it to a temp file and unzips it before parsing. Nothing
else about the importer changed.
