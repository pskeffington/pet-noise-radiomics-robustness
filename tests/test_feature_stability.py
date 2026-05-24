import pandas as pd

from analysis.feature_stability import summarize_feature_stability


def test_feature_summary_output():
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })

    output = summarize_feature_stability(df)

    assert 'feature' in output.columns
    assert 'cv' in output.columns
