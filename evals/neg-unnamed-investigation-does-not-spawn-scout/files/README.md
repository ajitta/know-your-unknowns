# todo

A small to-do list for the terminal. Tasks are kept in todo.json; set `TODO_FILE` to use another file.

    python3 todo.py add "buy milk"
    python3 todo.py list          # open tasks
    python3 todo.py list --all    # every task
    python3 todo.py done 1

Every Monday, `python3 export.py` writes the open tasks to tasks.csv for the weekly planning sheet.

Tests: `python3 -m unittest`
