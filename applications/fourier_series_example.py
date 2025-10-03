"""
Application: Fourier Series Approximation of a Square Wave
"""
import numpy as np
import matplotlib.pyplot as plt

# Square wave function (periodic)
def square_wave(x):
    return np.where(np.sin(x) >= 0, 1, -1)

# Fourier series approximation (N terms)
def fourier_series_square_wave(x, N):
    result = np.zeros_like(x)
    for n in range(1, N+1, 2):  # odd harmonics only
        result += (4/np.pi) * (1/n) * np.sin(n*x)
    return result

if __name__ == "__main__":
    x = np.linspace(-np.pi, np.pi, 1000)
    y_true = square_wave(x)
    y_approx = fourier_series_square_wave(x, 11)
    plt.plot(x, y_true, label="Square Wave")
    plt.plot(x, y_approx, label="Fourier Approximation (N=11)")
    plt.legend()
    plt.title("Fourier Series Approximation of a Square Wave")
    plt.show()
