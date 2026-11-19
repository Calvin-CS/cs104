# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 6, Friday

<!-- Covers: POGIL Act06 (flow of execution, return vs. print) from Week 5 Monday, plus the Week 6 functions slides and Labs 6.12-6.15; Quiz 3 prep (writing functions that loop and return values). -->

## Q

In what order do the lines of output appear?

```python
def greet(name):
    print("Hello, " + name)
# --- main program ---
print("Start")
greet("Sam")
print("End")
```

[[CHOICES]]
- `Hello, Sam`, then `Start`, then `End`
- `Start`, then `End`, then `Hello, Sam`
* `Start`, then `Hello, Sam`, then `End`
- Only `Start`, then `End`
[[/CHOICES]]

## Q

What is the complete output of this code?

```python
def add_one(x):
    print(x + 1)
# --- main program ---
result = add_one(5)
print(result)
```

[[CHOICES]]
- `6`, then `6`
- Only `6`
- `None`, then `6`
* `6`, then `None`
[[/CHOICES]]

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

Assume a function `cube(x)` has been defined that returns `x` cubed. What does `print(cube(1 + 2 + 3))` print?

[[CHOICES]]
- `36`
- `6`
* `216`
- `18`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a function `count_above(numbers, limit)` that returns how many elements of the list `numbers` are greater than `limit`. Then write one line that calls it with the list `[3, 8, 1, 9, 5]` and the limit `4`, and prints the result (which should be `3`).

[[BLANK height=190]]

[[KEY]]
Sample solution:

```python
def count_above(numbers, limit):
    count = 0
    for n in numbers:
        if n > limit:
            count = count + 1
    return count

print(count_above([3, 8, 1, 9, 5], 4))
```
[[/KEY]]
