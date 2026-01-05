import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_POS = 260

from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_car()


    def initialize_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.pace = STARTING_MOVE_DISTANCE
        self.goto(STARTING_X_POS,random.randint(-260,260))


    def move_ahead(self):
        if self.xcor() < -280:
            new_y_cor = random.randint(-280, 280)
            self.pace += MOVE_INCREMENT
            self.goto(STARTING_X_POS, new_y_cor)
        else:
            self.goto(self.xcor()-self.pace,self.ycor())
