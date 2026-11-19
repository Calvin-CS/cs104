# Introduction

### CS-104 · Week 1

---

# Monday

---

## We're in this together

> Do nothing out of selfish ambition or vain conceit. Rather, in humility value others above yourselves, not looking to your own interests but each of you to the interests of the others.

Philippians 2:3-4

Serving each other by helping each other learn
<!-- .element: class="fragment" -->

---

# Let's read the syllabus!

---

# Failure Tips

Great ways to **fail** this class:
- Skim over the readings
- Skip classes
- Do the lab/homework exercises with AI
  - Quizzes are supposed to be easy if you actually do the exercises yourself!
- Do not seek help

---

# Program

---

## Program

- Programming = writing programs. What are programs?

<div class="columns" style="display:flex; gap:1.5rem; align-items:center;">
<div style="flex:7; text-align:center">

![program flow example](images/program.png)

</div>
<div style="flex:3; text-align:center">

![program](images/original-4779988-3.jpg)

</div>
</div>

---

![lego bricks](images/lego.jpg)

---

## Programs are forms of wisdom

<div class="columns" style="display:flex; gap:1.5rem; align-items:center; justify-content:center;">
<div style="flex:1; text-align:center">

![complete metamorphosis](images/complete-metamorphosis.gif)

</div>
<div style="flex:1; text-align:center">

![DNA reaction](images/dnareaction.png)

</div>
</div>

---

## Programs are forms of wisdom

> 22 "The Lord brought me forth as the first of his works, before his deeds of old; 23 I was formed long ages ago, at the very beginning, when the world came to be. 24 When there were no watery depths, I was given birth, when there were no springs overflowing with water; 25 before the mountains were settled in place, before the hills, I was given birth, 26 before he made the world or its fields or any of the dust of the earth. 27 I was there when he set the heavens in place, when he marked out the horizon on the face of the deep, 28 when he established the clouds above and fixed securely the fountains of the deep, 29 when he gave the sea its boundary so the waters would not overstep his command, and when he marked out the foundations of the earth. 30 Then I was constantly at his side. I was filled with delight day after day, rejoicing always in his presence, 31 rejoicing in his whole world and delighting in mankind.

---

## Drawing as a program

![turtle animation](images/Turtle-animation.gif)

---

# Computation

---

## Computation

- We use programs to **compute** numbers.

<div class="columns" style="display:flex; gap:1.5rem;">
<div style="flex:1; text-align:center">

![abacus](images/fred-flintstone-abacus.gif)

</div>
<div style="flex:1; text-align:center">

![multiplication](images/Poser-une-multiplication.gif)

</div>
<div style="flex:1; text-align:center">

![calculator](images/calculator.gif)

</div>
</div>

---

## Automatic computation

- Charles Babbage is known for developing the first automatic computer machine (1820s)
  - "the faster and more reliably one could calculate, the more money businesses could make."

<div class="columns" style="display:flex; gap:1.5rem; align-items:center;">
<div style="flex:7; text-align:center">

![Babbage's Analytical Engine](images/Babbage-Analytical-Engine.jpg)

</div>
<div style="flex:3; text-align:center">

![Charles Babbage](images/Charles_Babbage_-_1860.jpg)

</div>
</div>

---

## Ada Lovelace's program

- Ada Lovelace, daughter of Lord Byron, became enamoured by Babbage's machine and developed the first **algorithm**, to calculate a sum of numbers:

<div class="columns" style="display:flex; gap:1.5rem; align-items:center;">
<div style="flex:7; text-align:center">

![Ada Lovelace's algorithm](images/adaalgorithm.png)

</div>
<div style="flex:3; text-align:center">

![Ada Lovelace](images/lovelace.jpg)

</div>
</div>

---

## Algorithm

- Basically, a program: a description of a series of operations.
- But with some specific features:
  1. Precise and unambiguous steps
  2. Definite results
  3. Finite
  4. Generalizable (works with a range of possible inputs)
  5. Usually expressed through abstract/mathematical notation

---

## STEM today is programming computations

- For complex calculations, we don't rely anymore on pressing calculator buttons. We have to program!

[![animation example](images/animation_example_1.gif)](https://blogs.mathworks.com/pick/2021/03/26/animation-playback-controls-in-live-scripts-r2021a/)

---

# Code

---

## Code

- Initially, computer operators had to set the program manually to run...

![ENIAC](images/eniac.png)

---

## The punched card

- At the end of the 1800s, Herman Hollerith invented the punched card, to be automatically read by a machine.
- Instructions were then **CODED** in the punched card.

<div class="columns" style="display:flex; gap:1.5rem; align-items:center;">
<div style="flex:6; text-align:center">

![Hollerith punched card machine](images/hollerith.png)

</div>
<div style="flex:4; text-align:center">

![player piano roll](images/piano002.gif)

</div>
</div>

---

## Grace Hopper's proposal

- Later, in 1949, Grace Hopper invented the first programming language: COBOL (COmmon Business-Oriented Language)
  - For example, the user would write:

    `COMPUTE SUM = (1 + 3)`

    `DIVIDE SUM BY 2 GIVING AVERAGE`
- Crucial to this was the development of the **compiler**: a program capable of converting a sentence very much like an English phrase (with syntax and semantics) into machine instructions.

---

## So, what's a code?

- "A program that follows a set of rules" (in order to be correctly interpreted)
- To learn how to program, then, is to learn **how to express yourself correctly through the code**
  - Notice the origin of the word - [codex](https://www.britannica.com/topic/codex-manuscript)

![code](images/code.png)

---

## Python programming language

- Invented in the early 1990s by Guido van Rossum, named after Monty Python's Flying Circus
- Open source project
- High-level, general-purpose language
- Widely available, easy to learn, rich in tools and libraries, and portable

![python logo](images/python.png)

---

![top programming languages 2022](images/ieelanguages.png)

*[Source: IEEE Spectrum, Top Programming Languages 2022](https://spectrum.ieee.org/top-programming-languages-2022)*

---

![python meme](images/pythonmeme.png)

---

## Integrated Development Environment (IDE)

- In our classes, we will be using [Thonny](https://thonny.org/)
  - Notice the panels for scripting and for interactive shell
  - There is also a helper and variable explorer for debugging code

---

![Thonny IDE overview](images/thonnyOverview.png)

---

## Exercise 1.a.1

Form teams of two. The 1st student, the *explainer*, explains how to draw an image. The explainer:

- knows what the image is supposed to be.
- may not use their hands.
- may only specify actions the drawer knows how to perform.

The 2nd student, the *drawer*, draws the image as specified. The drawer:

- doesn't know what the image is supposed to be.
- can follow directions like:
  - **go forward** 10 units
  - **turn right** 90 degrees
  - **pick your pen up** and **put your pen down**
- can't remember anything.

Sample images to draw:

<div class="columns" style="display:flex; gap:1.5rem; align-items:flex-end;">
<div style="flex:1; text-align:center">

![2](images/2.png)

2

</div>
<div style="flex:1; text-align:center">

![5](images/5.png)

5

</div>
<div style="flex:1; text-align:center">

![face](images/face.png)

face *(optional, more complex)*

</div>
<div style="flex:1; text-align:center">

![tic-tac-toe](images/tictactoe.png)

tic-tac-toe *(optional, more complex)*

</div>
</div>

Note:
Example images (from the explainer/drawer exercise):

- [2](https://cs.calvin.edu/courses/cs/106/cur/01introduction/images/2.png)
- [5](https://cs.calvin.edu/courses/cs/106/cur/01introduction/images/5.png)
- face and tic-tac-toe are optional, more complicated alternates.

---

## Additional Reference Images

*Pulled in from related Week 1 lab/homework materials for this unit — shown here for reference, not part of the original slide content.*

<div class="columns" style="display:flex; gap:1.5rem; flex-wrap:wrap;">
<div style="flex:1; min-width:120px; text-align:center">

![five-pointed star](images/star.png)

Turtle Star (Lab 1.2)

</div>
<div style="flex:1; min-width:120px; text-align:center">

![example initials](images/initials.png)

Homework: initials

</div>
<div style="flex:1; min-width:120px; text-align:center">

![turtle CS example](images/turtleCS.png)

Older lab example

</div>
<div style="flex:1; min-width:120px; text-align:center">

![olympics rings example](images/olympics.png)

Older homework example

</div>
<div style="flex:1; min-width:120px; text-align:center">

![abstraction example](images/abstraction.png)

Older homework example

</div>
<div style="flex:1; min-width:120px; text-align:center">

![zyLabs IO test](images/zylabs_io_test.png)

zyLabs I/O test screenshot

</div>
</div>

---

## Exercise 1.a.2

Explain what the following *algorithm* does.

> 1. **Given:** two positive natural numbers *a* & *b*
> 2. **Set** *remainder* = some non-zero value
> 3. **Repeat** these steps **until** *remainder* = 0
>     1. **Set** *remainder* = the remainder of *a* divided by *b*
>     2. **If** *remainder* = 0 **Then**
>         1. **Print** GCD is *b*
>     3. **Else**
>         1. **Set** *a* = *b* and *b* = *remainder*
>     4. **Go on to** the next repetition
> 4. **Test Cases:** GCD(36,16)→4; GCD(1,1)→1; GCD(1260,198)→18

---

# Wednesday class

---

## Lab Recap

- On your own, write the solution to the "square area" problem without looking at what you did in lab.
- Compare your solution with people around you. Try to find someone who took a different approach!
- Discuss with each other
  - What challenges you faced in lab
  - What you're curious about or tried on your own
  - How you felt about the lab, and this class so far

---

## Process-Oriented Guided Inquiry Learning (POGIL)

### [What](https://cspogil.org/What%2Bis%2BPOGIL)

- based on research on how people learn most effectively
- **team activities** to construct understanding of key concepts
- develop process skills: **communication**, **critical thinking**, **problem solving**
- The instructor is not a lecturer, but an active facilitator of student learning

### How

Form teams of three:

- a *programmer* (runs the exercises in [Thonny](https://thonny.org/))
- a *recorder* (writes the team's answers to the exercises)
- a *manager/presenter* (keeps the team on track; interacts with class)

---

## POGIL

Form teams of three:

- a *programmer* (runs the exercises in [Thonny](https://thonny.org/))
- a *recorder* (writes the team's answers to the exercises)
- a *manager/presenter* (keeps the team on track; interacts with class)

*Activities for CS1 in Python*, [Introduction to Python](https://cs.calvin.edu/courses/cs/106/cur/resources/pogil/Act01-IntroPython_Student.pdf):

1. *Model 1*. Getting Started with Thonny
2. *Model 2*. Python Build-In Functions
3. *Model 3*. Variables and Assignment

These exercises are available as [editable PDFs](https://cs.calvin.edu/courses/cs/106/cur/resources/pogil). If editing doesn't work for you, try a different browser or PDF viewer.

---

# Friday class

---

## Objects

- Python syntax specifies some ways to represent different types of data. A data representation in Python is called an "object".

| Type | Object type in Python | Example |
|---|---|---|
| Integer number | `int` | `123` |
| Decimal number (floating point) | `float` | `3.14` |
| Logic value | `bool` | `True`, `False` |
| Text | `string` | `"Hello World!"` |

---

# Variables

---

## Variables

- Variables are names we set to refer to objects.
  - A not-so-good metaphor: variables are containers for objects
  - A better metaphor: objects are houses, variables are addresses of these houses

```python
x = 123  # a variable x that contains the integer value 123
x = x + 1  # x is updated with the value of x + 1, becoming 124...
hello = "Hello World!"  # a variable that contains the string "Hello World!"
is_done = True  # a variable is_done with the logic value True
```

---

## Assigning objects to variables

![assigning objects to variables](images/assignment.jpg)

---

## Objects x variables

- It is **very important** to differentiate!
- Which of the following are variables and which are objects?

```
"hello"

hello

132

var_1

truev

True
```

---

## Variable naming conventions in Python

- They MUST start with a letter or with _ (underline)
- They are case sensitive ('C' is different from 'c')
- They can't contain: `{ ( + - * / \ ; . , ?`
- They can't have names of words already reserved for other purposes in Python:

![Python reserved words](images/reserved.png)

---

What happens if?

```python
True = 123
```

```python
"Hello" = world
```

```python
1stcar = 2000
```

---

## Exercise 1.c.1

With a partner, decide which of these are **valid** variable names. For the invalid ones, say why.

```
my_score      2fast        _temp
class         total-cost   Total
firstName     print        x2
```

Note:
Valid: `my_score`, `_temp`, `Total`, `firstName`, `x2`, `print` (valid but a bad idea — it hides the built-in `print()` function!).
Invalid: `2fast` (starts with a digit), `class` (reserved word), `total-cost` (contains `-`, read as subtraction).

---

## Exercise 1.c.2

Without running it, predict what each program prints. Then check in Thonny.

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
a = 5
b = a
a = 10
print(a, b)
```

</div>
<div style="flex:1">

```python
x = "7"
y = 7
print(x, y)
print(type(x), type(y))
```

</div>
<div style="flex:1">

```python
name = "Ada"
name = "Grace"
print("name")
print(name)
```

</div>
</div>

Note:
1. `10 5` — `b` refers to the object `5`; reassigning `a` doesn't change `b`.
2. `7 7` then `<class 'str'> <class 'int'>` — they print the same but are different types.
3. `name` then `Grace` — quotes make a string object, not a variable.

---

# Input/Output

---

## Input/Output

- Programming is nothing without the design of an **interface**!
  - I have to be able to **input** data in the program, and
  - I have to be able to get results (**output**) from the program.

![vending machine](images/vending-machine.gif)

---

## Graphical user interface (GUI)

- Kind of mimics the way we use mechanical input and output
- Traditionally, [WIMP](https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/wimp) (Windows, Icons, Menus and Pointers)

![graphical user interface example](images/ui.jpg)

---

## Text input/output

- Even simpler, however, it is a good start for programming!

```python
name = input("Please enter your name:")
reverse = name[::-1]
print("Your name in reverse is", reverse)
```

The command-line interface will ask for input from our keyboard, and then:

![input/output example](images/ioexample.png)

---

## Python text output: `print()`

- Put what you want to print between the parentheses: `print("Hello World")`
- If you want to jump to a new line, use `\n`: `print("Hello\nWorld")`
- You can also pass multiple arguments by separating them with commas: `print("x has the value:", x, "\nand y has the value:", y)`

---

## Python text input: `input()`

- The command waits until the user types some text in the command-line interface and finishes with ENTER
- The term `input()` "turns" into the text entered, and is **ALWAYS** an object the type `string`!
- Thus, it needs to be saved into a variable: `x = input()`
  - After the user types "Hi", for example, it is as if: `x = "Hi"`
- You can customize an input message by passing a string:

```python
x = input("Please enter your name: ")
```

---

## Input of numeric values

- Now, suppose we want to calculate the sum of two numbers:

```python
x = input("Please enter first number: ")
y = input("Please enter second number: ")
z = x + y
print("The sum is", z)
```

What happened???

![wellwellwell reaction meme](images/wellwellwell.png)

- We were adding two strings together, not two numbers! (`input()` gives strings!)

---

## Converting string to number types

- You can convert a string to a number using the methods `int()` and `float()`
  - The string that goes inside the parentheses (which we call the "argument" of the method) will be turned to an integer/float

```python
xstring = input("Please enter your age: ")
x = int(xstring)
print("Your age is ", x)
```

- Just make things shorter by chaining one method into another!

```python
x = int(input("Please enter your age: "))
print("Your age is ", x)
```

---

## Exercise 1.c.3

Suppose the user types `3` and then `4`. What does each program print?

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

```python
a = input("First: ")
b = input("Second: ")
print(a + b)
```

</div>
<div style="flex:1">

```python
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)
```

</div>
<div style="flex:1">

```python
a = float(input("First: "))
b = input("Second: ")
print(a, b)
```

</div>
</div>

What happens in the second program if the user types `3.5`?
<!-- .element: class="fragment" -->

Note:
1. `34` — string concatenation.
2. `7` — integer addition.
3. `3.0 4` — `a` is a float, `b` is still a string.
Typing `3.5` into `int(...)` gives a `ValueError`: `int()` can't convert a string with a decimal point.

---

## Exercise 1.c.4

Write a program in Thonny that:

1. asks the user for their name,
2. asks for their favorite food,
3. asks how many servings they could eat (an integer),
4. prints a sentence using all three answers, for example:

```
Hi Ada! You could eat 3 servings of pizza.
```

**Challenge:** save it as `food.py` and run it from the command line with `python3 food.py`.

Note:
Possible solution:

```python
name = input("What is your name? ")
food = input("What is your favorite food? ")
servings = int(input("How many servings could you eat? "))
print("Hi", name + "! You could eat", servings, "servings of", food + ".")
```

---

# Running code

---

## Running code

Try:

- Saving some previous code as `program.py`
- Open a command-line interface in your computer and run: `python3 program.py`
  - You need to have python3 installed in your machine
  - You need to be in the directory of the file `program.py`

---

Python can be run in two modes:

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

### Script / Program

- All lines of code executed without stop
- Run in command-line as `python3 program.py`
- Only print what is specifically passed through `print()`

</div>
<div style="flex:1">

### Interactive shell

- Run lines of code each at a time, as user enters them
- Open in command-line just by typing `python3`
- Typing an expression without being assigned to a variable will "print" the result

</div>
</div>