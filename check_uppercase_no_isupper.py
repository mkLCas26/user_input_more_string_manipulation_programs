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
    if x in upper or x == " ":
        result = True
    elif x.isalnum(): 
        result = False
        break
    else:
        result = False
        break

print(f"The string is in capital letters? {result}")