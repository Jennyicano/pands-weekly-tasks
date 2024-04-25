# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author Jennifer Ibanez Cano

# The file is in the same folder as the program. 

filename= "moby-dick.txt"

with open(filename, 'r') as f:
    for data in f:
        print(data.strip() )


# The program gives an error: 
# FileNotFoundError: [Errno 2] No such file or directory: 'moby-dick.txt'
# As the file is in the same folder as the program it gives an error, 
# so I moved the file outside of the folder Week07. 

# For the command line arguments I'll need to import sys argv

import sys
filename = sys.argv[0]

def letternumber(filename, letter):
    file = open(filename, "r")
    # Here the program will read the file and then return the number of 'e' in the text.
    text = file.read()
    return text.count(letter)

print("The number of 'e' in the text is", letternumber('moby-dick.txt', 'e'))

