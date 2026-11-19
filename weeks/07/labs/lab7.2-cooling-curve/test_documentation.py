# Test case: Documentation
# Confirms cooling.py has a docstring containing @author, with the
# template's placeholder name(s) replaced by the student's own.

FILENAMES = ["cooling.py"]


import ast
import traceback


def test_passed(test_feedback):
    for FILENAME in FILENAMES:
        try:
            source = open(FILENAME).read()
            parsed = ast.parse(source, filename=FILENAME)
            docstring = ast.get_docstring(parsed)
        except SyntaxError:
            test_feedback.write(traceback.format_exc(limit=0))
            return False
        except:
            test_feedback.write("Unknown error reading documentation. Ask the course staff for help.\n\n" + traceback.format_exc())
            return False

        if docstring is None or '@author' not in docstring:
            test_feedback.write(FILENAME + " documentation should include author (see the template).")
            return False

        if any(x in docstring for x in ['YOUR-NAME', 'yourid123', 'PARTNER-NAME', 'theirid123']):
            test_feedback.write(FILENAME + ": Please replace the template names and userids with your own.")
            return False

    test_feedback.write("Passed!")
    return True
