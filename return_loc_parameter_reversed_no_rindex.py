# B7 Prog10. Return first loc of fun parameter in string 
# starting from last charac
# Don't use rindex()

"""
PSEUDOCODE

user input
ask for word/charac that user want the location of
find parameter's loc in string that is reversed
print index
"""

user = input("Enter word/s: ")
parameter = input("Character/word to know the index in your input: ")

for letter in range(len(user) - len(parameter) + 1, -1, -1):
    if user[letter: letter + len(parameter)] == parameter:
        print(f"Index is: {letter}")
        break