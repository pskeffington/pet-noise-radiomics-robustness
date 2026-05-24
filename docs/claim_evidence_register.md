# Claim Evidence Register

## Purpose

This register links future manuscript claims to verified evidence objects. It prevents early project notes from becoming unsupported manuscript language.

## Claim status labels

- `draft`: claim is being considered but has not been checked.
- `evidence-pending`: claim requires dataset, output, or citation support before use.
- `supported`: claim has verified evidence and can be used in manuscript text.
- `revise`: claim is directionally plausible but overstates the evidence.
- `exclude`: claim should not be used.

## Evidence object types

- `dataset-source`: official dataset or challenge source.
- `method-citation`: verified methodological literature.
- `analysis-output`: reproducible table, figure, or model output from this repository.
- `software-record`: official software documentation, version record, or configuration file.
- `limitation-note`: explicitly stated boundary or uncertainty.

## Register

| Claim ID | Draft claim | Evidence object | Evidence status | Claim status | Action |
|---|---|---|---:|---:|---|
| `claim_001` | Open PET/CT cancer imaging datasets can support a reproducible PET radiomics robustness study. | `src_fdg_pet_ct_lesions`; `src_autopet`; `src_lung_pet_ct_dx`; `src_psma_pet_ct_lesions` | source-page-pending | evidence-pending | Verify official source pages and access terms. |
| `claim_002` | FDG-PET-CT-Lesions is the primary dataset candidate for lesion-level radiomics robustness. | `data/manifests/dataset_registry.csv`; `docs/dataset_validation_log.md` | manual-source-check-required | evidence-pending | Complete Issue #14. |
| `claim_003` | PyRadiomics can be used for standardized feature extraction. | `meth_pyradiomics`; future `config/pyradiomics_pet.yaml` | partially-verified | evidence-pending | Obtain direct publisher, PubMed, or DOI-registry confirmation before manuscript use. |
| `claim_004` | IBSI guidance should inform feature naming and reproducibility reporting. | `meth_ibsi` | verified | supported | Use in methods planning and later manuscript methods section. |
| `claim_005` | Noise perturbation claims must distinguish synthetic perturbation from true scanner reconstruction. | `docs/noise_framework.md`; `meth_low_count_pet_noise` | not-created | evidence-pending | Draft noise framework before methods claims. |
| `claim_006` | ICC and coefficient of variation can summarize radiomics stability across perturbation levels. | `meth_icc`; future `analysis/05_feature_stability_metrics.py` | doi-pending | evidence-pending | Verify statistical citations and implement metrics. |

## Supported claim notes

### `claim_004`

IBSI can support methods language on standardized radiomics nomenclature, benchmark data, benchmark values, and reproducibility reporting guidance. It does not by itself validate this project's PET/CT datasets, noise perturbation design, or PyRadiomics implementation.

## Manuscript rule

Only claims marked `supported` may enter manuscript sections without qualification.

Claims marked `evidence-pending` can remain in planning documents but must not appear as completed findings.

Claims marked `revise` require narrowed wording before manuscript use.

Claims marked `exclude` must be removed from manuscript drafts.
