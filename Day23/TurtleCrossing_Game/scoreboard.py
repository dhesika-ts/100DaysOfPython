from turtle import Turtle
FONT=("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.disp_score()

    def level_up(self):
        self.level+=1
        self.disp_score()

    def disp_score(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)