# Upload instructions

Use the existing repository `virayupr/breast-thermography-robustness`. The connected GitHub branch already contains historical code and some figures/tables, but this ZIP contains the complete prepared aggregate package.

Upload these files as a separate `release/` folder to avoid overwriting existing records. Drag the folder into GitHub > Add file > Upload files, then commit. Do not upload raw images, patient identifiers, or historical patient-split CSVs.

After upload, run `python release/verify_aggregate_results.py` in a clone and compare the output. The notebook is not an independently verified end-to-end training pipeline.
