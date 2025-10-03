"""
Demonstrates basic properties of real numbers: completeness, order, and density of rationals.
"""
import numpy as np

# Example: Density of rationals

def find_rational_between(a, b):
    """Find a rational number between a and b (a < b)."""
    if a >= b:
        raise ValueError("a must be less than b")
    return (a + b) / 2

if __name__ == "__main__":
    a = 1.414
    b = 1.415
    q = find_rational_between(a, b)
    print(f"A rational between {a} and {b} is approximately {q}")
