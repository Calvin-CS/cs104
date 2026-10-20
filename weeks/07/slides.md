# Libraries, NumPy, and Matplotlib

### CS-104 · Week 7

---

# Installing Libraries

---

## Libraries (a.k.a. Dependencies)

- Python ships with many **built-in** modules: `random`, `math`, `turtle`, `os`, ...
- A **library** (or *dependency*) is a package your project needs that *isn't* built into Python.
- Install with `pip install package_name`; check what's installed with `pip list`.
  - In Thonny: **Tools → Manage Packages** does the same thing without a terminal.
- Good projects record their dependencies (e.g. in a `requirements.txt`, via `pip freeze > requirements.txt`) so others can install the same things.

---

## Virtual Environments (briefly)

- A **virtual environment** is an isolated, project-specific set of installed packages — it keeps one project's dependencies from colliding with another's.
- Create one: `python3 -m venv env`
- Activate it before installing anything:
  - macOS/Linux: `source env/bin/activate`
  - Windows: `env\Scripts\activate`
- We won't dwell on this today — just know it exists for when a project needs it.

---

## This Week's Libraries

```
pip install numpy matplotlib
```

- **NumPy** — fast, array-based math in Python
- **Matplotlib** — turns numbers into plots
- Together: compute something, then *see* it

---

# NumPy Basics

---

## Why Not Just Use Lists?

- Plain Python lists are flexible, but awkward for math.

```python
prices = [10, 20, 30]
prices * 1.1          # TypeError! can't multiply a list by a float
```

- **NumPy arrays** let you do math on a whole collection of numbers at once.

```python
import numpy as np

prices = np.array([10, 20, 30])
print(prices * 1.1)   # [11. 22. 33.]
```

---

## Creating Arrays

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.arange(0, 10, 2)     # 0, 2, 4, 6, 8
c = np.linspace(0, 1, 5)    # 5 evenly spaced points from 0 to 1
```

- `np.arange(start, stop, step)` — like `range()`, but returns an array
- `np.linspace(start, stop, num)` — `num` evenly spaced points from `start` to `stop` (inclusive)

---

## Array Math is Element-by-Element

- No loop needed — the operation applies to every value at once:

```python
import numpy as np

t = np.array([0, 1, 2, 3])
print(t * 2 + 1)   # [1 3 5 7]
print(np.exp(t))   # e^0, e^1, e^2, e^3
print(np.sqrt(t))  # square root of each value
```

- Useful constants and functions: `np.pi`, `np.e`, `np.exp()`, `np.sin()`, `np.sqrt()`, ...

---

## Exercise 7.a: Array Practice

*Exercise*

```python
import numpy as np

t = np.linspace(0, 10, 5)
```

- What are the 5 values in `t`?
- Without running it, predict what `t * 2` will be. Check your answer.
- Compute `np.exp(-t)` — what happens to the values as `t` gets bigger?

---

# Matplotlib Basics

---

## Your First Plot

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
```

- `plt.plot(x, y)` draws a line through the (x, y) points
- `plt.show()` opens the plot window

---

## Labeling a Plot

```python
plt.plot(x, y)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("My First Plot")
plt.grid(True)
plt.show()
```

- Always label your axes — a plot without labels doesn't tell anyone anything!

---

## Exercise 7.b: Plot Something of Your Own

*Exercise*

- Make an array `x = np.linspace(0, 20, 200)`.
- Plot `y = x ** 2`, with axis labels and a title.
- Then plot `y = np.sin(x)` on its own, separate plot.
- Which one needed more points in `x` to look smooth? Why?

---

# Main Activity: Plotting an RC Circuit Response

---

## The RC Circuit

- A **resistor (R)** and **capacitor (C)** in series, connected to a voltage source `V0`.
- When the switch closes, the capacitor **charges up** over time — it doesn't jump instantly to `V0`.
- Charging voltage across the capacitor, as a function of time:

```
V(t) = V0 * (1 - e^(-t / (R * C)))
```

- `R * C` is called the **time constant**, `tau` — how fast the circuit responds.

---

## Exercise 7.c: Charging Curve

*Exercise*

```python
import numpy as np
import matplotlib.pyplot as plt

V0 = 5       # source voltage, in volts
R = 1000     # resistance, in ohms
C = 0.001    # capacitance, in farads

tau = R * C
t = np.linspace(0, 5 * tau, 200)
v = V0 * (1 - np.exp(-t / tau))

plt.plot(t, v)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Charging Response")
plt.grid(True)
plt.show()
```

- What is `tau` for these values of R and C?
- Around what time does the voltage look like it's "basically done" charging?

---

## Exercise 7.d: Marking the Time Constant

*Exercise*

Add a vertical line at `t = tau`, and a horizontal line at `V0 * (1 - e^(-1))` (about 63% of `V0`) — the voltage reached after exactly one time constant.

```python
plt.axvline(tau, color="gray", linestyle="--")
plt.axhline(V0 * (1 - np.exp(-1)), color="gray", linestyle="--")
```

- Confirm on your plot: after one time constant, the capacitor has charged to about 63% of `V0`.

---

## Exercise 7.e: Discharging

*Exercise*

Now plot the **discharging** response instead — the capacitor starts fully charged at `V0` and decays back to 0 once the source is removed:

```
V(t) = V0 * e^(-t / (R * C))
```

- Modify your charging code to plot this instead.
- Compare the two shapes — how are charging and discharging related?

---

## Exercise 7.f: Try Your Own Values

*Exercise*

With a partner, pick your own R and C values.

- Predict (before running!) whether the circuit will respond faster or slower than the example.
- Plot it and check your prediction.
- Put both your charging and discharging curves on the **same plot**, and add `plt.legend()` so they're labeled.

---

## Wrap-Up

By now you should be able to:

- Install external libraries with `pip`, and explain briefly what a virtual environment is for
- Create NumPy arrays and do element-wise math on them
- Make a labeled plot with Matplotlib
- Use NumPy and Matplotlib together to model and visualize an RC circuit's response over time

You just turned a physics equation into a picture — nice work!
