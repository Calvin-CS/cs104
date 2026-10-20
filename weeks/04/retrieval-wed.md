# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Wednesday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: Conditionals slides, POGIL Act04, Labs 4.11-4.13. -->

## Q

What does this code print?

```python
x = 95
if x >= 90:
    print("You've got an A")
if x >= 80:
    print("You've got a B")
else:
    print("Keep studying!")
```

[[CHOICES]]
- Only `You've got an A`
- Only `You've got a B`
* `You've got an A` and then `You've got a B`
- `You've got an A` and then `Keep studying!`
[[/CHOICES]]

## Q

Which expression is **not** equivalent to `13 <= age < 20`?

[[CHOICES]]
- `13 <= age and age < 20`
- `age >= 13 and age < 20`
- `not (age < 13 or age >= 20)`
* `13 < age <= 20`
[[/CHOICES]]

## Q

What does this code print?

```python
a = 5
result = (a == 3 or 4)
if result:
    print("yes")
else:
    print("no")
```

[[CHOICES]]
* `yes`, because `False or 4` gives `4`, which is truthy
- `no`, because `a` is not 3
- Nothing; it raises a `TypeError`
- Nothing; neither branch runs
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that reads a pH value (a float) from the user and prints `error` if it is outside the range 0 to 14. Otherwise it prints `acid` if the pH is below 7, `base` if it is above 7, and `neutral` if it is exactly 7.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
ph = float(input("pH: "))
if ph < 0 or ph > 14:
    print("error")
elif ph < 7:
    print("acid")
elif ph > 7:
    print("base")
else:
    print("neutral")
```
[[/KEY]]
