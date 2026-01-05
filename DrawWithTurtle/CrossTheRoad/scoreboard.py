FONT = ("Courier", 18, "normal")
from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.write(f"Level : {self.level}", False,"Left", FONT)


    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", False, "Left", FONT)