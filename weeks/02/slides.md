# Operators

### CS-104 · Week 2

---

## Any logistics questions?

---

## POGIL 2

Process-Oriented Guided Inquiry Learning

[Activity 2: Arithmetic Expressions](https://cs.calvin.edu/courses/cs/108/kvlinden/resources/pogil/Act02-Arithmetic_Student.pdf)

Roles:

- a *programmer* (runs the exercises in [Thonny](https://thonny.org/))
- a *recorder* (writes the team's answers to the exercises)
- a *manager/presenter* (keeps the team on track; interacts with class)

---

## Days and weeks

Write an *algorithm* (on paper, in English not Python code) that

- *prompts the user* for a number of days, and
- *prints* the equivalent number of weeks and (remaining) days.

Now, write the Python code.

When finished or stuck, share with your neighbor(s).
<!-- .element: class="fragment" -->

---

## Gather-Compute-Use Pattern

1. **Gather** input
    - `total_days = int(input("days: "))`
2. **Compute** new information
    - `weeks = total_days // 7`, `days = total_days % 7`
3. **Use** the computed information
    - `print(weeks, "weeks and", days, "days")`

---

## Homework Prep

How do you draw a filled shape?

Looking up documentation.

---

## Circle Math

Write an *algorithm* (on paper, in English not Python code) that

- *prompts* the user for the diameter of a circle in *inches*, then
- prints the *circumference* of the circle in *centimeters*, then
- prints the *area* of the circle in square centimeters

Now, write the Python code.

When finished or stuck, share with your neighbor(s).
<!-- .element: class="fragment" -->

---

## Escape Sequences

Escape sequences are used to represent special characters in strings.

- `\'` - single quote
- `\"` - double quote
- `\\` - backslash
- `\n` - newline
- `\t` - tab
- `☃` - [Unicode](https://www.babelstone.co.uk/Unicode/unicode.html) [snowman](https://www.compart.com/en/unicode/U+2603)
- `\U0001F600` - Unicode [grinning face](https://www.compart.com/en/unicode/U+1F600)

---

## Escape Sequence Exercise

Write a single `print` call that gives the following output:

```
Don't say "I can't"
  until you've tried 😀
```

```python
print(
    "Don't say " +
    "\"I can't\"\n" +
    "  until you've tried " +
    "\U0001F600")
```
<!-- .element: class="fragment" -->

- We needed to escape the double quotes with a backslash.
- We needed to include a newline using `\n`.
- We split the string across multiple lines for readability.
- We used the `+` operator to concatenate the strings.
<!-- .element: class="fragment" -->

---

## Exercise

a. What is the output of the following code?

```python
x = 37
y = x + 2
x = 20
x = x + 1
print(x)
print(y)
```

b. What is the output of the following code?

```python
y = 3
x = 7
y = 1 + 2 * 3
print(x)
print(y)
```

Check your thinking on [PythonTutor](https://pythontutor.com/render.html#mode=edit).

---

## Python Basic Data Types

- `int` - integer (whole numbers)
  - in Python: practically unlimited size
- `float` - floating point numbers
  - has fractional part
  - limited size (e.g., 64 bits)
  - used for measurements, scientific calculations
  - *floating* point: some of those bits say *where* the decimal point goes
    - represented as a whole number, scaled by a power of 2
- `str` - strings (sequence of characters)
  - practically unlimited size

---

## Limits of Computers' Numeric Representations

- **Overflow**: result of a calculation is too large to be represented
  - e.g., using 8 bits to represent a number, but the result is 256
  - see [integer.exposed/#0xff](https://integer.exposed/#0xff)
  - Python `ints` grow instead of overflowing
- **Loss of precision**
  - example: `2 ** 53 + 1.0 + 1.0 + 1.0`
  - `float` has 53 bits of precision
  - see [float.exposed/0x6800](https://float.exposed/0x6800)

---

## Bounds

What do these two videos have in common?

- <https://www.youtube.com/watch?v=9bZkp7q19f0>
- <https://www.youtube.com/watch?v=gp_D8r-2hwk>

References:

- [integer.exposed](https://integer.exposed/#0x00000000)
- [Ars article](https://arstechnica.com/information-technology/2014/12/gangnam-style-overflows-int_max-forces-youtube-to-go-64-bit/)

Note:
- Both demonstrate anomalies caused by bounded representation.
  - The Ariane V initiated a self-destruct when encountering an out-of-range value.
    - <https://www.youtube.com/watch?v=PK_yguLapgA> (0:38-2:10)
    - [detailed report](http://www-users.math.umn.edu/~arnold//disasters/ariane5rep.html)
  - The counter for the Gangnam Style video rolled over: [ArsTechnica article](https://arstechnica.com/information-technology/2014/12/gangnam-style-overflows-int_max-forces-youtube-to-go-64-bit/)
    - (2^31 - 1) / 365 / 24 / 60 / 60 = 68.1 (~68 plays per second for a year)
  - cf. [Boeing Generator Control Unit lifetime counter overflow](https://www.theregister.co.uk/2015/05/01/787_software_bug_can_shut_down_planes_generators/)
- Solutions
  - Refactor to using 64-bit integers? Will 2^63-1 (> 9 quintillion) be big enough?
  - Python extends integers infinitely, within the limit of system memory.
- Character representations are similarly limited.
  - ASCII only really works in North America.
  - UNICODE covers most of the world's scripts, but not all - Wycliffe has UNICODE people on staff.
- "We have to recognise that in software we are always approximating reality," - B. Scherlis (see BBC article)
- Reference: <http://www.bbc.com/future/story/20150505-the-numbers-that-lead-to-disaster>

---

## Limitations

> Can you fathom the mysteries of God?
>     Can you probe the limits of the Almighty?
> They are higher than the heavens above—what can you do?
>     They are deeper than the depths below—what can you know?
> Their measure is longer than the earth
>     and wider than the sea.
>
> — Job 11:7-9 (NIV)

**Discuss with neighbors**: What do we lose when we reduce the world to `int`s, `float`s, and `str`ings?

Note:
- We're limited (by design and by sin); God is unlimited
- Cf. God's response in Job 38.
