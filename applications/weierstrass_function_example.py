"""
Application: The Weierstrass Function (Continuous Everywhere, Differentiable Nowhere)
"""
import numpy as np
import matplotlib.pyplot as plt

def weierstrass(x, a=0.5, b=7, n_terms=20):
    result = np.zeros_like(x)
    for n in range(n_terms):
        result += a**n * np.cos(b**n * np.pi * x)
    return result

if __name__ == "__main__":
    x = np.linspace(-2, 2, 1000)
    y = weierstrass(x)
    plt.plot(x, y)
    plt.title("Weierstrass Function: Continuous Everywhere, Differentiable Nowhere")
    plt.show()
