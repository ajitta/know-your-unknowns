#!/usr/bin/env bash
# The pilot's plan, report, records and deviation log, in the run's working directory.
set -eu
cp -R "$(dirname "$0")/files/." .
