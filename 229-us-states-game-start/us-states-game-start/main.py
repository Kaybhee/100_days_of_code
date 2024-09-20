import turtle
import pandas as pd
screen = turtle.Screen()
image = r"C:\Users\Kaybee\Videos\100_days_of_code\229-us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

right_guess = []
while len(right_guess) < 40:
    state_name = screen.textinput(title = f"Guess {len(right_guess)}/50 state", prompt = "Which state name do you know?" ).title()
    # answer = print(state_name)

    data = pd.read_csv(r"C:\Users\Kaybee\Videos\100_days_of_code\229-us-states-game-start\us-states-game-start\50_states.csv")
    # if data[data["state"] == "answer"]:
    #     turtle.goto(data[["x", "y"]])
    list_states = data["state"].to_list()
    if state_name in list_states:
        right_guess.append(state_name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data["state"] == state_name]
        t.goto(int(state_row["x"]), int(state_row["y"]))
        t.write(state_row["state"].item())
    if state_name == "exit":
        missing_states = [states for states in list_states if states not in right_guess]
        print(missing_states)
        # missing_states = []
        # for states in list_states:
        #     if states not in right_guess:
        #         missing_states.append(states)
        #         print(missing_states)
        df = pd.DataFrame(missing_states)
        df.to_csv("States_to_learn.csv")

        exit()

        
    




# To determine the position of each maps on the image
# def diff_coorde(x, y):
#     print(x,y)
# turtle.onscreenclick(diff_coorde)
# To ask a prompt


# To keep the system running even clicked
# screen.mainloop()
screen.exitonclick()