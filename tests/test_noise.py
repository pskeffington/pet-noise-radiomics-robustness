import numpy as np

from analysis.noise_simulation import apply_gaussian_noise
from analysis.noise_simulation import apply_poisson_noise


def test_gaussian_noise_shape():
    image = np.ones((32, 32))
    output = apply_gaussian_noise(image)
    assert output.shape == image.shape


def test_poisson_noise_shape():
    image = np.ones((32, 32))
    output = apply_poisson_noise(image)
    assert output.shape == image.shape
