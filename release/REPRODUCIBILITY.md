# Reproducibility levels

**Level 1 — exported results arithmetic (verified):** `python verify_aggregate_results.py` recomputes mean and sample standard deviation for five metrics across each model/degradation group. Single-run original conditions legitimately have undefined sample standard deviations (`NaN`).

**Level 2 — original experiment code (archived, not rerun):** the notebook contains the author's training and evaluation workflow, with execution outputs removed. Some unsafe discovery/deletion cells were disabled. Google Colab/Drive paths remain as historical examples; adapt paths and dependencies before executing. Execute selectively in a disposable runtime.

**Level 3 — full independent reproduction (not established):** requires access to the original images under valid terms, the same patient-disjoint split, preprocessing, model initialization/training details, exact software versions, seeds, and independent numerical comparison.

The held-out test set comprises 18 patients (five malignant); interpret the simulated corruption results as exploratory, not clinical performance.
