import random
import os
clear = lambda: os.system('cls')
clear()
def deal_card():
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_cards = random.choice(card)
    return random_cards
def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)
def compare_cards(user_score, customer_score):
    if user_score == customer_score:
        return "It's a Draw"
    elif customer_score == 0:
        return "You lost, the opponent has a blackjack"
    elif user_score == 0:
        return "You won with a blackjack"
    elif user_score > 21:
        return "You went over, you lose!"
    elif customer_score > 21:
        return "The opponent went over, you win!"
    elif user_score > customer_score:
        return "You win!"
    else:
        return "You lose!"
def card_game():
    is_game = False
    user_card = []
    customer_card = []
    for i in range(2):
        user_card.append(deal_card())
        customer_card.append(deal_card())
    while not is_game:
        user_score = calculate_score(user_card)
        customer_score = calculate_score(customer_card)
        print(f"{user_card} : {user_score}")
        print(f"Computer's first card : {customer_card[0]}")
        if user_score == 0 or customer_score == 0 or user_score > 21:
            is_game = True
        else:
            do_continue = input("Do you want to to deal another card, type 'y' for yes and 'n' for no: ")
            if do_continue == 'y':
                user_card.append(deal_card())
            else:
                is_game = True 
        while customer_score != 0 and customer_score < 17 :
            customer_card.append(deal_card())
            customer_score = calculate_score(customer_card)
    print(f"The customer's hand {customer_card} : {customer_score}")
    print(compare_cards(user_score, customer_score))
while input("Do you want to play the Blackjack game, type 'y' for yes and 'n' for no: ") == 'y':
    clear()
    card_game()

    
