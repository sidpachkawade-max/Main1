import pytest

def test_fahrenheit_to_celsius(run_script):
    script = "fahrenheit_to_celsius.py"
    input_data = "72.3\n"
    expected = ("Enter a temperature in degrees Fahrenheit: "
                "72.3 degrees Fahrenheit correspond to 22.39 degrees Celsius\n")
    
    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()