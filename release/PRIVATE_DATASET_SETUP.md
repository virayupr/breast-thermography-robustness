# Private dataset validation and patient split reconstruction

The dataset is **not distributed in this public repository**. The dataset archive and diagnostics workbook must remain in an authorized private location.

With access to the licensed original archive, install dependencies:

```bash
python -m pip install pandas scikit-learn openpyxl
python release/validate_private_dataset.py --zip "/path/to/Breast Thermography.zip" --diagnostics "/path/to/Diagnostics.xlsx"
```

The validator checks ZIP integrity, patient class uniqueness, the three required views per patient, and reproduces the **split algorithm** recorded in notebook cell 19: stratified 70/30 patient split at seed 42, followed by equal validation/test stratified split at seed 42. It outputs **counts only**, never patient IDs, file paths or individual predictions. The original historical split has not been authenticated. Differences in source dataset versions or ordering could change assignments.

This validator **does not** run training, calibration, degradation experiments or figure regeneration. End-to-end numerical reproduction remains pending a controlled fresh GPU run and an author-approved dataset provenance/environment record. See `RERUN_GUIDE.md`.

Do not upload the original ZIP, `Diagnostics.xlsx`, patient-level split files, image data, or private model artifacts to GitHub.
