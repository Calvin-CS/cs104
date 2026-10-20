# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 2, Wednesday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: POGIL Act02 (Python calculator, dividing numbers, ints and floats), Labs 2.10-2.11; reviews Week 1 errors. -->

## Q

What is the value of the expression `3 * 4 + 2.0`?

[[CHOICES]]
- `14`
- `18.0`
* `14.0`
- `20.0`
[[/CHOICES]]

## Q

What does `print(17 // 5, 17 % 5)` display?

[[CHOICES]]
* `3 2`
- `3.4 2`
- `2 3`
- `3 2.0`
[[/CHOICES]]

## Q

What happens when this code runs?

```python
a = 2
x = 5
y = ax + 1
```

[[CHOICES]]
- `y` gets the value `11`
- It raises a `SyntaxError`
- It raises a `TypeError`
* It raises a `NameError`, because Python reads `ax` as one variable name (it should be `a * x`)
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that reads a three-digit integer from the user and prints the sum of its digits. For example, for `472` it prints `13` (4 + 7 + 2). Use `//` and `%` to get each digit.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
number = int(input("Number: "))
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
print(hundreds + tens + ones)
```
[[/KEY]]
