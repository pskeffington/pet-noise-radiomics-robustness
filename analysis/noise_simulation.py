import numpy as np


def apply_gaussian_noise(image: np.ndarray, sigma: float = 0.05):
    noise = np.random.normal(0, sigma, image.shape)
    return image + noise


def apply_poisson_noise(image: np.ndarray, scale_factor: float = 1.0):
    scaled = image * scale_factor
    noisy = np.random.poisson(scaled)
    return noisy / scale_factor


if __name__ == '__main__':
    rng_image = np.random.rand(128, 128)

    gaussian_output = apply_gaussian_noise(rng_image)
    poisson_output = apply_poisson_noise(rng_image)

    print('Gaussian output shape:', gaussian_output.shape)
    print('Poisson output shape:', poisson_output.shape)
