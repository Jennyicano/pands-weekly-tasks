# Week02 task
# Author Jennifer Ibanez


amount1 = input ("Enter amount1(in cent): ")
# we must convert the string that input returns to an int
amount1 = int(amount1)

# print (type(amount1)) 
amount2 = input ("Enter amount2(in cent): ")
amount2 = int(amount2)
# Divide by 100.0 or else it won't convert to float properly
sum = (amount1 + amount2)/100.0

print ("The sum of these is €", sum)

