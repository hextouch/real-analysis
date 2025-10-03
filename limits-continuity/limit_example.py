"""
Demonstrates the epsilon-delta definition of a limit for f(x) = 2x as x approaches 1.
"""
def limit_2x_at_1(epsilon):
    x0 = 1
    L = 2 * x0
    delta = epsilon / 2
    print(f"For epsilon = {epsilon}, choose delta = {delta}")
    print(f"If 0 < |x - {x0}| < {delta}, then |2x - {L}| < {epsilon}")

if __name__ == "__main__":
    limit_2x_at_1(0.1)
    limit_2x_at_1(0.01)
