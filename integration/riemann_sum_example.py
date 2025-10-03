"""
Demonstrates a Riemann sum approximation for the integral of f(x) = x^2 on [0, 1].
"""
import numpy as np

def f(x):
    return x ** 2

def riemann_sum(a, b, n):
    x = np.linspace(a, b, n+1)
    dx = (b - a) / n
    left_sum = np.sum(f(x[:-1]) * dx)
    print(f"Riemann sum approximation with n={n}: {left_sum}")

if __name__ == "__main__":
    riemann_sum(0, 1, 10)
    riemann_sum(0, 1, 100)
