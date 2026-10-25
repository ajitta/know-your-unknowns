# Output routing — reactable Markdown in the conversation

Every skill delivers Markdown in the conversation. A presentation page, viewer, shell, and Python are not required.

## 1. Lay out the deliverable

1. Keep the skill's structure and fields: finding cards, option comparisons, decision tables, questions, or a review checklist.
2. Number every item the user can react to. Give alternatives within an item stable labels or numbers.
3. State what a reply changes: include a prompt fix, choose an intervention, steal or skip an element, approve a decision, correct a semantics row, or approve a sign-off item.
4. Write user-facing prose in the language the user is writing in. Keep file names, record field keys, and code identifiers fixed.

Use Markdown tables for parallel comparisons and lists for sequential instructions. Put a short summary before long supporting details. Runnable prototypes remain task outputs in files when the host can write them; the comparison itself stays in the conversation.

## 2. Collect reactions

Ask for the item numbers and changes, with an example such as "2 and 4; item 3 needs revision". Accept prose corrections as well as digits. A missing selection leaves that item undecided; it does not mean approval. When the skill prescribes a default reply, label it as a draft until the user confirms it.

Use the question tool when one exists. No question tool → present a numbered list the user can answer with a digit.

## 3. Assemble the reply

Apply the user's selections to the skill's deliverable: an improved prompt, precise request, requirements list, decision summary, correction list, or review-comment draft. Preserve unresolved items and the skill's approval gate. For a quiz, wait for answers, grade in the conversation, then assemble the score and sections to re-read; never show the teach-back key before the answer.

End the turn with the assembled reply as plain text in chat.

When the skill is a loop stage, fold its closing offer into the loop's single stage checkpoint instead of asking twice.

## 4. Save records

When a skill writes a tracker, scorecard, or deviation log, use its named file in the project. A writable session workspace can hold the same file; tell the user it is session-local and provide it at wrap-up.

No file system → print the record in the chat as Markdown, say which named file the user should save it as, and restate the whole updated record whenever it changes. The quiz key is the exception to printing a record immediately: keep it hidden until the user answers, then print it when grading. See `surfaces.md` in this folder for the tool fallbacks.
