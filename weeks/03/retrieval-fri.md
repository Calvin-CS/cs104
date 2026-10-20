# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 3, Friday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Covers: POGIL Act03 (lists, sequences, dictionaries), Labs 3.8-3.11. -->

## Q

Given `primes = [2, 3, 5, 7, 11, 13]`, what is `primes[4]`?

[[CHOICES]]
- `7`
* `11`
- `13`
- It raises an `IndexError`
[[/CHOICES]]

## Q

What happens when this code runs?

```python
s = "one two"
s[1] = "X"
```

[[CHOICES]]
- `s` becomes `"oXe two"`
- `s` becomes `"Xne two"`
- It raises an `IndexError`
* It raises a `TypeError`, because strings are immutable
[[/CHOICES]]

## Q

What happens when this code runs?

```python
elements = {'C': 'carbon', 'H': 'hydrogen', 'O': 'oxygen'}
print(elements['carbon'])
```

[[CHOICES]]
* It raises a `KeyError`, because `'carbon'` is a value, not a key
- It prints `C`
- It prints `carbon`
- It raises a `NameError`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Assume `temps = [12.5, 15.0, 9.5, 18.0]`. Write a code segment that (1) reads one more temperature from the user (as a float) and adds it to the end of `temps`; (2) prints the last temperature in the list using a negative index; and (3) prints how many temperatures there are, along with the lowest and the highest.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
temps.append(float(input("Temperature: ")))
print(temps[-1])
print(len(temps), min(temps), max(temps))
```
[[/KEY]]
