import random

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

num_alp = int(input("Enter the number of alphabets you want : "))
num_num = int(input("Enter the number of numbers you want : "))
num_char = int(input("Enter the number of characters you want : "))

password_lst = []

for i in range(0, num_alp):
    password_lst.append(random.choice(alp))

for i in range(0, num_num):
    password_lst.append(random.choice(num))

for i in range(0, num_char):
    password_lst.append(random.choice(char))

random.shuffle(password_lst)

password = ""
for i in password_lst:
    password += i

print(f"Your Password is : {password}")

