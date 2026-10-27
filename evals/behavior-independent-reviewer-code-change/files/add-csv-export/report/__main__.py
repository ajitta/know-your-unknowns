import sys

from report.core import load, to_csv, to_text, totals


def main(argv):
    path = argv[0]
    fmt = argv[argv.index("--format") + 1] if "--format" in argv else "text"
    sums = totals(load(path))
    print(to_csv(sums) if fmt == "csv" else to_text(sums))


if __name__ == "__main__":
    main(sys.argv[1:])
