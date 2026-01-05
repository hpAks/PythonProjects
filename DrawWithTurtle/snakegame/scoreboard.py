from turtle import Turtle
ALIGNMENT="center"
FONT=("ARIAL",15, "normal")
SCORE_FILE="score.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.high_score = 0
        self.read_high_score()
        self.penup()
        self.goto(0,270)
        self.write_to_score()

    def read_high_score(self):
        with open(SCORE_FILE) as file:
            self.high_score = file.read()

    def write_to_score(self):
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)


    def update_scoreboard(self):
        self.score +=1
        self.clear()
        self.write_to_score()

    def game_over(self):
        if int(self.high_score) < self.score:
            self.high_score = self.score
        self.write_high_score()
        self.score = 0
        self.clear()
        self.write_to_score()
        #self.goto(0,0)
        #self.write(f"GAME OVER",align="CENTER",font=FONT)

    def write_high_score(self):
        with open(SCORE_FILE, mode="w") as file:
            file.write(str(self.high_score))