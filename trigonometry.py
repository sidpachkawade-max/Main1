"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""
import math

def format_auto(num):
    """
    Formats a number to one or two decimal places automatically.
    - If the second decimal place is a zero (e.g., 0.10), it returns a string
      with one decimal place (e.g., "0.1").
    - Otherwise, it returns a string with two decimal places (e.g., "0.31").
    """
    # Format the number to a string with exactly two decimal places.
    two_places = f"{num:.2f}"
    
    # If the string ends with '0', trim the last character.
    if two_places.endswith('0'):
        return two_places[:-1]
    
    # Otherwise, return the original two-decimal-place string.
    return two_places

# --- Main Program ---

# 1. Print the table header exactly as required by the test.
print("radians |  sine | tangent")
print("-------------------------")

# 2. Initialize the starting value for the loop.
radians = 0.0

# 3. Loop in steps of 0.1 as long as the value is less than pi.
while radians < math.pi:
    # Calculate the trigonometric values.
    sine_value = math.sin(radians)
    tangent_value = math.tan(radians)
    
    # Use the helper function to get the correctly formatted strings.
    sine_str = format_auto(sine_value)
    tangent_str = format_auto(tangent_value)

    # Print the formatted row. The alignment specifiers (e.g., >5)
    # ensure the columns line up neatly as seen in the test output.
    print(f"{radians:7.1f} | {sine_str:>5} | {tangent_str:>7}")
    
    # Increment for the next iteration.
    radians += 0.1

# 4. The test requires the final value to be exactly pi (printed as 3.14).
# We handle this last line separately to ensure its inclusion and proper formatting.
final_radians = math.pi
final_sine = math.sin(final_radians)
final_tangent = math.tan(final_radians)

sine_str = format_auto(final_sine)
tangent_str = format_auto(final_tangent)

# Print the final formatted row.
print(f"{final_radians:7.2f} | {sine_str:>5} | {tangent_str:>7}")