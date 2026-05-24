# Manual Dataset Validation Checklist

## Purpose

Use this checklist when automated source validation cannot confirm official dataset metadata. No dataset can support manuscript claims until this checklist is completed and summarized in `docs/dataset_validation_log.md` and `data/manifests/dataset_registry.csv`.

## Required capture fields

For each dataset, record:

- dataset ID;
- official source URL;
- access date;
- source owner;
- collection title exactly as listed;
- persistent identifier or DOI if provided;
- required citation text;
- license or data-use terms;
- access method;
- account/authentication requirement;
- download tool or API requirement;
- imaging modality;
- tracer;
- disease site or clinical domain;
- number of patients or studies if listed;
- segmentation, mask, annotation, or label availability;
- annotation file format;
- metadata completeness;
- redistribution restrictions;
- decision: include, hold, or exclude;
- reason for decision.

## FDG-PET-CT-Lesions checklist

- [ ] Official TCIA page opens in normal browser.
- [ ] Collection title confirmed.
- [ ] Data citation captured.
- [ ] TCIA wiki or collection page citation captured if separate.
- [ ] License/use restrictions captured.
- [ ] Download mechanism confirmed.
- [ ] PET/CT modality confirmed.
- [ ] FDG tracer confirmed.
- [ ] Lesion mask or annotation format confirmed.
- [ ] Local manifest feasibility confirmed.
- [ ] Inclusion decision recorded.

## AutoPET checklist

- [ ] Grand Challenge page opens in normal browser.
- [ ] Account/authentication requirement captured.
- [ ] Challenge rules and data-use restrictions captured.
- [ ] Dataset citation captured.
- [ ] PET/CT modality confirmed.
- [ ] FDG tracer confirmed if listed.
- [ ] Segmentation mask availability confirmed.
- [ ] Redistribution limits captured.
- [ ] Inclusion decision recorded.

## LUNG-PET-CT-DX checklist

- [ ] Official TCIA page opens in normal browser.
- [ ] Collection title confirmed.
- [ ] Data citation captured.
- [ ] License/use restrictions captured.
- [ ] Download mechanism confirmed.
- [ ] PET/CT modality confirmed.
- [ ] Lung cancer clinical domain confirmed.
- [ ] Annotation or label availability confirmed.
- [ ] Inclusion decision recorded.

## PSMA-PET-CT-Lesions checklist

- [ ] Official TCIA page opens in normal browser.
- [ ] Collection title confirmed.
- [ ] Data citation captured.
- [ ] License/use restrictions captured.
- [ ] Download mechanism confirmed.
- [ ] PSMA PET/CT modality confirmed.
- [ ] Prostate cancer clinical domain confirmed.
- [ ] Lesion mask or annotation format confirmed.
- [ ] Inclusion decision recorded.

## Decision rule

Prioritize `fdg_pet_ct_lesions` for v0.1.0 if it confirms PET/CT modality, lesion-level masks or annotations, stable access, and clear citation requirements.

Hold AutoPET as a secondary option until challenge data-use terms are confirmed.

Do not use PSMA-PET-CT-Lesions as the first workflow unless FDG-PET-CT-Lesions is rejected or inaccessible.
