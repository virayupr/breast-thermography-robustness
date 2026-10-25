#!/usr/bin/env python3
"""Offline, dataset-free integrity and archive verification; not model retraining."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    manifest = ROOT / "SHA256SUMS.txt"
    lines = [line.strip() for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
    failures = []
    for line in lines:
        digest, relative = line.split(maxsplit=1)
        path = ROOT / relative.strip()
        if not path.is_file():
            failures.append(f"MISSING {relative}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            failures.append(f"HASH MISMATCH {relative}")
    notebook = ROOT / "notebooks" / "ICVGIP_original_code_outputs_removed.ipynb"
    if notebook.exists():
        nb = json.loads(notebook.read_text(encoding="utf-8"))
        for i, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") == "code" and (cell.get("outputs") or cell.get("execution_count") is not None):
                failures.append(f"Notebook cell {i} has stored outputs/execution count")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(lines)} SHA256 checks; notebook output check")
    return subprocess.call([sys.executable, str(ROOT / "verify_aggregate_results.py")])

if __name__ == "__main__":
    sys.exit(main())
