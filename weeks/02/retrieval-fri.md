# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 2, Friday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: cumulative Weeks 1-2 (variable reassignment, precedence, escape sequences, // and %). -->

## Q

What does this code print?

```python
x = 37
y = x + 2
x = 20
x = x + 1
print(x, y)
```

[[CHOICES]]
- `21 22`
- `38 39`
* `21 39`
- `20 39`
[[/CHOICES]]

## Q

What is the value of `2 ** 1 ** 3`? (Remember: `**` is evaluated from right to left.)

[[CHOICES]]
- `8`
- `6`
- `1`
* `2`
[[/CHOICES]]

## Q

Which statement prints exactly: `She said "hi"`

[[CHOICES]]
- `print("She said "hi"")`
* `print("She said \"hi\"")`
- `print("She said /"hi/"")`
- `print("She said ""hi""")`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that reads a whole number of minutes from the user and prints it as hours and minutes. For example, for `135` it prints `2 hours and 15 minutes`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
total = int(input("Minutes: "))
hours = total // 60
minutes = total % 60
print(hours, "hours and", minutes, "minutes")
```
[[/KEY]]
