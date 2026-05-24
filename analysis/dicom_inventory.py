from pathlib import Path
import pydicom
import pandas as pd


def inventory_dicom_tree(root_dir: str):
    rows = []
    root = Path(root_dir)

    for file in root.rglob('*'):
        if not file.is_file():
            continue

        try:
            ds = pydicom.dcmread(str(file), stop_before_pixels=True)

            rows.append({
                'file_path': str(file),
                'patient_id': getattr(ds, 'PatientID', None),
                'study_uid': getattr(ds, 'StudyInstanceUID', None),
                'series_uid': getattr(ds, 'SeriesInstanceUID', None),
                'modality': getattr(ds, 'Modality', None)
            })

        except Exception:
            continue

    return pd.DataFrame(rows)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--root_dir', required=True)
    parser.add_argument('--output_csv', default='dicom_inventory.csv')

    args = parser.parse_args()

    df = inventory_dicom_tree(args.root_dir)
    df.to_csv(args.output_csv, index=False)

    print(df.head())
    print(f'Total records: {len(df)}')
