# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 7, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: Quiz 3 prep — NumPy arrays, np.exp, and Matplotlib (POGIL Act09). -->

## Q

What do the two print statements output?

```python
import numpy as np
values = [4, 5]
arr = np.array(values)
print(values * 3)
print(arr * 3)
```

[[CHOICES]]
- `[12, 15]`, then `[12 15]`
* `[4, 5, 4, 5, 4, 5]`, then `[12 15]`
- `[4, 5, 4, 5, 4, 5]`, then `[4 5 4 5 4 5]`
- A `TypeError` for both
[[/CHOICES]]

## Q

Which call produces the array `[0. 0.25 0.5 0.75 1.]`?

[[CHOICES]]
- `np.arange(0, 1, 0.25)`
- `np.linspace(0, 1, 4)`
- `np.arange(0, 1, 5)`
* `np.linspace(0, 1, 5)`
[[/CHOICES]]

## Q

What does this code print?

```python
import numpy as np
x = np.array([0, 1, 2, 3])
y = x ** 2
print(y)
```

[[CHOICES]]
* `[0 1 4 9]`
- `[0 2 4 6]`
- `[0, 1, 2, 3, 0, 1, 2, 3]`
- It raises a `TypeError`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

A radioactive sample decays over time. The amount left after `t` years is

N = 100 × e^(-0.5 t)

Write a code segment that uses NumPy to create 50 evenly spaced times from 0 to 8 years, computes the amount left at each time (use `np.exp`), and uses Matplotlib to plot amount versus time with the axis labels `Time (years)` and `Amount (g)` and a title.

[[BLANK height=190]]

[[KEY]]
Sample solution:

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8, 50)
n = 100 * np.exp(-0.5 * t)
plt.plot(t, n)
plt.xlabel("Time (years)")
plt.ylabel("Amount (g)")
plt.title("Radioactive Decay")
plt.show()
```
[[/KEY]]
