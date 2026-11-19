# CS-104 Quiz 2
meta: Fall 2026

This is an in-class, closed-book quiz (30 points). If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

<!-- Version A. Covers Weeks 4-5: boolean expressions, if/elif/else, for and while loops, range, accumulators. -->

## Q (5 points)

Assume `x = 4`, `y = 9`, and `name = 'Ada'`. Give the value of each Python expression below (½ point each). If it raises an error instead, name the error.

[[PAIRS]]
EX: >>> not True -> False
>>> x > 3 and y < 9
>>> x > 3 or y < 9
>>> not x == 4
>>> 3 < x <= 4
>>> x % 2 == 0 and y % 2 == 0
>>> 'd' in name
>>> 'A' in name.lower()
>>> y == 4 or 5
>>> not (x > y)
>>> x + y > 12 and name == 'ada'
[[/PAIRS]]

[[KEY]]
Answers: `False`, `True`, `False`, `True`, `False`, `True`, `False`, `5`, `True`, `False`.
[[/KEY]]

## Q (4 points)

What does this code print? Write every line of output.

```python
total = 0
for i in range(1, 10, 3):
    if i % 2 == 0:
        total = total + i
    else:
        total = total - 1
    print(i, total)
print("done", total)
```

[[BLANK height=100]]

[[KEY]]
`1 -1`, `4 3`, `7 2`, `done 2` (one line each; 1 point per line).
[[/KEY]]

## Q (7 points)

Write a code segment that computes a shipping cost. It inputs a package weight in kg (as a float) and whether the shipping is express (the user types `yes` or `no`). Then:

- If the weight is 0 or less, print `invalid weight` and nothing else.
- Otherwise, the base cost is $5 for up to 1 kg, $9 for more than 1 kg and up to 5 kg, and for more than 5 kg it is $9 plus $2 for every kg above 5 (e.g. 7.5 kg costs 9 + 2 × 2.5 = $14).
- Express shipping adds $10 to the base cost.
- Print the final cost, e.g. `Cost: 24.0`.

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=230]]

[[KEY]]
```python
weight = float(input("Weight (kg): "))
express = input("Express (yes/no): ")
if weight <= 0:
    print("invalid weight")
else:
    if weight <= 1:
        cost = 5
    elif weight <= 5:
        cost = 9
    else:
        cost = 9 + 2 * (weight - 5)
    if express == "yes":
        cost = cost + 10
    print("Cost:", cost)
```

Grading: inputs with conversion 1, invalid check 1, three weight ranges 3, express surcharge 1, output 1.
[[/KEY]]

## Q (2 points)

Fill in the blanks in each `range(...)` call so the loop prints exactly the numbers described (1 point each).

a) Every multiple of 7 from 7 to 70, inclusive:

```python
for n in range(___, ___, ___):
    print(n)
```

b) The numbers 30, 27, 24, ..., 6, 3 (counting down by 3):

```python
for n in range(___, ___, ___):
    print(n)
```

[[BLANK height=20]]

[[KEY]]
a) `range(7, 71, 7)` (any stop from 71 to 77 works). b) `range(30, 0, -3)` (any stop from 0 to 2 works).
[[/KEY]]

## Q (4 points)

Consider the following (syntactically correct) code segment:

```python
count = 0
for i in range(10, 0, -2):
    count = count + i
print(count)
```

a) What does it print? b) Write a `while` loop that does the same thing.

[[BLANK height=130]]

[[KEY]]
a) `30` (1 point). b) 3 points:

```python
count = 0
i = 10
while i > 0:
    count = count + i
    i = i - 2
print(count)
```
[[/KEY]]

## Q (8 points)

Write a code segment that repeatedly inputs whole numbers from the user until the user enters `0`. Then it prints how many numbers were entered (not counting the 0), their sum, and the largest one. Do **not** use the built-in `max` function or a list. If no numbers were entered before the 0, print `no numbers` instead. Example run:

```
Number: 4
Number: 11
Number: -2
Number: 0
Count: 3, sum: 13, largest: 11
```

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=230]]

[[KEY]]
```python
count = 0
total = 0
largest = None
n = int(input("Number: "))
while n != 0:
    count = count + 1
    total = total + n
    if largest is None or n > largest:
        largest = n
    n = int(input("Number: "))
if count == 0:
    print("no numbers")
else:
    print("Count:", count, "sum:", total, "largest:", largest)
```

Grading: loop that stops at 0 2, count 1, sum 1, largest (works for negatives) 2, "no numbers" case 1, output 1. Starting `largest` at 0 loses the "largest" point if all numbers are negative.
[[/KEY]]
