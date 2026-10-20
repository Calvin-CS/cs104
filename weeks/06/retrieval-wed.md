# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 6, Wednesday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: POGIL Act06 (flow of execution, arguments, return values), Labs 6.12-6.15; uses Week 5 loops. -->

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

What do the two calls print?

```python
def show(a, b):
    print(a, b)
# --- main program ---
show(1, 2)
show(b=1, a=2)
```

[[CHOICES]]
- `1 2`, then `1 2`
* `1 2`, then `2 1`
- `1 2`, then an error
- `2 1`, then `2 1`
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
