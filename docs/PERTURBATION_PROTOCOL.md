# Perturbation Protocol

## Purpose

Define the first reproducible PET noise and radiomics feature-stability perturbation protocol.

## Current status

Early-stage methods development.

## Protocol decisions

| Decision | Status | Notes |
|---|---|---|
| Public PET/CT dataset | Pending | Record dataset source and access terms |
| Lesion segmentation source | Pending | Manual, provided, or algorithmic segmentation |
| Noise model | Pending | Define simulated perturbation assumptions |
| Perturbation levels | Pending | Define reproducible levels and seeds |
| Radiomics feature extractor | Pending | Record software and settings |
| Stability metric | Pending | Define ICC, coefficient of variation, rank stability, or other metric |

## Output targets

- `results/tables/feature_stability_summary.csv`
- `results/tables/perturbation_manifest.csv`
- `results/figures/feature_stability_plot.png`
- `results/logs/run_manifest.json`

## Validation boundary

This protocol supports exploratory robustness evaluation. Do not claim clinical robustness, diagnostic performance, or deployed-model reliability without validated results and documented limitations.
