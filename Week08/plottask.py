# Week08 task

# Write a program that displays a histogram of a normal distribution of a 1000 values 
# with a mean of 5 and standard deviation of 2.
# The program will also displays a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
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

#count, bins, ignored = plt.hist(nd, 1000)
#plt.show()
count, bins, ignored = plt.hist(nd)

plt.title("Histogram", color="green")
plt.show()

    # We will need to close this plot to can see the next one. 

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
plt.title('Function', color="green")
plt.show()
