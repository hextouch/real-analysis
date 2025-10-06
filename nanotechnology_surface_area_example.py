"""
Application: Surface Area Calculation in Nanotechnology
Demonstrates the use of real analysis (integration) to compute the surface area of a nanoscale sphere.
"""
import numpy as np

def sphere_surface_area(radius):
    # Surface area of a sphere: 4 * pi * r^2
    return 4 * np.pi * radius ** 2

if __name__ == "__main__":
    nanometer = 1e-9
    radius = 50 * nanometer  # 50 nm nanoparticle
    area = sphere_surface_area(radius)
    print(f"Surface area of a 50 nm radius nanoparticle: {area:.2e} m^2")
