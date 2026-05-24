# Source Citation Registry

## Purpose

This registry separates dataset-source citations from methodological literature. It prevents manuscript claims from depending on unverified collection pages, challenge pages, or secondary summaries.

## Status labels

- `verified`: confirmed against DOI, publisher, PubMed, TCIA, or official challenge source.
- `methods-planning-ready`: enough metadata exists for methods planning, but direct publisher, DOI-registry, or PubMed capture remains required before submission.
- `partially-verified`: key bibliographic metadata found, but at least one preferred source such as publisher page or PubMed remains unreached in the current validation pass.
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
| `meth_pyradiomics` | PyRadiomics feature extraction | partially-verified | Candidate record: van Griethuysen et al. 2017, Cancer Research, 77(21), e104-e107, DOI 10.1158/0008-5472.CAN-17-0339. Direct publisher, DOI-registry, or PubMed confirmation still required before final manuscript use. | Hold |
| `meth_ibsi` | Image Biomarker Standardisation Initiative | methods-planning-ready | Zwanenburg et al. 2020, Radiology, DOI 10.1148/radiol.2020191145. arXiv record confirms title, authorship group, Radiology 2020 journal reference, and related DOI. Direct Radiology, DOI-registry, or PubMed capture still required before submission. | Planning only |
| `meth_icc` | Intraclass correlation coefficient | doi-pending | Select appropriate statistical reference and verify metadata. | Hold |
| `meth_bland_altman` | Bland-Altman agreement analysis | doi-pending | Verify original or appropriate methodological reference. | Hold |
| `meth_low_count_pet_noise` | Low-count PET noise simulation or denoising | doi-pending | Identify source directly supporting count reduction/noise assumptions. | Hold |
| `meth_pet_radiomics_robustness` | PET radiomics repeatability and robustness | doi-pending | Priority lead: Leijenaar et al. 2013, Acta Oncologica, on FDG-PET radiomics feature stability. Verify DOI, publisher page, and PubMed before promotion. | Hold |

## Method citation notes

### `meth_ibsi`

APA 7 working citation:

Zwanenburg, A., Leger, S., Vallières, M., Löck, S., & Image Biomarker Standardisation Initiative. (2020). The image biomarker standardization initiative. *Radiology*. https://doi.org/10.1148/radiol.2020191145

Supported planning claim:

IBSI provides standardized radiomics nomenclature, benchmark data, benchmark values, and reporting guidance for reproducible image-biomarker extraction.

Submission requirement:

Capture direct Radiology, DOI-registry, or PubMed metadata before manuscript submission.

### `meth_pyradiomics`

APA 7 working citation pending final source confirmation:

van Griethuysen, J. J. M., Fedorov, A., Parmar, C., Hosny, A., Aucoin, N., Narayan, V., Beets-Tan, R. G. H., Fillon-Robin, J.-C., Pieper, S., & Aerts, H. J. W. L. (2017). Computational radiomics system to decode the radiographic phenotype. *Cancer Research, 77*(21), e104-e107. https://doi.org/10.1158/0008-5472.CAN-17-0339

Supported planning claim:

PyRadiomics is a candidate open-source feature-extraction tool for this project. Final manuscript use requires direct publisher, DOI-registry, or PubMed confirmation.

### `meth_pet_radiomics_robustness`

Priority candidate pending verification:

Leijenaar, R. T. H., Carvalho, S., Velazquez, E. R., van Elmpt, W. J. C., Parmar, C., Hoekstra, O. S., Hoekstra, C. J., Boellaard, R., Dekker, A. L. A. J., Gillies, R. J., Aerts, H. J. W. L., & Lambin, P. (2013). Stability of FDG-PET radiomics features: An integrated analysis of test-retest and inter-observer variability. *Acta Oncologica, 52*(7), 1391-1397.

Supported planning claim:

This is the highest-priority PET-specific robustness lead because it directly addresses FDG-PET radiomic feature stability, test-retest variation, and inter-observer variation.

## Claim-control rule

A manuscript claim can use a citation only when the citation status is `verified`.

A planning claim can cite `source-page-pending`, `doi-pending`, `partially-verified`, or `methods-planning-ready` only if the text explicitly states that verification remains pending.

No manuscript section should cite a row labeled `UNVERIFIED — POSSIBLE SIMULATION`.

## Immediate verification order

1. `meth_pyradiomics`
2. `meth_pet_radiomics_robustness`
3. `meth_ibsi`
4. `src_fdg_pet_ct_lesions`
5. `meth_low_count_pet_noise`
6. `src_autopet`
