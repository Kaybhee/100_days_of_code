from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
score_board = ScoreBoard()
food = Food()
#Event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    score = 0
    screen.update()
    time.sleep(0.1)
    # for move_fd in new_segment:
    #     move_fd.forward(20)
    #     new_segment[0].rt(90)
    snake.move()

    # To create when the snake collides with a food
    if snake.head.distance(food) < 15:
        food.change_food_location()
        score_board.increase_score()








screen.exitonclick()
