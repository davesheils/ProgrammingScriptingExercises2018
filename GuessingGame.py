# David sheils

# 12 Feb 2018

# Guessing game in Python

# so.. python generates random number between 1 and 10 

# requets the user to guess the number (as an integer)

# if input is correct, prints " well done," and exits

# so long as input isnot equal to teh random number ...

# if guess > random, " too high"

# if guess < random, " too low"


import random # imports module to generate random numbers

x = random.randint(1,10) # assigns to x a randomly generated number
# from 1 to 10

n = int(input("Please enter an integer: "))

while n != x: # i.e. while the number guessed is wrong!
    if n > x:
        print("Too high!!!")
    if n < x:
        print("Too low!!!")
    print("have another go!")
    n = int(input("Please enter an integer: "))

print("well done!!!")
        
 
