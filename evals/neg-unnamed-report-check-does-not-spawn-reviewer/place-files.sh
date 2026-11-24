#!/usr/bin/env bash
# The pilot's plan, report, records and deviation log, in the run's working directory:
# the same material as behavior-independent-reviewer-report-vs-records, where the user
# names the agent. Here the user does not.
set -eu
cp -R "$(dirname "$0")/files/." .
