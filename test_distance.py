import pytest

@pytest.mark.parametrize("input_data, expected_output", [
    pytest.param("3.0\n7.0\n-2.0\n3.0\n",
                 "First point's x-coordinate: First point's y-coordinate: "
                 "Second point's x-coordinate: Second point's y-coordinate: "
                 "The euclidean distance between the two points is 6.4031.\n",
                 marks=pytest.mark.points(0.5)),
    
    pytest.param("2.0\n0.0\n3.0\n3.0\n",
                 "First point's x-coordinate: First point's y-coordinate: "
                 "Second point's x-coordinate: Second point's y-coordinate: "
                 "The euclidean distance between the two points is 3.1623.\n",
                 marks=pytest.mark.points(0.5))
])
def test_distance(run_script, input_data, expected_output):
    script = "distance.py"
    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected_output.split(), "Incorrect output."

# Add this block to run this test file individually
if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()