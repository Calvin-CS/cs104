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

# Types and their properties

---

## Python's built-in types

| Family | Types |
|---|---|
| Numeric | `int`, `float`, `complex` |
| Boolean | `bool` (`True` / `False`) |
| Sequence | `str`, `list`, `tuple`, `range`, ... |
| Mapping | `dict` |
| Set | `set`, `frozenset` |

What can each type do (and not do)?
Check the [Python docs: Built-in Types](https://docs.python.org/3/library/stdtypes.html).

---

## Containers

Some types are *containers*: they hold a collection of other objects.

- A variable can name a single number...
- ...or a whole collection of numbers, strings, or even other collections

Like a bookshelf: one shelf, many boxes and drawers.

| Containers | Not containers |
|---|---|
| `str`, `list`, `tuple`, `dict`, `set` | `int`, `float`, `bool` |

---

## Subscripting with `[]`

Think of objects as buildings and variables as their addresses.

Some buildings hold many units: 1234 Smith Ave **Apt 101**.
The apartment number is a *subscript*.

```python
condo = ["room 1", "room 2", "room 3"]
print(condo[0])    # room 1
```

Not every building has apartments:

```python
house = 3
house[0]    # TypeError: 'int' object is not subscriptable
```

---

## Sequences: subscripts are indexes

`str`, `list`, `tuple`: subscripts are integers called *indexes*, starting at **0**.

```python
condo = ("room 1", "room 2", "room 3")
print(condo[0])    # room 1
print(condo[2])    # room 3
print(condo[-1])   # room 3   (negative indexes count from the end)
print(condo[4])    # IndexError: tuple index out of range
```

---

## Mappings: subscripts are keys

`dict`: subscripts are *keys*, which can be any immutable object (so no lists).

```python
band = {"vocals": "Jon Anderson", "guitar": "Steve Howe",
        "bass": "Chris Squire", "keyboard": "Rick Wakeman"}
print(band["vocals"])   # Jon Anderson
print(band["guitar"])   # Steve Howe
```

---

## Type properties

- **Container**: holds other objects
- **Subscriptable**: items are reached with `[ ]`
- **Ordered** (sequence): items are reached by integer position
- **Mutable**: contents can change (**immutable**: they can't)
- **Callable**: can be run with `()`, like functions: `print("hi")`
  - try `type(print)` or `type(math.cos)`

---

## `[]`, `()`, or `{}`?

Predict what each line does.

```python
a = 1
a[0]
a(0)
a{0}
```

```python
a[0]    # TypeError: 'int' object is not subscriptable
a(0)    # TypeError: 'int' object is not callable
a{0}    # SyntaxError: invalid syntax
```
<!-- .element: class="fragment" -->

- `name[...]` gets an item (subscript)
- `name(...)` calls it (function)
- `{ }` never follows a name: it *creates* dicts and sets

<!-- .element: class="fragment" -->

---

Assume `x = 'alphabet'`
How could you get the `b`?

- x(6)
- x[6]
- x[5]
- x(-4)
- x{-3}

Note:
`x[5]`. (`x[-3]` also works, but isn't an option.) `( )` tries to call `x`; `{ }` is a syntax error.

---

# Sequences

`str` · `list` · `tuple`

---

## Object methods

Many objects come with their own functions, called *methods*.

Syntax: `object.method(arguments)`

```python
a = ["you", "shall", "not", "pass"]
print(a.index("not"))   # 2

s = "hello"
print(s.upper())        # HELLO
print(s.count("l"))     # 2
```

Note:
Contrast with plain functions like `len(a)`, which take the object as an argument.

---

## Sequence operations

These work on every sequence: `str`, `list`, and `tuple`.

| Operation | Result |
|---|---|
| `x in s`, `x not in s` | is `x` an item of `s`? (`True` / `False`) |
| `s + t` | `s` and `t` joined together |
| `s * n` | `s` repeated `n` times |
| `s[i]` | the item at index `i` (from 0) |
| `s[i:j]` | slice from `i` up to (not including) `j` |
| `s[i:j:k]` | slice from `i` to `j`, taking every `k`th item |
| `len(s)` | number of items |
| `min(s)`, `max(s)` | smallest / largest item |
| `s.index(x)` | index of the first `x` in `s` |
| `s.count(x)` | how many times `x` appears in `s` |

<!-- .element: style="font-size: 0.55em" -->

---

## Unpacking sequences

Any sequence can be *unpacked* into several variables at once.

```python
s = ["I", "am", "your", "father"]
a, b, c, d = s
print(a, b)             # I am

ch1, ch2, ch3 = "hi!"
print(ch1, ch2, ch3)    # h i !
```

The number of variables must match the number of items:

```python
a = [1, 2, 3]
v1, v2, v3, v4 = a
# ValueError: not enough values to unpack (expected 4, got 3)
```

---

## Quick check: sequences

Predict the output, then check in Thonny.

```python
s = [3, 1, 4, 1, 5]
print(1 in s, s.count(1), s.index(4))
print(s[1:3], len(s), max(s))

w = "banana"
print(w[1:4], w[::2], w * 2)
```

```plaintext
True 2 2
[1, 4] 5 5
ana bnn bananabanana
```
<!-- .element: class="fragment" -->

---

# Mutable or immutable?

Can the object change after it's created?

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

Note:
- Left: `TypeError: 'str' object does not support item assignment`. Strings are immutable.
- Right: `x` becomes `[1, 3]`. Lists are mutable.

---

## Strings

Strings are *immutable* sequences that hold *only characters*.

```python
a = "Hello World"
print(a[1])      # e
print(a[4:9])    # o Wor

a[0] = "J"
# TypeError: 'str' object does not support item assignment
```

To "change" a string, build a new one:

```python
a = "J" + a[1:]
print(a)         # Jello World
```

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

Note:
- Left: `x` and `y` are both still `'hi'`. `upper()` returned a new string `'HI'` that was never saved.
- Right: `x` and `y` are both `['h', 'o']`. They name the *same* list.

---

## Methods on immutables return new objects

A string can't change, so string methods *return a new string*.

```python
a = "Hello"
b = a.upper()
print(a, b)      # Hello HELLO
print(id(a))     # 140402468101104
print(id(b))     # 140402467911024   (a different object!)
```

`id()` gives each object's unique identity number. (Your numbers will differ.)

To keep the result, assign it: `a = a.upper()`

---

## Lists

Lists are *mutable* sequences, written with `[ ]`.

```python
x = []                              # an empty list
x = [1, 3.33333, "hello", True, 4]  # items can be any type
```

Lists can hold lists (and tuples can hold tuples). A 3×3 matrix:

```python
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mat[0][1])    # row 0, column 1: 2
```

**Quick check**: what are `mat[2][0]`, `mat[1]`, and `len(mat)`?

`7`, `[4, 5, 6]`, and `3`
<!-- .element: class="fragment" -->

---

## Changing vs. copying

With mutable objects, always ask: does this *change* the object, or make a *copy*?

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
a = [1, 2, 3]
b = a
a[1] = 5
print(b)  # [1, 5, 3]
print(id(a) == id(b))  # True
```

**One** list, two names.

</div>
<div style="flex:1">

```python
a = [1, 2, 3]
b = a.copy()
a[1] = 5
print(b)  # [1, 2, 3]
print(id(a) == id(b))  # False
```

**Two** separate lists.

</div>
</div>

Lists and dictionaries are mutable: copy them when you need an independent version.
Immutable objects never need copying.
<!-- .element: class="fragment" -->

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

1. (correct)
2. thinks that `a.copy()` still shares the same list
3. thinks that `+` operates elementwise, and that `a` and `b` still share the same list
4. thinks that `+` operates elementwise, but got the copy right

---

## Tuples

Tuples are *immutable* sequences: values separated by commas, usually in `( )`.

```python
fruits = "banana", "apple", "orange"
fruits = ("banana", "apple", "orange")    # same thing
print(fruits[1])    # apple
```

**Why use something that can't change?**
<!-- .element: class="fragment" -->

- uses less memory and less processing
- never needs copying: sharing it with another variable is always safe

<!-- .element: class="fragment" -->

---

## What if I *really* want to change a tuple?

```python
fruits = ("banana", "apple", "orange")
fruits[1] = "pineapple"
# TypeError: 'tuple' object does not support item assignment
```

```python
# Option 1: build a new tuple
fruits = (fruits[0], "pineapple", fruits[2])

# Option 2: convert to a list, change it, convert back
temp = list(fruits)
temp[1] = "pineapple"
fruits = tuple(temp)
```

Option 2 builds a new list *and* a new tuple: costly with big data.

---

## Quick check: tuples

```python
birthday = (2005, 3, 14)
```

1. Unpack `birthday` into `year`, `month`, and `day`.
2. Oops: the birthday is really the 15th. "Change" `birthday`.

```python
year, month, day = birthday
birthday = (year, month, 15)
```
<!-- .element: class="fragment" -->

---

# Dictionaries

keys → values

---

## Dictionaries

A *mapping* type: each *key* maps to a *value*. A key-value pair is an *entry*.

```python
phones = {'Sarah': '476-3321', 'Nathan': '351-7743'}
users = {'Name': 'Molly', 'Age': 18}
emp = {}    # an empty dictionary

print(phones['Sarah'])    # 476-3321
```

- Look items up by **key**, not by position
- Keys must be **immutable** (`str`, `int`, `tuple`, ...)
- Not a sequence: `phones[0]` looks for the *key* `0` (`KeyError`)

Note:
Since Python 3.7, dicts remember the order entries were added, but you still can't reach an entry by position.

---

## Adding, changing, and deleting entries

```python
phones = {'Sarah': '476-3321', 'Nathan': '351-7743'}

phones['Bob'] = '123-4567'      # add: assign to a new key
phones['Sarah'] = '999-9999'    # change: assign to an existing key
del phones['Nathan']            # delete

print(phones)
# {'Sarah': '999-9999', 'Bob': '123-4567'}
```

Adding and changing use the same syntax. Which one happens depends on whether the key already exists.

---

## Quick check: dictionaries

Predict the output.

```python
stock = {'apples': 5, 'pears': 2}
stock['kiwis'] = 7
stock['apples'] = stock['apples'] - 1
del stock['pears']
print(stock)
print(stock['kiwis'], len(stock))
```

```plaintext
{'apples': 4, 'kiwis': 7}
7 2
```
<!-- .element: class="fragment" -->

---

## Quick check: dictionary errors

Continuing from the previous slide, what does each line do?

```python
print(stock['pears'])
d = {[1, 2]: 'pair'}
```

- `KeyError: 'pears'`, because that entry was deleted
- `TypeError: unhashable type: 'list'`, because keys must be immutable (use `(1, 2)` instead)

<!-- .element: class="fragment" -->

---

## Exercise 3.b.2.c

How would similar code segments work on integers, floats, dictionaries and tuples?

Note:
- `int` / `float`: immutable, and not subscriptable at all. `x = x + 1` makes a new object and moves the name `x` to it; `y` keeps the old value.
- tuples: like strings (`TypeError` on item assignment).
- dicts: like lists (`y = x` shares the same dict, so changes show through both names).

---

## Summarizing properties

| Type | Container | Subscriptable | Ordered (sequence) | Mutable |
|---|---|---|---|---|
| numbers, booleans | No | No | No | No |
| lists | Yes | Yes (integers) | Yes | Yes |
| tuples | Yes | Yes (integers) | Yes | No |
| strings | Yes (only characters) | Yes (integers) | Yes | No |
| dictionaries | Yes | Yes (immutable keys) | No | Yes |
| sets | Yes (only immutable objects) | No | No | Yes |

<!-- .element: style="font-size: 0.6em" -->

Look back at Exercise 3.b.1: would you change any of your choices?

---

## Which makes most sense to you?

> a. "[Technology is] essentially amoral, a thing apart from values, an instrument which can be used for good or ill." — R. Buchanan, *Technology and Social Progress*, 1965.
>
> b. "Embedded in every tool is an ideological bias, a predisposition to construct the world as one thing rather than another, to value one thing over another, to amplify one sense or skill or attitude more loudly than another." — N. Postman, *Technopoly: The Surrender of Culture to Technology*, 1992.
>
> c. "...automated machine processes not only *know* our behavior but also *shape* our behavior... the goal now is to *automate us*...through the automated medium of an increasingly ubiquitous computational architecture of "smart" devices, things, and spaces." — S. Zuboff, *The Age of Surveillance Capitalism*, 2019, p.8
