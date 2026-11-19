# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 4, Wednesday

<!-- Covers: Labs 4.11-4.13 (Automobile Service Cost, Wind Chill, Zeller's Congruence). -->

## Q

In the Automobile Service Cost lab, a student wrote the code below. What does it print when the user enters `oil change`?

```python
service = input("service: ")
if service == "oil change":
    print("cost of oil change: $35")
if service == "tire rotation":
    print("cost of tire rotation: $19")
if service == "car wash":
    print("cost of car wash: $7")
else:
    print("error:", service, "is not recognized")
```

[[CHOICES]]
- Only `cost of oil change: $35`
* `cost of oil change: $35` and then `error: oil change is not recognized`
- Only `error: oil change is not recognized`
- Nothing, because only the last `if` has an `else`
[[/CHOICES]]

## Q

In the Wind Chill lab, the formula only works when the wind speed `v` is at least 2 mph **and** the temperature `ta` is between -58 and 41 degrees. Which condition is `True` exactly when the input is **invalid**?

[[CHOICES]]
- `v < 2 and (ta < -58 or ta > 41)`
- `v >= 2 and -58 <= ta <= 41`
* `v < 2 or ta < -58 or ta > 41`
- `v < 2 and ta < -58 and ta > 41`
[[/CHOICES]]

## Q

In the Zeller's Congruence lab, January and February must become months 13 and 14 of the previous year. A student wrote the code below. What are `month` and `year` after the user enters `2026` and then `5`?

```python
year = int(input("Enter year: "))
month = int(input("Enter month: "))
if month == 1 or 2:
    month = month + 12
    year = year - 1
```

[[CHOICES]]
- `5` and `2026`, because 5 is neither 1 nor 2
* `17` and `2025`, because `month == 1 or 2` gives `2`, which is truthy
- `17` and `2026`, because only the first line of the block runs
- Nothing; it raises a `SyntaxError`
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Assume `wc_temp` already holds the wind-chill temperature (a float). Write a code segment that prints how many layers to wear, using the Wind Chill lab's cutoffs:

- below -40: `Stay home!`
- from -40 up to (not including) -10: `Four layers`
- from -10 up to (not including) 20: `Three layers`
- from 20 up to (not including) 40: `Two layers`
- 40 or above: `One layer`

[[BLANK height=170]]

[[KEY]]
Sample solution:

```python
if wc_temp < -40:
    print("Stay home!")
elif wc_temp < -10:
    print("Four layers")
elif wc_temp < 20:
    print("Three layers")
elif wc_temp < 40:
    print("Two layers")
else:
    print("One layer")
```
[[/KEY]]
