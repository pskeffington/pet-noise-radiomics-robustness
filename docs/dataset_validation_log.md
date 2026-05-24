# Dataset Validation Log

## Purpose

This log controls whether a dataset can carry analytic or manuscript weight. A dataset is not analysis-ready until source existence, access terms, modality, annotation availability, citation requirements, and local manifest feasibility are verified.

## Validation statuses

- `pending`: listed as a candidate but not yet verified.
- `source-verified`: official source page exists and matches the intended dataset.
- `access-verified`: data can be accessed under documented terms.
- `annotation-verified`: lesion masks, labels, or segmentations are confirmed and usable.
- `manifest-ready`: local manifest can be generated without committing raw imaging.
- `analysis-ready`: dataset passes all required checks for v0.1.0 analysis.
- `excluded`: dataset fails scope, access, annotation, or reproducibility requirements.

## Candidate dataset table

| Dataset ID | Dataset | Status | Required next check | Inclusion role |
|---|---|---:|---|---|
| `fdg_pet_ct_lesions` | FDG-PET-CT-Lesions | pending | Verify TCIA source page, collection citation, segmentation/mask format, and download workflow. | Primary candidate |
| `autopet` | AutoPET PET/CT challenge dataset | pending | Verify challenge access terms, citation rules, segmentation masks, and redistribution limits. | Secondary candidate |
| `lung_pet_ct_dx` | LUNG-PET-CT-DX | pending | Verify PET/CT modality, clinical labels, annotation availability, and collection citation. | Secondary candidate |
| `psma_pet_ct_lesions` | PSMA-PET-CT-Lesions | pending | Verify TCIA source page, PSMA tracer metadata, lesion annotation format, and collection citation. | Exploratory candidate |

## Minimum evidence fields

Each dataset must eventually document:

- official source URL;
- source owner;
- access date;
- access terms or license summary;
- citation requirement;
- modality;
- tracer;
- body region or disease focus;
- annotation or mask availability;
- expected local storage path;
- local manifest path;
- exclusion reason if rejected.

## Current decision

Do not begin manuscript claims or radiomics extraction until `fdg_pet_ct_lesions` reaches at least `manifest-ready` status.
