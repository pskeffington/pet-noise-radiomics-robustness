# Initial Subset Source

## Recommended first subset

Use the AutoPET public PET/CT dataset as the first working subset.

## Rationale

AutoPET is the cleanest first source because it is already organized around whole-body PET/CT lesion segmentation, includes PET/CT image pairs, and is directly aligned with lesion segmentation and radiomics robustness work. Recent AutoPET challenge literature describes public FDG and PSMA PET/CT training data and supports the relevance of automated lesion segmentation in PET/CT imaging.

## Initial local subset target

Start with a small local pilot subset:

- 10 FDG PET/CT cases;
- include available lesion masks when provided;
- store raw data outside the repository;
- commit only manifests, checksums, derived tables, and scripts.

## Secondary source

Use TCIA as the next validation source after AutoPET pilot execution.

Candidate TCIA pathway:

- search TCIA PET/CT collections through NBIA;
- prioritize FDG PET/CT oncology collections;
- generate local manifests;
- validate dataset citation requirements before manuscript use.

## Repository rule

Do not commit DICOM, NIfTI, or compressed imaging archives.
