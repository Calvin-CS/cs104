# Conditionals

### CS-104 · Week 4

---

## Boolean

- Built-in type
- Only 2 possible values:
  - `True`
  - `False`

---

## Boolean Operators (evaluate to `bool`)

- Comparison: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Logical: `and`, `or`, `not`
- Membership: `in`, `not in`
- Identity: `is`, `is not`

---

## What is the output of the following code?

```python
a = 3
b = (a != 3)
print(b)
```

- `True`
- `False`
- `3`
- Syntax error

---

## Logical Operators

Combine two boolean expressions:

- `p and q` ("both `p` and `q`")
  - `True` only if *both* are true, otherwise `False`
- `p or q` ("`p` or `q` or both")
  - `True` if at least one is true.
- `not p` ("opposite of `p`")
  - `True` if `p` is `False`
  - `False` if `p` is `True`

[Order of operations](https://docs.python.org/3/reference/expressions.html#operator-precedence): `not`, then `and`, then `or`

---

Which expression evaluates to `True` exactly when *at least one* of the following is true:

- `a` and `b` are equal
- `a` has a value of 5

- `a == b == 5`
- `a == b or a == 5`
- `a == b and a == 5`
- `a == (b == 5)`

---

Suppose we run

```python
a = True
b = False
c = True
```

What is the value of this expression:

`not a and b or c`

- `True`
- `False`

---

## Teenager

Write a boolean expression that evaluates to `True` if `age` indicates a teenager.

We'll call someone a teenager if we say "teen" when we say their age (and they're not over 100).

(Assume `age` has been previously defined.)

`13 <= age and age < 20`
<!-- .element: class="fragment" -->

`13 <= age < 20`
<!-- .element: class="fragment" -->

`13 <= age and 20 > age`
<!-- .element: class="fragment" -->

---

## Leap Year

Write a single expression that determines whether or not a previously defined `year` is a leap year.

A leap year is:

- Divisible by 4 and not divisible by 100
- *or*
- Divisible by 400

*hint*: `year % 4 == 0`

---

## When your `bool` isn't a `bool`

What does this do?

```python
result = (a == 3 or 4) # 3 and 4 are both valid
```

```python
>>> False or "something"
'something'
```
<!-- .element: class="fragment" -->

- When `a` is 3: `True or 4` -> `True`.
- otherwise: `False or 4` -> `4`.
<!-- .element: class="fragment" -->

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
>>> bool(4)
True
```

</div>
<div style="flex:1">

- "4 is truth-y"
- So `bool(result)` is always `True`

</div>
</div>
<!-- .element: class="fragment" -->

---

# `if`

---

## Syntax

```python
if condition:
    # code to run if condition is True
elif condition2:
    # code to run if condition2 is True and condition is False
else:
    # code to run if all conditions above are False
```

- `condition` is a boolean expression.
- `elif` and `else` are optional.
- Unlimited `elif` blocks allowed, but at most one `else`.

---

## `if` examples

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
x = 5
if x > 2:
      x = -3
      x = 1
else:
      x = 3
      x = 2
```

</div>
<div style="flex:1">

What is the value of `x` after this code runs?

- -3
- 1
- 2
- 3
- 5

</div>
</div>

---

## What does this do?

```python
x = int(input("Enter your score: "))
if x >= 90:
    print("You've got an A")
if x >= 80:
    print("You've got a B")
else:
    print("Keep studying!")
```

---

## Fixed?

```python
if x >= 90:
    print("You've got an A")
if not (x >= 90) and x >= 80:
    print("You've got a B")
else:
    print("Keep studying!")
```

```python
if x >= 90:
    print("You've got an A")
elif x >= 80:
    print("You've got a B")
else:
    print("Keep studying!")
```
<!-- .element: class="fragment" -->

---

```python
x = int(input("Enter your score:"))
if x >= 60:
    print("You've got a D")
elif x >= 70:
    print("You've got a C")
elif x >= 80:
    print("You've got a B")
elif x >= 90:
    print("You've got an A")
else:
    print("Keep studying!")
```

---

## Examples

Complete the following code to find the max of x, y and z. Do not use the built-in `max` function.

```python
x = int(input("Enter value 1:"))
y = int(input("Enter value 2:"))
z = int(input("Enter value 3:"))
my_max = ...
<your code here>
print('The maximum value is:', my_max)
```

---

## pH

Write a program that

- prompts the user to enter a pH value
- tells the user whether the pH given indicates an acid (value < 7.0), base (value > 7.0) or neutral (value is 7.0) substance.

pH values range from 0 to 14.

Now, update your program so that only valid pH values are considered. Display an error for invalid inputs.
<!-- .element: class="fragment" -->

---

## `== True`

Does it ever make sense to write code like this?

```
if _____ == True:
    # some code here
```

for example:

```
if age < 18 == True:
    print("You are a minor.")
```

No:
<!-- .element: class="fragment" -->

1. It's usually redundant.
2. In some cases it can make the *wrong* thing happen: try `2 == 2 == True`
<!-- .element: class="fragment" -->
