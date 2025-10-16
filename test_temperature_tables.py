import pytest

def test_temperature_tables(run_script):
    script = "temperature_tables.py"
    input_data = "C\n"
    expected = ("For C => F enter C, for F => C enter F: "
"""-20 C => -4.0 F
-19 C => -2.2 F
-18 C => -0.4 F
-17 C => 1.4 F
-16 C => 3.2 F
-15 C => 5.0 F
-14 C => 6.8 F
-13 C => 8.6 F
-12 C => 10.4 F
-11 C => 12.2 F
-10 C => 14.0 F
-9 C => 15.8 F
-8 C => 17.6 F
-7 C => 19.4 F
-6 C => 21.2 F
-5 C => 23.0 F
-4 C => 24.8 F
-3 C => 26.6 F
-2 C => 28.4 F
-1 C => 30.2 F
0 C => 32.0 F
1 C => 33.8 F
2 C => 35.6 F
3 C => 37.4 F
4 C => 39.2 F
5 C => 41.0 F
6 C => 42.8 F
7 C => 44.6 F
8 C => 46.4 F
9 C => 48.2 F
10 C => 50.0 F
11 C => 51.8 F
12 C => 53.6 F
13 C => 55.4 F
14 C => 57.2 F
15 C => 59.0 F
16 C => 60.8 F
17 C => 62.6 F
18 C => 64.4 F
19 C => 66.2 F
20 C => 68.0 F
21 C => 69.8 F
22 C => 71.6 F
23 C => 73.4 F
24 C => 75.2 F
25 C => 77.0 F
26 C => 78.8 F
27 C => 80.6 F
28 C => 82.4 F
29 C => 84.2 F
30 C => 86.0 F
31 C => 87.8 F
32 C => 89.6 F
33 C => 91.4 F
34 C => 93.2 F
35 C => 95.0 F
36 C => 96.8 F
37 C => 98.6 F
38 C => 100.4 F
39 C => 102.2 F
40 C => 104.0 F
""")
    
    stdout, stderr = run_script(script, input_data)
    assert not stderr, f"Your script produced an error:\n{stderr}"
    assert stdout.split() == expected.split(), "Incorrect output."

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()