from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"SCORE : {self.score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"SCORE : {self.score}", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over your score is : {self.score}", align="center", font=("Arial", 15, "normal"))


        

        
