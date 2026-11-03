# Test case: Body temperature cooling toward room temperature
# Repeats the same checks (curve, labels, title, both marker lines) for a
# different starting temperature, room temperature, and time constant, to
# catch a solution that only works for the lab's one worked example.

FILENAME = "cooling.py"
T0 = 37.0
T_ROOM = 22.0
TAU = 8.0


import io
import runpy
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")  # no display needed/available on the grading server
import matplotlib.pyplot as plt
plt.show = lambda *a, **k: None  # never block / warn waiting for a window


def run_with_input(path, values):
    text_input = "\n".join(str(v) for v in values) + "\n"
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    try:
        sys.stdin = io.StringIO(text_input)
        sys.stdout = io.StringIO()
        plt.close("all")
        runpy.run_path(path, run_name="__main__")
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout


def classify_lines(ax):
    """Split this axes' plotted lines into (main_curve, horizontal_marker,
    vertical_marker) based on their shape, or raise ValueError describing
    what's missing/ambiguous."""
    curves, h_markers, v_markers = [], [], []
    for line in ax.get_lines():
        xdata, ydata = np.asarray(line.get_xdata()), np.asarray(line.get_ydata())
        if len(xdata) > 10:
            curves.append(line)
        elif np.ptp(ydata) < 1e-9:
            h_markers.append(line)
        elif np.ptp(xdata) < 1e-9:
            v_markers.append(line)
    if len(curves) != 1:
        raise ValueError(
            "expected exactly 1 main curve (from plt.plot(t, temp)), found {}"
            .format(len(curves)))
    if len(h_markers) != 1:
        raise ValueError(
            "expected exactly 1 horizontal marker line (from plt.axhline(...)), "
            "found {}".format(len(h_markers)))
    if len(v_markers) != 1:
        raise ValueError(
            "expected exactly 1 vertical marker line (from plt.axvline(...)), "
            "found {}".format(len(v_markers)))
    return curves[0], h_markers[0], v_markers[0]


def test_passed(test_feedback):
    case_label = "T0={}, T_room={}, tau={}".format(T0, T_ROOM, TAU)
    try:
        run_with_input(FILENAME, [T0, T_ROOM, TAU])
    except Exception as e:
        test_feedback.write("Your program raised an error for {}:\n{}".format(case_label, e))
        return False

    if not plt.get_fignums():
        test_feedback.write(
            "For {}, no plot was created. Make sure you call plt.plot(...) "
            "and plt.show().".format(case_label))
        return False

    ax = plt.gca()

    if ax.get_xlabel().strip() != "Time (minutes)":
        test_feedback.write(
            "For {}, the x-axis label should be exactly 'Time (minutes)', "
            "but got '{}'.".format(case_label, ax.get_xlabel()))
        return False

    if ax.get_ylabel().strip() != "Temperature (°C)":
        test_feedback.write(
            "For {}, the y-axis label should be exactly 'Temperature (°C)', "
            "but got '{}'.".format(case_label, ax.get_ylabel()))
        return False

    if ax.get_title().strip() != "Newton's Law of Cooling":
        test_feedback.write(
            "For {}, the plot title should be exactly \"Newton's Law of "
            "Cooling\", but got '{}'.".format(case_label, ax.get_title()))
        return False

    try:
        curve, h_marker, v_marker = classify_lines(ax)
    except ValueError as e:
        test_feedback.write("For {}, {}.".format(case_label, e))
        return False

    xdata, ydata = np.asarray(curve.get_xdata()), np.asarray(curve.get_ydata())
    if len(xdata) != 200:
        test_feedback.write(
            "For {}, expected 200 points from np.linspace, but the main "
            "curve has {} points.".format(case_label, len(xdata)))
        return False

    t_max_expected = 5 * TAU
    if abs(xdata[0] - 0.0) > 1e-6 or abs(xdata[-1] - t_max_expected) > 1e-4:
        test_feedback.write(
            "For {}, expected t to range from 0 to 5*tau = {:.4f}, but it "
            "ranged from {:.4f} to {:.4f}."
            .format(case_label, t_max_expected, xdata[0], xdata[-1]))
        return False

    expected_temp = T_ROOM + (T0 - T_ROOM) * np.exp(-xdata / TAU)
    if not np.allclose(ydata, expected_temp, atol=1e-6):
        worst = np.argmax(np.abs(ydata - expected_temp))
        test_feedback.write(
            "For {}, the plotted temperature doesn't match T(t) = T_room + "
            "(T0 - T_room) * e^(-t/tau) at every point — e.g. at t={:.4f}, "
            "expected T={:.4f} but got {:.4f}."
            .format(case_label, xdata[worst], expected_temp[worst], ydata[worst]))
        return False

    v_marker_x = np.asarray(v_marker.get_xdata())[0]
    if abs(v_marker_x - TAU) > 1e-6:
        test_feedback.write(
            "For {}, expected the vertical marker line at t = tau = {:.4f}, "
            "but found it at t = {:.4f}.".format(case_label, TAU, v_marker_x))
        return False

    h_marker_y = np.asarray(h_marker.get_ydata())[0]
    expected_marker_y = T_ROOM + (T0 - T_ROOM) * np.exp(-1)
    if abs(h_marker_y - expected_marker_y) > 1e-6:
        test_feedback.write(
            "For {}, expected the horizontal marker line at T_room + "
            "(T0 - T_room) * e^-1 = {:.4f}, but found it at {:.4f}."
            .format(case_label, expected_marker_y, h_marker_y))
        return False

    test_feedback.write("Passed!")
    return True
