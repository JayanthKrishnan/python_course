import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and 10 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You Win"
    elif computer_score > 21:
        return "Computer went over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


def play_game():
    print(logo)
    is_game_over = False
    while not is_game_over:
        user_score = calculate_scores(user_card)
        computer_score = calculate_scores(computer_card)

        print(f"Your cards :{user_card} Your Score : {user_score}")
        print(f"Computer first card : {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            response = input("Type 'y' to get another card or type 'n' to pass: ")
            if response == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_scores(computer_card)

    print(f" Your final deck: {user_card}, final score: {user_score}")
    print(f" Computer's final deck: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

play_game()
