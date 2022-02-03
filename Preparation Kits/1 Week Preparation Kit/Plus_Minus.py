""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros """

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
        
def plusMinus(arr):
    # Write your code here
    neg_sum = 0
    zero_sum = 0
    plus_sum = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            plus_sum +=1
        elif i < 0:
            neg_sum +=1
        elif i == 0:
            zero_sum += 1
    print("{:.6f}".format(plus_sum/n))        
    print("{:.6f}".format(neg_sum/n))
    print("{:.6f}".format(zero_sum/n))

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

