"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
def calculator_add ():
    while True:
        input_string = input('')
        tokens = input_string.split(" ")
        if tokens[0] == "q":
            return
        def plus_function():
            if tokens[0] == '+':
                result = add(int(tokens[1]), int(tokens[2]))
                print(result)
        return plus_function()

calculator_add()





