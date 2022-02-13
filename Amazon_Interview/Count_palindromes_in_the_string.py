# Task: for given string count the words-palindromes and output the palindromes and their counters together

import string

def Finding(text):
  # Let's remove the punctuation characters at first
    for character in string.punctuation:
        text = text.replace(character, ' ')
  # Let's split the string to the words and create a new list from them
    arr = text.split()
    result = []
  # Let's check if the word in the list is a palindrome and collect them all in a new list
    for i in range (0, len(arr)):
        word = arr[i]
        if word == word[::-1]:
            result.append(word) 
        else:
            pass
    # Let's create a new list with counters of all palindromes
    counter = [result.count(k) for k in result]
    # Let's zip the list of palindromes with the list of counters to the dictionary 'final_result
    final_result = dict(zip(result, counter))
    print(final_result)
   #Let's test our code with a test text
Finding('mom dad went out one day mamam mom dad')
