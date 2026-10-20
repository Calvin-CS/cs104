# Data Types

### CS-104 · Week 3

---

## Exercise 3.b.1

What data type would you use to represent the following?

a. A person's first name
b. The first names of all the students in this course
c. The Quiz 1 scores for each of those students
d. A person's birth date (year, month, and day)
e. An address book entry (name, email, major, ...)
f. A person's age in years
g. A person's height in meters

Write an example assignment statement for each.

### Example Assignment Statements

```python
a = "Alice"
b = ["Alice", "Bob", "Charlie"]
c = [90, 85, 95]
# or: c = {"Alice": 90, "Bob": 85, "Charlie": 95}
d = (2000, 1, 1)
e = {"name": "Alice", "email": "ak12@calvin.edu", "major": "Biology"}
f = 20
g = 1.75
```
<!-- .element: class="fragment" -->

Note:
```
a. str
b. List[str]
c. List[int] or Dict[str, int]
d. Tuple[int, int, int]
e. {'name': str, 'email': str, 'major': str, ...}
f. int
g. float
```

---

Assume `x = 'alphabet'`
How could you get the `b`?

- x(6)
- x[6]
- x[5]
- x(-4)
- x{-3}

---

## Exercise 3.b.2

Generally speaking, one can view strings as lists of characters, but &hellip;

---

## Exercise 3.b.2.a

Can you predict what the code segments do to the value of `x` and explain why they work that way?

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
x = '12'
x[1] = '3'
```

</div>
<div style="flex:1">

```python
x = [1, 2]
x[1] = 3
```

</div>
</div>

---

## Exercise 3.b.2.b

Can you predict what the code segments do to the values of `x` and `y` and explain why they work that way?

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
x = 'hi'
y = x
x.upper()
```

</div>
<div style="flex:1">

```python
x = ['h', 'i']
y = x
x[1] = 'o'
```

</div>
</div>

---

## Exercise 3.b.2.c

How would similar code segments work on integers, floats, dictionaries and tuples?

---

## Name-Object Diagrams

Draw the name-object diagram for the following code:

```python
s = "bht"
s.upper()
print(s)
```

Note that the `upper()` method creates a string with all uppercase letters.

Strings are *immutable*. The `upper()` method returns a *new* string.
<!-- .element: class="fragment" -->

---

## Name-Object Diagrams with Lists

```python
a = [3, 2, 1]
b = a
b[0] = 50
c = b + a
print(c)
```

- [50, 2, 1, 3, 2, 1]
- [50, 2, 1, 50, 2, 1]
- [100, 4, 2]
- [53, 4, 2]
- None of the above

Note:
Answers reflect misconceptions:

1. thinks that `b=a` copies `a`
2. (correct)
3. thinks that `+` operates elementwise, but got correct values
4. thinks that `+` operates elementwise, also thought `b=a` copies `a`

---

## Name-Object Diagrams with Lists, 2

```python
a = [3, 2, 1]
b = a.copy()
b[0] = 50
c = b + a
print(c)
```

- [50, 2, 1, 3, 2, 1]
- [50, 2, 1, 50, 2, 1]
- [100, 4, 2]
- [53, 4, 2]
- None of the above

Note:
Answers reflect misconceptions:

1. thinks that `b=a` copies `a`
2. (correct)
3. thinks that `+` operates elementwise, but got correct values
4. thinks that `+` operates elementwise, also thought `b=a` copies `a`

---

## Which makes most sense to you?

> a. "[Technology is] essentially amoral, a thing apart from values, an instrument which can be used for good or ill." — R. Buchanan, *Technology and Social Progress*, 1965.
>
> b. "Embedded in every tool is an ideological bias, a predisposition to construct the world as one thing rather than another, to value one thing over another, to amplify one sense or skill or attitude more loudly than another." — N. Postman, *Technopoly: The Surrender of Culture to Technology*, 1992.
>
> c. "...automated machine processes not only *know* our behavior but also *shape* our behavior... the goal now is to *automate us*...through the automated medium of an increasingly ubiquitous computational architecture of "smart" devices, things, and spaces." — S. Zuboff, *The Age of Surveillance Capitalism*, 2019, p.8
