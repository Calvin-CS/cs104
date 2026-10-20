# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 6, Friday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: Quiz 3 prep — writing and calling functions that return values (Week 6). -->

## Q

What does this code print?

```python
def half(x):
    return x / 2

# --- main program ---
total = half(10) + half(4)
print(total)
```

[[CHOICES]]
- `7`
* `7.0`
- `14.0`
- `None`
[[/CHOICES]]

## Q

What is wrong with this function?

```python
def fahrenheit(celsius)
    return celsius * 9 / 5 + 32
```

[[CHOICES]]
- It should use `print` instead of `return`
- `celsius` must be assigned a value before the function is defined
- Nothing; it is correct
* The `def` line is missing a colon (`:`) at the end
[[/CHOICES]]

## Q

Assume a function `cube(x)` has been defined that returns `x` cubed. What does `print(cube(1 + 2 + 3))` print?

[[CHOICES]]
- `36`
- `6`
* `216`
- `18`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

A cylinder's volume is pi × radius² × height. Write a function `cylinder_volume(radius, height)` that returns the volume, using `math.pi` (assume `import math` was already done). Then call it for a radius of 2 and a height of 10, store the result in a variable, and print it rounded to 1 decimal place.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

v = cylinder_volume(2, 10)
print(round(v, 1))
```
[[/KEY]]
