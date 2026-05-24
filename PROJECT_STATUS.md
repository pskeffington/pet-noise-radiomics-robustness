# Project Status

## Project

Open-data PET/CT radiomics robustness study focused on simulated noise perturbation, lesion segmentation stability, and downstream feature reliability.

## Current state

Stage 1 scaffold repository. The project currently defines scope, candidate datasets, modular analysis phases, and repository structure. No validated radiomics analysis results should yet be interpreted as manuscript findings.

## Current progress

| Module | Status | Notes |
|---|---|---|
| Research framing | Active | Focus is radiomics robustness under PET noise perturbation. |
| Dataset registry | Scaffolded | Candidate TCIA and AutoPET datasets identified. |
| Citation verification | Pending | Citation registry exists but requires DOI and metadata verification. |
| Analysis plan | Scaffolded | Planned workflow covers preprocessing, perturbation, extraction, and stability analysis. |
| Reproducibility boundaries | Defined | Raw imaging data excluded from repository commits. |
| Manuscript drafting | Pending | Manuscript structure remains pre-analysis. |

## Daily progress log

### 2026-05-24

- Repository state reviewed and classified as a scaffold-stage reproducible imaging project.
- Candidate open PET/CT datasets confirmed.
- Confirmed repository separation between raw imaging storage and committed reproducibility objects.

## Immediate next actions

1. Build `data_manifest/` acquisition manifests with dataset version, accession, checksum, and local-storage path rules.
2. Define a canonical lesion-object schema for segmentation tracking.
3. Add perturbation parameter registry for count reduction, Gaussian noise, reconstruction variation, and repeatability controls.
4. Define radiomics extraction standardization policy aligned with IBSI terminology where applicable.
5. Build feature-stability outputs around ICC, coefficient of variation, and perturbation sensitivity.

## Blockers

- No dataset manifests committed.
- No preprocessing scripts committed.
- No segmentation validation pipeline committed.
- No reproducible radiomics extraction workflow committed.
- No verified manuscript citations committed.
