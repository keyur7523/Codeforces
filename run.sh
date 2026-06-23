#!/usr/bin/env bash
# Local sample-tester for Codeforces solutions.
#
# Usage:
#   ./run.sh 977A_wrongSubtract.py            # feeds input.txt, prints your output
#   ./run.sh 977A_wrongSubtract.py my.txt     # feeds a custom input file
#
# If an expected.txt file exists, it also diffs your output against it
# and prints PASS / FAIL.

set -euo pipefail

sol="${1:?usage: ./run.sh <solution.py> [input_file]}"
infile="${2:-input.txt}"

if [[ ! -f "$infile" ]]; then
  echo "No input file '$infile'. Create it with the sample input." >&2
  exit 1
fi

actual="$(python3 "$sol" < "$infile")"

echo "----- your output -----"
echo "$actual"

if [[ -f expected.txt ]]; then
  expected="$(cat expected.txt)"
  echo "----- expected --------"
  echo "$expected"
  echo "-----------------------"
  if [[ "$actual" == "$expected" ]]; then
    echo "PASS ✅"
  else
    echo "FAIL ❌"
  fi
fi
