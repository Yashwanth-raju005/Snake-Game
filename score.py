from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0;
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()


    def update(self):
        self.write(f"Score: {self.score}",align="center",font=("Courier",24,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Courier",24,"normal"))

    def increse_Score(self):
        self.score+=1
        self.clear()
        self.update()

        