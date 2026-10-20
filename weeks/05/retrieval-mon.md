# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 5, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Quiz 2 prep: range (including counting down), for loops with if, while-loop accumulators, sentinel loops, tracking the largest value (POGIL Act05). -->

## Q

Which loop prints `20`, `15`, `10`, `5` (in that order)?

[[CHOICES]]
- `for n in range(20, 5, -5): print(n)`
- `for n in range(5, 20, 5): print(n)`
* `for n in range(20, 0, -5): print(n)`
- `for n in range(20, 0, 5): print(n)`
[[/CHOICES]]

## Q

What does this code print?

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        total = total + i
    else:
        total = total - 1
print(total)
```

[[CHOICES]]
- `15`
* `3`
- `6`
- `-3`
[[/CHOICES]]

## Q

What does this code print?

```python
i = 10
total = 0
while i > 0:
    total = total + i
    i = i - 3
print(total)
```

[[CHOICES]]
- `21`
- `18`
* `22`
- `10`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that keeps asking the user for whole numbers until they enter `0`. Then it prints how many numbers were entered (not counting the 0) and the largest one. It must work even if every number is negative, and you may not use `max` or a list.

[[BLANK height=190]]

[[KEY]]
Sample solution:

```python
count = 0
largest = None
n = int(input("Number: "))
while n != 0:
    count = count + 1
    if largest is None or n > largest:
        largest = n
    n = int(input("Number: "))
print(count, largest)
```
[[/KEY]]
