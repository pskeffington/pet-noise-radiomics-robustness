# Roadmap

## Project frame

Working title: **Noise Robustness of PET/CT Radiomics Features in Open Cancer Imaging Datasets**

Core question: Which PET/CT lesion radiomics features and segmentation-derived measurements remain stable under controlled PET noise perturbation?

Primary defensible lane: PET/CT cancer imaging noise + radiomics robustness using open imaging collections and fully reproducible perturbation workflows.

## Current status

Stage 1 scaffold is complete.

Stage 2 is active for dataset, citation, and source-access validation.

Stage 3 has started at the manifest-builder level because the FDG-PET-CT-Lesions manifest confirms CT/PT/SEG records, but preprocessing remains blocked until official source citation and data-use terms are captured.

## Stage 1 — Scaffold freeze

Status: complete.

Objects:

- `README.md`
- `docs/stage_1_scaffold.md`
- `docs/data_sources.md`
- `docs/citation_registry.md`
- `docs/analysis_plan.md`
- `docs/repo_structure.md`
- `.gitignore`

Exit condition:

- Repository has a publication-oriented structure and clearly states that raw imaging data are not committed.

## Stage 2 — Dataset and environment validation

Status: active.

Objects:

- `data/manifests/dataset_registry.csv`
- `docs/dataset_validation_log.md`
- `requirements.txt`
- `analysis/00_validate_dataset_registry.py`
- `tests/test_dataset_registry.py`
- `docs/source_citation_registry.md`
- `docs/claim_evidence_register.md`
- `docs/fdg_pet_ct_lesions_manifest_review.md`
- `data/manifests/fdg_pet_ct_lesions_manifest_summary.csv`

Exit condition:

- Every candidate dataset has a documented source page, access status, modality status, annotation/mask status, license or use-condition note, citation requirement, and inclusion decision.
- Environment dependencies install cleanly.
- Dataset registry validation passes.
- FDG-PET-CT-Lesions official source citation and access terms are captured.

## Stage 3 — Imaging manifest and preprocessing

Status: active for manifest construction; preprocessing queued.

Objects:

- `analysis/01_build_image_manifest.py`
- `data/manifests/image_manifest_schema.csv`
- `tests/test_image_manifest_builder.py`
- `analysis/02_preprocess_pet_ct.py` queued
- `docs/preprocessing_spec.md` queued

Exit condition:

- Local image inventory can be generated without committing raw DICOM, NIfTI, MHA, or MHD data.
- Derived manifest records participant identifiers, source accession, CT/PT/SEG linkage, modality-specific file IDs, file names, completeness flags, and byte-size summaries.
- Preprocessing does not start until source citation/access terms are verified.

## Stage 4 — Noise perturbation framework

Status: queued.

Objects:

- `analysis/03_simulate_pet_noise.py`
- `docs/noise_framework.md`
- `tests/test_noise_reproducibility.py`

Exit condition:

- Perturbation method is deterministic under fixed seed.
- Poisson/count-reduction assumptions are explicitly separated from true scanner reconstruction claims.
- Each perturbation level produces traceable derived output paths and metadata rows.

## Stage 5 — Radiomics extraction

Status: queued.

Objects:

- `analysis/04_extract_radiomics.py`
- `config/pyradiomics_pet.yaml`
- `tables/radiomics_feature_schema.csv`
- `tests/test_radiomics_table_schema.py`

Exit condition:

- Feature exports contain stable identifiers, perturbation level, image path, mask path, feature class, feature name, and numeric value.
- PyRadiomics configuration is versioned.

## Stage 6 — Robustness statistics

Status: queued.

Objects:

- `analysis/05_feature_stability_metrics.py`
- `tables/feature_stability_results.csv`
- `figures/feature_stability_heatmap.png`
- `docs/statistical_analysis_plan.md`

Exit condition:

- ICC, coefficient of variation, feature drift, and perturbation sensitivity are computed from exported radiomics tables.
- Robust, unstable, and excluded feature sets are declared with transparent thresholds.

## Stage 7 — Manuscript assembly

Status: queued.

Objects:

- `manuscript/main.tex`
- `manuscript/references.bib`
- `manuscript/sections/*.tex`
- `docs/claim_evidence_register.md`

Exit condition:

- Manuscript claims are bound to either validated outputs, verified citations, or explicitly marked limitations.

## Active issue map

- `#1` Validate TCIA and AutoPET dataset accessibility.
- `#2` Implement DICOM to NIfTI preprocessing pipeline.
- `#3` Implement PET radiomics robustness statistics.
- `#4` Implement PyRadiomics feature export validation.
- `#5` Validate citation metadata and DOI registry.
- `#14` Manually verify FDG-PET-CT-Lesions source metadata.
- `#17` Verify PET radiomics robustness and low-count PET noise literature.

## Immediate execution order

1. Run CI validation for dataset registry and image manifest builder.
2. Capture official FDG-PET-CT-Lesions source citation and access terms.
3. Build local participant image manifest from the uploaded GDC manifest.
4. Verify PyRadiomics and IBSI through direct publisher, DOI-registry, or PubMed records.
5. Verify ICC and Bland-Altman statistical-method citations.
6. Draft preprocessing specification only after source terms are captured.
7. Delay noise modeling until dataset access, citation, annotation availability, and preprocessing assumptions are confirmed.
