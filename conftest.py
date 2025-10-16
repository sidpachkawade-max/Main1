"""
CONTEST FOR STUDENT/SOLUTION SELF-GRADING

This configuration is used for running tests within a single solution folder
(e.g., by the student or for grading a specific solution).

It uses a "location-aware" run_script helper that assumes the Python scripts
to be tested are in the same directory as the test files.
"""

import pytest
import subprocess
import sys
import os

@pytest.fixture
def run_script(request):
    def _run_script(script_name, input_data="", timeout=3):
        test_dir = os.path.dirname(str(request.fspath))
        script_path = os.path.join(test_dir, script_name)
        
        if not os.path.exists(script_path):
            pytest.skip(f"Solution file '{script_name}' not found.")
        
        command = [sys.executable, script_path]
        try:
            process = subprocess.Popen(
                command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True, encoding='utf-8', cwd=test_dir
            )
            stdout, stderr = process.communicate(input_data, timeout=timeout)
            return stdout, stderr
        except subprocess.TimeoutExpired:
            pytest.fail(f"The script '{script_name}' ran for too long.")
    return _run_script

class PointsReporter:
    """The complete and correct PointsReporter plugin."""
    # This class remains unchanged and is correct.
    def __init__(self):
        self.achieved_points = 0.0
        self.total_possible_points = 0.0
        self.test_results = {}

    def pytest_configure(self, config):
        config.addinivalue_line("markers", "points(value): assign a custom point value")

    def pytest_collection_finish(self, session):
        self.achieved_points = 0.0
        self.total_possible_points = 0.0
        for item in session.items:
            marker = item.get_closest_marker("points")
            points = marker.args[0] if marker else 1.0
            self.total_possible_points += points
            self.test_results[item.nodeid] = {"points": points}
    
    def pytest_runtest_logreport(self, report):
        if report.when == 'call' and report.passed:
            nodeid = report.nodeid
            if nodeid in self.test_results:
                self.achieved_points += self.test_results[nodeid]["points"]

    def summary(self):
        print("\n" + "="*40)
        print(f"   🏆 Final Score: {self.achieved_points} / {self.total_possible_points} points 🏆")
        print("="*40)