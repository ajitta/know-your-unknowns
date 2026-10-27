# Plan: CSV export for the monthly report (approved 2026-03-28)

Outcome: the treasurer pastes the monthly report into the club's budget spreadsheet without retyping any figure.

Done criteria:

1. `python3 -m report expenses.csv --format csv` prints CSV with the header `category,total`.
2. Every total has two decimals (`18.50`, not `18.5`).
3. A month with no expenses prints the header row only.
4. The default text output is unchanged.
5. Unit tests cover the CSV output.

Log any deviation from this plan in IMPLEMENTATION_NOTES.md.
