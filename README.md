# PET Noise Radiomics Robustness

Reproducible open-data study evaluating how PET image noise affects lesion segmentation, radiomics feature stability, and downstream biomedical model reliability in public PET/CT cancer imaging datasets.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active research scaffold; no analysis results should be treated as final until data acquisition, citation validation, and reproducibility checks are complete.  
**Last documentation refresh:** 2026-08-17

## Public-Interest Research Boundary

This repository is maintained for biomedical imaging scholarship, open-data methods, reproducible radiomics research, and transparent methodological evaluation.

It does not provide clinical advice, patient-level findings, diagnostic interpretation, treatment recommendations, product claims, automated decision authority, regulatory conclusions, or deployment guidance. Any downstream modeling discussed here remains research-bounded until independently validated for its intended use.

## Working aim

This repository supports a nuclear-medicine and biomedical data-science project focused on low-count PET, simulated noise perturbation, radiomics robustness, and open cancer-imaging datasets.

## Core research question

How sensitive are PET/CT lesion radiomics features and segmentation-derived measures to simulated image noise, and which features remain stable enough for defensible downstream biomedical modeling?

## Current update — 2026-08-17

The repository remains pre-analysis and manuscript-preparation oriented. The current documentation priority is to verify dataset access terms, lock a manifest schema for imaging series and masks, preserve source and citation metadata, and keep all performance or robustness claims explicitly bounded until reproducibility and validation checks are complete.

### Current Stage

- Stage: Open-data biomedical imaging scaffold
- Evidence status: Analysis validation pending
- Data status: Public or appropriately governed imaging data only; raw imaging remains outside git unless redistribution is explicitly permitted
- Primary limitation: Requires dataset verification, reproducible extraction, sensitivity analysis, and independent validation before publication-level or clinical claims

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

Raw imaging data should not be committed to this repository. Store data locally or through approved external storage and track only download instructions, manifests, checksums, derived non-sensitive tables, and reproducible scripts.

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
- Distinguish synthetic or perturbation-based robustness findings from external clinical validity.
- Keep all claims traceable to source data, transformation steps, validation checks, and versioned outputs.

## Next execution steps

1. Verify candidate dataset availability and current access terms.
2. Build a machine-readable manifest schema for imaging series, masks, metadata, and derived feature tables.
3. Add a reproducible environment file once the initial Python/R imaging stack is selected.
4. Convert `docs/analysis_plan.md` into modular scripts for acquisition, preprocessing, perturbation, extraction, and stability testing.
5. Connect validated outputs to the broader public-health and biomedical portfolio evidence ledger.

## Status

Documentation refreshed on 2026-08-17. The repository remains pre-analysis and manuscript-preparation oriented, with public-interest, reproducibility, and claim-boundary language now aligned with the broader portfolio documentation standard.
