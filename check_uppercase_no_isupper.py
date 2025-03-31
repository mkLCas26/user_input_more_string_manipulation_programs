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

for letter in user:
    if letter in upper or letter == " ":
        result = True
    elif not letter.isalpha(): 
        continue
    else:
        result = False
        break

print(f"The string is in capital letters? {result}")