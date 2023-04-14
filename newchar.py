import turtle
from turtle import Turtle,Screen
from pokemon_build import Pokemon_start
from pokemon_appear import Food
from attack import Attack
from our_attack import My_attack
from pokemon_score import Score_board
from game_over_ import Game_Over

path_pokemon="/Users/HP/PycharmProjects/pong_game/pokemons/"
path_attack="./attacks/"

import time
list=['axew','gible','taillow','charizard','Mega_Charizard_X','Mega_Charizard_Y','pikachu','electabuzz','hitmonchan','carracosta','torterra','machoke','drapion','gengar','Mega_Gengar','grimmsnarl','golem','floatzel','Mega_Blastoise']
attack=['fire.gif','fire.gif','air.gif','fire.gif','blue_fire.gif','blaze_fire.gif','thunder.gif','thunder.gif','punch.gif','water.gif','grass_up.gif','rock.gif','poison.gif','ghost.gif','shadow_ball.gif','poison_ball.gif','ground.gif','hydropump.gif','water_blast.gif']


border=Turtle()
border.hideturtle()
border.penup()


for i in range(len(attack)):
    turtle.register_shape(f"{path_attack}{attack[i]}")






pokemon = Pokemon_start()
random_food= Food()
blast=Attack()
our_blast=My_attack()
my_score=Score_board()
end=Game_Over()
#our_blast.hideturtle()
screen=Screen()
screen.bgcolor("lightgreen")


border.goto(-220,220)
border.pendown()
border.fillcolor('lavender')
for i in range(4):               #making of the border
    border.begin_fill()
    border.forward(440)
    border.right(90)

border.end_fill()











screen.listen()
screen.onkey(pokemon.up,"Up")
screen.onkey(pokemon.down,"Down")
screen.onkey(pokemon.left,"Left")
screen.onkey(pokemon.right,"Right")
screen.onkey(pokemon.turn,"space")
screen.onkey(pokemon.change_pokemon,"q")
#screen.onkey(pokemon.go_back,"w")
screen.onkey(our_blast.my_attack,"e")
screen.onkey(pokemon.pokemon_count,'x')
screen.onkey(pokemon.pokemon_back,'z')
screen.onkey(pokemon.choose_pokemon,'c')


random_food.create_food()
random_food.food_place()


score=0
my_score.score_draw()
my_score.score_write(score)
keep_play=True
while keep_play==True:

    our_blast.goto(pokemon.xcor(),pokemon.ycor())




    if random_food.xcor()<=-200:
        random_food.setheading(0)
        random_food.forward(10)
    elif random_food.xcor()>=200:
        random_food.setheading(180)
        random_food.forward(10)
    else:
        random_food.forward(10)


    if random_food.xcor()%6==0:
        blast.fire()
        blast.goto(random_food.xcor(),random_food.ycor())
        blast.showturtle()
        blast.setheading(270)
        blast.speed("fastest")
        for i in range(100):

            for i in range(len(list)):
                # if pokemon.shape() == f"{list[i]}.gif" or pokemon.shape() == f"{list[i]}_right.gif":
                #     if pokemon.go_back == True:  # getting back to shape
                #         if i - 2 >= 0:
                #             pokemon.shape(f"{list[i - 2]}.gif")
                #             pokemon.go_back = False
                #         else:
                #             pokemon.shape(f"{list[-1]}.gif")  # going back in shape

                if pokemon.shape()==f"{path_pokemon}{list[i]}.gif" or pokemon.shape()==f"{path_pokemon}{list[i]}_right.gif":
                    our_blast.shape(f"{path_attack}{attack[i]}")


            blast.forward(5)
            if our_blast.launch==False:
                our_blast.goto(pokemon.xcor(), pokemon.ycor())
            if our_blast.launch==True:
                our_blast.setheading(90)
                our_blast.forward(20)
                if our_blast.distance(random_food)<=25:
                    score=score+1                            #here we keep track of the score
                    print(score)                             #when our attack hits computer
                    our_blast.hideturtle()
                    our_blast.goto(pokemon.xcor(), pokemon.ycor())
                    my_score.clear()
                    my_score.score_write(score)

                    # for i in range(len(list)):
                    #     if score==len(list):
                    #         random_food.shape(f"{list[0]}.gif")
                    #         blast.shape(attack[0])
                    #     else:
                    #         random_food.shape(f"{list[score%(len(list))]}.gif")
                    #         blast.shape(attack[score%(len(list))])
                if our_blast.ycor() >= 200:
                    our_blast.hideturtle()
                    our_blast.goto(pokemon.xcor(), pokemon.ycor())
                    our_blast.launch=False

            if pokemon.distance(blast) < 40:
                print("game over")
                end.game_over()
                keep_play=False               #when computer's attack hits our player

        blast.hideturtle()









screen.exitonclick()