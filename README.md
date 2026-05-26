# PET Noise Radiomics Robustness

Reproducible open-data study evaluating how PET image noise affects lesion segmentation, radiomics feature stability, and downstream biomedical model reliability in public PET/CT cancer imaging datasets.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active research scaffold; no analysis results should be treated as final until data acquisition, citation validation, and reproducibility checks are complete.  
**Last documentation refresh:** 2026-05-26

## Working aim

This repository supports a nuclear-medicine and biomedical data-science project focused on low-count PET, simulated noise perturbation, radiomics robustness, and open cancer-imaging datasets.

## Core research question

How sensitive are PET/CT lesion radiomics features and segmentation-derived measures to simulated image noise, and which features remain stable enough for defensible downstream biomedical modeling?

## Current update — 2026-05-26

The repository remains pre-analysis and manuscript-preparation oriented. The current documentation priority is to verify dataset access terms, lock a manifest schema for imaging series and masks, and keep citation/access metadata complete before any derived feature tables or radiomics stability claims are introduced.

## Current scope

Stage 1 establishes the manuscript and analysis scaffold. It does not claim completed analysis. The current repository purpose is to preserve a clean, reproducible object map before raw imaging, derived feature tables, or manuscript claims are introduced.

Current scaffold objects:

- `docs/stage_1_scaffold.md`: stage plan and execution map.
- `docs/data_sources.md`: open-data source registry.
- `docs/citation_registry.md`: citation-verification queue.
- `docs/analysis_plan.md`: planned reproducible workflow.
- `docs/repo_structure.md`: repository object map.
- `.gitignore`: exclusions for local data, build artifacts, and environment files.

## Candidate open datasets

Primary candidates:

- TCIA FDG-PET-CT-Lesions.
- AutoPET PET/CT challenge dataset.
- TCIA LUNG-PET-CT-DX.
- TCIA PSMA-PET-CT-Lesions.

Raw imaging data should not be committed to this repository. Store data locally or through approved external storage and track only download instructions, manifests, checksums, derived tables, and reproducible scripts.

## Planned analysis modules

1. Dataset acquisition and manifest creation.
2. PET/CT preprocessing and harmonization.
3. Lesion mask ingestion or segmentation baseline.
4. Simulated PET noise perturbation.
5. Radiomics extraction.
6. Feature stability analysis.
7. Reporting tables and figures.
8. Manuscript drafting.

## Documentation standards

- Keep dataset access requirements, licenses, and citation metadata in `docs/data_sources.md` before analysis begins.
- Keep DOI, dataset version, and retrieval-date checks in `docs/citation_registry.md`.
- Separate raw imaging data, intermediate image volumes, and derived feature tables from source-controlled code unless a file is small, non-identifying, and necessary for reproducibility.
- Record every analytic decision that affects feature stability, segmentation sensitivity, or model interpretation before manuscript drafting.

## Next execution steps

1. Verify candidate dataset availability and current access terms.
2. Build a machine-readable manifest schema for imaging series, masks, metadata, and derived feature tables.
3. Add a reproducible environment file once the initial Python/R imaging stack is selected.
4. Convert `docs/analysis_plan.md` into modular scripts for acquisition, preprocessing, perturbation, extraction, and stability testing.

## Status

Documentation refreshed for current scaffold use on 2026-05-26. The repository remains pre-analysis and manuscript-preparation oriented.
