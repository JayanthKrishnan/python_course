# Love Score Calculator
nameOne = input("Enter the name of Person 1 :\n")
nameTwo = input("Enter the name of Person 2 :\n")

name = nameTwo + nameOne

names = name.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) and (love_score > 90):
    print(f"Your love score is {love_score}. Your two are like mentos and coke.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your love score is {love_score}. Your alright together.")
else:
    print(f"Your love score is {love_score}.")
