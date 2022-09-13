#000 = 0 001 = 1 010 = 2 011 = 3 100 = 4 101 = 5 110 = 6 111 = 7

#Binary is base 2 and has 2 digits 0 and 1
#Decimal is similar, but base 10 and has 10 digits 0-9 1 = 1 * 10^0
#This ends up being 1 * 1, the next place over
# 20 = 0 * 1 in the first spot, and then 2 * 10^1 in the second spot which is 2 * 10 or 20

#ASCII American Standard Code for Information Interchange is a standard for encoding characters as numbers
# A is 65, B is 66, C is 67, etc. 0 is 48, 1 is 49, 2 is 50, etc.
#Byte is 8 bits, so 8 digits of 0 or 1 01001000 is 72 in decimal which is H in ASCII
# 01001001 is 73 which is I in ASCII so 01001000 01001001 is HI in ASCII

#Searching through a phone book
# 1. Start in the middle
# 2. If the name is before the middle, search the first half
# 3. If the name is after the middle, search the second half
# 4. If the name is the middle, you found it
# 5. If you can't find it, it's not there
# This is called a binary search
# This is O(log n) time complexity
# This is O(1) space complexity
# This is a divide and conquer algorithm
# This is a recursive algorithm
# You could pseudocode it out like this
# Pick up the phone book
# Open to middle of phone book
# Look at page
# If person is on page
#  Call person
# Else if person is earlier in book
#    Open to middle of left half of book
#    Go back to line 3
# Else if person is later in book
#    Open to middle of right half of book
#   Go back to line 3
