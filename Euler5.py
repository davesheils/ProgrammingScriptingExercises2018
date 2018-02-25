# David Sheils
# HDip in Data Analytics

# Exercise 4 (version 1)

# Please complete the following exercise this week. It is problem 5 from Project Euler. 
# The problem is as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. 

# Add your answer to your GitHub repository.

# Original problem: https://projecteuler.net/problem=5


# The version below works, but looks a bit "brute force". If time allows, and I can think of a more elegant method, I will upload another version.

# Method:
# Tests number 20 to see if it is divisible by numbers 1 to 20 inclusive. If any of these operations retursn a modulus other than zero
# the alldivisible flag is reset to False. This means that the variable num is not evenly divisible by all nums 1 - 20
# num is increased by 20
# operation is repeated for all multiples of 20 until:
# alldivisible is still true after num % i = 0 for all i = 1 - 20

# inelegant, but works!

num = 20
alldivisible = False 

while alldivisible == False:
    alldivisible = True
    for i in range(1,21):
        if num % i != 0:
            alldivisible = False
            num = num + 20

print(num)

# ends    

# at 21:11:14 22 Feb 2018

# Result: 232792560

# Congratulations, the answer you gave to problem 5 is correct.

# You are the 384504th person to have solved this problem.

# This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%

# https://projecteuler.net/problem=5