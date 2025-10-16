"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""

# 1. Ask the user which conversion they want to perform.
# The input is stored in the 'choice' variable.
choice = input("For C => F enter C, for F => C enter F: ")

# 2. Use a conditional block to decide which conversion to run.
# The .upper() method makes the input check case-insensitive (accepts 'c' or 'C').
if choice.upper() == 'C':
    # --- This block runs for Celsius to Fahrenheit conversion ---
    
    # Initialize the starting temperature for the loop.
    celsius = -20
    
    # Loop from -20 to 40 degrees Celsius (inclusive).
    while celsius <= 40:
        # Apply the formula to convert Celsius to Fahrenheit.
        fahrenheit = (9/5) * celsius + 32
        
        # Print the result, formatted to one decimal place.
        print(f"{celsius} C => {fahrenheit:.1f} F")
        
        # Increment the counter to process the next degree.
        celsius += 1

elif choice.upper() == 'F':
    # --- This block runs for Fahrenheit to Celsius conversion ---

    # Initialize the starting temperature for the loop.
    fahrenheit = -10
    
    # Loop from -10 to 110 degrees Fahrenheit (inclusive).
    while fahrenheit <= 110:
        # Apply the formula to convert Fahrenheit to Celsius.
        celsius = (5/9) * (fahrenheit - 32)
        
        # Print the result, formatted to one decimal place.
        print(f"{fahrenheit} F => {celsius:.1f} C")
        
        # Increment the counter to process the next degree.
        fahrenheit += 1
else:
    # --- This block runs if the user enters an invalid character ---
    print("Invalid input. Please run the program again and enter 'C' or 'F'.")
