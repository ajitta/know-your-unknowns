# Implementation notes

## CSV totals carry no currency symbol

- Plan: "Every total has two decimals."
- Observed: `to_csv` writes `18.50`, not `$18.50`.
- Attributed: a spreadsheet parses a bare number as a number; a currency symbol makes it text.
