---
description: "Persistence check: notes must write IMPLEMENTATION_NOTES.md, not only summarise in chat"
tags: [behavior, en, notes]
runs: 3
max_turns: 12
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

This project keeps its deviation log in IMPLEMENTATION_NOTES.md at the project root.
The file does not exist yet, so initialise it first, then record a deviation in it:
the plan said the importer would stream the vendor CSV row by row, but their endpoint
only serves a whole ZIP, so I download it to a temp file and unzip it before parsing.
Nothing else about the importer changed.
