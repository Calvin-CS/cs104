# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: review of Week 3 (aliasing, immutable strings, negative indexing, Exercise 3.b.1 dictionaries). -->

## Q

What does this code print?

```python
a = [3, 2, 1]
b = a
b[0] = 50
print(a)
```

[[CHOICES]]
- `[3, 2, 1]`
- `[50, 2, 1, 3, 2, 1]`
* `[50, 2, 1]`
- It raises an error
[[/CHOICES]]

## Q

What does this code print?

```python
s = "bht"
s.upper()
print(s)
```

[[CHOICES]]
* `bht`
- `BHT`
- `Bht`
- `None`
[[/CHOICES]]

## Q

Given `x = 'alphabet'`, what is `x[-3]`?

[[CHOICES]]
- `'e'`
- `'a'`
- `'h'`
* `'b'`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that creates a dictionary `person` with the keys `"name"`, `"email"`, and `"major"` holding `"Alice"`, `"ak12@calvin.edu"`, and `"Biology"`. Then read a new major from the user, update the dictionary with it, and print a message like `Alice (ak12@calvin.edu) now majors in Chemistry`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
person = {"name": "Alice", "email": "ak12@calvin.edu", "major": "Biology"}
person["major"] = input("New major: ")
print(person["name"], "(" + person["email"] + ")", "now majors in", person["major"])
```
[[/KEY]]
