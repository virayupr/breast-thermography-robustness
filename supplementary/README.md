# ICVGIP 2026 — Supplementary materials

**Accepted paper:** Beyond Clean Accuracy: Operating-Point Fragility under Image-Quality Shift in Breast Thermography  
**Authors:** Rajeswari Kannan and Vivekanandan N

## Available in this repository

- [Original experimental Colab notebook](../breast-thermography-robustness.ipynb) — original author code, with historical execution outputs; inspect before running
- [Clean vs quality-aware comparison](../clean_vs_quality_aware_comparison.csv)
- [Multi-seed degradation summary](../multi_seed_degradation_summary.csv)
- [Quality-augmented multi-seed summary](../quality_augmented_multiseed_summary.csv)
- [Calibration summary](../final_calibration_summary.csv)
- [Validation-selected thresholds](../validation_selected_thresholds.csv)
- [Multi-seed AUC plot](../multiseed_auc_degradation.png)
- [EfficientNet probability-shift plot](../efficientnet_b0_probability_shift.png)
- [MobileNetV3 probability-shift plot](../mobilenetv3_small_probability_shift.png)
- [ResNet-18 probability-shift plot](../resnet18_probability_shift.png)
- Additional figures and the patient-split CSV are in the root; see the GitHub file listing.

## Documentation

- [Reproducibility instructions](REPRODUCIBILITY.md)
- [Data availability and privacy](DATA_AVAILABILITY.md)
- [Audit and limitations](AUDIT.md)

## Status and important limitations

The repository contains substantive original research code and results, but it is **not a fully verified replication release**. The author's separate prepared local archive contains more aggregate CSVs and figures than are presently visible on GitHub. Exact software versions, a fresh end-to-end rerun and privacy/licensing review remain outstanding.

The existing public `dataset_with_patient_split.csv` requires a privacy and dataset-license review. No clinical efficacy is claimed; the test cohort is small, and quality shifts were simulated.

**Repository URL:** https://github.com/virayupr/breast-thermography-robustness
