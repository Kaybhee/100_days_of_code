import colorgram

import turtle as turtle_module
import random
turtle_module.colormode(255)
leggo = turtle_module.Turtle()
leggo.penup()
leggo.hideturtle()
color_list = [ (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (52,93, 124), (172, 154, 40), (140, 30, 19), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 92, 89), (32, 56, 87), (76,88, 97)]


leggo.speed("fastest")
leggo.setheading(225)
leggo.fd(300)
leggo.setheading(0)
dots_number = 101
for no_of_dots in range(1, dots_number):
    leggo.dot(20, random.choice(color_list))
    leggo.fd(50)
    if no_of_dots % 10 == 0:
        leggo.setheading(90)
        leggo.fd(50)
        leggo.setheading(180)
        leggo.fd(500)
        leggo.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()
