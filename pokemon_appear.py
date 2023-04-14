import turtle
from turtle import Turtle
import random
import time
list=['charizard','Mega_Charizard_X','Mega_Charizard_Y','pikachu','electabuzz','hitmonchan','carracosta','torterra','machoke','drapion','gengar','Mega_Gengar','grimmsnarl','golem','floatzel','Mega_Blastoise']



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.pick=random.choice(list)
        turtle.register_shape(f"/Users/HP/PycharmProjects/pong_game/pokemons/{self.pick}.gif")
        self.places=[]
        self.speed("slowest")



    def create_food(self):
        #self.food=Turtle()
        self.shape(f"/Users/HP/PycharmProjects/pong_game/pokemons/{self.pick}.gif")
        self.penup()
        self.color("yellow")

    def food_place(self):

        self.goto(-200,200)






    # def food_appearance(self):
    #     dist=[10,15,20,25,30]
    #     #choose=[self.forward(random.choice(dist)),self.backward(random.choice(dist)),self.food.left(90),self.food.right(90)]
    #
    #
    #     if self.food.xcor()<=-200:
    #         self.food.left(180)
    #     elif self.food.xcor()>=200:
    #         self.food.left(180)
    #     else:
    #         self.food.backward(20)



