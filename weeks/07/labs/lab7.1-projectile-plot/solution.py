"""CS 104 - Lab 7.1

Plotting Projectile Height: given an initial upward velocity, compute and
plot a projectile's height over its whole flight using NumPy and
Matplotlib.

@author: Course Staff
@date: semester, year
"""

import numpy as np
import matplotlib.pyplot as plt

G = 9.8  # acceleration of gravity, m/s^2


def main():
    v0 = float(input("Initial velocity (m/s): "))
    t_total = 2 * v0 / G

    t = np.linspace(0, t_total, 100)
    h = v0 * t - 0.5 * G * t ** 2

    plt.plot(t, h)
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Height")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
