# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 5, Monday

<!-- Covers: Week 5 Loops slides, taught on Week 4 Friday (for over strings, accumulators, cycling with %), plus Forum 2 (On Coding with Wisdom and Justice). -->

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

## Q

Which statement best captures the main argument of *On Coding with Wisdom and Justice* (Forum 2)?

[[CHOICES]]
- Algorithms are less fair than people, so decisions like welfare eligibility should never be automated.
- Code is neutral; any injustice comes from the people who use a program, not from the rules programmers write.
* Writing code means making judgments: rules leave out context that wisdom needs, so programmers must ask what their conditions assume.
- Failures like Indiana's come from bugs, so testing every branch carefully is enough to make an algorithm just.
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
