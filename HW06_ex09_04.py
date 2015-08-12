#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body

#1

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
        else:
            return True

##############################################################################
def main():
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if uses_only(word, 'acefhlo'):
                print word

if __name__ == '__main__':
    main()
