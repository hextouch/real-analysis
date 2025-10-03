"""
Demonstrates open and closed balls in the metric space (R, d), d(x, y) = |x - y|.
"""
def open_ball(center, radius, x):
    return abs(x - center) < radius

def closed_ball(center, radius, x):
    return abs(x - center) <= radius

if __name__ == "__main__":
    print("Is 1.5 in the open ball B(1, 1)?", open_ball(1, 1, 1.5))
    print("Is 2 in the closed ball B[1, 1]?", closed_ball(1, 1, 2))