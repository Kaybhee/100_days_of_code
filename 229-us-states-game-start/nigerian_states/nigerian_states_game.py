from turtle import Turtle, Screen , Shape
from tkinter import PhotoImage
import turtle
import pandas as pd
screen = Screen()
# screen.addshape("larger", Shape("image", larger))
# screen.addshape(image)
# turtle.shape(image)
# turtle.resizemode("auto")


larger = PhotoImage(file=r"C:\Users\intern2\Videos\100_days_of_code\229-us-states-game-start\nigerian_states\img (1).gif").subsample(4,4)

screen.addshape("larger", Shape("image", larger))

tortoise = Turtle("larger")

tortoise.stamp()

tortoise.hideturtle()

def coord(x,y):
    print(x,y)
turtle.onscreenclick(coord)
screen.mainloop()








screen.exitonclick()









screen.mainloop()
















