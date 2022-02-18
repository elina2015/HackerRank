# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. 
# For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for name is not found, print 'Not found' instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.
import sys

# Let's convert the input to the phone book
n = int(input())
phone_book = {}
for i in range (n):
    contact = input().split(' ')
    phone_book[contact[0]] = contact[1]
# Let's check the input and check if it's in the phone book
words = sys.stdin.readlines()
for word in words:
    name = word.strip()
    if name in phone_book:
        print(name + '=' + str(phone_book[name]))
    else:
        print('Not found')
