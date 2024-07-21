import random

def solution(text, ending):
    for word in text:
        if word[-2:] == ending[-2:]:
            print(f"{text}, {ending}")
            return True  # If a match is found, you might want to return True
    return False

text = ["bad", "deg", "rant"]  # Use a list instead of a set
ending = random.choice([" cad", "reg", " bant"])  # Choose a random ending
solution(text, ending)

