# CS-104 Quiz 2
meta: Fall 2026

This is an in-class, closed-book quiz (30 points). If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

<!-- Version B. Covers Weeks 4-5: boolean expressions, if/elif/else, for and while loops, range, accumulators. -->

<!-- Version B question order, as numbered in version A: 4, 6, 5, 2, 1, 3 -->

## Q (2 points)

Fill in the blanks in each `range(...)` call so the loop prints exactly the numbers described (1 point each).

a) Every multiple of 6 from 6 to 60, inclusive:

```python
for n in range(___, ___, ___):
    print(n)
```

b) The numbers 40, 36, 32, ..., 8, 4 (counting down by 4):

```python
for n in range(___, ___, ___):
    print(n)
```

[[BLANK height=20]]

[[KEY]]
a) `range(6, 61, 6)` (any stop from 61 to 66 works). b) `range(40, 0, -4)` (any stop from 0 to 3 works).
[[/KEY]]

## Q (8 points)

Write a code segment that repeatedly inputs whole numbers from the user until the user enters `0`. Then it prints how many numbers were entered (not counting the 0), their average, and the smallest one. Do **not** use the built-in `min` function or a list. If no numbers were entered before the 0, print `no numbers` instead. Example run:

```
Number: 4
Number: 11
Number: -3
Number: 0
Count: 3, average: 4.0, smallest: -3
```

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=230]]

[[KEY]]
```python
count = 0
total = 0
smallest = None
n = int(input("Number: "))
while n != 0:
    count = count + 1
    total = total + n
    if smallest is None or n < smallest:
        smallest = n
    n = int(input("Number: "))
if count == 0:
    print("no numbers")
else:
    print("Count:", count, "average:", total / count, "smallest:", smallest)
```

Grading: loop that stops at 0 2, count 1, average 1, smallest (works for positives) 2, "no numbers" case 1, output 1. Starting `smallest` at 0 loses the "smallest" point if all numbers are positive.
[[/KEY]]

## Q (4 points)

Consider the following (syntactically correct) code segment:

```python
count = 0
for i in range(15, 0, -3):
    count = count + i
print(count)
```

a) What does it print? b) Write a `while` loop that does the same thing.

[[BLANK height=130]]

[[KEY]]
a) `45` (1 point). b) 3 points:

```python
count = 0
i = 15
while i > 0:
    count = count + i
    i = i - 3
print(count)
```
[[/KEY]]

## Q (4 points)

What does this code print? Write every line of output.

```python
total = 0
for i in range(2, 12, 3):
    if i % 2 == 0:
        total = total + i
    else:
        total = total - 1
    print(i, total)
print("done", total)
```

[[BLANK height=100]]

[[KEY]]
`2 2`, `5 1`, `8 9`, `11 8`, `done 8` (grading: ¾ point per loop line, 1 point for the last line).
[[/KEY]]

## Q (5 points)

Assume `x = 6`, `y = 11`, and `word = 'Bob'`. Give the value of each Python expression below (½ point each). If it raises an error instead, name the error.

[[PAIRS]]
EX: >>> not False -> True
>>> x > 5 and y < 11
>>> x > 5 or y < 11
>>> not x == 6
>>> 5 < x <= 6
>>> x % 2 == 0 and y % 2 == 0
>>> 'o' in word
>>> 'B' in word.lower()
>>> y == 6 or 7
>>> not (x > y)
>>> x + y > 15 and word == 'bob'
[[/PAIRS]]

[[KEY]]
Answers: `False`, `True`, `False`, `True`, `False`, `True`, `False`, `7`, `True`, `False`.
[[/KEY]]

## Q (7 points)

Write a code segment that computes a movie ticket price. It inputs the customer's age (as an integer) and the day of the week (e.g. `Tue`). Then:

- If the age is negative, print `invalid age` and nothing else.
- Otherwise, the base price is $7 for ages under 12, $12 for ages 12 to 64, and $8 for ages 65 and up.
- On Tuesdays (`Tue`), every ticket is $3 off.
- Print the final price, e.g. `Price: 9`.

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=230]]

[[KEY]]
```python
age = int(input("Age: "))
day = input("Day: ")
if age < 0:
    print("invalid age")
else:
    if age < 12:
        price = 7
    elif age <= 64:
        price = 12
    else:
        price = 8
    if day == "Tue":
        price = price - 3
    print("Price:", price)
```

Grading: inputs with conversion 1, invalid check 1, three age ranges 3, Tuesday discount 1, output 1.
[[/KEY]]
