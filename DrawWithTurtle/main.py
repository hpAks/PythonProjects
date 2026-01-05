import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def get_turn_angle(sides):
    return 360/sides

tim.shape("turtle")
tim.speed("fastest")
screen.colormode(255)

def draw_shape(shape_side):
    for i in range(0, shape_side):
        tim.forward(100)
        tim.right(get_turn_angle(shape_side))

direction = ["backward","forward"]
turn = ["right", "left"]

def get_color_tuple():
     my_tuple = tuple()
     my_tuple = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
     return my_tuple

def change_direction():
    if random.choice(direction) == "backward":
        tim.color(get_color_tuple())
        tim.pensize(random.randint(5,10))
        tim.back(30)
    else:
        tim.pensize(random.randint(5, 10))
        tim.forward(30)
    if random.choice(turn) == "right":
        tim.right(90)
    else:
        tim.left(90)

def draw_shapes():
    for side in range(4,11):
        tim.color(get_color_tuple())
        draw_shape(side)

def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)
        tim.color(get_color_tuple())

#for index in range(0,200):
#    change_direction()
draw_spirograph(5)

screen.exitonclick()