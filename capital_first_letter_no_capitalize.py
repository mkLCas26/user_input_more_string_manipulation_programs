# B6 Prog09. Capitalize the first letter of string and lowercase the rest
# Don't use capitalize()

"""
PSEUDOCODE

define dictionary to make lowercase letters to upper
user input
make capitalization applicable to first word first letter only
make the rest lowercase
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
final = ""

for key, letter in enumerate(user):
    if key == 0 and letter in to_upper:
        final += to_upper[letter]
    else: 
        final += letter.lower()
    
print(final)
    
# for x in words[0]:
#     if x in to_upper:
#         final += to_upper[x]
#         words[0][1:].lower
        
        
# print(final)