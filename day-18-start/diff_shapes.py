import turtle as t
from turtle import Screen
leggo = t.Turtle()
import random
#     leggo.forward(10)
#     leggo.penup()
#     leggo.forward(10)
#     # leggo.pensize(10)
#     # leggo.width(10)
#     leggo.pendown()
#     leggo.hideturtle()
    # leggo.shape("triangle")
color = ["red", "navy", "blue", "black", "white", "yellow", "pink", "purple", "green"]
def num_of_sides(side):
    for i in range(side):
        angle = 360 / side
        leggo.fd(100)
        leggo.rt(angle) 

for shape_sides in range(3, 11):
    leggo.color(random.choice(color))
    num_of_sides(shape_sides)


on_screen = Screen()
on_screen.exitonclick()