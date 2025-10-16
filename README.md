[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5I_3rsMw)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21049722)
# CMS2 - HW1 - Basics
Add your homework solutions in the directory contained in the repostitory. Each of your files should contain your name using the following template
```
"""
.. moduleauthor:: Your Name
"""
```
Note that putting the author name on top is not mandatory, but good practice.

We did not discuss every detail required to solve the following tasks. Use your favorite search engine and some common sense to solve the tasks. 
**Use exactly the same input prompts and output messages as in the provided examples.** This is **important** as your results will partly be **graded automatically**.
When completing the tasks you might get the impression that all of these could be solved simpler using a spreadsheet program like LibreOffice Calc... and you would be right. However, remember that this is the first real code you write in a programming language. The upcoming homeworks will be much more thrilling.

### How to get automatic feedback
The folder contains `test_*.py` files for each task. You can test task `x` by executing `test_x.py`. This will verify if you did the task correctly, or if there are some errors. You can do this for each task. To get feedback for all tasks at once run `grade_homework.py`. Not that you can run these files as often as you want. What counts is the last commited version before the submission deadline.


**If not stated otherwise, you can achieve at most one point per task.**

## 1. Simple Calculation
The first exercise concerns basic mathematics: Write a program for printing the result of `8+3*6`.
A sample run of this program:

```
26
```

Name the program file: `simplemath.py`


## 2. Convert Fahrenheit to Celsius
Ask the user to enter a floating point number denoting a temperature in degrees Fahrenheit. There must be a single space after the colon of the input prompt. Use the exact same wording for the input prompt and output as in the example below. Print that number converted to Celsius using the formula $C=\frac{5}{9}(F−32)$. The result must be rounded to two digits after the decimal point.
A sample run of this program:

```
Enter a temperature in degrees Fahrenheit: 72.3
72.3 degrees Fahrenheit correspond to 22.39 degrees Celsius
```
Name the program file: `fahrenheit_to_celsius.py` 


## 3.  Compute the return of investing money
Ask the user to enter a three values - a bank’s interest rate in percent per year, an initial investment and a number of years. Print both the earnings and the future value at the end of the investment. Assume that there are no taxes. The result must be rounded to two digits after the decimal point.
A sample run of this program:

```
Enter the fixed interest rate in percent: 3.2
Enter the amount of money you want to invest: 3000.0
Enter the number of years the money will be invested: 5
The earned interest is 511.72.
The terminal value amounts to 3511.72.
```
Name the program file: `interest.py` 


## 4.  Surface area and volume of a sphere
The program below should print the surface area and volume of a sphere given its radius. However, it contains errors. Fix the program.

```python
from math import PI
radius = input("Enter a radius: ")
area = 2 * r**2 ** pi
volume = (4 div 3) * r^3 * PI
print("The sphere has a volume of", round(volume, 2));
print("The surface area of this sphere is", round(Area, 2));
```
Name the program file: `sphere.py` 


## 5.  Convert Celsius to Fahrenheit
Instead of asking the user for input, simply print all temperatures from `-15` degrees Celsius to `+35` degrees Celsius in Fahrenheit. Use the formula $F=\frac{9}{5}C+32$. [hint: use a while loop]
A sample run of this program:
```
-15 C => 5.0 F
-14 C => 6.8 F
-13 C => 8.6 F
[...]
34 C => 93.2 F
35 C => 95.0 F
```
Name the program file: `celsius_to_fahrenheit.py` 


## 6. Imperial units
Ask the user for a length in meters and print the corresponding length measured in inches, in feet, in yards, and in miles. Assume that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one British mile is 1760 yards. Round all results to two digits for printing.
A sample run of this program:
```
Enter a distance in meters: 1.3
51.18 inch
4.27 feet
1.42 yards
0.00 miles
```
Name the program file: `imperial_units.py`

## 7. Mathematical functions
Write a program that prints the sine and tangent of all values between `0` and `$\pi$` in steps of `0.1`. The last value must be $\pi$. All values should be rounded to two digits after the decimal point. Hint: check the documentation of the format function.
A sample run of this program:
```
radians |  sine | tangent
-------------------------
    0.0 |   0.0 |     0.0
    0.1 |   0.1 |     0.1
    0.2 |   0.2 |     0.2
[...]
    3.0 |  0.14 |   -0.14
    3.1 |  0.04 |   -0.04
   3.14 |   0.0 |    -0.0
```
Name the program file: `trigonometry.py` 

`Hint:` The tricky part in this exercise is to find the right format of the decimals in each column. The number of `--------` above a column can help you to find the right format. Also note that the last value in the first column (radians) has a different format than the other values of that column.


## 8. Distance between two points
Write a program that asks the user for two points in a two-dimensional plane. The program must calculate and print the euclidean distance between the two points, rounded to four digits.
A sample run of this program:
```
First point's x-coordinate: 3.0
First point's y-coordinate: 7.0
Second point's x-coordinate: -2.0
Second point's y-coordinate: 3.0
The euclidean distance between the two points is 6.4031.
```
Name the program file: `distance.py`


## 9. Conversion between Celsius and Fahrenheit
Create a new program using the formulas from Exercises `2` and `5` that first asks the user whether a conversion from Celsius to Fahrenheit or the other way around is desired. Then print a table of values converting one unit to the other. For the conversion from `C` to `F` print the range of values from `-20` to `+40`; for conversion from `F` to `C` print the values from `-10` to `+110`.
A sample run of this program:
```
For C => F enter C, for F => C enter F: C
-20 C => -4.0 F
-19 C => -2.2 F
[...]
39 C => 102.2 F
40 C => 104.0 F
```
Name the program file: `temperature_tables.py` 
