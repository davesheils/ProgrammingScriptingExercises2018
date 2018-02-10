# Collatz Conjecture - code to generate sequence, stopping at 1
# David Sheils - Higher Diploma in Computing (Data Analytics) February 2018

# background: https://en.wikipedia.org/wiki/Collatz_conjecture


# Methodology:
# take a number n (either assigned to a variable in the body of the code or by user input)
# perform the folowing operation
# if n is even, i.e if the remainder (modulus) of n divided by 2 is 0,
# then n = n/2
# Otherwise, n = 3n +1
# repeat this operation on n until n = 1, printing n

n = int(input("Please enter an integer: "))

while n > 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = (3 * n) + 1
    print(int(n))


# end
