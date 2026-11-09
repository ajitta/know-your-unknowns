---
type: llm
focus: transcript
---

The user is a developer adding an export dialog to a desktop video editor whose users
mostly post to YouTube, Instagram and TikTok; export today writes one hardcoded MP4. They
asked to learn the vocabulary (codecs, bitrates, containers) so they could write the
dialog's spec. When the assistant asked which preset and terms to keep, the user replied
with one short line picking the first preset the assistant had listed and its second,
fourth and sixth numbered terms (only the second and fourth if it numbered fewer than
six), and gave nothing else: no settings changes, no figures, no answers to other
questions.

Judge the assistant's last reply, the one that answers that pick. Check the picks
against the presets and numbered terms in the assistant's earlier reply. If the user
never made such a pick, fail. All of these must hold:

1. The reply gives a precise request for the export dialog: the user's original request
   rewritten in the vocabulary taught earlier and built on the user's picks. It uses the
   picked preset and every picked term, and it does not bring in another preset or
   another taught term as if the user had chosen it.
2. Every detail in that request which the user did not supply is marked as an
   assumption for the user to confirm, or as still open, so the user can tell which
   details are assumed: inline marks or a list that names each assumed detail both
   pass; a blanket line such as "adjust as needed" does not. The picked preset's own
   settings, as the assistant described them before the pick, count as chosen by the
   user, and facts in the user's messages count as given. Anything else counts as not
   supplied, for example bitrate or quality figures, resolutions or frame rates beyond
   the preset, codecs or containers offered besides the preset's, which controls the
   dialog shows or hides, default values, file-size limits, hardware encoding.
3. The reply leaves the next step to the user: it asks the user to confirm or correct
   the assumptions, or offers next steps for the user to choose, and does not go on by
   itself.
4. The reply does not start building the dialog. It contains no program code (no UI
   component or markup, no source code, no encoder command line or script to run), and
   it does not say it has created files for the dialog or is now implementing it.

Fail if the reply starts building the dialog or writes code, if it presents a detail the
user never gave as decided (for example a bitrate figure, a list of resolutions or a
codec choice stated as settled with no assumption mark), or if no precise request built
from the user's picks appears.
