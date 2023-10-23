import turtle as t
from turtle import Screen
import random
leggo = t.Turtle()
t.colormode(255)


# leggo.shape("turtle")


# for i in range(15):
#     leggo.forward(10)
#     leggo.penup()
#     leggo.forward(10)
#     # leggo.pensize(10)
#     # leggo.width(10)
#     leggo.pendown()
#     leggo.hideturtle()
    # leggo.shape("triangle")
# color = ["red", "navy", "blue", "black", "white", "yellow", "pink", "purple", "green"]
# def num_of_sides(side):
#     for i in range(side):
#         angle = 360 / side
#         leggo.fd(100)
#         leggo.rt(angle) 

# for shape_sides in range(3, 11):
#     leggo.color(random.choice(color))
#     num_of_sides(shape_sides)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r , g, b)
    return random_colors

choice =[0, 90, 180, 270]
for i in range(300):
    leggo.fd(30)
    # leggo.bk(random.choice(choice))
    leggo.rt(random.choice(choice))
    leggo.color(random_colors())
    leggo.speed(10)
    # leggo.lt(random.choice(choice))
    leggo.width(12)















on_screen = Screen()
# on_screen.getshapes("arrow")
on_screen.exitonclick()