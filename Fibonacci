# David Sheils - HDip in Data Analytics - Feb 2008
# A program that displays Fibonacci numbers using people's names - second version

# Discussion Forum comments for topic 1 
 
#My name is David, so the fist and last letters of my name (d + d = 4 + 4) give 8.
#Fibonacci number 8 is 21.


# The following is the Python Script for exercise 2.
#
# My observations on the ord() function are give by way of comments in the body of the code itself
# where it assigns to the variables first and last the unicode number of the first and last letters respectively
# of the string name.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

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
