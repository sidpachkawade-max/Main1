"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""

# Ask the user for input
fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (5/9) * (fahrenheit - 32)

# Print the result rounded to two decimal places
print(f"{fahrenheit:.1f} degrees Fahrenheit correspond to {celsius:.2f} degrees Celsius")

