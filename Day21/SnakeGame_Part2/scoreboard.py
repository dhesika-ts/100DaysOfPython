from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 18, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.disp_score()


    def update_score(self):
        self.score+=1
        self.clear()
        self.disp_score()

    def disp_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)