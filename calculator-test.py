from arithmetic import *

while True:
    input_string = input('')
    tokens = input_string.split(" ")

    if 'q' in tokens:
        print("See you later")
        break

    nums1 = int(tokens[1])
    if len(tokens) < 3:
        nums2 = '0'
    else:
        nums2 = int(tokens[2])

    if tokens[0] == '+':
        result = add(nums1, nums2)
    elif tokens[0] == '-':
        result = subtract(nums1, nums2)
    elif tokens[0] == '*':
        result = multiply(nums1, nums2)
    elif tokens[0] == '/':
        result = divide(nums1, nums2)
    elif tokens[0] == 'square':
        result = square(nums1)
    elif tokens[0] == 'cube':
        result = cube(nums1)
    elif tokens[0] == 'power':
        result = power(nums1, nums2)
    elif tokens[0] == 'mod' or tokens[0] == '%':
        result = mod(nums1, nums2)
    print (result)