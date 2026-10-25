# ICVGIP 2026 — Research code and aggregate results

**Accepted paper:** Beyond Clean Accuracy: Operating-Point Fragility under Image-Quality Shift in Breast Thermography  
**Authors:** Rajeswari Kannan and Vivekanandan N

This supplementary archive contains the authors' historical Colab research notebook (outputs removed and selected destructive/discovery cells disabled), 16 aggregate CSV tables, seven figures, and reproducibility documentation.

## Quick verification

```bash
python -m pip install numpy pandas
python verify_aggregate_results.py
```

This independently recomputes **exported summary arithmetic** from per-seed aggregate tables; it does **not** reproduce model training or image inference. Reproducing the experiment from raw thermograms requires the source dataset, verified dataset permissions, the authors' exact patient-disjoint split, preprocessing choices, checkpoints or training, and environment alignment. The original notebook contains historical Google Drive paths and exploratory/recovery cells; inspect and adapt it before running.

No raw images, patient-level predictions, or patient-split CSV are distributed. This is an exploratory study with a small held-out test cohort (18 patients; five malignant) and simulated image-quality shifts. Not a clinical validation.

## Files

- `notebooks/`: archival notebook, execution outputs removed
- `results/tables/`: aggregate exported tables
- `results/figures/`: exported plots
- `verify_aggregate_results.py`: deterministic summary consistency check
- `REPRODUCIBILITY.md`, `DATA_AVAILABILITY.md`, `AUDIT.md`: limitations and use notes
- `SHA256SUMS.txt`: integrity checks for this package

## Reproducibility entry points

- **Dataset-free checks:** `python release/verify_release.py` from repository root (SHA-256 integrity, notebook output state, and aggregate summary arithmetic).
- **Private source dataset audit:** `python release/validate_private_dataset.py --zip "/private/path/Breast Thermography.zip" --diagnostics "/private/path/Diagnostics.xlsx"` (requires pandas and scikit-learn). See [PRIVATE_DATASET_SETUP.md](PRIVATE_DATASET_SETUP.md).
- **Rerun prerequisites and limitations:** [RERUN_GUIDE.md](RERUN_GUIDE.md). The historical notebook is **not** a verified one-command end-to-end pipeline. A fresh GPU retraining and numerical comparison have not been completed.

**Do not upload the thermograms, diagnostics workbook, patient IDs, patient split CSVs, or patient-level predictions to this public repository.**
