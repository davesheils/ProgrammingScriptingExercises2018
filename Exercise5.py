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
        sepalLength = line.split(',')[0]
        sepalWidth = line.split(',')[1]
        petalLength = line.split(',')[2]
        petalWidth = line.split(',')[3]
        # The following works, because all data is in the format 1.1.
        print(sepalLength," ",sepalWidth," ",petalLength," ",petalWidth)
        # print('{0:2d} {1:3d} {2:4d}'.format(sepalLengthf,sepalWidth,petalLength)) this only works with numerical values

# Also, getting the following error:
# Traceback (most recent call last):
# File "exercise5.py", line 22, in <module>
#    sepalWidth = line.split(',')[1]
# IndexError: list index out of range
# 
# Looks like I need to tell the program that we have reached the end of file.
# Not sure why this should be the case
# Might need to review the video .. I may not have been paying attention ...
#         