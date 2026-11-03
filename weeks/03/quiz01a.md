# CS-104 Quiz 1
meta: Fall 2026

This is an in-class, closed-book quiz (30 points). If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

<!-- Covers Weeks 1-3: expressions and types, conversions, errors, strings, lists, dictionaries, aliasing. -->

## Q (5 points)

Give the value of each Python expression below (½ point each). Make the resulting type clear (e.g., `8` vs. `8.0` vs. `'8'`). If it raises an error instead, name the error (e.g., "IndexError").

[[PAIRS]]
EX: >>> 'a' + 'b' -> 'ab'
>>> 17 // 5
>>> 17 % 5
>>> 2 ** 3 ** 2
>>> 4 * 2.0
>>> 'ab' * 3
>>> '5' + '5'
>>> int(3.9)
>>> 'python'[-2]
>>> len('python')
>>> str(4) + 4
[[/PAIRS]]

[[KEY]]
Answers: `3`, `2`, `512`, `8.0`, `'ababab'`, `'55'`, `3`, `'o'`, `6`, `TypeError`.
[[/KEY]]

## Q (6 points)

For each code segment below, identify the error and briefly explain how to fix it (2 points each: 1 for the error, 1 for the fix).

a)

```python
print('It's a wonderful world!')
```

[[BLANK height=30]]

b)

```python
a = 1
b = -5
c = 6
x = 0
y = ax**2 + bx + c
```

[[BLANK height=30]]

c)

```python
x = input("Enter a number")
x = x / 10
print(x)
```

[[BLANK height=30]]

[[KEY]]
a) The `'` in "It's" ends the string early (SyntaxError): use double quotes outside, or `\'`. b) `ax` and `bx` are read as variable names (NameError): write `a*x` and `b*x`. c) `input()` returns a string, so `/` fails (TypeError): use `float(input(...))`.
[[/KEY]]

## Q (4 points)

Consider the code below. What do the three `print` statements output?

```python
a = [4, 8, 15]
a[0] = 16
a.append(23)
b = a[1] + a[2]
a = a + [42]
print(a)
print(b)
print(len(a))
```

[[BLANK height=110]]

[[KEY]]
`[16, 8, 15, 23, 42]`, then `23`, then `5`. Grading: 1 point per line, plus 1 point for all three correct.
[[/KEY]]

## Q (4 points)

Write one Python statement for each task below (1 point each).

Assume `inventory = {'apples': 12, 'pears': 5}`.

a) Add a new entry mapping `'plums'` to `8`.

[[BLANK height=26]]

b) Increase the number of apples by 3, using its current value (don't just write 15).

[[BLANK height=26]]

c) Remove the entry for `'pears'` completely.

[[BLANK height=26]]

d) Print how many entries `inventory` has.

[[BLANK height=26]]

[[KEY]]
a) `inventory['plums'] = 8`  b) `inventory['apples'] = inventory['apples'] + 3`  c) `del inventory['pears']`  d) `print(len(inventory))`
[[/KEY]]

## Q (6 points)

Write a code segment that inputs a number of total seconds from the user (as an integer) and prints how many whole hours, remaining minutes, and remaining seconds that is. Here is an example run:

```
Total seconds: 3725
1 hours, 2 minutes, 5 seconds
```

Note that you should:

- implement the prompt as shown.
- use `//` and `%` as appropriate.
- print the result in the format shown above.

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=170]]

[[KEY]]
```python
total = int(input("Total seconds: "))
hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
```

Grading: input/int conversion 1, hours 1, minutes 2, seconds 1, output format 1.
[[/KEY]]

## Q (5 points)

Write a code segment that builds a username. It inputs the user's first name, last name, and birth year (keep the year as a string), and then prints a username made of:

- the first letter of the first name,
- followed by the whole last name,
- followed by the **last two** digits of the birth year (use indexing),

all in lowercase. Example run:

```
First name: Grace
Last name: Hopper
Birth year: 1906
Username: ghopper06
```

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=190]]

[[KEY]]
```python
first = input("First name: ")
last = input("Last name: ")
year = input("Birth year: ")
username = (first[0] + last + year[-2] + year[-1]).lower()
print("Username:", username)
```

Grading: three inputs 1, `first[0]` 1, last name 1, `year[-2] + year[-1]` (or `year[2] + year[3]`) 1, lowercase 1.
[[/KEY]]
