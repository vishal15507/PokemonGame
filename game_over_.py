from turtle import Turtle

class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def game_over(self):
        self.hideturtle()
        self.write("GAME OVER",False,align="center",font=("arial",16,"normal"))