# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Friday

<!-- Covers: the week on conditionals (elif order, equivalent conditions, input() types, pH exercise) plus POGIL Act05 Model 3 (while loops: order of statements in the body). Forum 2 is in this class, so its question moved to Week 5 Monday. -->

## Q

What does this code print?

```python
x = 95
if x >= 60:
    print("You've got a D")
elif x >= 70:
    print("You've got a C")
elif x >= 80:
    print("You've got a B")
elif x >= 90:
    print("You've got an A")
else:
    print("Keep studying!")
```

[[CHOICES]]
* `You've got a D`
- `You've got an A`
- All four grade messages
- `Keep studying!`
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

What happens when the user enters `3`?

```python
ph = input("pH: ")
if ph < 7.0:
    print("acid")
```

[[CHOICES]]
- It prints `acid`
- It prints nothing
- It raises a `ValueError`
* It raises a `TypeError`, because a string can't be compared with a float
[[/CHOICES]]

## Q

What does this code print?

```python
i = 0
while i < 3:
    i = i + 1
    print(i)
```

[[CHOICES]]
- `0`, `1`, `2`
* `1`, `2`, `3`
- `0`, `1`, `2`, `3`
- Nothing; it loops forever
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
