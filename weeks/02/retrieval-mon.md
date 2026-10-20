# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 2, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: review of Week 1 Friday slides (objects vs. variables, print, input, int/float conversion; Exercises 1.c.2 and 1.c.3). -->

## Q

What does this code print?

```python
x = 3
y = x
x = 8
print(x, y)
```

[[CHOICES]]
- `8 8`
* `8 3`
- `3 3`
- `3 8`
[[/CHOICES]]

## Q

What does this code print?

```python
city = "Paris"
city = "Rome"
print("city")
```

[[CHOICES]]
- `Rome`
- `Paris`
* `city`
- `"Rome"`
[[/CHOICES]]

## Q

The user types `3` and then `4`. What does this code print?

```python
a = input("First: ")
b = input("Second: ")
print(a + b)
```

[[CHOICES]]
- `7`
- `3 4`
- It raises a `TypeError`
* `34`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a program that asks the user for two numbers (which may have decimals), then prints their sum and their average. For example, for `3` and `4` it prints `Sum: 7.0` and `Average: 3.5`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
x = float(input("First number: "))
y = float(input("Second number: "))
print("Sum:", x + y)
print("Average:", (x + y) / 2)
```
[[/KEY]]
