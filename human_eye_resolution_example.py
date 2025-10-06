"""
Application: Theoretical Resolution Limit of the Human Eye
Uses real analysis (limits and geometry) to estimate the smallest resolvable detail.
"""
import numpy as np

def eye_resolution_limit(pupil_diameter_mm=2.0, wavelength_nm=550):
    # Rayleigh criterion: theta = 1.22 * lambda / D
    wavelength_m = wavelength_nm * 1e-9
    pupil_diameter_m = pupil_diameter_mm * 1e-3
    theta = 1.22 * wavelength_m / pupil_diameter_m  # radians
    # Assume typical viewing distance of 25 cm
    distance = 0.25  # meters
    min_resolvable = theta * distance  # meters
    return min_resolvable

if __name__ == "__main__":
    min_detail = eye_resolution_limit()
    print(f"Theoretical minimum resolvable detail by the human eye: {min_detail*1e6:.2f} micrometers")
