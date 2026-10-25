# Release audit

- Source: authors' Colab notebook and exported aggregate result tables/figures.
- Code execution outputs removed from notebook.
- Historical cells containing `shutil.rmtree` disabled in release notebook.
- Two broad recursive Drive discovery cells disabled.
- No patient-level split CSV or per-patient prediction CSV distributed.
- Arithmetic of multi-seed and quality-aware multi-seed summary tables verified against per-seed CSVs.
- End-to-end training and inference **not** independently reproduced.
- Exact dataset provenance, licensing, original train/validation/test split, environment lock, and checkpoints require author confirmation.
- Existing public Git history may retain a patient-level CSV even after deletion from the current branch.
