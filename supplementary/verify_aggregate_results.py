#!/usr/bin/env python3
"""Verify the published aggregate results against their exported seed-level CSVs.

This checks exported arithmetic only; it does not retrain models or rerun image inference.
Usage: python supplementary/verify_aggregate_results.py
Requires: pandas, numpy.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "supplementary" / "results" / "tables"
REQUIRED = ["multi_seed_degradation_results.csv", "multi_seed_degradation_summary.csv",
            "quality_augmented_multiseed_results.csv", "quality_augmented_multiseed_summary.csv"]
METRICS = ["auc", "accuracy", "sensitivity", "specificity", "f1"]

def verify(prefix):
    raw = pd.read_csv(TABLES / (prefix + "_results.csv"))
    summary = pd.read_csv(TABLES / (prefix + "_summary.csv"))
    assert not raw.empty and not summary.empty, "Empty input tables"
    assert not raw.duplicated(["model", "degradation", "seed"]).any(), "Duplicate seed rows"
    grouped = raw.groupby(["model", "degradation"], dropna=False)
    seen = set()
    for _, row in summary.iterrows():
        key = (row["model"], row["degradation"])
        assert key not in seen, f"Duplicate summary row: {key}"
        seen.add(key)
        vals = grouped.get_group(key)
        for metric in METRICS:
            x = pd.to_numeric(vals[metric], errors="raise").to_numpy(dtype=float)
            assert np.isfinite(x).all(), f"Nonfinite {metric}: {key}"
            for field, expected in (("mean", x.mean()), ("std", x.std(ddof=1))):
                observed = float(row[f"{metric}_{field}"])
                assert np.isclose(observed, expected, rtol=1e-4, atol=1e-4), (
                    f"{prefix} {key} {metric}_{field}: reported={observed}, computed={expected}")
    assert seen == set(grouped.groups), "Missing or extra summary groups"
    print(f"PASS {prefix}: {len(raw)} seed-level rows, {len(summary)} summary groups")

def main():
    missing = [p for p in REQUIRED if not (TABLES / p).is_file()]
    if missing:
        raise SystemExit("NOT YET VERIFIABLE: missing GitHub result files: " + ", ".join(missing))
    verify("multi_seed_degradation")
    verify("quality_augmented_multiseed")
    print("PASS exported aggregate arithmetic; no model retraining performed.")

if __name__ == "__main__":
    main()
