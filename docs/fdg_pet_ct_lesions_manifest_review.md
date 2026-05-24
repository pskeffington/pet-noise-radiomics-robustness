# FDG-PET-CT-Lesions Manifest Review

## Uploaded source object

- File: `GC_manifest_FDG-PET-CT-Lesions_20260326.csv`
- Date embedded in file name: 2026-03-26
- Repository action: summarize only; do not commit raw imaging or full external manifest without need.

## Manifest-level findings

| Field | Value |
|---|---:|
| Study name | A whole-body FDG-PET/CT dataset with manually annotated tumor lesions |
| Accession | `phs004225` |
| Rows | 3,042 |
| Unique participants | 900 |
| File type | DICOM |
| Study data type | Image Annotation, Imaging |
| CT records | 1,014 |
| PT records | 1,014 |
| SEG records | 1,014 |
| Participants with CT, PT, and SEG | 900 |
| Total listed size | 166.557 GB |
| CT listed size | 139.926 GB |
| PT listed size | 26.603 GB |
| SEG listed size | 0.028 GB |
| Duplicate file IDs | 0 |
| Duplicate file names | 0 |

## Interpretation

The uploaded manifest materially improves Stage 2 dataset feasibility. It confirms that the primary candidate has DICOM CT, PET, and segmentation records and that all 900 participants have all three modality classes represented.

This does not yet complete official citation validation. The official TCIA or source collection page must still be captured for:

- official citation text;
- data-use/access terms;
- collection description;
- download workflow;
- any publication or DOI tied to the collection;
- annotation documentation.

## Decision

Move `fdg_pet_ct_lesions` from a purely manual source-check candidate to a `manifest-received` dataset candidate in planning notes.

Do not mark it `analysis-ready` until official source-page citation and access terms are verified.

## Next actions

1. Preserve only summary-level manifest metadata in the repo.
2. Use the full CSV locally for acquisition planning.
3. Add an image-manifest builder that can ingest the full local CSV and emit participant-level CT/PT/SEG linkage tables.
4. Continue to block manuscript claims that depend on official collection citation or data-use terms.
