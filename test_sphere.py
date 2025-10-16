import pytest

def test_sphere(run_script):
    script = "sphere.py"
    input_data = "2\n"
    expected = ("Enter a radius: "
                "The sphere has a volume of 33.51\n"
                "The surface area of this sphere is 50.27\n")
    
    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()