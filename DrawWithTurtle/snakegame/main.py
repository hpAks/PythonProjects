import time

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")
screen.listen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.turn_up,"Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left ,"Left")
screen.onkey(snake.turn_right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.update_scoreboard()
        snake.add_segment()
        screen.update()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        snake.game_reset()
        scoreboard.game_over()

    for segment in snake.segments[1::1]:
        if snake.head.distance(segment) < 10:
            snake.game_reset()
            scoreboard.game_over()




screen.exitonclick()