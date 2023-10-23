import os
clear = lambda: os.system('cls')
clear()

#print(dict)
dict_1 = {}
bidder_checker = False
def highest_bidder(bid_record):
    highest_bid = 0
    winner = " "
    for new_bids in bid_record:
        bid_amount = bid_record[new_bids]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = new_bids
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidder_checker:
    name = input("What's your name?\n")
    bid = int(input("what's your bid?  $"))
    dict_1[name] = bid
    bidders = input("would you like to place another bid?\n 'yes' or 'no' ")
    if bidders == "no":
        bidder_checker = True
        highest_bidder(dict_1)
    elif bidders == "yes":
        clear()


