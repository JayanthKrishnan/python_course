import random

names = input("Enter the names : ").split(", ")
len_ = len(names)
random_num = random.randint(1, len_ - 1)                   # we can also use choice method to pick a name from the list
print(f"**{names[random_num]} will be paying the bill**")
