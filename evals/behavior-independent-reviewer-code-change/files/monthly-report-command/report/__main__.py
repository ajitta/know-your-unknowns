import sys

from report.core import load, to_text, totals


def main(argv):
    print(to_text(totals(load(argv[0]))))


if __name__ == "__main__":
    main(sys.argv[1:])
