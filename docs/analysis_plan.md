# Analysis Plan

## Planned workflow

### Acquisition

- Download approved open PET/CT datasets.
- Generate dataset manifests.
- Validate DICOM consistency.

### Preprocessing

- Resample voxel spacing.
- Normalize PET intensity.
- Standardize metadata.

### Noise perturbation

Candidate perturbations:

- Poisson count reduction;
- Gaussian perturbation;
- synthetic low-dose simulation.

### Segmentation

- ingest provided masks where available;
- benchmark automated segmentation where feasible.

### Radiomics extraction

Target software:

- PyRadiomics.

Target feature groups:

- first-order;
- texture;
- GLSZM;
- GLRLM;
- shape metrics.

### Stability analysis

Evaluate:

- intraclass correlation;
- feature drift;
- perturbation sensitivity;
- segmentation agreement.

### Reporting

Generate:

- reproducible tables;
- figure exports;
- manuscript-ready outputs.
