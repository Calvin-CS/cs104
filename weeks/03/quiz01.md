# CS-104 Quiz 1
meta: Fall 2026

This is an in-class, closed-book quiz. If you have any questions, please feel free to ask them. When you are finished, you can turn it in and go.

## Q (2 points)

Give the value of each Python expression below. Remember the resulting type (int, float, str...)! If it raises an error instead, name the error (e.g., "IndexError").

[[VERSION A]]
[[PAIRS]]
EX: >>> 'a' + 'b' -> 'ab'
>>> 7 // 2
>>> 2 ** 5
>>> 4 * 2.0
>>> 4 / 2
>>> [1, 2, 3][5]
[[/PAIRS]]
[[/VERSION]]

[[VERSION B]]
[[PAIRS]]
EX: >>> 'x' + 'y' -> 'xy'
>>> 15 // 4
>>> 3 ** 4
>>> 4 * 2.0
>>> 4 / 2
>>> [10, 20, 30][5]
[[/PAIRS]]
[[/VERSION]]

## Q (3 points)

For each code segment below, identify the error and briefly explain how to fix it.

[[VERSION A]]
a)

```python
print('It's a wonderful world!')
```

[[BLANK height=24]]

b)

```python
turtle.penup
turtle.forward(100)
turtle.pendown
```

[[BLANK height=24]]

c)

```python
a = 1
b = -5
c = 6
x = 0
y = ax**2 + bx + c
```

[[BLANK height=24]]

d)

```python
x = input("Enter a number")
x = x / 10
print(x)
```

[[BLANK height=24]]
[[/VERSION]]

[[VERSION B]]
a)

```python
print('I can't stop coding!')
```

[[BLANK height=24]]

b)

```python
turtle.pendown
turtle.forward(75)
turtle.penup
```

[[BLANK height=24]]

c)

```python
a = 2
b = 3
c = -4
x = 1
y = ax**2 + bx + c
```

[[BLANK height=24]]

d)

```python
age = input("Enter your age")
age = age + 1
print(age)
```

[[BLANK height=24]]
[[/VERSION]]

## Q (3 points)

[[VERSION A]]
Write a code segment that inputs a number of total minutes from the user (as an integer) and prints how many whole hours and remaining minutes that is. Here is an example run:

```
Total minutes: 130
Hours: 2, remaining minutes: 10
```

Note that you should:
- implement the prompt as shown (`Total minutes: `).
- use `//` and `%` as appropriate to compute the hours and remaining minutes.
- print the result in the format shown above.
[[/VERSION]]

[[VERSION B]]
Write a code segment that inputs a number of total seconds from the user (as an integer) and prints how many whole minutes and remaining seconds that is. Here is an example run:

```
Total seconds: 130
Minutes: 2, remaining seconds: 10
```

Note that you should:
- implement the prompt as shown (`Total seconds: `).
- use `//` and `%` as appropriate to compute the minutes and remaining seconds.
- print the result in the format shown above.
[[/VERSION]]

Just write a code segment; you don't need to include documentation, an algorithm, or test cases.

[[BLANK height=120]]

## Q (1 point)

[[VERSION A]]
a) Write a statement that creates a list called `colors` containing the strings `'red'`, `'green'`, and `'blue'`.

[[BLANK height=24]]

b) Write a statement that changes the **last** element of `colors` to `'purple'`.

[[BLANK height=24]]
[[/VERSION]]

[[VERSION B]]
a) Write a statement that creates a list called `sizes` containing the strings `'small'`, `'medium'`, and `'large'`.

[[BLANK height=24]]

b) Write a statement that changes the **first** element of `sizes` to `'tiny'`.

[[BLANK height=24]]
[[/VERSION]]

## Q (1 point)

[[VERSION A]]
Consider the dictionary defined below.

```python
prices = {'apple': 1.50, 'banana': 0.75}
```

Write a statement that adds a new entry mapping `'pear'` to `2.00` (or explain why this cannot be done).

[[BLANK height=28]]
[[/VERSION]]

[[VERSION B]]
Consider the dictionary defined below.

```python
ages = {'Sam': 21, 'Lee': 19}
```

Write a statement that adds a new entry mapping `'Kim'` to `22`, or explain why this cannot be done.

[[BLANK height=28]]
[[/VERSION]]
