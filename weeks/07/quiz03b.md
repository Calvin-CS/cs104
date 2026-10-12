# CS-104 Quiz 3
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (4 points)

Write a function called `cone_volume` that receives the radius (`radius`) and height (`height`) of a cone, and returns its volume. This can be computed as:

volume = (1/3) × π × radius² × height

where `math.pi` gives the value of π (assume `import math` has already been done). Be sure to use appropriate Python syntax. (You do not need to provide an algorithm, documentation, or test cases.)

[[BLANK height=160]]

## Q (2 points)

Assume a function `square(x)` has already been defined that returns the square of `x`. Write a code segment that uses (calls) this function to compute and print the sum of `square(2)`, `square(4)`, and `square(6)`.

[[BLANK height=90]]

## Q (2 points)

Consider the following code:

```python
import numpy as np
values = [10, 20]
arr = np.array(values)
print(values * 2)
print(arr * 2)
```

What does each `print` statement output, and why are the two results different?

[[BLANK height=100]]

## Q (2 points)

Consider the following code:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sqrt(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("square root")
plt.title("Square Roots")
plt.show()
```

In the space below, sketch roughly what the resulting plot will look like. Include the axes, the approximate shape of the curve, and where each label and the title appear. (It does not need to be precise.)

[[BLANK height=180]]
