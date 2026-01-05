from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle("square")
        self.initialize_paddle(position)

    def initialize_paddle(self,position):
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def move_paddle_up(self):
       self.paddle.goto(self.paddle.xcor(),self.paddle.ycor() + 20)

    def move_paddle_down(self):
      self.paddle.goto(self.paddle.xcor(),self.paddle.ycor() - 20)



