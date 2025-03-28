# B6 Prog07. Add space in the end at beginning 
# To center string input w/o using center()

"""
PSEUDOCODE

user input 
ask user how long do they want the string to be
print output
"""

left = 0
right = 0 
user = input("Enter word/s: ")
width = int(input("How long do you want the string to be? "))

if len(user) < width:
    width -= len(user)
    left = width // 2
    right = width - left

print(f"'{' ' * left}{user}{' ' * right}'")