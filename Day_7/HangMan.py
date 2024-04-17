import random
from HangManWordsAndStages import words,logo,stages

random_word = random.choice(words)
len_word = len(random_word)
display = []

print(logo)

for i in range(len_word):
    display += "_"
print(f'{" ".join(display)}')

chances = 6

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You Have Already Guessed {guess}')
        continue

    for i in range(len_word):
        letter = random_word[i]
        if guess == letter:
            display[i] = guess
    if guess not in random_word:
        chances -= 1
        print(f'Your Guess Is Wrong. You Lose a Life!')
        print(stages[chances])
        if chances == 0:
            game_over = True
            print("You Lose!")
            print(f'The Word is {random_word}')
    print(f'{" ".join(display)}')
    if "_" not in display:
        print("You Win!")
        game_over = True

