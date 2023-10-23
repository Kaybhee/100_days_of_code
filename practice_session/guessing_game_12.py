import random
# To compare the number guessed against the random numbers
def difficulty_level(guess, round_rand_int, no_of_turns):
    if guess > round_rand_int:
        print("Too high, try again!")
        return no_of_turns - 1
    elif guess < round_rand_int:
        print("Too low, try again!")
        return no_of_turns - 1
    elif guess == round_rand_int:
        print(f"You guessed right, the answer was {round_rand_int}")
    else:
        print("Invalid input")
        exit()
EASY_LEVEL = 5
HARD_LEVEL = 10
def level():
    game_level = input("Choose a difficulty. type 'Easy' or 'Hard': ")
    if game_level == 'easy':
        return EASY_LEVEL
    elif game_level == 'hard':
        return HARD_LEVEL
    else:
        print("Incorrect input")
        exit()
def game():
    rand_int = random.uniform(1,100)
    round_rand_int = round(rand_int, 2)
    print("Welcome to the number guessing game")
    print("Guess a number between 1 and 100")
    print(f"The answer is {round_rand_int}, but go ahead yeah!")
    no_of_turns = level()
    guess = 0
    while guess != round_rand_int:
        print(f"You have {no_of_turns} attempts remaining to guess the number")
        guess = float(input("Make a guess: "))
        no_of_turns = difficulty_level(guess, round_rand_int, no_of_turns)
        if no_of_turns == 0:
            return
game()

