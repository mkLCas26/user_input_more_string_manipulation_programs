# B6 Prog06. Add space at the end to satisfy the length in parameter
# Don't use ljust()

"""
PSEUDOCODE

user input
ask length wanted by the user
print string
"""

user = input("Enter word/s: ")
width = int(input("How long do you want the string to be? "))

if len(user) < width:
    width -= len(user)
    user += " " * width

print(f"Result: '{user}'")