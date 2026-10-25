# Reproducibility instructions (ICVGIP 2026)

The repository root contains the authors' original notebook: [breast-thermography-robustness.ipynb](../breast-thermography-robustness.ipynb). This is **historical experimental code**, not a verified one-click pipeline.

1. Obtain the underlying breast thermography dataset from its original distributor and follow its license and ethical requirements. No raw image data are supplied here.
2. Run in an isolated Google Colab environment with PyTorch, torchvision, NumPy, pandas, Pillow, scikit-learn, matplotlib, and other imports required by the notebook.
3. **Review every setup cell before execution.** The notebook uses hard-coded Google Drive paths, exploratory/recovery cells and a `shutil.rmtree` operation involving `/content/drive`. Do not run unreviewed deletion or broad Drive-search cells.
4. Configure dataset directories, patient-disjoint splits and output locations. Check that patient identifiers do not cross train/validation/test partitions.
5. Inspect saved outputs against exported tables. The reported 20-seed corruption analysis is a stochastic evaluation, not independent training replication.
6. A full clean-room rerun, exact environment version lock, and checkpoint verification have **not** been completed.

The original held-out test set was small (18 patients, five malignant). Results are exploratory; simulated quality shifts do not establish clinical deployment performance.
