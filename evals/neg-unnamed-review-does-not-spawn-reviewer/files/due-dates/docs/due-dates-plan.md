# Plan: due dates

People asked to see what they are late on. Add an optional due date to each task.

Done when:

1. `todo add "title" --due 2026-04-30` stores the due date with the task.
2. `todo list` shows a task's due date after its title.
3. `todo list --overdue` shows only open tasks whose due date is before today.
4. Tasks saved before this change, which have no due date, still load and list as before.
5. Tests cover the new options.
