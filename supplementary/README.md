# ICVGIP 2026 supplementary reproducibility materials

**Paper:** Beyond Clean Accuracy: Operating-Point Fragility under Image-Quality Shift in Breast Thermography  
**Authors:** Rajeswari Kannan and Vivekanandan N  
**Status:** Accepted ICVGIP 2026 paper.

This folder is reserved for the original experiment notebook and exported aggregate results. The prepared supplementary archive has **not yet been uploaded to this GitHub repository**. Do not cite this folder as a complete replication package until the files are uploaded and verified.

## Intended files

- `notebooks/ICVGIP_original_code_outputs_removed.ipynb` — original research notebook with execution outputs removed
- `results/tables/` — 16 aggregate CSV tables
- `results/figures/` — seven experimental figures
- `requirements.txt`, `AUDIT.md`, `REPRODUCIBILITY.md`, `DATA_AVAILABILITY.md`, and provenance/checksum records

## Reproducibility caveats

The source notebook contains Google Colab/Drive-specific paths and repeated setup cells. In particular, **inspect the notebook before execution**: a setup cell removes a stale `/content/drive` directory with `shutil.rmtree`. Run only in an isolated environment after reviewing that operation.

The raw dataset, trained checkpoints, and patient-level prediction records are not part of the prepared public package. Dependencies are inferred rather than environment-locked. A fresh end-to-end rerun has not been verified. The dataset license and privacy requirements must be reviewed before adding further files.

Do not interpret the reported results as clinical validation; the held-out test cohort consists of 18 patients, including five malignant cases.
