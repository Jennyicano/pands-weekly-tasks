# Week07 task

# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author Jennifer Ibanez Cano

#!/usr/bin/python3.1

# import modules used here -- sys is a very standard one
import sys

# Gather the code in a main() function
def main():
   openfile(sys.argv[1])
     
# Command line args are in sys.argv[1], sys.argv[2] ..
# sys.argv[0] is the script name itself and can be ignored

# Error that can be happening: the filename cannot be found, wrong typing name, wrong filename

def openfile(filename):
    # Here the program will read the file and then return the number of 'e' in the text.
    try:
        file = open(filename, "r")
        text = file.read()
        file.close()
    except:
       print("The file cannot be found")
    else:
      print("The number of e's in the text file is", text.count('e'))
     
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()