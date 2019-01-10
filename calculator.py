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
    def multiply_function():
        result = multiply(int(tokens[1]), int(tokens[2]))
        print(result)
    def divide_function():
        result = divide(int(tokens[1]), int(tokens[2]))
        print(result)
    def square_function():
        result = square(int(tokens[1]))
        print(result)
    def cube_function():
        result = cube(int(tokens[1]))
        print(result)
    def power_function():
        result = power(int(tokens[1]), int(tokens[2]))
        print(result)
    def mod_function():
        result = mod(int(tokens[1]), int(tokens[2]))
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
        elif tokens[0] == '*':
            multiply_function()
        elif tokens[0] == '/':
            divide_function()
        elif tokens[0] == 'square':
            square_function()
        elif tokens[0] == 'cube':
            cube_function()
        elif tokens[0] == 'power':
            power_function()
        elif tokens[0] == 'mod' or tokens[0] == '%':
            mod_function()    
        
calculator ()





