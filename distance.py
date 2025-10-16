"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""
# 1. Import the 'math' module to get access to the square root function (math.sqrt)
import math

# 2. Get the coordinates of the two points from the user.
# The float() function converts the user's text input into a number with decimals.
x1 = float(input("First point's x-coordinate: "))
y1 = float(input("First point's y-coordinate: "))
x2 = float(input("Second point's x-coordinate: "))
y2 = float(input("Second point's y-coordinate: "))

# 3. Calculate the Euclidean distance using the formula.
# (x2 - x1)**2 calculates the square of the difference in x-coordinates.
# (y2 - y1)**2 calculates the square of the difference in y-coordinates.
# math.sqrt() calculates the square root of the sum.
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 4. Print the final result, formatted to four decimal places.
# An f-string is used for easy formatting.
# The ':.4f' specifier tells Python to format the number as a float
# with exactly four digits after the decimal point.
print(f"The euclidean distance between the two points is {distance:.4f}.")
