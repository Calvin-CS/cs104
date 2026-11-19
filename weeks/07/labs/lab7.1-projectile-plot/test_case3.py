# Test case: Low velocity / short flight
# Checks the same plot elements for a slower throw (v0 = 7.5 m/s), which
# produces a shorter, lower-arcing flight — catches formulas that happen
# to work only for the lab's one worked example.

FILENAME = "plot_projectile.py"
V0 = 7.5
G = 9.8


import io
import runpy
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")  # no display needed/available on the grading server
import matplotlib.pyplot as plt
plt.show = lambda *a, **k: None  # never block / warn waiting for a window


def run_with_input(path, v0):
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(str(v0) + "\n")
        sys.stdout = io.StringIO()
        plt.close("all")
        runpy.run_path(path, run_name="__main__")
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def test_passed(test_feedback):
    try:
        run_with_input(FILENAME, V0)
    except Exception as e:
        test_feedback.write("Your program raised an error for v0 = {}:\n{}".format(V0, e))
        return False

    if not plt.get_fignums():
        test_feedback.write(
            "For v0 = {}, no plot was created. Make sure you call plt.plot(...) "
            "and plt.show().".format(V0))
        return False

    ax = plt.gca()

    if ax.get_xlabel().strip() != "Time (s)":
        test_feedback.write(
            "For v0 = {}, the x-axis label should be exactly 'Time (s)', "
            "but got '{}'.".format(V0, ax.get_xlabel()))
        return False

    if ax.get_ylabel().strip() != "Height (m)":
        test_feedback.write(
            "For v0 = {}, the y-axis label should be exactly 'Height (m)', "
            "but got '{}'.".format(V0, ax.get_ylabel()))
        return False

    if ax.get_title().strip() != "Projectile Height":
        test_feedback.write(
            "For v0 = {}, the plot title should be exactly 'Projectile Height', "
            "but got '{}'.".format(V0, ax.get_title()))
        return False

    lines = ax.get_lines()
    if not lines:
        test_feedback.write(
            "For v0 = {}, the plot has no line — make sure you call "
            "plt.plot(t, h).".format(V0))
        return False

    xdata, ydata = np.asarray(lines[0].get_data()[0]), np.asarray(lines[0].get_data()[1])
    if len(xdata) != 100:
        test_feedback.write(
            "For v0 = {}, expected 100 points from np.linspace, but the "
            "plotted line has {} points.".format(V0, len(xdata)))
        return False

    t_total_expected = 2 * V0 / G
    if abs(xdata[0] - 0.0) > 1e-6 or abs(xdata[-1] - t_total_expected) > 1e-4:
        test_feedback.write(
            "For v0 = {}, expected t to range from 0 to {:.4f} (2*v0/g), but "
            "it ranged from {:.4f} to {:.4f}."
            .format(V0, t_total_expected, xdata[0], xdata[-1]))
        return False

    # Recompute the expected height AT THE STUDENT'S OWN SAMPLE POINTS
    # (rather than comparing to the continuous peak) so this check is
    # robust to exactly which 100 points np.linspace happened to land on,
    # while still verifying the formula itself is correct.
    expected_ydata = V0 * xdata - 0.5 * G * xdata ** 2
    if not np.allclose(ydata, expected_ydata, atol=1e-6):
        worst = np.argmax(np.abs(ydata - expected_ydata))
        test_feedback.write(
            "For v0 = {}, the plotted height doesn't match h(t) = v0*t - "
            "0.5*g*t**2 at every point — e.g. at t={:.4f}, expected h={:.4f} "
            "but got {:.4f}."
            .format(V0, xdata[worst], expected_ydata[worst], ydata[worst]))
        return False

    test_feedback.write("Passed!")
    return True
