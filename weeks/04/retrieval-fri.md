# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Friday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: Conditionals (elif order, input() types, Automobile Service Cost lab) plus boolean precedence (not/and/or). -->

## Q

Suppose `x = 4` and `y = 9`. What is the value of `not x == 4 or y < 5`?

[[CHOICES]]
- `True`
* `False`
- `None`
- It raises an error
[[/CHOICES]]

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

[[PAGEBREAK]]

## Q

Assume `prices = {"oil change": 35, "tire rotation": 19, "car wash": 7}`. Write a code segment that reads a service name from the user. If the service is in `prices`, print its cost (e.g. `car wash costs $7`); otherwise print an error such as `error: teleportation is not recognized`, using whatever the user typed.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
service = input("Service: ")
if service in prices:
    print(service, "costs $" + str(prices[service]))
else:
    print("error:", service, "is not recognized")
```
[[/KEY]]
