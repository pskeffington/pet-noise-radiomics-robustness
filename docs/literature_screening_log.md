# Literature Screening Log

## Purpose

This log preserves candidate literature leads without upgrading them to verified manuscript citations. A source listed here must still pass DOI, publisher, PubMed, or authoritative source verification before it can move into `docs/source_citation_registry.md` as `verified`.

## Screening statuses

- `candidate`: potentially relevant but not verified.
- `method-relevant`: supports a method concept but still requires metadata verification.
- `off-scope`: not directly useful for this PET/CT radiomics noise project.
- `verify-next`: high-priority candidate for DOI/publisher/PubMed confirmation.
- `verified`: moved to source citation registry.

## Candidate leads — 2026-05-24

| Lead ID | Topic | Candidate source | Screening status | Relevance | Verification needed |
|---|---|---|---:|---|---|
| `lead_pet_robust_001` | FDG-PET radiomics feature stability | Leijenaar et al., Stability of FDG-PET radiomics features: an integrated analysis of test-retest and inter-observer variability, Acta Oncologica, 52(7), 1391-1397 | verify-next | Directly aligned with PET radiomics repeatability and feature stability. | DOI, publisher page, PubMed if available. |
| `lead_perturb_001` | Radiomics robustness by perturbation | Zwanenburg et al., Assessing robustness of radiomic features by image perturbation | candidate | Supports perturbation-chain logic and ICC-based robustness filtering, but appears CT-focused in screening result. | Published version, DOI, modality scope, publisher page. |
| `lead_low_count_001` | PET image denoising and noise-level awareness | Li et al., A noise-level-aware framework for PET image denoising | candidate | Supports the concept that PET noise is count-dependent and spatially variable. | Published version or preprint decision, DOI if any, methods relevance to synthetic perturbation. |
| `lead_low_count_002` | Low-count PET reconstruction | Lim et al., Improved low-count quantitative PET reconstruction with an iterative neural network | candidate | Supports low-count PET reconstruction/noise framing. | Published version or preprint decision, DOI if any, relevance to this project's non-reconstruction perturbation assumptions. |
| `lead_low_count_003` | Low-count PET denoising | Xie et al., Unified noise-aware network for low-count PET denoising | candidate | Supports low-count PET denoising framing but may be deep-learning-denoising rather than radiomics robustness. | Published version or preprint decision, DOI if any, scope decision. |
| `lead_review_001` | PET/SPECT radiomics review | Salmanpour et al., Handcrafted vs. deep radiomics vs. fusion vs. deep learning review | candidate | Recent review lead; may help introduction only if peer-reviewed and relevant. | Publication status, DOI, journal, review quality. |

## Current decision

Do not mark `meth_pet_radiomics_robustness` or `meth_low_count_pet_noise` as verified from this pass.

Prioritize `lead_pet_robust_001` for direct verification because it appears most tightly aligned with FDG-PET radiomics feature stability.

Use low-count PET denoising/reconstruction leads only to support background framing after determining whether the project models image-domain perturbation, count-domain simulation, or reconstruction-domain effects.
