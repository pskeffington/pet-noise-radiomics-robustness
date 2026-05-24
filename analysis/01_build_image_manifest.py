#!/usr/bin/env python3
"""Build a participant-level image manifest from a GDC/TCIA-style CSV manifest.

The script summarizes source rows by participant and modality. It does not
read, write, or require raw imaging files.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = [
    "Study Name",
    "Accession",
    "File Name",
    "File ID",
    "File Type",
    "Participant ID",
    "File Size",
    "Study Data Type",
    "Image Modality",
]

MODALITIES = ["CT", "PT", "SEG"]

SIZE_FACTORS = {
    "B": 1,
    "KB": 1_000,
    "MB": 1_000_000,
    "GB": 1_000_000_000,
    "TB": 1_000_000_000_000,
}


def parse_size_to_bytes(value: object) -> int:
    """Convert manifest size strings such as '21.9 MB' to integer bytes."""
    if pd.isna(value):
        return 0
    text = str(value).strip()
    parts = text.split()
    if len(parts) != 2:
        raise ValueError(f"Could not parse file size: {value!r}")
    number, unit = parts
    unit = unit.upper()
    if unit not in SIZE_FACTORS:
        raise ValueError(f"Unsupported file size unit: {unit}")
    return int(round(float(number) * SIZE_FACTORS[unit]))


def pipe_join(values: pd.Series) -> str:
    """Return sorted unique non-empty values as a pipe-delimited string."""
    cleaned = sorted({str(v) for v in values.dropna() if str(v).strip()})
    return "|".join(cleaned)


def validate_source_columns(data: pd.DataFrame) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required source manifest columns: {missing}")


def build_image_manifest(source_path: Path) -> pd.DataFrame:
    data = pd.read_csv(source_path)
    validate_source_columns(data)

    data = data.copy()
    data["size_bytes"] = data["File Size"].map(parse_size_to_bytes)

    unknown_modalities = sorted(set(data["Image Modality"].dropna()) - set(MODALITIES))
    if unknown_modalities:
        raise ValueError(f"Unexpected image modalities: {unknown_modalities}")

    rows = []
    for participant_id, group in data.groupby("Participant ID", sort=True):
        row = {
            "participant_id": participant_id,
            "accession": pipe_join(group["Accession"]),
            "study_name": pipe_join(group["Study Name"]),
            "total_file_count": int(len(group)),
            "total_size_bytes": int(group["size_bytes"].sum()),
        }

        for modality in MODALITIES:
            subset = group[group["Image Modality"] == modality]
            prefix = modality.lower()
            row[f"{prefix}_file_count"] = int(len(subset))
            row[f"{prefix}_file_ids"] = pipe_join(subset["File ID"])
            row[f"{prefix}_file_names"] = pipe_join(subset["File Name"])
            row[f"{prefix}_size_bytes"] = int(subset["size_bytes"].sum())
            row[f"has_{prefix}"] = bool(len(subset) > 0)

        row["has_complete_ct_pt_seg"] = all(row[f"has_{m.lower()}"] for m in MODALITIES)
        rows.append(row)

    output = pd.DataFrame(rows)

    ordered_columns = [
        "participant_id",
        "accession",
        "study_name",
        "ct_file_count",
        "pt_file_count",
        "seg_file_count",
        "ct_file_ids",
        "pt_file_ids",
        "seg_file_ids",
        "ct_file_names",
        "pt_file_names",
        "seg_file_names",
        "total_file_count",
        "has_ct",
        "has_pt",
        "has_seg",
        "has_complete_ct_pt_seg",
        "total_size_bytes",
        "ct_size_bytes",
        "pt_size_bytes",
        "seg_size_bytes",
    ]
    return output[ordered_columns]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build participant-level CT/PT/SEG manifest.")
    parser.add_argument("--input", required=True, type=Path, help="Source CSV manifest path")
    parser.add_argument("--output", required=True, type=Path, help="Output participant manifest CSV")
    args = parser.parse_args()

    image_manifest = build_image_manifest(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image_manifest.to_csv(args.output, index=False)

    complete = int(image_manifest["has_complete_ct_pt_seg"].sum())
    print(f"Wrote {len(image_manifest)} participant rows to {args.output}")
    print(f"Participants with complete CT/PT/SEG: {complete}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
