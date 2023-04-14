from turtle import Turtle,register_shape
from pokemon_build import Pokemon_start

class My_attack(Turtle):
    def __init__(self):
        super().__init__()
        self.launch=False
        self.penup()
        self.hideturtle()


    def my_attack(self):
        register_shape("./attacks/thunder.gif")

        #self.hideturtle()
        self.showturtle()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_wid=1.1,stretch_len=1.1)
        self.color("orange")
        #self.goto(Pokemon_start.xcor(),Pokemon_start.ycor())

        self.penup()
        self.launch=True