from turtle import Turtle, Screen
leggo = Turtle()
screen = Screen()


def move_forward():
    return leggo.fd(10)
def move_backwards():
    return leggo.bk(10)
def counter_clockwise():
    return leggo.left(10)
def clockwise():
    return leggo.rt(10)
def clear_drawing():
    return leggo.clear()

screen.listen()
screen.onkey(key = "W", fun = move_forward)
screen.onkey(key = "S", fun = move_backwards)
screen.onkey(key = "A", fun = counter_clockwise)
screen.onkey(key = "D", fun = clockwise)
screen.onkey(key = "C", fun = clear_drawing)

on_screen = screen.exitonclick()