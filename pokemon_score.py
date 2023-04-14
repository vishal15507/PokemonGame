from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()

    def score_draw(self):
        self.hideturtle()
        self.penup()
        self.goto(0,225)
        self.speed("fastest")
        self.pendown()
        #self.write(f"Score={number}",move=False,align="center" ,font=("arial",16,"normal"))

    def score_write(self,number):
        self.write(f"Score={number}", move=False, align="center", font=("arial", 16, "normal"))

