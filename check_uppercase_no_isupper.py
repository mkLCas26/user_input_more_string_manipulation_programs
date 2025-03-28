# B6 Prog04. Check if string characs are uppercase w/o isupper() func

"""
PSEUDOCODE

user input
for loop for checking if charac is uppercase
print true or false
"""

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

user = input("Enter word/s: ")

for x in user:
    if x in upper:
        result = True
    else:
        result = False
        break

print(result)