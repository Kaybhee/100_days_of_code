from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180 
RIGHT = 0
POSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.new_segment = []
        self.create_snake()
        self.head = self.new_segment[0]

    def create_snake(self):
        for direction in POSITION:
            segment= Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(direction)
            self.new_segment.append(segment)

    def move(self):
        for seg_num in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[seg_num - 1].xcor()
            new_y = self.new_segment[seg_num - 1].ycor()
            self.new_segment[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
   

