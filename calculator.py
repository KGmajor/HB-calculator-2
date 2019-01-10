"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
def calculator ():
    def plus_function():
        result = add(int(tokens[1]), int(tokens[2]))
        print(result)
    def subtraction_function():
        result = subtract(int(tokens[1]), int(tokens[2]))
        print(result)

    while True:
        input_string = input('')
        tokens = input_string.split(" ")
        if tokens[0] == "q":
            return
        elif tokens[0] == '+':
            plus_function()
        elif tokens[0] == '-':
            subtraction_function()
        
calculator ()





