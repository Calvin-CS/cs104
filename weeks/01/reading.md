---
layout: week
title: "Week 1: Introduction"
week_number: 1
---

# What Is Programming?

## Giving a Computer Instructions

Programming is the practice of writing instructions that a computer can follow exactly. Computers are fast, but they are not flexible in the way people are. If you tell a friend, "add these numbers and show me the answer," they can fill in missing details. A computer cannot. It needs each step written clearly and in the right order.

That is why beginners often feel that programming is "picky." It is. The benefit of that precision is that once a program works, the computer can repeat the same process reliably as many times as you want.

---

## A Tiny Example

Here is a small Python program:

```python
name = "Ava"
print("Hello, " + name)
```

This program stores a value in the variable `name` and then prints a greeting. The computer does not infer anything extra. It follows the instructions exactly: store, then print.

---

## Programming Is Problem Solving

Writing code is not only about syntax. It is also about breaking a problem into smaller steps.

Suppose you want a program that tells a student whether they passed a quiz. A programmer might break the task into pieces like this:

1. Read the quiz score.
2. Compare the score to the passing cutoff.
3. Print the correct message.

Good programmers learn to move back and forth between the big goal and the small steps.

---

## Check Your Understanding

<!-- QUESTION:multiple-choice -->

**Which statement best describes programming?**

- [ ] Programming is teaching a computer to guess what the user wants.
- [x] Programming is writing precise instructions that a computer can execute.
- [ ] Programming only matters when building large software systems.
- [ ] Programming means memorizing lots of commands without understanding them.

<!-- END QUESTION -->

---

<!-- QUESTION:true-false
answer: false
-->

If a program is almost correct, the computer will usually figure out what the programmer meant.

<!-- END QUESTION -->

# A Beginner Workflow

## Build, Run, Check, Revise

Most programming happens in a simple cycle:

**1. Write a small piece of code.** Start with one step, not the whole problem.

**2. Run it.** See what the computer actually does.

**3. Compare the result to your expectation.** If they match, continue. If they do not, investigate.

**4. Revise and test again.** Programming improves through iteration.

This cycle matters because errors are normal. Good programmers do not avoid mistakes completely; they learn how to find and fix them efficiently.

---

## Reading Error Messages

An error message is not just bad news. It is information.

If Python shows a `SyntaxError`, it usually means the code is not written in a form Python can parse. If it shows a `NameError`, it usually means you tried to use a variable name that has not been defined.

Learning to slow down and read the message carefully is one of the most important early programming habits.

---

## Check Your Understanding

<!-- QUESTION:fill-in-the-blank -->

Complete the beginner workflow.

First, *[write]* a small piece of code. Next, *[run]* it and compare the result to what you expected. If something is wrong, *[revise]* the program and test it again.

<!-- END QUESTION -->

---

<!-- QUESTION:drag-the-words -->

Drag the correct term into each sentence.

A `SyntaxError` usually means Python cannot *[parse]* the code as written. A `NameError` usually means a variable name was used before it was *[defined]*. Careful *[testing]* helps programmers catch problems early.

<!-- END QUESTION -->

# Habits That Help

## Start Small and Stay Clear

Students often assume that strong programmers write long complicated code quickly. In reality, strong programmers usually do the opposite. They begin with a small working version, test often, and improve the code in stages.

Useful habits include:

- choosing clear variable names
- testing code with simple examples first
- changing one thing at a time when debugging
- keeping programs readable instead of overly clever

These habits make your code easier to understand now and easier to fix later.

---

<!-- QUESTION:true-false
answer: true
-->

Testing a small piece of code before adding more is usually a good strategy for beginners.

<!-- END QUESTION -->
