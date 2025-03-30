# B6 Prog10. Make the first letter of every word capital
# Don't use title()

"""
PSEUDOCODE 

dictionary for uppercase
user input
make first letter of every word into capital letters
print output
"""


to_upper = {
     "a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F",
     "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L",
     "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R",
     "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X",
     "y": "Y", "z": "Z"
}

user = input("Enter word/s: ")
title_case = ""

for key, letter in enumerate(user):
     if key == 0 or user[key - 1] == " ":
          title_case += to_upper.get(letter, letter)
     elif letter == " ":
          title_case += letter
     else:
          title_case += letter.lower()
          
print(title_case)