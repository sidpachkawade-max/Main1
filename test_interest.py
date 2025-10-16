import pytest

def test_interest(run_script):
    script = "interest.py"
    input_data = "3.2\n3000\n5\n"
    expected = ("Enter the fixed interest rate in percent: "
                "Enter the amount of money you want to invest: "
                "Enter the number of years the money will be invested: "
                "The earned interest is 511.72.\n"
                "The terminal value amounts to 3511.72.\n")
    
    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()