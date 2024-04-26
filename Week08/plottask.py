# Week08 task

# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author Jennifer Ibanez Cano

import numpy as np

from numpy.random import seed
from numpy.random import normal
from numpy.random import randint

# #make this example reproducible, I give a number to the seed to fix the randomness. So everytime this is executed the random n umbers will be the same. 
# seed(4654)

# generate sample of 1000 values that follow a normal distribution with mean 5 and s.d. 2

nd = normal(loc=5, scale=2, size=1000)

'''
# See the first numbers of the randomly generated distribution
# Using seed we will get every time the same numbers
print(nd[:5])
#check mean of distribution
print( nd.mean())
# Min value
print(min(nd))
# Max value
print(max(nd))
# print a random integer number
print("random integer number", randint(100))
# Import statistics Library
import statistics
# Calculate middle values
print(statistics.median(nd))
'''

import matplotlib.pyplot as plt

#count, bins, ignored = plt.hist(nd, 300)
#plt.show()
count, bins, ignored = plt.hist(nd)
plt.show()

# Second part:

# Define a Function
def h(x):
    return x ** 3

# Create x and y Ranges
x = np.linspace(0, 10, 1000)
# print(x[0:10])
y = h(x)

# Plot the Data

plt.plot(x, y, label = r'$h(x) = x^3$')
plt.legend(loc="upper left")
plt.title('Function')
plt.show()