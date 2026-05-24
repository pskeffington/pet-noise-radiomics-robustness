import pandas as pd
import numpy as np


def intraclass_correlation(values_a, values_b):
    values_a = np.asarray(values_a)
    values_b = np.asarray(values_b)

    if len(values_a) != len(values_b):
        raise ValueError('Input arrays must have equal length.')

    stacked = np.vstack([values_a, values_b])

    mean_raters = np.mean(stacked, axis=0)
    grand_mean = np.mean(stacked)

    ss_between = np.sum((mean_raters - grand_mean) ** 2) * 2
    ss_within = np.sum((stacked - mean_raters) ** 2)

    ms_between = ss_between / (len(values_a) - 1)
    ms_within = ss_within / len(values_a)

    icc = (ms_between - ms_within) / (ms_between + ms_within)

    return icc


if __name__ == '__main__':
    baseline = np.random.rand(50)
    perturbed = baseline + np.random.normal(0, 0.01, 50)

    icc_value = intraclass_correlation(baseline, perturbed)

    print('ICC:', round(float(icc_value), 4))
