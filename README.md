# breast-thermography-robustness
Code for evaluating architecture-dependent robustness and quality-aware learning in breast thermography under controlled image-quality degradation.
# Beyond Clean Accuracy: Architecture-Dependent Robustness and Quality-Aware Learning for Breast Thermography

This repository contains the implementation and experimental code for the paper:

**"Beyond Clean Accuracy: Architecture-Dependent Robustness and Quality-Aware Learning for Breast Thermography"**

Submitted to ICVGIP 2026.

## Overview

This work investigates the robustness of deep-learning models for breast
thermography classification under controlled image-quality degradation.

The evaluated architectures are:

- ResNet-18
- MobileNetV3-Small
- EfficientNet-B0

The robustness experiments consider four image-quality conditions:

- Original
- Mild
- Moderate
- Severe

Controlled degradation includes resolution reduction, Gaussian blur,
additive Gaussian noise, and contrast reduction.

## Dataset

Experiments use the publicly available breast thermography dataset
introduced by Rodriguez-Guerrero et al. (2024).

The dataset contains:

- 119 patients
- 84 benign cases
- 35 malignant cases
- 357 thermographic images
- Three views per patient

A strictly patient-disjoint training/validation/test split is used.

## Evaluation

Models are evaluated using patient-level:

- ROC-AUC
- Accuracy
- Sensitivity
- Specificity
- Precision
- F1-score
- Brier score
- Expected Calibration Error (ECE)

Patient-level predictions are obtained by averaging the malignant
probabilities from the three thermographic views.

For degraded conditions, experiments are repeated across 20 stochastic
corruption realizations on the same fixed test cohort.

Patient-level bootstrap confidence intervals are used to quantify
sampling uncertainty for clean-test ROC-AUC.

## Quality-Aware Training

The repository also includes experiments evaluating quality-aware
training for ResNet-18 and MobileNetV3-Small.

## Reproducibility

The main experimental workflow is provided in:

`breast_thermography_robustness.ipynb`

The notebook includes data preparation, patient-disjoint splitting,
model training, controlled degradation, patient-level inference,
robustness evaluation, calibration analysis, and bootstrap confidence
interval estimation.

## Citation

Citation information will be added after publication.
