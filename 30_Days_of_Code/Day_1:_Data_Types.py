# Objective
# Today, we're discussing data types. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

# Declare  variables: one of type int, one of type double, and one of type String.
# Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the  operator to perform the following operations:
# Print the sum of  plus your int variable on a new line.
# Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# Concatenate  with the string you read as input and print the result on a new line.

# Input Format

# The first line contains an integer that you must sum with .
# The second line contains a double that you must sum with .
# The third line contains a string that you must concatenate with .

# Output Format

# Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, and then the two concatenated strings on the third line.

#Sample Input

# 12
# 4.0
# is the best place to learn and practice coding!

# Sample Output

# 16
# 8.0
# HackerRank is the best place to learn and practice coding!
# _______________________________________________________________________________________________________________________________________________________
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.
my_int = int(input())
my_float = float(input())
my_string = input()

# Print the sum of both integer variables on a new line.
print (i + my_int)
# Print the sum of the double variables on a new line.
print("{:.1f}".format(d + my_float))
# Concatenate and print the String variables on a new line
print (s + my_string)
# The 's' variable above should be printed first.
