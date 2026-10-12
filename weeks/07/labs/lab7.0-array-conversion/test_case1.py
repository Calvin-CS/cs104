# Test case: Basic conversion
# Converts a small set of whole-number Celsius values (0, 20, 37, 100) to
# Fahrenheit and checks the printed NumPy array against the exact example
# from the lab instructions.

FILENAME = "array_conversion.py"
TEST_INPUT = "0,20,37,100"
EXPECTED_LINE = "[ 32.   68.   98.6 212. ]"
PROMPT = "Celsius temperatures (comma-separated): "


import io
import runpy
import sys


def run_with_input(path, text_input):
    """Run `path` as a script (so its `if __name__ == "__main__":` guard
    fires), with stdin feeding `text_input` and stdout captured. Returns
    the captured stdout text, or raises if the script errors."""
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(text_input + "\n")
        sys.stdout = io.StringIO()
        runpy.run_path(path, run_name="__main__")
        return sys.stdout.getvalue()
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_passed(test_feedback):
    try:
        output = run_with_input(FILENAME, TEST_INPUT)
    except Exception as e:
        test_feedback.write(
            "Your program raised an error for input '{}':\n{}".format(TEST_INPUT, e))
        return False

    # input() writes only the prompt to stdout (no newline, and nothing of
    # the typed response) — so a correct run's full captured output is just
    # PROMPT immediately followed by the printed array and a trailing
    # newline from print(), all on one line.
    if not output.startswith(PROMPT):
        test_feedback.write(
            "The prompt doesn't match. Make sure you call input() with "
            "exactly the prompt text\n'{}'.".format(PROMPT))
        return False

    actual_line = output[len(PROMPT):].strip()
    if actual_line != EXPECTED_LINE:
        test_feedback.write(
            "For input '{}', expected the printed array\n{}\nbut got\n{}\n"
            "(Remember to compute fahrenheit with NumPy array arithmetic, "
            "not a manual loop, and print the array itself rather than "
            "formatting each value yourself.)"
            .format(TEST_INPUT, EXPECTED_LINE, actual_line))
        return False

    test_feedback.write("Passed!")
    return True
