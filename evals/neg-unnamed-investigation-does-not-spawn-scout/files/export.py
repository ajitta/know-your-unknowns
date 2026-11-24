"""Write the open tasks to tasks.csv for the weekly planning sheet."""
import csv
import json

with open("todo.json", encoding="utf-8") as handle:
    tasks = json.load(handle)

with open("tasks.csv", "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["id", "title"])
    for task in tasks:
        if not task["done"]:
            writer.writerow([task["id"], task["title"]])
