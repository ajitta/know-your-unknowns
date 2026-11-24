"""A small to-do list kept in todo.json (or the file TODO_FILE names)."""
import argparse
import datetime
import json
import os

DATA = os.environ.get("TODO_FILE", "todo.json")


def load():
    if not os.path.exists(DATA):
        return []
    with open(DATA, encoding="utf-8") as handle:
        return json.load(handle)


def save(tasks):
    with open(DATA, "w", encoding="utf-8") as handle:
        json.dump(tasks, handle, indent=2)


def add(tasks, title, due=None):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    if due:
        task["due"] = due
    tasks.append(task)
    return task


def complete(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise SystemExit("no task %d" % task_id)


def pending(tasks):
    return [task for task in tasks if not task["done"]]


def overdue(tasks, today):
    """Unfinished tasks whose due date has passed. Dates are YYYY-MM-DD strings."""
    return [task for task in pending(tasks) if task.get("due") and task["due"] > today]


def line(task):
    text = "%s %d %s" % ("x" if task["done"] else "-", task["id"], task["title"])
    if task.get("due"):
        text += " (due %s)" % task["due"]
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)
    add_cmd = sub.add_parser("add")
    add_cmd.add_argument("title")
    add_cmd.add_argument("--due", help="due date, YYYY-MM-DD")
    done_cmd = sub.add_parser("done")
    done_cmd.add_argument("id", type=int)
    list_cmd = sub.add_parser("list")
    list_cmd.add_argument("--all", action="store_true")
    list_cmd.add_argument("--overdue", action="store_true")
    args = parser.parse_args(argv)

    tasks = load()
    if args.command == "add":
        task = add(tasks, args.title, args.due)
        save(tasks)
        print("added %d: %s" % (task["id"], task["title"]))
    elif args.command == "done":
        task = complete(tasks, args.id)
        save(tasks)
        print("done %d: %s" % (task["id"], task["title"]))
    else:
        if args.overdue:
            shown = overdue(tasks, datetime.date.today().isoformat())
        elif args.all:
            shown = tasks
        else:
            shown = pending(tasks)
        for task in shown:
            print(line(task))


if __name__ == "__main__":
    main()
