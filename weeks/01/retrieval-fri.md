# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 1, Friday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: Week 1 slides (objects, variables, input), POGIL Act01 (Thonny, built-in functions, variables and assignment). -->

## Q

Which of these is a valid Python variable name?

[[CHOICES]]
- `3data`
- `my data`
* `my_data`
- `True`
[[/CHOICES]]

## Q

Consider this code:

```python
x = input("Age: ")
print(x + 1)
```

The user types `20`. What happens?

[[CHOICES]]
- It prints `21`
- It prints `201`
* It raises a `TypeError`, because `input()` returns a string
- It raises a `NameError`, because `x` is not defined
[[/CHOICES]]

## Q

Consider this code:

```python
hot = 273 + 100
print(Hot - 100)
```

What happens?

[[CHOICES]]
- It prints `273`
* It raises a `NameError`, because Python is case-sensitive and `Hot` was never assigned
- It prints `373`
- It raises a `SyntaxError`, because variable names can't start with a capital letter
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a program that asks the user for their name and their age in years, and then prints about how many days old they are (age × 365). For example:

```python
Name: Ana
Age: 20
Ana is about 7300 days old
```

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
name = input("Name: ")
age = int(input("Age: "))
print(name, "is about", age * 365, "days old")
```
[[/KEY]]
