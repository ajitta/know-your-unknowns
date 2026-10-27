import csv
import io


def load(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def totals(rows):
    out = {}
    for row in rows:
        out[row["category"]] = out.get(row["category"], 0.0) + float(row["amount"])
    return dict(sorted(out.items()))


def to_text(sums):
    lines = ["%-10s %8.2f" % (name, value) for name, value in sums.items()]
    lines.append("%-10s %8.2f" % ("TOTAL", sum(sums.values())))
    return "\n".join(lines)


def to_csv(sums):
    if not sums:
        return ""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["category", "total"])
    for name, value in sums.items():
        writer.writerow([name, "%.2f" % value])
    return buffer.getvalue().rstrip("\n")
