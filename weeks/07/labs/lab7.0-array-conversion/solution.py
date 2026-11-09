"""CS 104 - Lab 7.0

Array Unit Conversion: read a comma-separated list of Celsius temperatures
and print the equivalent Fahrenheit temperatures, computed as a single
NumPy array (no explicit loop over the values).

@author: Course Staff
@date: semester, year
"""

import numpy as np

text = input("Celsius temperatures (comma-separated): ")
celsius = np.array([float(piece) for piece in text.split(",")])
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)
