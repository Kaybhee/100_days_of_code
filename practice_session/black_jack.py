
def deal_card():
    import random
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_cards = random.choice(card)
    return random_cards
def calculate_score(card):
    if sum(card) == 21 and len(card)                                                                                                                     == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)
def compare_cards(user_score, customer_score):
    if user_score == customer_score:
        return "It's a draw!"
    elif user_score > 21:
        return "You went over 21, you lost!"
    elif user_score == 0:
        return "You won with a blackjack!"
    elif customer_score == 0:
        return "Your opponent won with a blackjack!"
    elif customer_score > user_score:
        return "Your opponent won!"
    else:
        return "You win!"
is_game = False   
user_card = []
customer_card = []
for i  in range(2):
    user_card.append(deal_card())
    customer_card.append(deal_card())
    while user_card == 21:
        do_continue = input("Do you want to deal another card? type 'y' for yes and 'n' for no: ")
        if do_continue == 'y':
            user_card.append(deal_card())
        else:
            is_game = True
    

print(calculate_score(user_card))
print(calculate_score(customer_card))