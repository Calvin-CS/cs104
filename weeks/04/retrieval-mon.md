# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Monday

<!-- Covers: POGIL Act04 (Conditions and Logic): comparison operators and = vs ==, if/else and indented blocks, not/and/or precedence. -->

## Q

What does this code print?

```python
three = 3
four = 4
check = three > four
three = four
print(check, three == four)
```

[[CHOICES]]
* `False True`
- `True True`
- `False False`
- `False 4`
[[/CHOICES]]

## Q

What does this code print?

```python
number = 6
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
    print("Until next time...")
```

[[CHOICES]]
* Only `6 is even`
- `6 is even` and then `Until next time...`
- `6 is odd` and then `Until next time...`
- It raises a `SyntaxError`, because an `else` block can only hold one line
[[/CHOICES]]

## Q

Suppose `p`, `q`, and `r` are Boolean variables. Which version, with parentheses added, shows how Python evaluates `not p or q and r`?

[[CHOICES]]
- `not (p or (q and r))`
* `(not p) or (q and r)`
- `((not p) or q) and r`
- `not ((p or q) and r)`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that reads two integers `x` and `y` from the user. If both are positive, print their sum. Otherwise, print `at least one is not positive`. Finally, no matter which case happened, print `Until next time...`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
x = int(input("x: "))
y = int(input("y: "))
if x > 0 and y > 0:
    print(x + y)
else:
    print("at least one is not positive")
print("Until next time...")
```
[[/KEY]]
