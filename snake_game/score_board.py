from turtle import Turtle

ALIGNMENT = "center"
FONT = ("verdana", 18, "bold")
with open("data.txt", mode="r") as latest_score:
    latest_contents = latest_score.read()
    latest_contents = int(latest_contents)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = latest_contents
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}  high score:{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_score:
                new_score.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
