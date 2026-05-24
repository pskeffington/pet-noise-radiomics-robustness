from radiomics import featureextractor


DEFAULT_SETTINGS = {
    'binWidth': 25,
    'resampledPixelSpacing': None,
    'interpolator': 'sitkBSpline'
}


extractor = featureextractor.RadiomicsFeatureExtractor(**DEFAULT_SETTINGS)


if __name__ == '__main__':
    print('Radiomics extractor initialized.')
