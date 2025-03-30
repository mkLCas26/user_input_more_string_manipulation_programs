# B7 Prog03. Convert string characs into uppercase w/0 upper()

"""
PSEUDOCODE

dictionary for alphabets
user input and initialize needed variables
loop to check if characs are in uppercase
    convert if in lowercase
print
"""

to_upper = {
     "a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F",
     "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L",
     "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R",
     "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X",
     "y": "Y", "z": "Z"
}

user = input("Enter word/s: ")
upper = ""

for letter in user:
    if letter in to_upper:
        upper += to_upper[letter]
    else:
        upper += letter

print(upper)