# B6 Prog05. Check if string's end matches given parameter w/o endswith()
 
"""
PSEUDOCODE

user input
ask for parameter to check
print true or false
"""

user = input("Enter word/s: ")
checker = input("Character you would like to check at the end of the input: ")
result = ""

if user[-len(checker):] == checker:
    result = True
    print(f"Does it end with {checker}? {result}")
else: 
    result = False
    print(f"Does it end with {checker}? {result}")