"""
.. moduleauthor:: Siddesh Pachkawade <your.address@yourdomain.at>
"""
# 1. Get user input for the three required values
# The float() function is used to convert the user's text input into a number with decimals.
interest_rate_percent = float(input("Enter the fixed interest rate in percent: "))
initial_investment = float(input("Enter the amount of money you want to invest: "))
# The int() function is used to convert the input into a whole number for years.
years = int(input("Enter the number of years the money will be invested: "))

# 2. Perform the calculations
# Convert the interest rate from a percentage to a decimal for the formula
interest_rate_decimal = interest_rate_percent / 100

# Calculate the future value using the compound interest formula: P * (1 + r)^t
# The ** operator is used for exponentiation (raising to the power of).
future_value = initial_investment * (1 + interest_rate_decimal) ** years

# Calculate the total earnings by subtracting the initial investment from the final value
earned_interest = future_value - initial_investment

# 3. Print the formatted results
# An f-string is used to format the output.
# The ':.2f' part tells Python to format the number as a float with exactly two decimal places.
print(f"The earned interest is {earned_interest:.2f}.")
print(f"The terminal value amounts to {future_value:.2f}.")
