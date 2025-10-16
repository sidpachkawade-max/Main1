"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""
# 1. Define the necessary conversion 
INCH_IN_CM = 2.54
CM_IN_METER = 100
FEET_IN_INCHES = 12
YARDS_IN_FEET = 3
MILES_IN_YARDS = 1760

# 2. Get the user input

# The float() function converts the text input into a number that can have decimal places.

meters = float(input("Enter a distance in meters: "))

# 3. Perform the conversions
# First, convert meters to inches, which will be our base for other calculations.
# meters -> centimeters -> inches

inches = (meters * CM_IN_METER) / INCH_IN_CM

# Now, convert inches to the other units.
feet = inches / FEET_IN_INCHES
yards = feet / YARDS_IN_FEET
miles = yards / MILES_IN_YARDS

# 4. Print the formatted results
# The f-string and the ':.2f' format specifier are used to round the output to two decimal places.
print(f"{inches:.2f} inch")
print(f"{feet:.2f} feet")
print(f"{yards:.2f} yards")
print(f"{miles:.2f} miles")