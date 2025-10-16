"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""

# 1. Initialize the starting Celsius temperature
celsius = -15

while celsius <= 35: # 2. Set up the while loop to run from -15 to 35 (inclusive)
# The loop will continue as long as the condition (celsius <= 35) is true.

    fahrenheit = (9/5) * celsius + 32 # 3. Calculate the Fahrenheit value using the provided formula
    

    print(f"{celsius} C => {fahrenheit:.1f} F") # 4. Print the result in the specified format
    
    # An f-string is used for easy formatting.
    # The ':.1f' part formats the Fahrenheit value to one decimal place.

    celsius += 1 # 5. Increment the celsius counter by 1 for the next loop iteration # This is a critical step to prevent an infinite loop.
                 # This is shorthand for celsius = celsius + 1


