# CS-104 Retrieval Quiz
meta: Fall 2026 · Week 1, Friday

<!-- Covers: Week 1 slides (objects, variables, input), POGIL Act01 (Thonny, built-in functions, variables and assignment); Q4: objects vs. variable names and the int/float/str types. -->

## Q

Which of these is a valid Python variable name?

[[CHOICES]]
- `3data`
- `my data`
* `my_data`
- `True`
[[/CHOICES]]

## Q

Consider this code:

```python
x = input("Age: ")
print(x + 1)
```

The user types `20`. What happens?

[[CHOICES]]
- It prints `21`
- It prints `201`
* It raises a `TypeError`, because `input()` returns a string
- It raises a `NameError`, because `x` is not defined
[[/CHOICES]]

## Q

Consider this code:

```python
hot = 273 + 100
print(Hot - 100)
```

What happens?

[[CHOICES]]
- It prints `273`
* It raises a `NameError`, because Python is case-sensitive and `Hot` was never assigned
- It prints `373`
- It raises a `SyntaxError`, because variable names can't start with a capital letter
[[/CHOICES]]

[[PAGEBREAK]]

## Q

Variable names and objects are different things: an **object** is a piece of data (like `123` or `"hi"`), and a **variable** is a name that refers to an object. For each item below, write whether it is an **object** or a **variable name**. If it is an object, also write its type: `int`, `float`, or `str`.

[[PAIRS]]
EX: 12 -> object, int
"bye"
bye
75
count_2
2.5
"2.5"
total
'x'
-4
"7"
[[/PAIRS]]

[[KEY]]
`"bye"` object, str; `bye` variable name; `75` object, int; `count_2` variable name; `2.5` object, float; `"2.5"` object, str (the quotes make it text); `total` variable name; `'x'` object, str; `-4` object, int; `"7"` object, str.
[[/KEY]]
