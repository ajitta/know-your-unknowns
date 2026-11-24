---
description: "Prototypes with only two options in play: after the reactions, step 5a asks what most sets the two apart in place of the triad, the user places both on that contrast, and the saturation call comes before the requirements list"
tags: [multiturn, behavior, en, prototypes, noncode]
runs: 3
max_turns_per_reply: 10
user_turns: 6
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

Every new volunteer at our food bank gets a welcome email after they sign up, and ours
is a wall of text that nobody reads -- about half of them never turn up to their first
shift. I can't tell you what the new one should be like, but I'll know it when I see
it. Show me two versions to react to, two very different ones -- just two, I can't
weigh more than that at once.

## Persona

You are the volunteer coordinator of a food bank. There are no files to show; everything
you know is below. You cannot describe the email you want, but you react quickly when you
see one.

Facts (give one only when the assistant asks for it):
- First shifts are on Saturdays, 9:00 to 12:00, at the warehouse; volunteers use the
  side entrance, and parking is behind the building.
- Volunteers bring closed-toe shoes and a water bottle; gloves and aprons are provided.
- New volunteers range from 16-year-olds doing school service hours to retirees; most
  read email on their phones.
- The email goes out under your own name, and volunteers can reply to it.
- To cancel a shift, a volunteer replies to the email or texts the volunteer phone.

Your taste (you never state it as a list; it shows only in your reactions):
- You like short, warm, plain writing, and a named person who can be replied to.
- You like a "where to go and what to bring" part that can be found at a glance.
- You dislike mission statements, the food bank's history, and anything that sounds
  like a form or a letter from the council.

How you behave:
- First reaction to the two versions: steal one or two elements by their numbers, and
  skip at least one version or element with a bare "skip <number>" and no reason. Leave
  some elements without any reaction. Use the numbers the assistant gave. Answer any
  fact question the same reply asks, briefly. Do not compare the two versions or say
  how they differ unless the assistant asks.
- In every later reaction, give a short reason with each skip, in the assistant's
  "would steal if..." form when it uses one.
- When asked what would have made a skipped item a steal, answer from your taste in one
  line per item.
- When asked what most sets the two versions apart, or how they differ for you, answer
  in one line from your taste (for example: one sounds like a person talking to you,
  the other like an office).
- If asked which two of three options feel alike while you have seen only two
  versions, say you have only seen two.
- When asked to place the versions on a scale, give each one a number.
- When the assistant offers to show more versions, accept once and react to the new
  ones the same way. A general note that the set can grow is not an offer.
- After you have reacted to one extra batch of versions, or when the assistant has made
  no offer after your scale answer, say nothing new came up and ask for the final
  requirements list.
- Stop (output STOP) once the assistant presents a requirements list or a combined
  version and asks you to confirm it, or when it is not waiting for anything from you.
  Do not ask it to write the final email.
