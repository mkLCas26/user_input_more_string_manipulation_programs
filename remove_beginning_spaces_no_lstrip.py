# B6 Prog01: Remove spaces at the beginning w/o using lstrip()

"""
PSEUDOCODE

user input
use for loop to eliminate space
print output
"""

user = input("Enter word/s: ")

for x in user:
    if x == " ":
        continue
    else:
        print(user[x:])