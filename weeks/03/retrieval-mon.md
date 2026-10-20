# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 3, Monday

Closed book, no devices. For questions 1–3, circle the one best answer. For question 4, write your code in the space provided (no algorithm, documentation, or test cases needed).

<!-- Quiz 1 prep: strings (repetition, indexing, upper/lower), int() conversion, lists, and dictionaries from POGIL Act03. -->

## Q

What does `print('ab' * 3, int(3.9))` display?

[[CHOICES]]
- `ab3 4`
* `ababab 3`
- `ababab 4`
- It raises a `TypeError`
[[/CHOICES]]

## Q

What does this code print?

```python
nums = [5, 1, 4]
nums[1] = 9
nums.append(2)
print(nums[1], nums[-1], len(nums))
```

[[CHOICES]]
- `1 2 4`
- `9 4 3`
- `5 2 4`
* `9 2 4`
[[/CHOICES]]

## Q

What does this code print?

```python
grades = {'Ana': 88, 'Bo': 75}
grades['Cy'] = 90
del grades['Bo']
print(grades)
```

[[CHOICES]]
* `{'Ana': 88, 'Cy': 90}`
- `{'Ana': 88, 'Bo': 75, 'Cy': 90}`
- `{'Ana': 88, 'Bo': 90}`
- It raises a `KeyError`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Write a code segment that inputs a product name and a year (keep the year as a string), and prints a code made of the first letter of the name in uppercase, followed by the **last two** digits of the year (use indexing). For example, `laptop` and `2026` give `L26`.

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
name = input("Product: ")
year = input("Year: ")
print(name[0].upper() + year[-2] + year[-1])
```
[[/KEY]]
