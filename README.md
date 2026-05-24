# PET Noise Radiomics Robustness

Reproducible open-data study evaluating how PET image noise affects lesion segmentation, radiomics feature stability, and downstream biomedical model reliability in public PET/CT cancer imaging datasets.

## Working aim 

This repository supports a nuclear-medicine and biomedical data-science project focused on low-count PET, simulated noise perturbation, radiomics robustness, and open cancer-imaging datasets.

## Core research question

How sensitive are PET/CT lesion radiomics features and segmentation-derived measures to simulated image noise, and which features remain stable enough for defensible downstream biomedical modeling?

## Stage 1 scope

Stage 1 establishes the manuscript and analysis scaffold. It does not claim completed analysis.

Objects created in Stage 1:

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

## Status

Stage 1 scaffold initialized.
