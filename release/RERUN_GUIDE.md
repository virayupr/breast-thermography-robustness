# Reproduction guide and evidence boundary

## A. Reproduce archived calculations without clinical data (supported)

From the repository root:

```bash
python -m pip install numpy pandas
python release/verify_release.py
```

The verifier checks all files listed in `SHA256SUMS.txt`, checks that the archived notebook contains no saved execution outputs, and recomputes the multi-seed summary means and sample standard deviations from the per-seed tables. It **does not** regenerate training results, predictions, calibration, or figures from thermograms.

## B. Re-run the original study (requires author-controlled inputs and manual setup)

1. Obtain the original thermography images and `Diagnostics.xlsx` from the authorized source. Verify dataset licensing and ethical permissions. **Do not commit private images, identifiers, patient split files or predictions.**
2. Work in a fresh isolated Google Colab or equivalent GPU environment. Keep the dataset and outputs outside the public repository.
3. Review `notebooks/ICVGIP_original_code_outputs_removed.ipynb` before executing it. This is a historical research notebook, **not** a tested run-all pipeline. Some setup/deletion and recursive search cells were intentionally disabled.
4. The notebook expects an extracted dataset containing `Breast Thermography/Benign/` and `Breast Thermography/Malignant/` directories with patient-specific subdirectories and JPG images; it also searches for `Diagnostics.xlsx`. The patient ID is derived from the image parent directory. Verify that this structure matches the licensed source.
5. Configure `PROJECT`, `DATA_DIR`, `EXTRACT_DIR`, `RESULTS_DIR`, `MODELS_DIR`, and `FIGURES_DIR` for your own environment. The notebook has multiple historical definitions of these variables; check them throughout before execution. Do not run destructive filesystem commands.
6. The original split code uses stratified patient-level `train_test_split`: 30% held out at `random_state=42`, then that portion split equally into validation/test with `random_state=42`. **This may not reconstruct the identical historical split** unless dataset content, patient ordering, and package behavior match. The exact historical split has not been independently authenticated.
7. The notebook includes image resize to 224×224, ImageNet normalization, model training, threshold selection and simulated corruption evaluation. Confirm the exact sequence, checkpoints, hyperparameters, seeds, and model versions before claiming reproduction.
8. Save the installed environment (`python -m pip freeze > environment-resolved.txt`) and record the dataset version/checksum privately. Compare freshly generated results against archived CSVs, including all per-seed metrics, and investigate discrepancies.
9. Independently verify patient-disjoint splitting, no test-set leakage during threshold selection, and consistency between generated plots and CSVs. Do not claim successful end-to-end reproduction until a clean run has been completed and documented.

## Unresolved prerequisites

- Author-verified dataset origin, version, license and access procedure
- Authenticated original patient split or sufficient provenance to recreate it
- Exact tested Python/CUDA/PyTorch and package versions
- Independently rerun model training/inference and quantitative comparison

The public archive is reproducible at the **aggregate-verification** level only. It is not an independently validated clinical system.
