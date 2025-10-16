import pytest

def test_trigonometry(run_script):
    script = "trigonometry.py"
    input_data = ""
    expected = """radians |  sine | tangent
-------------------------
    0.0 |   0.0 |     0.0
    0.1 |   0.1 |     0.1
    0.2 |   0.2 |     0.2
    0.3 |   0.3 |    0.31
    0.4 |  0.39 |    0.42
    0.5 |  0.48 |    0.55
    0.6 |  0.56 |    0.68
    0.7 |  0.64 |    0.84
    0.8 |  0.72 |    1.03
    0.9 |  0.78 |    1.26
    1.0 |  0.84 |    1.56
    1.1 |  0.89 |    1.96
    1.2 |  0.93 |    2.57
    1.3 |  0.96 |     3.6
    1.4 |  0.99 |     5.8
    1.5 |   1.0 |    14.1
    1.6 |   1.0 |  -34.23
    1.7 |  0.99 |    -7.7
    1.8 |  0.97 |   -4.29
    1.9 |  0.95 |   -2.93
    2.0 |  0.91 |   -2.19
    2.1 |  0.86 |   -1.71
    2.2 |  0.81 |   -1.37
    2.3 |  0.75 |   -1.12
    2.4 |  0.68 |   -0.92
    2.5 |   0.6 |   -0.75
    2.6 |  0.52 |    -0.6
    2.7 |  0.43 |   -0.47
    2.8 |  0.33 |   -0.36
    2.9 |  0.24 |   -0.25
    3.0 |  0.14 |   -0.14
    3.1 |  0.04 |   -0.04
   3.14 |   0.0 |    -0.0
"""

    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    

    
    

    reporter.summary()