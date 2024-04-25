# Week03 task

# This program will read a 10 character account number and 
# it'll output the account number with only the last 4 digits showing, 
# the first 6 digits will be replaced with Xs.

# Author Jennifer Ibanez

amount1 = input ("Please enter a 10 digit account number: ")
print(type(amount1))

res = str(amount1)
print(type(res))
# we take only the four last digits
# This will work for any lenght of account number, even if it-s shorter than 4
res2 = res[-4:]
# We concatenate 6 X with the last 4 numbers that will be displayed
result = "XXXXXXX" + res2
# We print the hidden account number, showing only the four last digits
print(result)
