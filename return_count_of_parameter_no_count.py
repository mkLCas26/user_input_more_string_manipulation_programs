# B7 Prog08. Return how many times a function parameter appear 
# in the string. Don't use count()

"""
PSEUDOCODE

user input
ask the word/s user wants to count
determining the count of the parameter
print count
"""

user = input("Enter word/s: ").split()
parameter = input("\nCharacter/word to count in your input: ")
store = []

for word in user:
    if word == parameter:
        store.append(parameter)
    else:
        continue

print(len(store))