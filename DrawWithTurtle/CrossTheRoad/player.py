STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import  Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_turtle()

    def initialize_turtle(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)



