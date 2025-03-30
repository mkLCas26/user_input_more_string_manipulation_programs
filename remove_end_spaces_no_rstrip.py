# B7 Prog01. Remove space in the end of string w/o rstrip()

"""
PSEUDOCODE

user input
loop to remove spaces in the end
print output
"""

index = 0
user = input("Enter word/s: ")

for x in user:
    if x == " ":
        index -= 1
    else:
        break

print(f"'{user[0:index]}'")
        
    