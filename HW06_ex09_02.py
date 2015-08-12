#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# 1

def has_no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True

##############################################################################
def main():
    total = 0
    count = 0
    word = open('words.txt')
    for line in word:
        total += 1
        word = line.strip()
        if has_no_e(word):
            count += 1
    percentage = (float(count)/total)*100
    print "Percentage of no e words: %.2f" %(percentage)

if __name__ == '__main__':
    main()
