import time
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 360
LEFT = 180
ORIGINAL_COUNT = 3

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        snake_body_count = 0
        for count in range(1,4):
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.goto(-20 * snake_body_count, 0)
            snake_body.color("white")
            self.segments.append(snake_body)
            snake_body_count += 1

    def move_snake(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self):
        snake_body = Turtle("square")
        snake_body.penup()
        snake_body.color("white")
        self.segments.append(snake_body)

    def game_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



