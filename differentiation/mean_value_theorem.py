"""
Demonstrates the Mean Value Theorem for f(x) = x^2 on [1, 3].
"""
def f(x):
    return x ** 2

def mean_value_theorem(a, b):
    fa = f(a)
    fb = f(b)
    c = (fb - fa) / (b - a)
    print(f"MVT: There exists c in ({a}, {b}) such that f'(c) = {c}")
    # For f(x) = x^2, f'(x) = 2x, so 2c = c => c = c/2, but let's solve for c
    c_val = c / 2
    print(f"For f(x)=x^2, c = {c_val}")

if __name__ == "__main__":
    mean_value_theorem(1, 3)
