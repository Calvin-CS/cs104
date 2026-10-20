# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 6, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: review of Week 5 Loops (for over strings, accumulators, cycling with %). -->

## Q

What does this code print?

```python
s = "abc"
new_s = ''
for c in s:
    new_s = c + new_s
print(new_s)
```

[[CHOICES]]
- `abc`
* `cba`
- `a`
- `c`
[[/CHOICES]]

## Q

What does this code print?

```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)
```

[[CHOICES]]
- `10`
- `21`
* `15`
- `5`
[[/CHOICES]]

## Q

What does this code print?

```python
colors = ['red', 'black', 'blue']
i = 7
print(colors[i % len(colors)])
```

[[CHOICES]]
- `red`
- `blue`
- It raises an `IndexError`
* `black`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that reads a string from the user and uses a `for` loop to count how many times the letter `a` appears in it, in either lowercase or uppercase. Print the count. For example, `Banana Bread` gives `4`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
s = input("Text: ")
count = 0
for c in s:
    if c == 'a' or c == 'A':
        count = count + 1
print(count)
```
[[/KEY]]
