# B7 Prog07. Add 0 at the beginning of string to satisfy no. of characs
# Don't use zfill()

"""
PSEUDOCODE

user input
ask for length of string
if statement to add zeros
print
"""

user = input("Enter number/s: ")
width = int(input("How long do you want the string to be? "))

if len(user) < width:
    width -= len(user)
    user = ("0" * width) + user
    
print(f"Result: '{user}'")