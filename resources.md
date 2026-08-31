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

If you can't install Thonny locally (e.g., on a shared or locked-down computer), the course also offers a cloud-based coding environment through **Coder**.

- Log in at [Calvin's Coder instance](https://coder.cs.calvin.edu/workspaces) and open a workspace
- Your workspace includes Python and Thonny, ready to use — no local installation needed
- [What is Coder?](https://coder.com/docs/about) — remote development environments in a browser
- **Tip:** your files persist within your workspace — save often and keep your work organized

### Python

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Built-in functions](https://docs.python.org/3/library/functions.html)

### Thonny

**Thonny** is the IDE we use in this class — a simple, beginner-friendly editor built specifically for learning Python. It's already installed on the lab computers, but you'll likely want it on your own laptop too.

**Installing Thonny:**

1. Go to [thonny.org](https://thonny.org/) and download the installer for your operating system (Windows, Mac, or Linux)
2. Run the installer, accepting the default options
3. Open Thonny — it comes with Python already bundled, so there's nothing extra to install

**Getting set up:**

- When Thonny opens, you'll see two main areas: the **editor** (top, where you write and save your program) and the **Shell** (bottom, where output appears and you can try out code interactively)
- Write your code in the editor, then click the green **Run** button (or press <kbd>F5</kbd>) to run it
- Save your file with <kbd>Ctrl+S</kbd> before running — Thonny will prompt you to save if you forget

**Debugging in Thonny:**

- Click the bug icon (or press <kbd>Ctrl+F5</kbd>) to step through your code line by line
- Use the step buttons to watch variables change value as your program runs — this is one of Thonny's best features for beginners
- The **Variables** pane (View → Variables) shows the current value of every variable while your program runs or is paused

**If something looks different than expected:**

- Check that "Standard" mode is selected (View → uncheck "Regular mode" is not needed for this course — the defaults work fine)
- If packages are missing, use Tools → Manage Packages to install them
- [Thonny documentation](https://thonny.org/) has more on installation and troubleshooting for each OS

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
