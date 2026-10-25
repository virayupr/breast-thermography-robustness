# ICVGIP 2026 — Supplementary research materials

**Paper:** Beyond Clean Accuracy: Operating-Point Fragility under Image-Quality Shift in Breast Thermography  
**Authors:** Rajeswari Kannan and Vivekanandan N

## Materials available here

- [Original experiment notebook](notebooks/original_author_notebook.ipynb) — original notebook with saved outputs, copied from the existing public repository; **not cleaned or independently rerun**
- [Aggregate results tables](results/tables) — five verified summary CSVs
- [Experimental figures](results/figures) — four verified PNG figures
- [Reproducibility instructions](REPRODUCIBILITY.md)
- [Data availability and privacy](DATA_AVAILABILITY.md)
- [Audit and limitations](AUDIT.md)

Additional original results remain at the repository root. The author's prepared local supplementary archive contains more files (16 aggregate tables and seven figures); **not all have been transferred to GitHub**.

## Important limitations

This is an archival code-and-results supplement, not a clean-room reproducibility certification. The notebook contains Google Drive paths and an operation involving `shutil.rmtree`; review all cells before running. No raw patient images or trained checkpoints are supplied. The public root-level `dataset_with_patient_split.csv` still needs a redistribution/privacy review. The test set is small and quality degradations were simulated.

**Repository:** https://github.com/virayupr/breast-thermography-robustness
