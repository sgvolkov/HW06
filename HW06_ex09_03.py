#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################

# 1

def avoids(word,forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    else:
        return True

# 2

def no_forbidden(fin):
    forbidden = raw_input('Enter a string of forbidden letters: ')
    count = 0
    for word in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count += 1
    return count

#3

from collections import Counter
with open('words.txt', 'r') as fin:
    c = Counter()
    for x in fin:
        c += Counter(x.strip())
print c
# I got as far as finding the 5 lowest numbers, but I'm not sure how to do this
# all within a function :/
        

##############################################################################
def main():
    fin = open('words.txt', 'r')
    print no_forbidden(fin)
    print "Percentage avoided: ", (float(avoided)/words_count)*100

if __name__ == '__main__':
    main()
