from pathlib import Path

import pandas as pd

REGISTRY_PATH = Path("data/manifests/dataset_registry.csv")

REQUIRED_COLUMNS = [
    "dataset_id",
    "dataset_name",
    "source_owner",
    "source_url",
    "primary_modality",
    "clinical_domain",
    "annotation_status",
    "access_status",
    "raw_data_repo_policy",
    "citation_status",
    "inclusion_decision",
    "notes",
]


def validate_registry(path=REGISTRY_PATH):
    registry = pd.read_csv(path)

    missing = [column for column in REQUIRED_COLUMNS if column not in registry.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if registry.empty:
        raise ValueError("Dataset registry is empty")

    if registry["dataset_id"].duplicated().any():
        raise ValueError("Dataset registry contains duplicate dataset_id values")

    for column in ["dataset_id", "dataset_name", "source_owner", "source_url"]:
        blanks = registry[column].isna() | (registry[column].astype(str).str.strip() == "")
        if blanks.any():
            raise ValueError(f"Dataset registry contains blank values in {column}")

    invalid_url = ~registry["source_url"].astype(str).str.startswith(("https://", "http://"))
    if invalid_url.any():
        raise ValueError("Dataset registry contains invalid source_url values")

    return registry


if __name__ == "__main__":
    data = validate_registry()
    print(f"Validated {len(data)} candidate datasets")
