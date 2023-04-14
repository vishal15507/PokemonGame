from turtle import Turtle,register_shape
from pokemon_appear import Food
food=Food()
class Attack(Turtle):
    def __init__(self):
        super().__init__()



    def fire(self):
        register_shape("./attacks/air.gif")

        self.hideturtle()
        self.shape("./attacks/air.gif")
        self.shapesize(stretch_wid=1.1,stretch_len=1.1)
        self.color("orange")

        self.penup()

        # self.goto(food.xcor(),food.ycor())
        # self.setheading(270)
        # self.showturtle()
        # self.speed("fastest")
        # for i in range(100):
        #
        #     self.forward(5)
        # self.hideturtle()
