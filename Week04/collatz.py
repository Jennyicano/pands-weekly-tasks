# Week04 task

# This program asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author Jennifer Ibanez Cano

number = int(input("Please enter a positive integer: "))

while number > 1:
    print(number, end=' ')
    # The number is even, divide it by two.
    if number % 2 == 0:  
        number = int(number / 2)
    # The number is odd, multiply it by three and add one.
    else:
        number = number * 3 + 1        
else: # final number is 1, loop has ended, we'll print the last number.
    print(number, end=' ')