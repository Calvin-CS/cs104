"""CS 104 - Lab 7.2

Newton's Law of Cooling: given a starting temperature, a room temperature,
and a time constant, plot how an object's temperature decays toward room
temperature over time, with markers for the one-time-constant milestone.

@author: Course Staff
@date: semester, year
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    T0 = float(input("T0 (°C): "))
    T_room = float(input("T room (°C): "))
    tau = float(input("tau (minutes): "))

    t = np.linspace(0, 5 * tau, 200)
    temp = T_room + (T0 - T_room) * np.exp(-t / tau)

    plt.plot(t, temp)
    plt.xlabel("Time (minutes)")
    plt.ylabel("Temperature (°C)")
    plt.title("Newton's Law of Cooling")
    plt.grid(True)

    plt.axhline(T_room + (T0 - T_room) * np.exp(-1), color="gray", linestyle="--")
    plt.axvline(tau, color="gray", linestyle="--")

    plt.show()


if __name__ == "__main__":
    main()
