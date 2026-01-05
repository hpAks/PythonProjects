import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import scoreboard

screen = Screen()
screen.title("PONG")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = scoreboard()

screen.listen()
screen.onkey(left_paddle.move_paddle_up,"Up")
screen.onkey(left_paddle.move_paddle_down,"Down")
screen.onkey(right_paddle.move_paddle_up,"Right")
screen.onkey(right_paddle.move_paddle_down,"Left")

sleep_time = 0.1
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if 280 < ball.ycor() or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320 or (ball.xcor() < -320 and ball.distance(left_paddle.paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.r_score > 5 or scoreboard.l_score > 5:
        sleep_time = 0.2



screen.exitonclick()