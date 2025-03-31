# B7 Prog05. Check if string begins with characs with given parameter
# Don't use startswith()

"""
PSEUDOCODE

user input
ask for characs that user wants to check in the beginning
check if characs are at the beginning
print True or False
"""

user = input("Enter word/s: ")
checker = input("Character/s you would like to check at the beginning of your input: ")
result = "" 

if user[:len(checker)] == checker:
    result = True
    print(f"Does it start with {checker}? {result}")
else: 
    result = False
    print(f"Does it start with {checker}? {result}")