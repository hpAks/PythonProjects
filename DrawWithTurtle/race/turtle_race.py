import random
from turtle import Turtle,Screen


turtle_violet = Turtle(shape="turtle")
turtle_violet.color("violet")

turtle_indigo = Turtle(shape="turtle")
turtle_indigo.color("indigo")

turtle_blue = Turtle(shape="turtle")
turtle_blue.color("blue")

turtle_green = Turtle(shape="turtle")
turtle_green.color("green")

turtle_yellow = Turtle(shape="turtle")
turtle_yellow.color("yellow")

turtle_orange = Turtle(shape="turtle")
turtle_orange.color("orange")

turtle_red = Turtle(shape="turtle")
turtle_red.color("red")

screen = Screen()
screen.setup(width=500, height=400) # Give the screen some dimensions
#screen.colormode(255)

turtles = [turtle_violet, turtle_indigo, turtle_blue, turtle_green, turtle_yellow, turtle_orange, turtle_red]

paces = [10,20,30]
turtle_distance= {
    turtle_violet:0,
    turtle_indigo :0,
    turtle_blue:0,
    turtle_green:0,
    turtle_yellow:0,
    turtle_orange:0,
    turtle_red:0
}

def move_turtle(turtle):
        choice = random.choice(paces)
        turtle.forward(choice)
        turtle_distance[turtle] += choice
        if turtle_distance[turtle] >= 230:
            print(f"turtle color:{turtle.pencolor()}, distance travelled:{turtle_distance[turtle]}")
            return turtle.pencolor()
        return None

def turtle_take_positions():
    turtle_violet.penup()
    turtle_violet.goto(-200,-60)
    turtle_indigo.penup()
    turtle_indigo.goto(-200,-30)
    turtle_blue.penup()
    turtle_blue.goto(-200,0)
    turtle_green.penup()
    turtle_green.goto(-200,30)
    turtle_yellow.penup()
    turtle_yellow.goto(-200,60)
    turtle_orange.penup()
    turtle_orange.goto(-200,90)
    turtle_red.penup()
    turtle_red.goto(-200,120)

def start_game():
    screen.listen()
    ans = screen.textinput(title="Make your bet",prompt="select your bet on rainbow turtle : ")
    print(f"selected color to win:{ans}")
    turtle_take_positions()
    screen.update()
    go_on = True
    while go_on:
        random.shuffle(turtles)
        for turtle in turtles:
            turtle_movement = move_turtle(turtle)
            if turtle_movement == ans:
                print(f"You win!! Winner is turtle :{ans}")
                go_on = False
                break
            elif turtle_movement is not None and turtle_movement != ans:
                print(f"You lose... Winner is {turtle_movement}")
                go_on = False
                break
            else:
                continue
    screen.update()

