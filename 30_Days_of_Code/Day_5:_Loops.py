# Task
# Given an integer n, print its first 10 multiples. 
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for i in range (1,11):
    print('{} x {} = {}'.format(n, i, (n*i)))
