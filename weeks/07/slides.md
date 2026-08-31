# Modules, Dependencies, and Virtual Environments

### CS-104 · Week 7

---

# Recap

---

## Modules

- A **module** is just a Python file you can `import` and reuse.
- Python ships with many built-in modules: `random`, `math`, `turtle`, `os`, ...
- `import module_name` gives you `module_name.something`; `from module_name import something` gives you `something` directly.

---

## Dependencies

- A **dependency** is a package your project needs that *isn't* built into Python.
- Install with `pip install package_name`; check what's installed with `pip list`.
  - In Thonny: **Tools → Manage Packages** does the same thing without a terminal.
- Good projects record their dependencies (e.g. in a `requirements.txt`) so others can install the same things.

---

## Virtual Environments

- A **virtual environment** is an isolated, project-specific set of installed packages.
- It keeps one project's dependencies from colliding with another's.
- Create one with `python3 -m venv env`; activate it before installing anything.

---

## References

- [Python docs: Modules](https://docs.python.org/3/tutorial/modules.html)
- [PyPI — the Python Package Index](https://pypi.org/)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [Python docs: `venv`](https://docs.python.org/3/library/venv.html)

---

# POGIL Activity

---

## Exercise 7.a

*Exercise*

*Activities for CS1 in Python*, [Importing Modules](https://cs.calvin.edu/courses/cs/108/26sp/resources/pogil/Act08-Modules_Student.pdf)

Work through the following models:

1. *Model 1*. Random Numbers
2. *Model 2*. Multiple Modules (`__name__ == "__main__"`)
3. *Model 3*. Turtle Graphics

---

# Dependency Exercises

---

## Exercise 7.b.1: What's already installed?

*Exercise*

In your terminal (or Coder workspace), run:

```
pip list
```

- Is `turtle` in the list? Why or why not? *(Hint: it ships with Python — it's not a separate dependency.)*
- Pick one package you don't recognize and look up what it's for.

---

## Exercise 7.b.2: Installing a dependency

*Exercise*

Install a small, fun package:

```
pip install cowsay
```

Then write a two-line program that uses it:

```python
import cowsay
cowsay.cow("Hello, CS-104!")
```

Run `pip list` again — what changed?

---

## Exercise 7.b.3: Recording dependencies

*Exercise*

Generate a `requirements.txt` for the project above:

```
pip freeze > requirements.txt
```

- Open the file — what's in it?
- If a classmate ran `pip install -r requirements.txt` on their own machine, what would happen?

---

# Virtual Environment Exercises

---

## Exercise 7.c.1: Create and activate

*Exercise*

From your project folder:

```
python3 -m venv env
```

Activate it:

<div class="columns" style="display:flex; gap:2rem;">
<div style="flex:1">

**macOS / Linux:**

```
source env/bin/activate
```

</div>
<div style="flex:1">

**Windows:**

```
env\Scripts\activate
```

</div>
</div>

How can you tell the environment is active?

---

## Exercise 7.c.2: Isolation in action

*Exercise*

With your virtual environment **active**:

```
pip install cowsay
pip list
```

Now **deactivate** it:

```
deactivate
```

Run `pip list` again.

- Is `cowsay` still there?
- Why might this matter when two different projects need different versions of the same package?

---

# Class Activity

---

## Exercise 7.d: A small multi-file project

*Exercise*

Work with a partner. Structure a small project across multiple files:

1. Create `helpers.py` with at least one function (e.g. one that formats or validates input).
2. Create `main.py` that imports `helpers` and uses it to solve a small problem of your choosing.
3. Add `if __name__ == "__main__":` to `helpers.py` — confirm it behaves differently when run directly vs. imported.
4. Set up a virtual environment for the project, install at least one external package (even a small one like `cowsay`), and write its `requirements.txt`.

Be ready to explain your file structure to another pair.

---

## Wrap-Up

By now you should be able to:

- Import and use both built-in and third-party modules
- Install, check, and record a project's dependencies
- Create and use a virtual environment to keep projects isolated

That covers the whole first half of the sequence — nice work!
