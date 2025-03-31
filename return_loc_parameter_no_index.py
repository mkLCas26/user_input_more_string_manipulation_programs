# B7 Prog09. Return first loc of func parameter in string
# Don't use index()

"""
PSEUDOCODE

user input
ask for word/charac that user want the location of
find parameter's loc
print index
"""
user = input("Enter word/s: ")
parameter = input("Character/word to know the index in your input: ")

for letter in range(len(user) - len(parameter) + 1):
    if user[letter: letter + len(parameter)] == parameter:
        print(f"Index is: {letter}")
        break