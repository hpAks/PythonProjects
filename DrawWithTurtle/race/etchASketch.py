import turtle
from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_anti_clockwise():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

def move_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def draw_sketch():
    screen.listen()
    screen.onkey(key="c",fun=clear_screen)
    screen.onkey(key="w",fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a",fun=move_anti_clockwise)
    screen.onkey(key="d",fun=move_clockwise)
    screen.onkey(key="x",fun=screen.exitonclick)


