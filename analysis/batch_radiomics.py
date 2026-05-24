from pathlib import Path
import pandas as pd
from radiomics import featureextractor


extractor = featureextractor.RadiomicsFeatureExtractor()


def run_extraction(image_path: str, mask_path: str):
    result = extractor.execute(image_path, mask_path)
    return dict(result)


def batch_extract(manifest_csv: str, output_csv: str):
    manifest = pd.read_csv(manifest_csv)
    rows = []

    for _, row in manifest.iterrows():
        features = run_extraction(row['image_path'], row['mask_path'])
        features['subject_id'] = row['subject_id']
        rows.append(features)

    output_df = pd.DataFrame(rows)
    output_df.to_csv(output_csv, index=False)

    return output_df


if __name__ == '__main__':
    print('Batch radiomics module initialized.')
