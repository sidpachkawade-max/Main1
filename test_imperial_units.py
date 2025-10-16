import pytest

def test_imperial_units(run_script):
    script = "imperial_units.py"
    input_data = "1.3\n"
    expected = ("Enter a distance in meters: "
                "51.18 inch\n"
                "4.27 feet\n"
                "1.42 yards\n"
                "0.00 miles\n")

    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()