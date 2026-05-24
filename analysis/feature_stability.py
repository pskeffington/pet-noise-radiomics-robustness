import pandas as pd


def coefficient_of_variation(series):
    return series.std() / series.mean()


def summarize_feature_stability(df: pd.DataFrame):
    summaries = []

    for column in df.columns:
        summaries.append({
            'feature': column,
            'mean': df[column].mean(),
            'std': df[column].std(),
            'cv': coefficient_of_variation(df[column])
        })

    return pd.DataFrame(summaries)


if __name__ == '__main__':
    mock_df = pd.DataFrame({
        'feature_a': [1.0, 1.1, 1.2, 1.05],
        'feature_b': [10.0, 10.5, 9.8, 10.1]
    })

    print(summarize_feature_stability(mock_df))
