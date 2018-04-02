# Please complete the following exercise this week. Write a Python script containing a function called factorial() 
# that takes a single input/argument (x) which is a positive integer and returns its factorial. 
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with the values 5, 7, and 10.

# First define function factorial(x) returning factorial of input x

def factorial(x):
    result = x
    for a in range(x-1,1,-1): 
        result = result * a
    return result

# Test for numbers 5,7,10

for x in (5,7,10):
    print(f"{x}! = ",factorial(x))


# Results checked using scientifict calculator factorial function