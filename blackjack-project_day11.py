import random
def deal_card():
    card = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
    randomcards = random.choice(card)
    return randomcards
def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)
is_game = False
user_card = []
customer_card = []
for i in range(2):
    user_card.append(deal_card())
    customer_card.append(deal_card())
user_score = calculate_score(user_card)
customer_score = calculate_score(customer_card)
print(f"{user_card} :  {user_score}")
print(f"The customer card : {customer_card[0]}")
if user_score or customer_score == 0 or user_score > 21:
    is_game = True
else:
    do_continue = input("Do you still want to deal another card, type 'y' for yes and 'n' for no: ")
    if do_continue == "y":
        user_score.append(deal_card())
    else:
        is_game = True

