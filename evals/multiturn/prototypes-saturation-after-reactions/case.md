---
description: "Prototype reactions played out: after the user steals and skips, the skill asks for the contrast pole and runs the saturation check before the requirements list"
tags: [multiturn, behavior, en, prototypes]
runs: 3
max_turns_per_reply: 12
user_turns: 5
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

## Opening message

I need a settings screen for a small team-scheduling app. I have no visual taste --
give me a few widely different directions so I can react to them.

## Persona

You run a small team-scheduling app. Its admins are cafe and shop managers, not
technical people, who change settings a few times a month, usually on a tablet at the
counter. You cannot describe a design up front, but you react quickly when you see one.

Your taste (you never state it as a list; it shows only in your reactions):
- You like seeing what a setting does to the actual schedule.
- You dislike anything dark, dense, or keyboard-driven: it scares your admins.
- You dislike long wordy text; short labels are fine.
- Big touch-friendly controls are good. Integrations and roles hardly matter to you.

How you behave:
- First reaction to the options: steal one or two elements by their numbers, and skip
  at least two options or elements with a bare "skip <number>" and no reason. Leave
  some items without any reaction. Use the numbers the assistant gave.
- In every later reaction, give a short reason with each skip, in the assistant's
  "would steal if..." form when it uses one.
- When asked what would have made a skipped item a steal, answer from your taste in one
  line per item.
- When asked which two of three options feel alike and how the third differs, answer
  honestly from your taste (for example calm and visual versus busy and technical).
- When asked to place every option on a scale, give each option a number.
- If offered more options, accept them once and react to the new ones the same way.
- After you have reacted to one extra batch of options, say nothing new came up and ask
  for the final requirements list. If that reply also answers a triad question, leave the
  request out of it and make it in your next reply, after any rating question that follows.
- Stop (output STOP) once the assistant presents a requirements list or a combined
  option and asks you to confirm it, or when it is not waiting for anything from you.
  Do not ask it to build the final screen.
