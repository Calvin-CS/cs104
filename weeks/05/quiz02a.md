# CS-104 Quiz 2
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (2 points)

Give the value of each Python expression below. If it raises an error instead, name the error.

[[PAIRS]]
EX: >>> not False -> True
>>> True and False
>>> 4 <= 4 and 2 > 5
>>> 10 != 10
>>> 3 < 5 or 1 > 100
[[/PAIRS]]

## Q (3 points)

Write a code segment that inputs a temperature in Fahrenheit from the user (as a float) and prints one of the following, based on the value:

- `"freezing"` if the temperature is at or below 32
- `"cold"` if the temperature is above 32 and below 60
- `"mild"` if the temperature is between 60 and 80 (inclusive)
- `"hot"` if the temperature is above 80

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=180]]

## Q (2 points)

Fill in the blanks in the `range(...)` call below so this code prints every multiple of 5 from 5 to 50, inclusive:

```python
for n in range(___, ___, ___):
    print(n)
```

[[BLANK height=60]]

## Q (2 points)

Consider the following (syntactically correct) code segment:

```python
total = 0
for i in range(1, 11):
    total = total + i
print(total)
```

Write a `while` loop that does the same thing.

[[BLANK height=110]]

## Q (1 point)

The following code is supposed to print the numbers 1 through 5, but it has a bug. Identify the bug and explain how to fix it.

```python
i = 1
while i < 5:
    print(i)
    i = i + 1
```

[[BLANK height=70]]
