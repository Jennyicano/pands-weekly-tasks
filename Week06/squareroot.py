# Write a program that takes a positive floating-point number as input 
# and outputs an approximation of its square root.

# Author Jennifer Ibanez Cano

# example square root of 5 = 2.2360679775 from Google
# 2.236067977499978 

# First I'll define the function

def sqrt(n) :
 
    # Tolerance level using Newton's method
    # I use a fix number 0.0001
    # The smaller the tolerance level the preciser the result
    l = 0.000000001
    
    # I create the variable  y .
    # In the first round it will store the number I want 
    # to calculate the root square of  
    y = n 
    
    # With the variable count I will print the number of rounds 
    # it goes throug the loop during testing phase 
    count = 0
 
    while (1) :
        count += 1
        # Printing count during testing
        # If l is smaller the function will go through more rounds
        print("count", count)

        # Calculate the assumed root during this round.
        root = 0.5 * (y + (n / y)) 
        print("root", root)
        
        print("difference", abs(root - y))
        # Check if assumption is good enough 
        # giving the tolerance level that I chose
        # abs --> |-5| =5   |5| = 5 
        # the while loop will finish if it's good enough.
        if (abs(root - y) < l) :
            break
 
        # Update y value for next round's calculation 
        y = root
 
    return root 

# The program will ask for a positive number from the user.
# The input returns a string. 
# I store the value in a variable number as a float. 

number = float(input("Please enter a positive number: "))

# print(type(number))

result = sqrt(number)
result = round(result, 1)
    # I'll use round to get only 1 decimal in the result


print("The square root of ",number," is approx. ",result,".",sep='')


# Result of square 5 
# with l = 0.0001
# Please enter a positive number: 5
# count 1
# root 3.0
# difference 2.0
# count 2
# root 2.3333333333333335
# difference 0.6666666666666665
# count 3
# root 2.238095238095238
# difference 0.09523809523809534
# count 4
# root 2.2360688956433634
# difference 0.0020263424518747186
# count 5
# root 2.236067977499978
# difference 9.18143385320036e-07
# The square root of 5.0 is approx. 2.2.

# with l = 0.000000001 
# tolerance is lower so we go through an extra round of loop.
# Please enter a positive number: 5
# count 1
# root 3.0
# difference 2.0
# count 2
# root 2.3333333333333335
# difference 0.6666666666666665
# count 3
# root 2.238095238095238
# difference 0.09523809523809534
# count 4
# root 2.2360688956433634
# difference 0.0020263424518747186
# count 5
# root 2.236067977499978
# difference 9.18143385320036e-07
# count 6
# root 2.23606797749979
# difference 1.8829382497642655e-13
# The square root of 5.0 is approx. 2.2.