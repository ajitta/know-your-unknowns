---
description: "Teach-me carried past its explainer: after the user picks a preset and three numbered terms, the reply is a precise-request draft with its assumptions marked, and nothing gets built"
tags: [multiturn, behavior, en, teach-me]
runs: 3
max_turns_per_reply: 8
user_turns: 2
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

## Opening message

I'm adding an export dialog to the video editor I work on. It's a desktop app, and most
of our users cut YouTube videos and short clips for Instagram and TikTok. Right now
"Export" just writes one hardcoded MP4, and the next release needs a real dialog with
choices.

The problem is that I don't know this area. Codecs, bitrates, containers, frame rates,
"constant vs variable" something: I've seen the words in other apps' export screens, but
I couldn't tell you what each one changes or which of them a user should even see. Can
you teach me enough of it that I can write the spec for this dialog?

## Persona

You are a developer on a desktop video editor for Windows and macOS. You are a capable
programmer but have never worked with video encoding. There is no code to show in this
conversation; if the assistant asks for files or paths, say there are none here and it
should work from your description.

What you know (give a fact only when the assistant asks for it):
- Most users are hobbyist creators posting to YouTube, Instagram and TikTok.
- Export today writes one hardcoded MP4; nobody on the team remembers the settings
  behind it.
- The dialog ships in the next release, and your PM asked you to write its spec.

What you do not know: bitrate figures, which codecs to offer, licensing, hardware
encoding, the platforms' file-size or format limits. If asked about any of these, say
you do not know.

How you behave:
- Answer only what the assistant's last reply asked, briefly. If it asks about your
  level or goal before teaching, say you are a beginner in video and want to spec the
  export dialog. If it asks whether to go ahead, say "go ahead".
- When the assistant asks which preset and which terms to keep (or include, or pick),
  reply with one short line naming the first preset it listed and the terms it numbered
  2, 4 and 6, for example: "The first preset (<its name>), plus terms 2, 4 and 6." Use
  the assistant's own name for the preset. If its terms are numbered within groups
  rather than straight through, take the second, fourth and sixth terms in the order
  they appear and name each by the label the assistant gave it; if there are fewer than
  six, name only the second and fourth. Add nothing else: no settings changes, no
  comparisons, no figures, no reasons, and no answers to any other question in that
  reply.
- Stop (output STOP) once the assistant has replied to that pick, whatever that reply
  says or asks. Do not ask it to build the dialog or to write anything.
