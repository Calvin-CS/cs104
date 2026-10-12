# CS-104 Quiz 3
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (4 points)

Write a function called `trapezoid_area` that receives the lengths of the two parallel sides (`base1` and `base2`) and the height (`height`) of a trapezoid, and returns its area. This can be computed as:

area = average_base × height

where `average_base` is the average (mean) of `base1` and `base2`. Be sure to use appropriate Python syntax. (You do not need to provide an algorithm, documentation, or test cases.)

[[BLANK height=160]]

## Q (2 points)

Assume a function `double(x)` has already been defined that returns twice the value of `x`. Write a code segment that uses (calls) this function to compute and print the sum of `double(3)`, `double(5)`, and `double(10)`.

[[BLANK height=90]]

## Q (2 points)

Consider the following code:

```python
import numpy as np
values = [1, 2, 3]
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
y = x ** 2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Squares")
plt.show()
```

In the space below, sketch roughly what the resulting plot will look like. Include the axes, the approximate shape of the curve, and where each label and the title appear. (It does not need to be precise.)

[[BLANK height=180]]
