# Source Citation Registry

## Purpose

This registry separates dataset-source citations from methodological literature. It prevents manuscript claims from depending on unverified collection pages, challenge pages, or secondary summaries.

## Status labels

- `verified`: confirmed against DOI, publisher, PubMed, TCIA, or official challenge source.
- `source-page-pending`: official source page must be checked before use.
- `doi-pending`: bibliographic record exists as a candidate but DOI/publisher metadata still requires verification.
- `excluded`: citation should not be used.
- `UNVERIFIED — POSSIBLE SIMULATION`: placeholder only; not usable in manuscript text.

## Dataset-source citations

| Citation ID | Source object | Citation type | Status | Required verification | Manuscript use |
|---|---|---:|---:|---|---|
| `src_fdg_pet_ct_lesions` | FDG-PET-CT-Lesions | dataset collection | source-page-pending | TCIA collection page, collection citation, DOI or persistent identifier if provided, data-use terms, access date. | Hold |
| `src_autopet` | AutoPET PET/CT challenge dataset | challenge dataset | source-page-pending | Grand Challenge page, dataset citation, data-use terms, access restrictions, redistribution limits. | Hold |
| `src_lung_pet_ct_dx` | LUNG-PET-CT-DX | dataset collection | source-page-pending | TCIA collection page, collection citation, modality confirmation, clinical-label documentation. | Hold |
| `src_psma_pet_ct_lesions` | PSMA-PET-CT-Lesions | dataset collection | source-page-pending | TCIA collection page, collection citation, tracer metadata, annotation documentation. | Hold |

## Method citations

| Citation ID | Topic | Status | Required verification | Manuscript use |
|---|---|---:|---|---|
| `meth_pyradiomics` | PyRadiomics feature extraction | doi-pending | Verify DOI, publisher page, author list, journal, year, and software version relevance. | Hold |
| `meth_ibsi` | Image Biomarker Standardisation Initiative | doi-pending | Verify DOI, publisher page, consensus methods, feature definitions, and relevance to PET radiomics. | Hold |
| `meth_icc` | Intraclass correlation coefficient | doi-pending | Select appropriate statistical reference and verify metadata. | Hold |
| `meth_bland_altman` | Bland-Altman agreement analysis | doi-pending | Verify original or appropriate methodological reference. | Hold |
| `meth_low_count_pet_noise` | Low-count PET noise simulation or denoising | doi-pending | Identify source directly supporting count reduction/noise assumptions. | Hold |
| `meth_pet_radiomics_robustness` | PET radiomics repeatability and robustness | doi-pending | Identify PET-specific robustness literature and verify DOI/publisher metadata. | Hold |

## Claim-control rule

A manuscript claim can use a citation only when the citation status is `verified`.

A planning claim can cite `source-page-pending` or `doi-pending` only if the text explicitly states that verification remains pending.

No manuscript section should cite a row labeled `UNVERIFIED — POSSIBLE SIMULATION`.

## Immediate verification order

1. `src_fdg_pet_ct_lesions`
2. `meth_pyradiomics`
3. `meth_ibsi`
4. `meth_pet_radiomics_robustness`
5. `meth_low_count_pet_noise`
6. `src_autopet`
