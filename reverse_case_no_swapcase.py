# B6 Prog08. Reverse the casing of each string charac w/o swapcase()

"""
PSEUDOCODE

define dictionaries for upper to lower, lower to upper
user input
swapcases of input
print output
"""

to_lower = {
    "A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f",
    "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l",
    "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
    "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x",
    "Y": "y", "Z": "z"
}

user = input("Enter word/s: ")
to_upper = {}
swap = ""

for key, value in to_lower.items():
    to_upper[value] = key

for letter in user:
    if letter in to_lower:
        swap += to_lower[letter]
    elif letter in to_upper:
        swap += to_upper[letter]
    else:
        swap += letter                    # for spaces and other unique characters
        
print(swap)