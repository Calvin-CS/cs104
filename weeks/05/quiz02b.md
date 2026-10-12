# CS-104 Quiz 2
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (2 points)

Give the value of each Python expression below. If it raises an error instead, name the error.

[[PAIRS]]
EX: >>> not True -> False
>>> False or True
>>> 6 >= 6 and 1 > 9
>>> 8 != 8
>>> 2 < 1 or 4 > 3
[[/PAIRS]]

## Q (3 points)

Write a code segment that inputs a numeric test score from the user (as a float, 0-100) and prints one of the following, based on the value:

- `"A"` if the score is 90 or above
- `"B"` if the score is at least 80 and below 90
- `"C"` if the score is at least 70 and below 80
- `"F"` if the score is below 70

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=180]]

## Q (2 points)

Fill in the blanks in the `range(...)` call below so this code prints every multiple of 4 from 4 to 40, inclusive:

```python
for n in range(___, ___, ___):
    print(n)
```

[[BLANK height=60]]

## Q (2 points)

Consider the following (syntactically correct) code segment:

```python
total = 0
for i in range(2, 21, 2):
    total = total + i
print(total)
```

Write a `while` loop that does the same thing.

[[BLANK height=110]]

## Q (1 point)

The following code is supposed to print the numbers 1 through 5, but it has a bug. Identify the bug and explain how to fix it.

```python
i = 1
while i <= 5:
    print(i)
```

[[BLANK height=70]]
