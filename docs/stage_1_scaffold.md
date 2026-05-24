# Stage 1 Scaffold

## Objective

Create a publication-oriented repository structure emphasizing:

- reproducibility;
- citation verification;
- open-data transparency;
- modular biomedical imaging workflows;
- future manuscript portability.

## Immediate execution order

### 1. Dataset validation

Validate existence, licensing, modality, and download accessibility for:

- TCIA FDG-PET-CT-Lesions;
- AutoPET;
- TCIA LUNG-PET-CT-DX;
- TCIA PSMA-PET-CT-Lesions.

### 2. Environment definition

Establish:

- Python version;
- package requirements;
- notebook policy;
- deterministic seed policy.

### 3. Noise framework

Define:

- synthetic PET count reduction strategy;
- Gaussian/Poisson perturbation assumptions;
- reconstruction assumptions;
- perturbation reproducibility.

### 4. Feature extraction plan

Target:

- PyRadiomics;
- SUV metrics;
- texture features;
- shape features;
- repeatability statistics.

### 5. Stability metrics

Candidate metrics:

- ICC;
- coefficient of variation;
- Bland-Altman;
- feature drift analysis.

### 6. Manuscript preparation

Target journal candidates:

- Journal of Nuclear Medicine;
- EJNMMI Physics;
- BMC Medical Imaging;
- Scientific Reports.
