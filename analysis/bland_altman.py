import numpy as np
import matplotlib.pyplot as plt


def bland_altman_plot(values_a, values_b, output_path=None):
    values_a = np.asarray(values_a)
    values_b = np.asarray(values_b)

    means = np.mean([values_a, values_b], axis=0)
    diffs = values_a - values_b

    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs)

    plt.figure(figsize=(6, 4))
    plt.scatter(means, diffs)
    plt.axhline(mean_diff)
    plt.axhline(mean_diff + 1.96 * std_diff, linestyle='--')
    plt.axhline(mean_diff - 1.96 * std_diff, linestyle='--')

    plt.xlabel('Mean')
    plt.ylabel('Difference')
    plt.title('Bland-Altman Plot')

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')

    return mean_diff, std_diff


if __name__ == '__main__':
    a = np.random.rand(50)
    b = a + np.random.normal(0, 0.05, 50)

    bland_altman_plot(a, b)
    print('Bland-Altman plot generated.')
