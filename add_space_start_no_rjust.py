# B7 Prog06. Add space at the beginning of string to satisfy 
# required no. of characs. Don't use rjust()

"""
PSEUDOCODE 

user input
ask length of string preferred by the u
if statement for adding spaces to reach length 
print 
"""

user = input("Enter word/s: ")
width = int(input("How long do you want the string to be? "))

if len(user) < width:
    width -= len(user)
    user = (" " * width) + user

print(f"Result: '{user}'")
