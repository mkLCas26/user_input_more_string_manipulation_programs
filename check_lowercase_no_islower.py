# B7 Prog04. Check if characs are in lower case w/o islower()

"""
PSEUDOCODE

user input and initialize needed variables
check if characs are in lower case
print
"""

lower = "abcdefghijklmnop"
result = ""
user = input("Enter word/s: ")


for letter in user:
    if letter in lower or letter == " ":
        result = True
    elif letter.isalnum():
        result = False
    else: 
        result = False

print(f"The string is in lowercase? {result}")