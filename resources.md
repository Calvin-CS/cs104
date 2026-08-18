---
layout: default
title: Resources
permalink: /resources/
---

# Resources

## Getting Started

New to programming entirely? Work through these before (or alongside) the first few weeks of class:

1. [Hedy](https://hedy.org/) — a very gentle introduction to programming
2. [futurecoder](https://futurecoder.io/) — an interactive, step-by-step Python course
3. Kaggle's [Python](https://www.kaggle.com/learn/python) and [pandas](https://www.kaggle.com/learn/pandas) tutorials

## Development Environment

### Coder

The course can use a cloud-based coding environment through **Coder**, so you do not need to install everything locally to get started.

- Log in at [Calvin's Coder instance](https://coder.cs.calvin.edu) and open a workspace
- Your workspace includes Python and the tools needed for class work
- [What is Coder?](https://coder.com/docs/about) — remote development environments in a browser
- **Tip:** your files persist within your workspace — save often and keep your work organized

### Python

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Built-in functions](https://docs.python.org/3/library/functions.html)

### VS Code

VS Code is a good editor for writing, running, and debugging Python programs.

- [Download VS Code](https://code.visualstudio.com/)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)
- [Debugging in VS Code](https://code.visualstudio.com/docs/editor/debugging)

### Debugging Help

- [Python Tutor](https://pythontutor.com/) — step through code execution visually
- [Common Python errors](https://docs.python.org/3/tutorial/errors.html)
- [PEP 8 style guide](https://peps.python.org/pep-0008/) — for readable Python code

---

## How to Succeed in This Class

> Starting early is essential to success in programming. Newcomers sometimes think that they can start an assignment at the last minute and do reasonably well. Programming isn't like writing a paper... In programming, it often either works or it doesn't.

### Attendance & Support

- Come to class, lab, study sessions, and office hours
- Ask for help early — don't wait until you're stuck for hours

### Helpful Habits

- Don't just "get it working" — understand *why* it works
- Start early; take frequent breaks
- Take small steps (run your code frequently, not just at the end)
- Retry lab and homework exercises later without looking at your prior solution
- Review class materials (POGIL activities, slides, retrieval quizzes)
- Discuss problems with classmates
- Create your own syntax/concept cheat-sheets as you go
- Review quiz and assignment feedback closely

### Extra Practice

1. Complete "Challenge" exercises in the textbook
2. [Python practice problems](https://cs.calvin.edu/courses/cs/108/resources/python_problems/index.html)
3. More [Python practice problems](https://py-reference.netlify.app/)
4. Search online for "Python practice" — there's no shortage of it

---

## Patterns

### Gather, Compute, Use

A simple pattern for structuring small programs:

```python
# Gather
n = int(input("Enter a number: "))
# Compute
result = n * 2
# Use
print("Twice", n, "is", result)
```

## Problem-Solving Strategies

### Once, Twice, Many

A strategy for writing loops: solve the problem for one item, then two, then generalize into a loop.

**Once** — get it working for a single item:

```python
numbers = [5]
total = numbers[0]
print("The sum is", total)
```

**Twice** — extend it to two items:

```python
numbers = [5, 7]
total = numbers[0] + numbers[1]
print("The sum is", total)
```

**Many** — notice the duplicated pattern, then turn it into a loop:

```python
numbers = [5, 7, 3, 8]
total = 0
for n in numbers:
    total = total + n
print("The sum is", total)
```

---

## Other Resources

### Free

- [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp) and [Quiz](https://www.w3schools.com/python/python_quiz.asp)
- [Python standard library](https://docs.python.org/3/library/index.html)

### Paid

- [Codecademy's "Learn Python" course](https://www.codecademy.com/learn/learn-python-3)
- [Educative Python tutorial](https://www.educative.io/courses/learn-python-3-from-scratch)

## Fun Stuff

Play with [tixy](https://www.mathsuniverse.com/tixy/) — a tiny, playful way to build computational thinking.

## Other Interesting Things

- [Falsehoods Programmers Believe About Names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)
- How integers and floats actually work:
  - [Interactive tutorial](https://dennisforbes.ca/articles/understanding-floating-point-numbers.html)
  - [float.exposed](https://float.exposed/0x40000000) and [integer.exposed](https://integer.exposed/#0x0000)
  - [Comprehensive reference](https://www3.ntu.edu.sg/home/ehchua/programming/java/datarepresentation.html)
