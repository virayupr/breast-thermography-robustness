#!/usr/bin/env python3
"""Check reported aggregate tables from original seed-level CSVs; no retraining."""
from pathlib import Path
import numpy as np
import pandas as pd

P=Path(__file__).resolve().parent/"results"/"tables"
METRICS=["auc","accuracy","sensitivity","specificity","f1"]

def check(prefix):
    raw=pd.read_csv(P/f"{prefix}_results.csv")
    summary=pd.read_csv(P/f"{prefix}_summary.csv")
    assert not raw.duplicated(["model","degradation","seed"]).any()
    groups=raw.groupby(["model","degradation"])
    assert len(groups)==len(summary)
    for _,r in summary.iterrows():
        sub=groups.get_group((r["model"],r["degradation"]))
        for m in METRICS:
            vals=sub[m].to_numpy(dtype=float)
            for name,calc in [("mean",np.mean(vals)),("std",np.std(vals,ddof=1))]:
                reported=float(r[f"{m}_{name}"])
                assert ((np.isnan(calc) and np.isnan(reported))
                        or np.isclose(calc,reported,rtol=1e-4,atol=1e-4)), (
                            prefix,r["model"],r["degradation"],m,name,calc,reported)
    print(f"PASS: {prefix}, {len(raw)} seed-level rows and {len(summary)} groups")

if __name__=="__main__":
    check("multi_seed_degradation")
    check("quality_augmented_multiseed")
    print("Exported aggregate arithmetic verified. Training/inference NOT rerun.")
