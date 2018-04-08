# Exercise 5

# Please complete the following exercise this week. 
# Write a Python script that reads the Iris data set in and 
# prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, petal width, 
# sepal length and sepal width, and these values  should have the 
# decimal places aligned, with a space between the columns.



# Source data:
# 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# 
# saved as data\iris.csv


with open('data/iris.csv') as f:
    for line in f:
        # The following lines correct a recurring error occurring in
        # earlier versions of this script - comments below        
        line = f.readline()
        if not line:
            break 
        sepalLength = line.split(',')[0]
        sepalWidth = line.split(',')[1]
        petalLength = line.split(',')[2]
        petalWidth = line.split(',')[3]
        print("{} {} {} {}".format(sepalLength,sepalWidth,petalLength,petalWidth))




# earlier (since overwritten) attempts at this exercise worked, but 
# produced the following error:
# Traceback (most recent call last):
# File "exercise5.py", line 22, in <module>
#    sepalWidth = line.split(',')[1]
# IndexError: list index out of range
# 
# The final version adds a test to see if there is an line, and exits otherwise.
#         
