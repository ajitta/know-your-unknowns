# todo

A small to-do list for the terminal. Tasks are kept in todo.json; set `TODO_FILE` to use another file.

    python3 todo.py add "buy milk"
    python3 todo.py add "file taxes" --due 2026-04-30
    python3 todo.py list            # open tasks, with due dates
    python3 todo.py list --all      # every task
    python3 todo.py list --overdue  # open tasks whose due date has passed
    python3 todo.py done 1

Tests: `python3 -m unittest`
