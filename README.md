# Beyond Clean Accuracy: Operating-Point Fragility under Image-Quality Shift in Breast Thermography

**ICVGIP 2026 — accepted paper**  
**Authors:** Rajeswari Kannan and Vivekanandan N

This repository archives the authors' research code, experimental figures, and aggregate evaluation results for breast thermography classification under simulated image-quality degradation. The study examines the fragility of fixed decision thresholds across architectures and evaluates quality-aware training.

## Supplementary material

- [Supplementary index](supplementary/README.md)
- [Original experimental notebook](supplementary/notebooks/original_author_notebook.ipynb)
- [Published aggregate tables](supplementary/results/tables)
- [Published figures](supplementary/results/figures)
- [Verification script](supplementary/verify_aggregate_results.py)
- [Reproducibility guidance](supplementary/REPRODUCIBILITY.md)
- [Data availability and privacy notes](supplementary/DATA_AVAILABILITY.md)
- [Limitations and audit](supplementary/AUDIT.md)

The original research files remain at the repository root for historical continuity. This is an experimental archive, **not a claim of independent end-to-end numerical reproduction**. Some supplementary CSVs and figures from the local archive have not yet been uploaded to GitHub.

## Research scope and limitations

Experiments use a patient-disjoint split, three deep-learning architectures, fixed validation-selected operating thresholds, multiple stochastic quality-shift seeds, and quality-aware learning. The held-out test cohort includes 18 patients (five malignant); results are exploratory and not clinical validation.

**Data caution:** The historical patient-level split CSV has been removed from the current public branch because it contained patient identifiers and local paths. Git history may still retain earlier copies; further history cleanup requires separate review. Raw thermography images and model checkpoints are not distributed.

## Citation

Please cite the associated ICVGIP 2026 paper. Citation metadata is in [CITATION.cff](CITATION.cff).
