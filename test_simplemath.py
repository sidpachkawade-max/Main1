import pytest

def test_simplemath(run_script):
    script = "simplemath.py"
    expected = "26\n"
    stdout, stderr = run_script(script)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()