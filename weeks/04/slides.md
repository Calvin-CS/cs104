---
marp: true
title: "Week 4: Conditionals"
theme: default
paginate: true
---

# Conditionals

### CS-104 · Week 4

---

## Branching Logic

- Use `if` when code should run only in some cases.
- Use `elif` for additional checks.
- Use `else` for the remaining case.

---

## Boolean Expressions

- Conditionals depend on a true or false result.
- Write conditions that are easy to read.
- Test edge cases, not just typical cases.

---

## Example Pattern

```python
if score >= 90:
	letter = "A"
elif score >= 80:
	letter = "B"
else:
	letter = "C or below"
```

---

## Common Errors

- Overlapping conditions
- Missing edge cases
- Nesting too deeply when simpler logic would do
