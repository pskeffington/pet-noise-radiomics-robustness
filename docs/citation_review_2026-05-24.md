# Citation Review Memo — 2026-05-24

## Scope

This memo reviews citation readiness for the PET/CT radiomics noise-robustness project. It separates manuscript-ready citations from planning-only leads.

## Review rule

A citation is manuscript-ready only when confirmed through at least one strong source:

- publisher page;
- DOI registry;
- PubMed;
- TCIA or official challenge record for dataset sources;
- official software documentation when the claim concerns software behavior or versioning.

Secondary pages, search snippets, Wikipedia pages, and unsourced bibliographies are not sufficient for manuscript-use verification.

## Citation status table

| Citation object | Topic | Current status | Manuscript use | Review decision |
|---|---|---:|---:|---|
| `meth_ibsi` | Image Biomarker Standardisation Initiative | methods-planning ready; final-check pending | Methods planning only until publisher/DOI/PubMed page is directly captured | arXiv record confirms title, authors, Radiology 2020 journal reference, and related DOI, but direct publisher/PubMed/DOI-registry capture should be added before submission. |
| `meth_pyradiomics` | PyRadiomics feature extraction | partially verified | Hold | Search found the expected title, journal, volume, pages, and DOI only through weak/secondary indexing. Direct publisher/PubMed/DOI-registry confirmation remains required. |
| `meth_pet_radiomics_robustness` | PET radiomics repeatability/robustness | unverified lead | Hold | Leijenaar et al. is highly relevant but currently supported only by secondary bibliographic discovery in this pass. Verify DOI, publisher, and PubMed before promotion. |
| `meth_low_count_pet_noise` | PET low-count/noise framing | unverified leads | Hold | Current leads are mostly arXiv/deep-learning denoising or reconstruction papers. They may support background only after scope triage and publication/DOI verification. |
| `src_fdg_pet_ct_lesions` | TCIA FDG-PET-CT-Lesions dataset | source-page pending | Hold | Official TCIA source-page validation is still required. |
| `src_autopet` | AutoPET challenge dataset | source-page pending | Hold | Official challenge access/citation validation is still required. |

## Verified or near-verified details captured

### `meth_ibsi`

Working APA 7 citation:

Zwanenburg, A., Leger, S., Vallières, M., Löck, S., & Image Biomarker Standardisation Initiative. (2020). The image biomarker standardization initiative. *Radiology*. https://doi.org/10.1148/radiol.2020191145

Evidence captured:

- arXiv record title: *Image biomarker standardisation initiative*.
- Authors: Alex Zwanenburg, Stefan Leger, Martin Vallières, Steffen Löck, for the Image Biomarker Standardisation Initiative.
- Journal reference: *Radiology* (2020).
- Related DOI: `10.1148/radiol.2020191145`.
- The abstract states that IBSI provides image-biomarker nomenclature, definitions, benchmark datasets, benchmark values, and reporting guidelines for high-throughput image analysis.

Use decision:

Use for methods planning now. Before manuscript submission, capture a direct Radiology, DOI-registry, or PubMed page.

### `meth_pyradiomics`

Working APA 7 citation pending final verification:

van Griethuysen, J. J. M., Fedorov, A., Parmar, C., Hosny, A., Aucoin, N., Narayan, V., Beets-Tan, R. G. H., Fillon-Robin, J.-C., Pieper, S., & Aerts, H. J. W. L. (2017). Computational radiomics system to decode the radiographic phenotype. *Cancer Research, 77*(21), e104-e107. https://doi.org/10.1158/0008-5472.CAN-17-0339

Use decision:

Hold for manuscript use until directly verified through AACR/Cancer Research, DOI registry, or PubMed.

## High-priority literature leads

### `lead_pet_robust_001`

Candidate citation:

Leijenaar, R. T. H., Carvalho, S., Velazquez, E. R., van Elmpt, W. J. C., Parmar, C., Hoekstra, O. S., Hoekstra, C. J., Boellaard, R., Dekker, A. L. A. J., Gillies, R. J., Aerts, H. J. W. L., & Lambin, P. (2013). Stability of FDG-PET radiomics features: An integrated analysis of test-retest and inter-observer variability. *Acta Oncologica, 52*(7), 1391-1397.

Review decision:

This is the strongest PET-specific robustness lead because it directly addresses FDG-PET radiomic feature stability, test-retest variation, and inter-observer variation. It should be the next source verified through DOI, publisher, and PubMed before being promoted into `docs/source_citation_registry.md`.

### `lead_software_benchmark_001`

Candidate citation:

Lei, M., Varghese, B., Hwang, D., Cen, S., Lei, X., Azadikhah, A., Desai, B., Oberai, A., & Duddalwar, V. (2020). Benchmarking features from different radiomics toolkits / toolboxes using Image Biomarkers Standardization Initiative. arXiv:2006.12761.

Review decision:

Useful as a planning lead for cross-toolkit variability, not a core manuscript citation unless a peer-reviewed version or a deliberate preprint-citation decision is made.

### `lead_mri_repeatability_001`

Candidate citation:

Schwier, M., van Griethuysen, J., Vangel, M. G., Pieper, S., Peled, S., Tempany, C. M., Aerts, H. J. W. L., Kikinis, R., Fennessy, F. M., & Fedorov, A. (2018). Repeatability of multiparametric prostate MRI radiomics features. arXiv:1807.06089.

Review decision:

Useful for general repeatability logic and PyRadiomics workflow awareness, but not PET-specific. Do not use as a primary PET robustness citation.

### `lead_fdg_lymphoma_pvc_001`

Candidate citation:

Hasanabadi, S., Azimi, M. S., Karam, M. B., & Arabi, H. (2025). Evaluating the impact of partial volume correction on FDG PET radiomics reproducibility in lymphoma lesions. arXiv:2511.09293.

Review decision:

Potentially useful modern FDG-PET reproducibility lead, but preprint status and publication status require verification. Do not use for manuscript claims unless peer-reviewed status or preprint-use policy is explicitly accepted.

## Literature-review synthesis

The defensible literature structure is narrow and should be built in layers. First, IBSI anchors radiomics standardization: nomenclature, definitions, benchmark data, benchmark values, and reporting guidance. Second, PyRadiomics can be used as the planned extraction platform only after direct citation verification and software-version pinning. Third, FDG-PET radiomics robustness requires PET-specific repeatability evidence, with Leijenaar et al. as the next high-priority verification target. Fourth, low-count PET/noise literature should not be mixed with radiomics robustness until the project decides whether its noise model is image-domain perturbation, count-domain simulation, or reconstruction-domain modeling.

## Manuscript-risk assessment

Current manuscript risk is moderate.

Safe now:

- describe the project as a planned reproducible PET/CT radiomics robustness workflow;
- cite IBSI in planning language, with final-check pending;
- describe the need to verify dataset access and annotation status.

Unsafe now:

- claim FDG-PET-CT-Lesions is analysis-ready;
- claim PyRadiomics is verified as the extraction platform;
- claim a PET noise simulation method is validated;
- cite low-count PET denoising papers as if they validate synthetic radiomics perturbation.

## Next verification order

1. Capture direct publisher/DOI/PubMed record for PyRadiomics.
2. Capture direct DOI/publisher/PubMed record for Leijenaar et al. 2013.
3. Capture direct publisher/DOI/PubMed record for IBSI Radiology 2020.
4. Decide whether low-count/noise citations must be peer-reviewed only or whether arXiv preprints can support background framing.
5. Only after steps 1-4, draft `docs/noise_framework.md` and `docs/statistical_analysis_plan.md`.
