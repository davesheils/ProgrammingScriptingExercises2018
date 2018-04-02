# Exercise 1 and 2, PROGRAMMING AND SCRIPTING 


# A program that displays Fibonacci numbers using people's names.


# Exercise 1:
# My name is David, so the fist and last letters of my name (d + d = 4 + 4) give 8.
# Fibonacci number 8 is 21.

# Exercise 2

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# I have added my understanding of how the program works by way of comments within the code itself:

name = "Sheils" # assigns the string to variable name
first = name[0] # first letter of the string name
last = name[-1] # last letter of the string name
firstno = ord(first) # assigns to firstno the Unicode number of the first letter of name
lastno = ord(last) # assigns  the Unicode number of the first letter of name
x = firstno + lastno # assigns to x the sum of firstno and lastno (i.e the sum of the unicode numbers for the first and last letters of the name)

ans = fib(x) # calls function fib on x (see above function definition)

print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


# Output of program:

# My surname is Sheils
# The first letter S is number 83
# The last letter s is number 115
# Fibonacci number 198 is 107168651819712326877926895128666735145224

# I have added my understanding of how the program works by way of comments within the code itself:


