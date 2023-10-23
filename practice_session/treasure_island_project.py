# Welcome to treasure island
# Day 3 project
print("Welcome to Treasure island")
print("Your mission is to find the treasure")
game = input ('You\'re at a cross road, where do you want to go "L" or "R"?\n')
if game == "L":
    choice1 = input("you\' come to a lake, there is an island in the middle of the lake. type 'wait' to wait for boat, type 'swim' to swim across")
    if choice1== "wait":
        choice2 = input("You arrived at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which color would you choose?")
        if choice2 == "red":
            print("It's a room full of fire, Game over!")
        elif choice2 == "yellow":
            print("You just found the treasure, you win!")
        elif choice2 == "blue":
            print("You chose a room filled with beasts, Game over")
        else:
            print("The door doesn't exist , game over")
    else:
        print("you got attacked, Game over!")
else:
    print("You fell into a hole, Game over")
