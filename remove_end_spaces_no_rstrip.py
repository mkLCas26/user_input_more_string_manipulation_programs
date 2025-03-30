# B7 Prog01. Remove space in the end of string w/o rstrip()

"""
PSEUDOCODE

user input
loop to remove spaces in the end
print output
"""


user = input("Enter word/s: ")
index = 0

for x in user[::-1]:
    if x == " ":
        index -= 1
    else:
        break

print(f"'{user[0:index]}'")
        
    