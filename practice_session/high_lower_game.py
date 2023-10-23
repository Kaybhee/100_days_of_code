import random
from game_data import data
import os
clear = lambda: os.system('cls')
clear()
from art import logo, vs
#create a function then access the dictionary in the list
def format_account(account):
    acc_name = account['name'] 
    acc_description = account["description"]
    acc_country = account['country']
    return f"{acc_name}, a {acc_description} from {acc_country}"
#Create a function then compare the followers and the guess from the user
def compare(followers, a_follower, b_follower):
    if a_follower > b_follower:
        if followers == "a":
            return True
        else:
            return False
    if b_follower > a_follower:
        if followers == "b":
            return True
        else:
            return False
print(logo)
do_continue = False
#score them a point for every correct guess
score = 0
#Get a random of all data 
a_list = random.choice(data)
#your code should keep running until you make a wrong guess
#while do_continue != False:
while not do_continue:
    b_list = random.choice(data)
    if a_list == b_list:
        b_list = random.choice(data)

    print(f"compare A: {format_account(a_list)}")
    print(vs)
    print(f"against B: {format_account(b_list)}")
   
    aA = a_list['follower_count']
    bB = b_list['follower_count']
    followers = input("Who has more followers? Type A or B: ").lower()
 #make an if statemnt to compare between the follower account of the two different random account
    is_correct = compare(followers, aA, bB)
    if is_correct:
#if guessed correctly make the second question assume the first in ur next question
        a_list = b_list
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score {score}")
      
    else:
        print(f"sorry, You're wrong ur score is {score}")
        do_continue = True
   

    