import importlib.util
from pathlib import Path

import pandas as pd


MODULE_PATH = Path("analysis/01_build_image_manifest.py")


def load_builder_module():
    spec = importlib.util.spec_from_file_location("image_manifest_builder", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_parse_size_to_bytes():
    module = load_builder_module()
    assert module.parse_size_to_bytes("1 KB") == 1000
    assert module.parse_size_to_bytes("2.5 MB") == 2500000
    assert module.parse_size_to_bytes("0.001 GB") == 1000000


def test_build_image_manifest(tmp_path):
    module = load_builder_module()
    source = tmp_path / "source_manifest.csv"

    sample = pd.DataFrame(
        [
            {
                "Study Name": "A whole-body FDG-PET/CT dataset with manually annotated tumor lesions",
                "Accession": "phs004225",
                "File Name": "ct.zip",
                "File ID": "ct-1",
                "File Type": "DICOM",
                "Sample ID": "Not Applicable",
                "Participant ID": "PETCT_001",
                "File Size": "1 MB",
                "Study Data Type": "Image Annotation,Imaging",
                "Library Strategy": "Not Applicable",
                "Supplementary Files": "",
                "Image Modality": "CT",
            },
            {
                "Study Name": "A whole-body FDG-PET/CT dataset with manually annotated tumor lesions",
                "Accession": "phs004225",
                "File Name": "pt.zip",
                "File ID": "pt-1",
                "File Type": "DICOM",
                "Sample ID": "Not Applicable",
                "Participant ID": "PETCT_001",
                "File Size": "2 MB",
                "Study Data Type": "Image Annotation,Imaging",
                "Library Strategy": "Not Applicable",
                "Supplementary Files": "",
                "Image Modality": "PT",
            },
            {
                "Study Name": "A whole-body FDG-PET/CT dataset with manually annotated tumor lesions",
                "Accession": "phs004225",
                "File Name": "seg.zip",
                "File ID": "seg-1",
                "File Type": "DICOM",
                "Sample ID": "Not Applicable",
                "Participant ID": "PETCT_001",
                "File Size": "3 KB",
                "Study Data Type": "Image Annotation,Imaging",
                "Library Strategy": "Not Applicable",
                "Supplementary Files": "",
                "Image Modality": "SEG",
            },
        ]
    )
    sample.to_csv(source, index=False)

    manifest = module.build_image_manifest(source)

    assert len(manifest) == 1
    row = manifest.iloc[0]
    assert row["participant_id"] == "PETCT_001"
    assert row["ct_file_count"] == 1
    assert row["pt_file_count"] == 1
    assert row["seg_file_count"] == 1
    assert bool(row["has_complete_ct_pt_seg"])
    assert row["total_size_bytes"] == 3003000
