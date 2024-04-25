# Week05 task

# This program will outputs whether or not today is a weekday.

# Author Jennifer Ibanez Cano 

# I'll import the datetime package. Python’s built-in datetime library 
# is one of the most common modules to manipulate date and time object data. 
from datetime import datetime

# datetime.today stores the today's date 
# .weekday() will return an integer with the day of the week:
# 0 = Mon, 1 = Tue, 2 = Wed, 3 = Thur, 4 = Fri, 5 = Sat, 6 = Sun

if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
    print("It is the weekend, yay!")

else:
    print("Yes, unfortunately today is a weekday")