from turtle import Turtle
FONT = ("courier", 24, "normal")
FONT_GO = ("courier", 100, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("white")
        self.setposition(-200,260)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def clear_gamescore(self):
        self.clear()
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("white")
        self.setposition(0, 0)

    def show_game_over(self):
        self.write(arg=f"GAME OVER", align="center", font=FONT_GO)