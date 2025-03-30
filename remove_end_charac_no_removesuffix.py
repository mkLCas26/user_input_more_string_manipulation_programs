# B7 Prog02. Remove characs at the end of string w/o removesuffix()

"""
PSEUDOCODE

user input 
ask charac/s that needs to be removed
if statement for removing characs
print 
"""

user = input("Enter word/s: ")
remove = input("Characters you want to remove at the end: ")

if user.endswith(remove):
    remlength = len(remove)
    user = user[:remlength]
    print(f"'{user}'")
else:
    print(f"ERROR!'{remove}' can't be found at the end of your string.")