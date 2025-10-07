#!/usr/bin/env bash
set -euxo pipefail

PYTHON_SCRIPT="/mnt/data/swe_world_2/SWE-bench/generate_f2p_p2p.py"
INPUT_DIR="/mnt/data/swe_world_2/SWE-EVO/output_v4"

for jsonfile in "$INPUT_DIR"/*.json; do
  if [ ! -e "$jsonfile" ]; then
    echo "No JSON files found in $INPUT_DIR"
    break
  fi

  echo "Processing $jsonfile ..."

  python "$PYTHON_SCRIPT" --input_json "$jsonfile" --overwrite 0

  if [ $? -ne 0 ]; then
    echo "WARNING: Processing $jsonfile failed"
  else
    echo "✅ Done $jsonfile"
  fi

  echo "-----------------------------"
done

echo "All done."
