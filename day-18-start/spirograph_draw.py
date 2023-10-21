import turtle as t
from turtle import Screen
import random
timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



def draw_spirograph(num_of_sides):
    angle = int(360 / num_of_sides)
    for i in range(angle):
        timmy.circle(100)
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + num_of_sides)

draw_spirograph(5)








on_screen = Screen()
on_screen.exitonclick
