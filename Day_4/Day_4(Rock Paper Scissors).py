import random

print("\n***Welcome to Rock Paper Scissors Game***\n")
userChoice = int(input("Enter your choice :\n"))

computerChoice = random.randint(0, 2)

emojis = ["✊", "✋", "✌️"]

if userChoice <= 2:
    print(f"Your Choice :\n{emojis[userChoice]}\n")
    print(f"Computer Choice :\n{emojis[computerChoice]}\n")
    if userChoice == computerChoice:
        print("It's a Draw")
    elif userChoice == 0:
        if computerChoice == 2:
            print("You Win!")
        elif computerChoice == 1:
            print("You Lose!")
    elif userChoice == 1:
        if computerChoice == 0:
            print("You Win!")
        elif computerChoice == 2:
            print("You Lose!")
    elif userChoice == 2:
        if computerChoice == 1:
            print("You Win!")
        elif computerChoice == 0:
            print("You Lose!")
else:
    print("Wrong Number. You Lose!")
