# CS-104 Quiz 3
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (8 points)

Write a function called `cone_volume` that receives the radius (`radius`) and height (`height`) of a cone, and returns its volume. This can be computed as:

volume = (1/3) × π × radius² × height

where `math.pi` gives the value of π (assume `import math` has already been done). Be sure to use appropriate Python syntax. (You do not need to provide an algorithm, documentation, or test cases.)

[[BLANK height=160]]

## Q (4 points)

Assume a function `square(x)` has already been defined that returns the square of `x`. Write a code segment that uses (calls) this function to compute and print the sum of `square(2)`, `square(4)`, and `square(6)`.

[[BLANK height=90]]

## Q (4 points)

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

## Q (4 points)

The following code is supposed to plot a labeled graph of y = √x, but running it produces a plot with no axis labels or title. Add the line(s) needed to give the plot an x-axis label of `"x"`, a y-axis label of `"square root"`, and a title of `"Square Roots"`.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sqrt(x)

plt.plot(x, y)
plt.show()
```

[[BLANK height=100]]
