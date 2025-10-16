
length = int(input('Enter the length of the rectangle: '))
rec_area = int(input('Enter a the Area of the rectangle: '))
try: width = rec_area / length
except ZeroDivisionError:
        print("Error: Length cannot be 0")

        raise
print(width)

amount = int(input('Enter a Priciple Amount: '))
goal = int(input('Enter Investment Goal: '))
interest = int(input('Enter Annual Compounding % Rate: '))
years = int(input('How long do you plan to invest in years: '))
while amount < goal:
    years += 1
    amount = amount * (1 + interest)

print(f"you'll reach your investment goal after {years} years")

#### task ####
import random
random_number = random.randint(1, 100)
try:
    guess = int(input('Enter a random Number upto 100: '))
    if guess == 58:
        print("you guessed it right")
    else:
        print("you suck at guessing, try again!")
except ValueError:
    print("Please enter an integer next time.")




