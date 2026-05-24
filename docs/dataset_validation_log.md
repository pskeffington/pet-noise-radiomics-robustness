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
- `manual-source-check-required`: official source likely exists, but automated validation could not complete because the source page rejected or failed automated access.

## Candidate dataset table

| Dataset ID | Dataset | Status | Required next check | Inclusion role |
|---|---|---:|---|---|
| `fdg_pet_ct_lesions` | FDG-PET-CT-Lesions | manual-source-check-required | Verify TCIA source page in a normal browser session; capture collection citation, license/use conditions, segmentation/mask format, and download workflow. | Primary candidate |
| `autopet` | AutoPET PET/CT challenge dataset | manual-source-check-required | Verify Grand Challenge access terms, citation rules, segmentation masks, and redistribution limits in authenticated or browser-based access. | Secondary candidate |
| `lung_pet_ct_dx` | LUNG-PET-CT-DX | manual-source-check-required | Verify TCIA source page in a normal browser session; confirm PET/CT modality, clinical labels, annotation availability, and collection citation. | Secondary candidate |
| `psma_pet_ct_lesions` | PSMA-PET-CT-Lesions | manual-source-check-required | Verify TCIA source page in a normal browser session; confirm PSMA tracer metadata, lesion annotation format, and collection citation. | Exploratory candidate |

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

## Automated validation attempt — 2026-05-24

Automated web access could not fully verify the source pages.

Observed tool-level results:

- TCIA collection pages for FDG-PET-CT-Lesions, LUNG-PET-CT-DX, and PSMA-PET-CT-Lesions returned server errors to the automated browser.
- AutoPET Grand Challenge returned a forbidden response to the automated browser.
- This is not evidence that the datasets are unavailable. It is evidence that automated source validation is incomplete.

External literature search suggests AutoPET remains a relevant PET/CT lesion-segmentation source, but literature references do not replace official dataset-page validation.

## Current decision

Do not begin manuscript claims or radiomics extraction until `fdg_pet_ct_lesions` reaches at least `manifest-ready` status.

Do not label any candidate dataset as `source-verified`, `access-verified`, or `analysis-ready` until the official source page, citation requirement, access terms, and annotation format are manually confirmed.
