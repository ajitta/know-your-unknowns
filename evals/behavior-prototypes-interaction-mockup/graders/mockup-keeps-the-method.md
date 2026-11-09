---
type: llm
---

Judge the HTML mockup the assistant wrote and its final reply together, as one
deliverable (the final reply alone when it wrote no file).

The user asked, before anything is wired up, for a single HTML file mocking the new
toolbar of their photo editor with fake data, to see where the buttons go. They named
no tools, platform or users. All of these must hold:

1. The mockup offers clearly different toolbar layouts, side by side or behind a
   toggle that switches between them. The layouts differ in where the toolbar sits or
   how its buttons are grouped and revealed (for example a top bar, a left rail, a
   floating toolbar that appears beside the selection), not one layout in a few
   colours or icon sizes. Its content is made up (a placeholder photo, sample tool
   names and values), not read from a real app.
2. The user is asked to react by saying what to keep or drop, from each layout or
   from its parts, in the reply or in the mockup itself (for example keep and drop
   buttons). Asking only which single layout they prefer does not count.
3. The reply or the mockup asks the user about gaps (what the assistant does not know
   or is assuming, and the decisions the mockup leaves open, such as which tools the
   toolbar holds or whether the editor runs on desktop or the web), and those
   questions sit in one list. A statement of what the mockup assumes may stand apart
   when it asks nothing the list asks. The same list repeated item for item in the
   file and in the reply counts as one list.

Fail if it offers a single toolbar layout and asks for no reaction, or if two lists
under different headings (for example "what I don't know, please correct me" and
"open questions") ask the user about the same gaps.
