#!/usr/bin/env python3
"""Private-data validation and reproducible patient-disjoint split audit.

Reads a local dataset ZIP; never publishes images, IDs or patient-level splits.
This reconstructs the notebook's split algorithm, NOT an authenticated historical split.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

import pandas as pd
from sklearn.model_selection import train_test_split

def inspect_dataset(zip_path, diagnostics_path=None):
    with zipfile.ZipFile(zip_path) as archive:
        if archive.testzip() is not None:
            raise ValueError("Corrupt ZIP entry")
        paths = archive.namelist()
        images = []
        for name in paths:
            p = PurePosixPath(name)
            if len(p.parts) == 4 and p.parts[0] == "Breast Thermography" and p.parts[1] in ("Benign", "Malignant") and p.suffix.lower() in (".jpg", ".jpeg"):
                images.append((p.parts[1], p.parts[2], p.parts[3]))
        if not images:
            raise ValueError("No expected thermography images found")
        embedded = archive.read("Breast Thermography/Diagnostics.xlsx")
    if diagnostics_path:
        if hashlib.sha256(embedded).digest() != hashlib.sha256(Path(diagnostics_path).read_bytes()).digest():
            raise ValueError("External Diagnostics.xlsx differs from ZIP")
    by_patient = collections.defaultdict(list)
    for label, patient, filename in images:
        by_patient[(label, patient)].append(filename)
    ids = [patient for _, patient in by_patient]
    if len(ids) != len(set(ids)):
        raise ValueError("Patient ID occurs in multiple classes")
    expected_views = {"anterior", "oblleft", "oblright"}
    for files in by_patient.values():
        views = {next((v for v in expected_views if v in f.lower()), "unknown") for f in files}
        if len(files) != 3 or views != expected_views:
            raise ValueError("Missing/duplicated view in one or more patients")
    # The notebook enumerates sorted JPG paths class-by-class before drop_duplicates.
    rows = []
    for label, patient in sorted(by_patient, key=lambda t: (("Benign", "Malignant").index(t[0]), t[1])):
        rows.append({"patient_id": patient, "label": int(label == "Malignant")})
    patients = pd.DataFrame(rows)
    train, temp = train_test_split(patients, test_size=0.30, stratify=patients.label, random_state=42)
    val, test = train_test_split(temp, test_size=0.50, stratify=temp.label, random_state=42)
    sets = [set(frame.patient_id) for frame in (train, val, test)]
    if any(sets[i] & sets[j] for i in range(3) for j in range(i+1, 3)):
        raise AssertionError("Patient leakage")
    counts = lambda frame: {"patients": len(frame), "benign": int((frame.label == 0).sum()), "malignant": int((frame.label == 1).sum())}
    return {"dataset": {"images": len(images), "patients": len(patients), "benign": int((patients.label == 0).sum()), "malignant": int((patients.label == 1).sum()), "three_views_per_patient": True}, "reconstructed_split": {"train": counts(train), "validation": counts(val), "test": counts(test)}, "historical_split_authenticated": False, "raw_data_published": False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--diagnostics", type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect_dataset(args.zip, args.diagnostics), indent=2))

if __name__ == "__main__":
    main()
