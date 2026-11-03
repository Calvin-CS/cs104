# Test case: Negative values and the C/F crossing point
# Converts negative and boundary values, including -40 — the one
# temperature where the Celsius and Fahrenheit scales coincide — to catch
# sign errors in the conversion formula.

FILENAME = "array_conversion.py"
TEST_INPUT = "-40,0,100"
EXPECTED_LINE = "[-40.  32. 212.]"
PROMPT = "Celsius temperatures (comma-separated): "


import io
import runpy
import sys


def run_with_input(path, text_input):
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

    if not output.startswith(PROMPT):
        test_feedback.write(
            "The prompt doesn't match. Make sure you call input() with "
            "exactly the prompt text\n'{}'.".format(PROMPT))
        return False

    actual_line = output[len(PROMPT):].strip()
    if actual_line != EXPECTED_LINE:
        test_feedback.write(
            "For input '{}', expected the printed array\n{}\nbut got\n{}\n"
            "(-40 is a special case: -40°C and -40°F are the same "
            "temperature, so the first value shouldn't change.)"
            .format(TEST_INPUT, EXPECTED_LINE, actual_line))
        return False

    test_feedback.write("Passed!")
    return True
