# B6 Prog02. Remove characs at the beginning of a string
# w/o removeprefix(), replicate its function

"""
PSEUDOCODE

user input
ask for a charac to be removed 
use if statement and .startswith() func
print output
"""

user = input("Enter word/s: ")
rem = input("Characters you want to remove: ")

if user.startswith(rem):
    remlength = len(rem)
    user = user[remlength:]
    print(user)
